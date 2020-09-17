#!/usr/bin/env python

# -*- *************** -*-
# @File  : thread_local_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-17 10:36
# -*- *************** -*-


import threading
from concurrent.futures import ThreadPoolExecutor

# 定义线程局部变量
mydata = threading.local()


# 定义准备作为相册执行体使用的函数
def action(max):
    for i in range(max):
        try:
            mydata.x += i
        except:
            mydata.x = i
        # 访问 mydata 的 x 的值
        print("%s mydata.x 的值为：%d" % (threading.current_thread().name, mydata.x))

# 使用线程池启动两个子线程
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(action, 10)
    pool.submit(action, 10)
