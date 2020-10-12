#!/usr/bin/env python

# -*- *************** -*-
# @File  : client.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-12 17:51
# -*- *************** -*-


# 下面的客户端程序也非常简单，它仅仅使用 socket 建立与指定 IP 地址和端口的连接，井从
# socket 中获取服务器端发送的数据 。
import socket

# 创建socket对象
s = socket.socket()
# 连接远程服务器
s.connect(('127.0.0.1', 30000))
print('--%s--' % s.recv(1024).decode('utf-8'))
s.close()
