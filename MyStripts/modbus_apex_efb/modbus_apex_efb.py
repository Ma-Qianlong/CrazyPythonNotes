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


def server_target(redis, efb, scan_interval):
    try:
        efb.to_connect()
        while efb.online:
            dd = efb.poll_and_analysis()
            redis.putRTData(dd)
            logger.debug("****** scan onece for %s:%d slave-%s finished, data size: %d" % (efb.host, efb.port, efb.slave, len(dd)))
            time.sleep(scan_interval)

    except Exception as e:
        logger.error("****** scan onece for %s:%d slave-%s ERROR, %s" % (efb.host, int(efb.port), efb.slave, e))


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

    tagPrefix_efb_dict = {}
    for i in range(int(base_dict.get('meter_no'))):
        efb_ = cofig.get_items('EFB-' + str(i + 1))
        efbCfg = dict(efb_)
        logger.info(efbCfg)

        redis = HandleRedis(host=redis_dict.get("host"), port=int(redis_dict.get("port")), db=int(redis_dict.get("db")), key_prefix=redis_dict.get("rt_key_prefix"))
        efb = ApexEfb(host=efbCfg.get("host"), port=int(efbCfg.get("port")), timeout=float(efbCfg.get("out_time")), tag_prefix=efbCfg.get("tag_prefix"))
        tagPrefix_efb_dict[efbCfg.get("tag_prefix")] = efb
        threading.Thread(target=server_target, args=(redis, efb, float(efbCfg.get("scan_interval")))).start()

    # time.sleep(5)
    # print("&&&&&&&& " + str(tagPrefix_efb_dict.get("SS#DD#MM#d01#").online))
if __name__ == '__main__':
    do_start()