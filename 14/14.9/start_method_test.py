#!/usr/bin/env python

# -*- *************** -*-
# @File  : start_method_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/9/29 15:57
# -*- *************** -*-


import multiprocessing
import os


def foo(q):
    print('被启动的新线程：（%s）' % os.getpid())
    q.put('Python')


if __name__ == "__main__":
    # 设置使用fork方式启动进程
    # multiprocessing.set_start_method('fork')  # 只能UNIX平台
    multiprocessing.set_start_method('spawn')  # 只能Windows平台
    q = multiprocessing.Queue()
    # 创建进程
    mp = multiprocessing.Process(target=foo, args=(q,))
    # 启动进程
    mp.start()
    # 获取队列中的消息
    print((q.get()))
    mp.join()
