#!/usr/bin/env python

# -*- *************** -*-
# @File  : server.py.py
# @Description : 
# @Author: mql
# @Time  : 2021/1/28 16:47
# -*- *************** -*-


import socket

# 创建 socket 对象
s = socket.socket()
# 将 socket 绑定到本机IP地址和端口
s.bind(('127.0.0.1', 30000))
# 服务端开始监听来自客户端的连接
s.listen()
# 每当接收到客户端socket请求时，该方法返回对应的socket和远程地址
skt, addr = s.accept()
skt.send("服务器第一行数据源".encode('utf-8'))
skt.send("服务器第二行数据源".encode('utf-8'))
# 关闭 socket 的输出部分，表明数据数据已经结束
skt.shutdown(socket.SHUT_WR)
while True:
    # 从socket中读取数据
    line = skt.recv(2048).decode('utf-8')
    if line is None or line == '':
        break
    print(line)
skt.close()