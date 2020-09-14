#!/usr/bin/env python

# -*- *************** -*-
# @File  : add_done_callback.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-14 10:07
# -*- *************** -*-



from concurrent.futures import ThreadPoolExecutor
import threading
import time

# 线程任务函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))
        my_sum += i
    return my_sum

# 创建一个含有两个线程的线程池
with ThreadPoolExecutor(max_workers=2) as pool:
    # 向线程池中提交一个任务， 50 会作为 action（）函数的参数
    futrue1 = pool.submit(action, 50)
    # 向线程池中再提交一个任务， 100 会作为 action（）函数的参数
    futrue2 = pool.submit(action, 100)

    def get_result(future):
        print(future.result())
    # 为 future1 添加线程完成的回调函数
    futrue1.add_done_callback(get_result)
    # 为 future2 添加线程完成的回调函数
    futrue2.add_done_callback(get_result)
    print('------------------')