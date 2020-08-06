#!/usr/bin/env python

# -*- *************** -*-
# @File  : deamon_thread.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-06 16:31
# -*- *************** -*-


import threading

# 定义一个普通的action方法，该方法准备作为线程执行体
def action(max):
    for i in range(max):
        print(threading.current_thread().getName() + " " + str(i))

t = threading.Thread(target=action, args=(100,), name="后台线程")
# 将此线程设置成后台线程
# 也可以在创建 Thread 对象时通过 daemon 参数将其设置为后台线程
t.daemon = True
# 启动后台线程
t.start()
for i in range(10):
    print(threading.current_thread().name + " " + str(i))

#  ------ 程序执行到此处，前台线程（主线程）结束 ------
# 后台线程也应该随之结束