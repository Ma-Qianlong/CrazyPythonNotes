#!/usr/bin/env python

# -*- *************** -*-
# @File  : map_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-14 11:14
# -*- *************** -*-


import threading
from concurrent.futures import ThreadPoolExecutor


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))
        my_sum += i
    return my_sum


# 创建一个包含 4 个线程的线程池
with ThreadPoolExecutor(max_workers=4) as pool:
    # 使用线程执行map计算
    # 后面元组有3个元素， 因此程序启动3个线程来执行action函数
    results = pool.map(action, (50, 100, 150))
    print('------------')
    for r in results:
        print(r)
