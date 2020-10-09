#!/usr/bin/env python

# -*- *************** -*-
# @File  : pool_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-09 13:59
# -*- *************** -*-


import multiprocessing
import time
import os


def action(name='default'):
    print('(%s)进程正在执行，参数为：%s' % (os.getpid(), name))
    time.sleep(3)


if __name__ == '__main__':
    # 创建包含 4 个进程的进程池
    pool = multiprocessing.Pool(processes=4)
    # 将 action 分三次提交给进程池
    pool.apply_async(action)
    pool.apply_async(action, args=('位置参数',))
    pool.apply_async(action, kwds={'name':'关键参数'})
    pool.close()
    pool.join()
