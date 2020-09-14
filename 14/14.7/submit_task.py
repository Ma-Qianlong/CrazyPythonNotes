#!/usr/bin/env python

# -*- *************** -*-
# @File  : submit_task.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-14 9:59
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
pool = ThreadPoolExecutor(max_workers=2)
# 向线程池中提交一个任务， 50 会作为 action（）函数的参数
futrue1 = pool.submit(action, 50)
# 向线程池中再提交一个任务， 100 会作为 action（）函数的参数
futrue2 = pool.submit(action, 100)

# 判断 future1 代表的任务是否结束
print(futrue1.done())
time.sleep(3)
# 判断 future2 代表的任务是否结束
print(futrue2.done())

# 查看 future1 代表的任务返回的结果
print(futrue1.result())
# 查看 future2 代表的任务返回的结果
print(futrue2.result())

# 关闭线程池
pool.shutdown()