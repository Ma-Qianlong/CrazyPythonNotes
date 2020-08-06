#!/usr/bin/env python

# -*- *************** -*-
# @File  : start_dead.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-06 16:06
# -*- *************** -*-


import threading

# 定义一个普通的action方法，该方法准备作为线程执行体
def action(max):
    for i in range(max):
        # 调用 threading 模块的 current_thread() 函数获取当前线程
        # 调用线程对象的 getName() 方法获取当前线程的名字
        print(threading.current_thread().getName() + " " + str(i))

# 创建线程对象
sd = threading.Thread(target=action, args=(100,))
for i in range(300):
    # 调用threading.current_thread()来获取当前线程
    print(threading.current_thread().name + " " + str(i))
    if i == 20:
        # 启动线程
        sd.start()
        # 判断启动后线程的的is_alive()值， 输出True
        print(sd.is_alive())
    # 当线程处于新建、死亡两种状态时 ， is_alive （）方法返回 False
    # 当 i > 20 时 ， 该线程肯定已经启动过了， 如果 sd.is_alive（）为 False
    # 那么就处于死亡状态了
    if i > 20 and not(sd.is_alive()):
        # 试图再次启动线程
        sd.start()


# 上面程序中的粗体字代码试图在线程己死亡的情况下再次调用 start（）方法来启动该线程 。 运行
# 上面程序，将引发 RuntimeError 异常 ， 这表明处于死亡状态的线程无法再次运行。