#!/usr/bin/env python

# -*- *************** -*-
# @File  : first_process.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-17 17:37
# -*- *************** -*-


import multiprocessing
import os


# 定义一个普通的 action 函数，该函数准备作为进程执行体
def action(max):
    for i in range(max):
        print("(%s)子进程(父进程：（%s）): %d" % (os.getpid(), os.getppid(), i))


if __name__ == "__main__":
    # 下面是主程序(也是主程序)
    for i in range(100):
        print("（%s）主进程： %d" % (os.getpid(), i))
        if i == 20:
            # 创建并启动第一个进程
            mp1 = multiprocessing.Process(target=action, args=(100,))
            mp1.start()

            # 创建并启动第二个进程
            mp2 = multiprocessing.Process(target=action, args=(100,))
            mp2.start()
            mp2.join()

    print('主进程执行完毕！')