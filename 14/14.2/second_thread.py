#!/usr/bin/env python

# -*- *************** -*-
# @File  : second_thread.py
# @Description : 
# @Author: mql
# @Time  : 2020-07-24 17:17
# -*- *************** -*-


import threading


# 通过继承 threading.Thread 类来创建线程类
class FkThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0

    # 重写 run() 方法作为线程执行体
    def run(self):
        while self.i < 100:
            # 调用 threading 模块的 current_thread() 函数获取当前线程
            # 调用线程对象的 getName() 方法获取当前线程的名字
            print(threading.current_thread().getName() + " " + str(self.i))
            self.i += 1


# 下面是主程序（也就是主线程的线程执行体）
for i in range(100):
    # 调用 threading 模块的 current_thread() 函数获取当前线程
    print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        # 创建并启动第一个线程
        t1 = FkThread()
        t1.start()
        # 创建并启动第二个线程
        t2 = FkThread()
        t2.start()

print("主线程执行完成！")
