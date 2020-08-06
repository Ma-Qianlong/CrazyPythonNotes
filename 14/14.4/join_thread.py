#!/usr/bin/env python

# -*- *************** -*-
# @File  : join_thread.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-06 16:25
# -*- *************** -*-


import threading

# 定义一个普通的action方法，该方法准备作为线程执行体
def action(max):
    for i in range(max):
        # 调用 threading 模块的 current_thread() 函数获取当前线程
        # 调用线程对象的 getName() 方法获取当前线程的名字
        print(threading.current_thread().getName() + " " + str(i))


# 启动子线程
threading.Thread(target=action, args=(100,), name="新线程").start()
for i in range(100):
    if i == 20:
        jt = threading.Thread(target=action, args=(100,), name="被Join的线程")
        jt.start()
        # 主线程调用了 jt 线程的join()方法
        # 主线程必须等 jt 执行结束后才会向下执行
        jt.join()
    print(threading.current_thread().name + " " + str(i))