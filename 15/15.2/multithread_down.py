#!/usr/bin/env python

# -*- *************** -*-
# @File  : multithread_down.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-12 14:11
# -*- *************** -*-

from DownUtil import *
import time

du = DownUtil("http://127.0.0.1/cmder.zip", "D://my_du.zip", 5)

sT = time.time()

du.download()

def show_process():
    print("已完成： %.2f %%, 已耗时(s)：%.3f" % (du.get_complete_rate()*100, time.time() - sT))
    global t
    if du.get_complete_rate() < 1:
        # 通过定时器启动 0.1s 后执行 show_process 函数
        threading.Timer(0.1, show_process).start()
    else:
        print("下载完成！")
# 通过定时器启动 0.1s 后执行 show_process 函数
threading.Timer(0.1, show_process).start()


