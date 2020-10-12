#!/usr/bin/env python

# -*- *************** -*-
# @File  : server.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-12 17:46
# -*- *************** -*-

# 服务器端程序非常简单，它仅仅建立 socket，并监听来自客户端的连接，只要客户端连
# 接进来，程序就会向 socket 发送一条简单的信息 。
import socket

# 创建 socket 对象
s = socket.socket()
# 将 socket 绑定本机的 IP 地址和端口
s.bind(('127.0.0.1', 30000))
# 服务端开始监听来自客户端的连接
s.listen()
while True:
    # 每当接收到客户端 socket 的请求时，该方法就返回对应的 socket 和远程地址
    c, addr = s.accept()
    print(c)
    print('连接地址：', addr)
    c.send('您好，服务器向你送--新年祝福！'.encode('utf-8'))
    # 关闭连接
    c.close()