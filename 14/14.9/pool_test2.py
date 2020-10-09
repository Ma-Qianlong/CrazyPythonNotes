#!/usr/bin/env python

# -*- *************** -*-
# @File  : pool_test2.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-09 14:15
# -*- *************** -*-


import multiprocessing
import os


# 定义一个准备作为进程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print('(%s)进程正在执行：%d' % (os.getpid(), i))
        my_sum += i

    return my_sum


if __name__ == '__main__':
    # 创建一个包含4个进程的进程池
    with multiprocessing.Pool(processes=4) as pool:
        # 使用进程执行map计算
        # 后面的元组有3个元素，因此程序启动3个进程来执行action函数
        results = pool.map(action, (50, 100, 150))
        print('---------------')
        for r in results:
            print(r)
