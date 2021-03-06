#!/usr/bin/env python

# -*- *************** -*-
# @File  : MyClient.py
# @Description : 
# @Author: mql
# @Time  : 2020/11/9 20:18
# -*- *************** -*-


import socket
import threading

# 创建socket对象
s = socket.socket()
# 连接远程服务器
s.connect(('127.0.0.1', 30000))
s.setblocking(True)
def read_from_server(s):
    print("!!!!!!!!!!!!!!!")
    while True:
        # print(1111111111111)
        line = s.recv(2048).decode('utf-8')
        if len(line) > 0:
            # print(2222222222222)
            print(line)
# 客户端启动线程不断的读取来自服务器端的数据
threading.Thread(target=read_from_server, args=(s, )).start() # ①
while True:
    line = input('')
    if line is None or line == 'exit':
        break
    # 将用户输入的内容写入到socket中
    s.send(line.encode('utf-8'))