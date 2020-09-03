#!/usr/bin/env python

# -*- *************** -*-
# @File  : Queue_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-03 11:29
# -*- *************** -*-


import queue

# 定义一个长度为2的阻塞队列
bq = queue.Queue(2)
bq.put("Python")
bq.put("Python")
print("111111111111111")
bq.put("Python") # 阻塞线程
print("222222222222222")