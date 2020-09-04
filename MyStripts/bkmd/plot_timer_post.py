#!/usr/bin/env python

# -*- *************** -*-
# @File  : plot_timer_post.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-04 12:09
# -*- *************** -*-


from concurrent.futures import ThreadPoolExecutor
import threading
from  threading import Timer
import requests
import json
from datetime import datetime, timedelta
import plot_bkmd_kpa
from mycolorlog import logger



# postdata = {'json': json.dumps([{"tagName":"test#test#zzx#test", "time": "2020-09-04 13:10:00", "value": "9999"}])}
# r = requests.post('http://127.0.0.1/sightApi/other/saveHistoryDataFromNodeJs', data=postdata)
# print(r.text)
#
# postdata1 = {"keyVal":json.dumps({"test#test#zzx#test": 999})}
# r = requests.post('http://127.0.0.1/sightApi/redis/setAcqdataRDatas', data=postdata1)
# print(r.text)

# 放采集的数据
tagnameValue={}
collect_frequency = 3
post_rt_url = 'http://127.0.0.1/sightApi/redis/setAcqdataRDatas'
post_his_url = 'http://127.0.0.1/sightApi/other/saveHistoryDataFromNodeJs'
# ip_tagPrefix = {"http://127.0.0.1/bkmd/192.168.10.40.html":"ZSZL#ZSZL#MGM#BCM08#",
#                 "http://127.0.0.1/bkmd/192.168.10.46.html":"ZSZL#ZSZL#MGM#BCM02#"}
ip_tagPrefix={}


def loadCfgInfo():
    with open("plot.cfg", mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    logger.info("读取到的配置文件：" + str(lines))

    isBase = False
    isTagPrefix = False
    for line in lines:

        if (not line or line == "" or line == '\n' or line.isspace()):
            continue

        print(line)

        if (line.startswith("# base")):
            isBase = True
            isTagPrefix = False
            continue
        if (line.startswith("# collect_ip_tagPrefix")):
            isBase = False
            isTagPrefix = True
            continue
        if (isBase):
            if (line.startswith("collect_frequency")):
                collect_frequency = int(line.split("=")[1])
            if (line.startswith("post_rt_url")):
                post_rt_url = str(line.split("=")[1])
            if (line.startswith("post_his_url")):
                post_his_url = str(line.split("=")[1])

        if (isTagPrefix):
            if (line.index(",") > 0):
                ddd = line.split(",")
                ip_tagPrefix[ddd[0]] = str(ddd[1].split()[0])

    logger.info("collect_frequency= %d" % collect_frequency)
    logger.info("post_rt_url= %s" % post_rt_url)
    logger.info("post_his_url= %s" % post_rt_url)
    logger.info("ip_tagPrefix: %s" % str(ip_tagPrefix))


def collectData(ipAddr, tagPrefix):
    # {"oxy": lis_O[0], "mda": lis_M[0], "vac": lis_V[0]}
    ipData = plot_bkmd_kpa.getOneMeterDate(ipAddr)
    if(ipData is not None):
        tagnameValue[tagPrefix+"oxy"] = ipData['oxy']
        tagnameValue[tagPrefix+"mda"] = ipData['mda']
        tagnameValue[tagPrefix+"vac"] = ipData['vac']


def post2redis():
    r = requests.post(post_rt_url, data={"keyVal":json.dumps(tagnameValue)})
    logger.debug("post2redis: " + json.dumps(tagnameValue) + ", r=" + str(r))

def post2his(datatime):
    dArr=[]
    for tag in tagnameValue:
        dArr.append({"tagName":tag, "time": datatime, "value": tagnameValue[tag]})
    r = requests.post(post_his_url, data={"json": json.dumps(dArr)})
    logger.debug("post2redis: " + json.dumps(dArr) + ", r=" + str(r))


pool = ThreadPoolExecutor(max_workers=len(ip_tagPrefix)+2)

def do_collect():
    logger.debug("##### do_collect and post2redis ##### ")
    for vv in ip_tagPrefix:
        #threading.Thread(target=collectData, args=(vv, ip_tagPrefix[vv])).start()
        pool.submit(collectData, vv, ip_tagPrefix[vv])
    pool.submit(post2redis)
    Timer(collect_frequency, do_collect).start()

def do_his():
    tt = datetime.now().strftime("%Y-%m-%d %H:%M") + ":00"
    logger.debug("##### do post2his ##### " + tt)
    pool.submit(post2his, tt)
    Timer(60*5, do_his).start()
    # Timer(5, do_his).start()


def do_run():
    Timer(1, do_collect).start()

    nowTime = datetime.now()
    logger.info("当前时间：" + nowTime.strftime("%Y-%m-%d %H:%M:%S"))
    nextTT = (nowTime + timedelta(minutes=(5 - (nowTime.minute % 5))))
    next5T = nextTT.strftime("%Y-%m-%d %H:%M")+":00"
    logger.info("下个5分钟的时间：" + next5T)

    nT = datetime(nextTT.year, nextTT.month, nextTT.day, nextTT.hour, nextTT.minute, 0)
    startAfter = (nT-nowTime).seconds + 5
    logger.info(str(startAfter) + "秒后开始执行历史数据入库")
    Timer(startAfter, do_his).start()
    # Timer(1, do_his).start()

if __name__ == "__main__":
    loadCfgInfo()
    logger.info("读取配置信息OK, 15秒后开始启动爬取数据。。。。。")
    Timer(15, do_run()).start()

