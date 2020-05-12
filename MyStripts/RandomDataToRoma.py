#!/usr/bin/env python

# -*- *************** -*-
# @File  : RandomDataToRoma.py
# @Description : 向MySQL数据库模拟随机数据
# @Author: mql
# @Time  : 2020/5/12 17:47
# -*- *************** -*-


import random
from datetime import datetime, timedelta
import pymysql
import time

# 获取俩浮点数之间的伪随机数
def getRandomFloat(sF, eF):
    randomStr = '%.2f' % random.uniform(2.5, 10.0);
    return float(randomStr)

# 获取每几分钟数据
def getEveryMinute(begin_time, end_time, durion):
    '''
    获取每几分钟数据
    :param begin_time: string 开始时间
    :param end_time: string 结束时间
    :param durion: integer 分钟间隔
    :return: list 时间字符串列表
    '''
    time_list = []
    begin_time = datetime.strptime(begin_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    while begin_time <= end_time:
        time_str = begin_time.strftime('%Y-%m-%d %H:%M:%S')
        time_list.append(time_str)
        begin_time += timedelta(minutes=durion)
    return time_list

# 向数据库写数据，datas元组
def exec_many(datas):
    conn = pymysql.connect(host='192.168.5.249', port=3136, user="root", password="root", database='db-deepctrls-cecep-roma')
    cursor = conn.cursor()
    cursor.executemany('insert into cecep_huawei_roma_test values (%s, %s, %s)', datas)
    conn.commit()
    cursor.close()
    conn.close()


def oneTagDataToMySQL(tagname, sT, eT):
    timeList = getEveryMinute(sT, eT, 5)
    lastTupleList = []
    for time in timeList:
        tupleD = (tagname, time, getRandomFloat(0, 255))
        lastTupleList.append(tupleD)
    print('data list for 【%s】 size: %d' % (tagname, len(lastTupleList)))
    exec_many(tuple(lastTupleList))

oneTagDataToMySQL("test_test_test_test_test", '2020-05-10 00:00:00', '2020-05-10 23:00:00')
print("当前进程使用CPU时间(ns): %d" % time.process_time_ns())