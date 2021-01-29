#!/usr/bin/env python

# -*- *************** -*-
# @File  : client.py
# @Description : 
# @Author: mql
# @Time  : 2021/1/28 17:41
# -*- *************** -*-


import selectors, socket, threading

# 创建默认的 selectors 对象
sel = selectors.DefaultSelector()


# 负责监听 “有数据可读” 事件的函数
def read(conn, mask):
    data = conn.recv(1024)  # should bu ready
    if data:
        print(data.decode('utf-8'))
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


# 创建 socket 对象
s = socket.socket()
# 连接远程服务器
s.connect(('127.0.0.1', 30000))
# 设置该 socket 是非阻塞的
s.setblocking(False)
# 使用 sel 为 s 的 EVENT_READ 事件注册 read 监听函数
sel.register(s, selectors.EVENT_READ, read)  # ①


# 定义不断读取用户的键盘输入内容的函数
def keyboard_input(s):
    while True:
        line = input('')
        if line is None or line == 'exit':
            break
        # 将用户的键盘输入内容写入socket中
        s.send(line.encode('utf-8'))


# 采用线程不断的读取用户的键盘输入内容
threading.Thread(target=keyboard_input, args=(s,)).start()
while True:
    # 获取事件
    events = sel.select()
    for key, mask in events:
        # 使用 key 的 data 属性获取为该事件注册的监听函数
        callback = key.data
        # 调用监听函数，使用 key 的 fileobj 属性获取被监听的 socket 对象
        callback(key.fileobj, mask)

# 上面程序中的①号粗体字代码为 socket 的 EVENT_READ 事件注册了 read（）监听函数，这样每
# 当 socket 中有数据可读时，程序就会触发 read（）函数来读取 socket 中的数据。
# 程序最后也采用死循环不断地调用 selectors 的 se lect（）方法“监测”事件，每当监测到相应的
# 事件之后，程序就会调用对应的事件监昕函数。
# 先运行上面的服务器端程序，该程序运行后只是作为服务器，看不到任何输出信息 。 再运行多
# 个客户端程序一一相当于启动多个聊天室客户端登录该服务器 。 接下来可以在任何一个客户端通过
# 键盘输入一些内容，然后按回车键，即可在所有客户端（包括自己）的控制台上接收到刚刚输入的
# 内容 。 这也是一个粗略的 C/S 结构的聊天室应用。
