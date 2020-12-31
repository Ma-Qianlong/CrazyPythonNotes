#!/usr/bin/env python

# -*- *************** -*-
# @File  : modbus_apex_efb.py
# @Description : 
# @Author: mql
# @Time  : 2020/12/19 23:12
# -*- *************** -*-


import threading
import time
from datetime import datetime
from read_config import ReadConfig
from handle_redis import HandleRedis
from handle_mysql import doDbOpt
from apex_efb import ModbusTCP_apex_efb as ApexEfb
from mycolorlog import *

from flask import Flask
from flask_restful import Api, reqparse, abort, Resource, request
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域
api = Api(app)


def abort_if_param_doesnt_exist(args):
    if False:
        abort(404, message="the requirted param is empty")


class WriteTagVal(Resource):
    def post(self):
        # args = parser.parse_args()
        args = request.json
        logger.info("requet to write tag-val：" + str(args))
        try:
            tagvals = args.get("data")
            logger.info("to write tag-vals：" + str(tagvals))
            if tagvals is not None and len(tagvals) > 0:
                writeToEfb(tagvals)

        except Exception as e:
            logger.error("requet to write tag-val：%s ERROR, %s" % (str(args), e))
            return {'success': False, 'msg': e.args[0]}, 201
        else:
            return {'success': True, 'msg': 'to write tag-val SUCCESS！'}, 201


##
## Actually setup the Api resource routing here
##
api.add_resource(WriteTagVal, '/writeTagVal')


def writeToEfb(tagVals):
    pre_tagvals = {}

    for tagval in tagVals:
        tag = tagval.get("tag")
        pre = tag[:find_last(tag, '#') + 1]
        tvs = pre_tagvals.get(pre)
        if tvs is None:
            tvs = []
        tvs.append(tagval)
        pre_tagvals[pre] = tvs

    logger.info("will write tagvals: " + str(pre_tagvals))

    for kk in pre_tagvals.keys():
        efb = tagPrefix_efb_dict.get(kk)
        if efb is not None:
            efb.write_with_single(pre_tagvals.get(kk))


def find_last(string, str):
    last_position = -1
    while True:
        position = string.find(str, last_position + 1)
        if position == -1:
            return last_position
        last_position = position

tagPrefix_fault_dict = {}

def server_target(redis, efb, scan_interval):
    try:
        efb.to_connect()
        logger.info("****** it will start scan for %s:%d slave-%s after 3 second ..." %
                    (efb.host, efb.port, efb.slave))
        time.sleep(3)
        while efb.online:
            dd = efb.poll_and_analysis()
            redis.putRTData(dd)
            logger.info("****** scan onece for %s:%d slave-%s finished, data size: %d" %
                        (efb.host, efb.port, efb.slave, len(dd)))
            # global tagPrefix_fault_dict
            # if tagPrefix_fault_dict.get(efb.tag_prefix) is None:
            #     tagPrefix_fault_dict[efb.tag_prefix] = efb.has_fault
            # # 产生了故障
            # if efb.has_fault == 1 and tagPrefix_fault_dict.get(efb.tag_prefix) == 0:
            #     # 故障产生时间
            #     faultTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #     # 故障设备
            #     assetName = efb.tag_prefix.split("#")[3]
            #     # 故障代码
            #     faultCode = efb.fault_code
            #     # 故障录波
            #     recData = None
            if efb.fault_rec == 1 and efb.reading_rec is not True:
                # 故障产生时间
                faultTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # 故障设备
                assetName = efb.tag_prefix.split("#")[3]
                # 故障代码
                faultCode = efb.fault_code

                ts = time.time()
                logger.info("****** there has fault recode for %s:%d slave-%s to read" %
                            (efb.host, efb.port, efb.slave))
                # threading.Thread(target=efb.poll_fault_recode, args=(redis,))
                recData = efb.poll_fault_recode_toMysql()
                logger.info("****** fault recode for %s:%d slave-%s read finished, cost time(s): %f" %
                            (efb.host, efb.port, efb.slave, (time.time() - ts)))
                # 向mysql数据库保存故障事假及录波数据
                # threading.Thread(target=inserRecToMysql, args=(assetName, faultCode, faultTime, efb.fault_rec, recData))
                try:
                    inserRecToMysql(assetName, faultCode, faultTime, efb.fault_rec, recData)
                    # 下发录波数据已读取命令
                    efb.set_fault_rec_readed()
                except Exception as e:
                    logger.error("****** Insert Rec To Mysql for %s:%d slave-%s ERROR, %s" % (efb.host, int(efb.port), efb.slave, e))
            time.sleep(scan_interval)

    except Exception as e:
        logger.error("****** scan onece for %s:%d slave-%s ERROR, %s" % (efb.host, int(efb.port), efb.slave, e))


tagPrefix_efb_dict = {}
mysql = None

def do_start():
    logger.info("### read config info ... ")
    cofig = ReadConfig()

    baseCfg = cofig.get_base()
    base_dict = dict(baseCfg)
    logger.info(base_dict)

    redisCfg = cofig.get_redis()
    redis_dict = dict(redisCfg)
    logger.info(redis_dict)

    mysqlCfg = cofig.get_mysql()
    mysql_dict = dict(mysqlCfg)
    logger.info(mysql_dict)

    # 设置日志级别
    logger.setLevel(base_dict.get("log_level"))

    # mysql
    global mysql
    mysql = doDbOpt(mysql_dict.get('host'), int(mysql_dict.get("port")), mysql_dict.get("user"), mysql_dict.get("password"), mysql_dict.get("database"))

    logger.info("### start load %s meters threads ... " % base_dict.get('meter_no'))
    for i in range(int(base_dict.get('meter_no'))):
        efb_ = cofig.get_items('EFB-' + str(i + 1))
        efbCfg = dict(efb_)
        logger.info(efbCfg)

        redis = HandleRedis(host=redis_dict.get("host"), port=int(redis_dict.get("port")), db=int(redis_dict.get("db")),
                            key_prefix=redis_dict.get("rt_key_prefix"),
                            fault_rec_prefix=redis_dict.get('fault_rec_prefix'))
        efb = ApexEfb(host=efbCfg.get("host"), port=int(efbCfg.get("port")), timeout=float(efbCfg.get("out_time")),
                      tag_prefix=efbCfg.get("tag_prefix"))
        tagPrefix_efb_dict[efbCfg.get("tag_prefix")] = efb
        threading.Thread(target=server_target, args=(redis, efb, float(efbCfg.get("scan_interval")))).start()

    # time.sleep(5)
    # print("&&&&&&&& " + str(tagPrefix_efb_dict.get("SS#DD#MM#d01#").online))

def inserRecToMysql(assetName, faultCode, faultTime, faultRec=0, faultData=None):
    global mysql
    if mysql is None:
        cofig = ReadConfig()
        mysqlCfg = cofig.get_mysql()
        mysql_dict = dict(mysqlCfg)
        mysql = doDbOpt(mysql_dict.get('host'), int(mysql_dict.get("port")), mysql_dict.get("user"), mysql_dict.get("password"), mysql_dict.get("database"))
    mysql.insertFaultRecData(assetName, faultCode, faultTime, faultRec, faultData)

if __name__ == '__main__':
    do_start()
    time.sleep(5)
    server_port = ReadConfig().get_items("BASE", 'server_port')
    server_port = int(server_port)
    logger.info("start web server on port %d ...\n" % server_port)
    app.run(host="0.0.0.0", port=server_port, debug=False)
