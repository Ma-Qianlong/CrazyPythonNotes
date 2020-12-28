#!/usr/bin/env python

# -*- *************** -*-
# @File  : modbus_apex_efb.py
# @Description : 
# @Author: mql
# @Time  : 2020/12/19 23:12
# -*- *************** -*-


import threading
import time
from read_config import ReadConfig
from handle_redis import HandleRedis
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
            if efb.fault_rec == 1 and efb.reading_rec is not True:
                ts = time.time()
                logger.info("****** there has fault recode for %s:%d slave-%s to read" %
                            (efb.host, efb.port, efb.slave))
                # threading.Thread(target=efb.poll_fault_recode, args=(redis,))
                efb.poll_fault_recode(redis)
                logger.info("****** fault recode for %s:%d slave-%s read finished, cost time(s): %f" %
                            (efb.host, efb.port, efb.slave, (time.time() - ts)))

            time.sleep(scan_interval)

    except Exception as e:
        logger.error("****** scan onece for %s:%d slave-%s ERROR, %s" % (efb.host, int(efb.port), efb.slave, e))


tagPrefix_efb_dict = {}


def do_start():
    logger.info("### read config info ... ")
    cofig = ReadConfig()

    baseCfg = cofig.get_base()
    base_dict = dict(baseCfg)
    logger.info(base_dict)

    redisCfg = cofig.get_redis()
    redis_dict = dict(redisCfg)
    logger.info(redis_dict)

    # 设置日志级别
    logger.setLevel(base_dict.get("log_level"))

    server_port = int(base_dict.get('server_port'))

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


if __name__ == '__main__':
    do_start()
    time.sleep(5)
    server_port = ReadConfig().get_items("BASE", 'server_port')
    server_port = int(server_port)
    logger.info("start web server on port %d ...\n" % server_port)
    app.run(host="0.0.0.0", port=server_port, debug=False)
