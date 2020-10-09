#!/usr/bin/env python

# -*- *************** -*-
# @File  : Context_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/9/29 16:08
# -*- *************** -*-


import multiprocessing
import os


def foo(q):
    print('被启动的新线程：（%s）' % os.getpid())
    q.put('Python')


if __name__ == "__main__":
    # 设置使用fork方式启动进程, 并获取Context对象
    # ctx = multiprocessing.get_context('fork')  # 只能UNIX平台
    ctx = multiprocessing.get_context('spawn')  # 只能Windows平台
    # 接下来就可以使用 Context 对象来代替 mutliprocessing 模块
    q = ctx.Queue()
    # 创建进程
    mp = ctx.Process(target=foo, args=(q,))
    # 启动进程
    mp.start()
    # 获取队列中的消息
    print(q.get())
    mp.join()
