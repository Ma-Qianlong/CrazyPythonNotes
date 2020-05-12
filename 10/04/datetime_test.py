#!/usr/bin/env python

# -*- *************** -*-
# @File  : datetime_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/5/12 16:56
# -*- *************** -*-


import datetime


# 获取两日期间的所有日期
def getEveryDay(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        #print(date_str)
        date_list.append(date_str)
        timespan = datetime.timedelta(days=1)
        #print(timespan)
        begin_date += timespan

    return date_list

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
    begin_time = datetime.datetime.strptime(begin_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    while begin_time <= end_time:
        time_str = begin_time.strftime('%Y-%m-%d %H:%M:%S')
        time_list.append(time_str)
        begin_time += datetime.timedelta(minutes=durion)
    return time_list

print(getEveryDay("2019-12-12", '2020-03-15'))

print(getEveryMinute('2020-03-10 00:00:00', '2020-03-15 23:00:00', 5))
