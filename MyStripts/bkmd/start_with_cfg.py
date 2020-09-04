#!/usr/bin/env python

# -*- *************** -*-
# @File  : start_with_cfg.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-04 11:24
# -*- *************** -*-


import codecs
from mycolorlog import logger

# f = codecs.open("plot.cfg", 'r', 'utf-8', buffering=True)
# # 读取所有行
# lines = f.readlines()
# f.close()

with open("plot.cfg", mode='r', encoding='utf-8') as f:
    lines = f.readlines()

logger.info("读取到的配置信息：" + str(lines))

collect_frequency = 3
post_rt_url = "http://127.0.0.1/sightApi/other/saveHistoryDataFromNodeJs"
post_his_url = "http://127.0.0.1/sightApi/redis/setAcqdataRData"
ip_tagPrefix = {}

isBase = False
isTagPrefix = False
for line in lines:

    if(not line or line == "" or line == '\n' or line.isspace()):
        continue

    print(line)

    if(line.startswith("# base")):
        isBase = True
        isTagPrefix = False
        continue
    if(line.startswith("# collect_ip_tagPrefix")):
        isBase = False
        isTagPrefix = True
        continue
    if(isBase):
        if(line.startswith("collect_frequency")):
            collect_frequency = int(line.split("=")[1])
        if(line.startswith("post_rt_url")):
            post_rt_url = str(line.split("=")[1])
        if(line.startswith("post_his_url")):
            post_his_url = str(line.split("=")[1])

    if(isTagPrefix):
        if(line.index(",") > 0):
            ddd = line.split(",")
            ip_tagPrefix[ddd[0]] = str(ddd[1].split()[0])

logger.info("collect_frequency= %d" % collect_frequency)
logger.info("post_rt_url= %s" % post_rt_url)
logger.info("post_his_url= %s" % post_rt_url)
logger.info("ip_tagPrefix: %s" % str(ip_tagPrefix))
print(len(ip_tagPrefix))


