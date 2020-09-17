#!/usr/bin/env python

# -*- *************** -*-
# @File  : Timer_test2.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-17 10:37
# -*- *************** -*-


from threading import Timer
import time

count = 0
def print_time():
    print("当前时间：%s" % time.ctime())
    global t, count
    count += 1

    if count < 10:
        t = Timer(1, print_time)
        t.start()

t = Timer(1, print_time)
t.start()