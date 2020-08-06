#!/usr/bin/env python

# -*- *************** -*-
# @File  : invoke_run.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-06 16:02
# -*- *************** -*-


import threading


# 定义一个普通的action方法，该方法准备作为线程执行体
def action(max):
    for i in range(max):
        # 调用 threading 模块的 current_thread() 函数获取当前线程
        # 调用线程对象的 getName() 方法获取当前线程的名字
        print(threading.current_thread().getName() + " " + str(i))


for i in range(100):
    # 调用 threading 模块的 current_thread() 函数获取当前线程
    print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        # 直接调用线程对象的 run()方法
        # 系统会把线程对象当成普通对象，把 run （）方法当成普通方法
        # 所以下面两行代码并不会启动两个线程，而是依次执行两个 run （）方法
        threading.Thread(target=action, args=(100,)).run()
        threading.Thread(target=action, args=(100,)).run()

# 上面程序在创建线程对象后，直接调用了线程对象的 run（）方法（如粗体字代码所示），程序运
# 行的结果是整个程序只有一个线程：主线程。还有一 点需要指出 ，如果直接调用线程对象的 run()
# 方法，则在 run（）方法中不能直接通过 name 属性（ getName（）方法）来获取当前执行线程的名字，
# 而是需要使用 threading. current_thread（）函数先获取当前线程，然后再i周用线程对象的 name 属性来
# 获取线程的名字。
# 通过上面程序不难看出，启动线程的正确方法是调用 Thread 对象的 start（）方法，而不是直接调
# 用 run（）方法：否则就变成单线程程序了。
# 需要指出的是，在调用线程对象的 run（）方法之后，该线程己经不再处于新建状态，不要再次
# 调用线程对象的 start（）方法。