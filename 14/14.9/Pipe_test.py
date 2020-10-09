#!/usr/bin/env python

# -*- *************** -*-
# @File  : Pipe_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-09 18:17
# -*- *************** -*-


import multiprocessing


def f(conn):
    print('(%s) 进程开始发送数据。。。' % multiprocessing.current_process().pid)
    # 使用 conn 发送数据
    conn.send('Python')


if __name__ == '__main__':
    # 创建Pipe, 该函数返回两个 PipeConnection 对象
    parent_conn, child_conn = multiprocessing.Pipe()
    # 创建子进程
    p = multiprocessing.Process(target=f, args=(child_conn,))
    # 启动子进程
    p.start()
    print('(%s) 进程开始接收数据。。。' % multiprocessing.current_process().pid)
    # 通过 conn 读取数据
    print(parent_conn.recv())
    p.join()
