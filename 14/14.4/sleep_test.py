#!/usr/bin/env python

# -*- *************** -*-
# @File  : sleep_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-06 16:34
# -*- *************** -*-


import time

for i in range(10):
    print("当前时间：%s" % time.ctime())
    # 调用 sleep() 函数让当前线程暂停 1s
    time.sleep(1)