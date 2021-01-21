#!/usr/bin/env python

# -*- *************** -*-
# @File  : Server.py
# @Description : 
# @Author: mql
# @Time  : 2020/11/26 21:54
# -*- *************** -*-


import socket, threading, CrazyitDict, CrazyitProtocol

from ServerThread import server_target
SERVER_PORT = 30000
# 使用 CrazyitDict 来保存每个用户名和对应 socket 之间的映射关系
clients = CrazyitDict.CrazyitDict()
# 创建 socket 对象
s = socket.socket()
try:
    # 将 socket 绑定到本地IP地址和端口
    s.bind(('127.0.0.1', SERVER_PORT))
    # 服务器开始监听来自客户端的连接
    s.listen()
    # 采用死循环不断地接收来自客户端的请求
    while True:
        # 每当接收到客户端 socket 的请求时，该方法都将返回对应的 socket 和远程地址
        c, addr = s.accept()
        threading.Thread(target=server_target, args=(c, clients)).start()
    # 如果抛出异常
except:
    print("服务器启动失败，是否端口%d已被占用？" % SERVER_PORT)