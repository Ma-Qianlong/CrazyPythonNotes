#!/usr/bin/env python

# -*- *************** -*-
# @File  : Client.py
# @Description : 
# @Author: mql
# @Time  : 2021/1/21 10:11
# -*- *************** -*-


import socket, threading, CrazyitProtocol, os
from  tkinter import simpledialog
import time

SERVER_PORT = 30000

# 定义一个读取键盘输入内容， 并向网络中发送的函数
def read_send(s):
    # 采用死循环不断地读取键盘输入内容
    while True:
        line = input('')
        if line is None or line == 'exit':
            break
        # 如果发送信息中有冒号，且以//开头， 则认为像发送私聊信息
        if ":" in line and line.startswith("//"):
            line = line[2:]
            s.send((CrazyitProtocol.PRIVATE_ROUND
                    + line.split(":")[0] + CrazyitProtocol.SPLIT_SIGN
                    + line.split(":")[1] + CrazyitProtocol.PRIVATE_ROUND).encode('utf-8'))
        else:
            s.send((CrazyitProtocol.MSG_ROUND + line
                    + CrazyitProtocol.MSG_ROUND).encode('utf-8'))

# 创建socket对象
s = socket.socket()
try:
    # 连接远程服务器
    s.connect(('127.0.0.1', SERVER_PORT))
    tip = ""
    # 采用循环不停的弹出对话框要求用户驶入用户名
    while True:
        user_name = input(tip + "输入用户名:\n") # ①
        # 在用户输入的用户名前后增加协议字符串后发送
        s.send((CrazyitProtocol.USER_ROUND + user_name + CrazyitProtocol.USER_ROUND).encode('utf-8'))
        time.sleep(0.2)
        # 读取服务器的相应信息
        result = s.recv(2048).decode('utf-8')
        if result is not None and result != '':
            # 如果用户名重复，则开始下一次循环
            if result == CrazyitProtocol.NAME_REP:
                tip = "用户名重复！请重新输入"
                continue
                # 如果服务器端返回登录成功的信息，则结束循环
            if result == CrazyitProtocol.LOGIN_SUCCESS:
                break
# 捕获到异常，关闭网络资源，并退出该程序
except:
    print("网络异常！请重新登录！")
    s.close()
    os._exit(1)

def client_target(s):
    try:
        # 不断地从socket中读取数据，并将这些数据打印出来
        while True:
            line = s.recv(2048).decode('utf-8')
            if line is not None:
                print(line)
            # ＃本例仅打印出从服务器端读取到的内容。实际上，此处可以更复杂，如果希望
            # ＃客户端能看到聊天室的用户列表，则可以让服务器端在每次有用户 登录、用户
            # ＃退出时，都将所有的用户列表信息向客户端发送一遍。为了区分服务器端发送
            # ＃的是聊天信息还是用户列表信息，服务器端也应该在要发送的信息前后添加协
            # ＃议字符串，客户端则根据协议字符串的不同而进行不同的处理
            # ＃更复杂的情况是
            # ＃如果两端进行游戏，则还有可能发送游戏信息 。 例如两端进行五子棋游戏，则
            # ＃需要发送下棋坐标信息等，服务器端同样需要在这些下棋坐标信息前后添加协
            # ＃议字符串，然后再发送，客户端就可以根据该信息知道对手的下棋坐标了
        # 用 finally 块来关闭该线程对应的 socket
    finally:
        s.close()

# 启动客户端线程
threading.Thread(target=client_target, args=(s,)).start()
read_send(s)