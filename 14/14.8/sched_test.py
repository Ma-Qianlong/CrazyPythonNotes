#!/usr/bin/env python

# -*- *************** -*-
# @File  : sched_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-17 11:08
# -*- *************** -*-


import sched, time
import threading

# 定义线程调度器
s = sched.scheduler()


# 定义被调度的函数
def print_time(name="dufault"):
    print("%s 的时间：%s" % (name, time.ctime()))


print("主线程：" + time.ctime())
# 指定10s后执行
s.enter(10, 1, print_time)

# 指定5s后执行，优先级为2
s.enter(5, 2, print_time, argument=('位置参数',))
# 指定5s后执行，优先级为1
s.enter(5, 1, print_time, kwargs={'name': '关键参数'})

# 执行调度任务
s.run()
print('主线程：', time.ctime())
