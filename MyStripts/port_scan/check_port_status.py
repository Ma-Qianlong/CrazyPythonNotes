#!/usr/bin/env python

# -*- *************** -*-
# @File  : check_port_status.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-08 9:41
# -*- *************** -*-

import os
import telnetlib
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import queue
import requests
import json
from datetime import datetime, timedelta
from mycolorlog import *


class CountDownLatch:
    def __init__(self, count):
        self.count = count
        self.condition = threading.Condition()

    def wait(self):
        try:
            self.condition.acquire()
            # logger.debug("0---" + str(self.count))
            while self.count > 0:
                self.condition.wait()
                # logger.debug("1---" + str(self.count))
        finally:
            self.condition.release()

    def countDown(self):
        try:
            self.condition.acquire()
            self.count -= 1
            self.condition.notifyAll()
            # logger.debug("2---" + str(self.count))
        finally:
            self.condition.release()

def ping(ip):
    re = os.system("ping -n 1 -w 1 %s" % ip)
    if re:
        print('ping %s is fail' % ip)
        return 0
    else:
        print('ping %s is ok' % ip)
        return 1

server = telnetlib.Telnet()
def getPortStatus(ip, port, timeout):
    try:
        server.open(ip, port, timeout)
        logger.info('{0} port {1} is open'.format(ip, port))
        return 1
    except Exception as err:
        logger.info('{0} port {1} is not open'.format(ip, port))
    finally:
        server.close()
    return 0


def check_open_acion1(timeout):
    try:
        while True:
            ipport = queue_todo.get_nowait()
            r = getPortStatus(ipport['ip'], ipport['port'], timeout)
            tagnameValue[ipport['tagname']] = r
            # time.sleep(0.1)
    except queue.Empty as e:
        pass
    finally:
        latch.countDown()


def loadCfgInfo():
    with open("port_scan.cfg", mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    logger.info("读取到的配置文件：" + str(lines))

    ports_list = []
    isBase = False
    isTagPrefix = False
    for line in lines:

        if (not line or line == "" or line == '\n' or line.isspace()):
            continue

        if (line.startswith("[BASE]")):
            isBase = True
            isTagPrefix = False
            continue
        if (line.startswith("[PORT]")):
            isBase = False
            isTagPrefix = True
            continue
        if (isBase):
            if (line.startswith("collect_frequency")):
                collect_frequency = int(line.split("=")[1])
            if (line.startswith("thread_pool_max_workers")):
                thread_pool_max_workers = int(line.split("=")[1])
            if (line.startswith("telnet_timeout")):
                telnet_timeout = int(line.split("=")[1])
            if (line.startswith("post_rt_url")):
                post_rt_url = str(line.split("=")[1]).split()[0]
            if (line.startswith("post_his_url")):
                post_his_url = str(line.split("=")[1]).split()[0]

        if (isTagPrefix):
            if (line.index(",") > 0):
                ddd = line.split(",")
                ports_list.append({"ip": ddd[0], "port": ddd[1], "tagname": ddd[2].split()[0]})

    logger.info("collect_frequency= %d" % collect_frequency)
    logger.info("post_rt_url= %s" % post_rt_url)
    logger.info("post_his_url= %s" % post_rt_url)
    logger.info("ports_list: %s" % str(ports_list))
    return (collect_frequency, thread_pool_max_workers, telnet_timeout, post_rt_url, post_his_url, ports_list)

# 放采集的数据
tagnameValue={}
def post2redis():
    r = requests.post(post_rt_url, data={"keyVal":json.dumps(tagnameValue)})
    logger.debug("post2redis: " + json.dumps(tagnameValue) + ", r=" + str(r))

def post2his(datatime):
    dArr=[]
    for tag in tagnameValue:
        dArr.append({"tagName":tag, "time": datatime, "value": tagnameValue[tag]})
    r = requests.post(post_his_url, data={"json": json.dumps(dArr)})
    logger.debug("post2his: " + json.dumps(dArr) + ", r=" + str(r))

def do_his():
    tt = datetime.now().strftime("%Y-%m-%d %H:%M") + ":00"
    logger.debug("##### do post2his ##### " + tt)
    post2his(tt)
    threading.Timer(60*5, do_his).start()
    # threading.Timer(10, do_his).start()

def do_start_his():
    nowTime = datetime.now()
    logger.info("当前时间：" + nowTime.strftime("%Y-%m-%d %H:%M:%S"))
    nextTT = (nowTime + timedelta(minutes=(5 - (nowTime.minute % 5))))
    next5T = nextTT.strftime("%Y-%m-%d %H:%M")+":00"
    logger.info("下个5分钟的时间：" + next5T)

    nT = datetime(nextTT.year, nextTT.month, nextTT.day, nextTT.hour, nextTT.minute, 0)
    startAfter = (nT-nowTime).seconds + 5
    logger.info(str(startAfter) + "秒后开始执行历史数据入库")
    threading.Timer(startAfter, do_his).start()



if __name__ == '__main__':

    cfg_tuple = loadCfgInfo()

    intervalTime = cfg_tuple[0]
    maxWork = cfg_tuple[1]
    telnet_timeout = cfg_tuple[2]
    post_rt_url = cfg_tuple[3]
    post_his_url = cfg_tuple[4]
    ports = cfg_tuple[5]

    do_start_his()

    queue_todo = queue.Queue()
    pool = ThreadPoolExecutor(max_workers=maxWork)

    latch = CountDownLatch(maxWork)

    while True:
        logger.debug("### check_port_open ## ss ## start onece")
        for ip in ports:
            queue_todo.put(ip)

        latch.count = maxWork

        for i in range(maxWork):
            pool.submit(check_open_acion1, telnet_timeout)

        latch.wait()
        post2redis()
        logger.debug("### check_port_open ## ee ## end onece")
        time.sleep(intervalTime)





