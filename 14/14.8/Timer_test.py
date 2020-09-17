#!/usr/bin/env python

# -*- *************** -*-
# @File  : Timer_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-17 10:37
# -*- *************** -*-


from threading import Timer

def hello():
    print("hello, world")

# 指定10s后执行hello函数
t = Timer(10.0, hello)
t.start()