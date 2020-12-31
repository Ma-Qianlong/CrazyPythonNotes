#!/usr/bin/env python

# -*- *************** -*-
# @File  : test.py
# @Description : 
# @Author: mql
# @Time  : 2020/12/31 10:20
# -*- *************** -*-


import threading


def server_ff():
    print("ff当前线程1：" + threading.current_thread().getName())
    threading.Thread(target=server_ff2).start()
    print("ff当前线程2：" + threading.current_thread().getName())

def server_ff2():
    print("ff2当前线程：" + threading.current_thread().getName())

if __name__ == '__main__':
    threading.Thread(target=server_ff).start()
