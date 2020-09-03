#!/usr/bin/env python

# -*- *************** -*-
# @File  : Event_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-03 13:53
# -*- *************** -*-


import threading
import time

event = threading.Event()
def cal(name):
    # 等待事件，进入等待阻塞状态
    print("%s 启动" % threading.current_thread().getName())
    print("%s 准备开始计算！" % name)
    event.wait() # ①
    # 收到事件后进入运行状态
    print("%s 收到通知了。" % threading.current_thread().getName())
    print("%s 正式开始计算！" % name)

# 创建并启动两个线程，它们都会在①号代码处等待
threading.Thread(target=cal, args=('甲',)).start()
threading.Thread(target=cal, args=('乙',)).start()
time.sleep(2) # ②
print("----------------")
# 发出事件
print('主线程发出事件')
event.set()

#   上面程序以 cal（）函数为 target，创建井启动了两个线程 。 由于 cal（）函数在①号代码处调用了
# Event 的 wait（），因此两个线程执行到①号代码处都会进入阻塞状态：即使主线程在②号代码处被
# 阻塞，两个子线程也不会向下执行 。
#   直到主程序执行到最后一行 ： 程序调用了 Event 的 set（）方法将 Event 的内部旗标设直为 True,
# 并唤醒所有等待的线程，这两个线程才能向下执行。