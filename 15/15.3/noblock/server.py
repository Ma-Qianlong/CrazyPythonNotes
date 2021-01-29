#!/usr/bin/env python

# -*- *************** -*-
# @File  : server.py
# @Description : 
# @Author: mql
# @Time  : 2021/1/28 17:41
# -*- *************** -*-


import selectors, socket

# 创建默认的 selectors 对象
sel = selectors.DefaultSelector()


# 负责监听“有数据可读”事件的函数
def read(skt, mask):
    try:
        # 读取数据
        data = skt.recv(1024)
        if data:
            # 将所读取的数据采用循环向每个 socket 发送一次
            for s in socket_list:
                s.send(data)  # Hope it won't block
        else:
            # 如果socket已被对方关闭， 则关闭socket
            # 并将其从 sokcet_list 列表中删除
            print('关闭', skt)
            sel.unregister(skt)
            skt.close()
            socket_list.remove(skt)
    # 如果捕获到异常， 则将该 socket 关闭，并将其从 socket_list 列表中删除
    except:
        print('关闭', skt)
        sel.unregister(skt)
        skt.close()
        socket_list.remove(skt)


socket_list = []


# 负责监听“有客户端连接进来”事件的函数
def accept(sock, mask):
    conn, addr = sock.accept()
    # 使用 socket_list 保存代表客户端的 socket
    socket_list.append(conn)
    conn.setblocking(False)
    # 使用 sel 为 conn 的 EVENT_READ 事件注册 read 监听函数
    sel.register(conn, selectors.EVENT_READ, read)  # ②


sock = socket.socket()
sock.bind(('127.0.0.1', 30000))
sock.listen()
# 设置该 socket 是非阻塞的
sock.setblocking(False)
# 使用 sel 为 sock 的 EVENT_READ 事件注册 accept 监听函数
sel.register(sock, selectors.EVENT_READ, accept)  # ①
# 采用死循环不断提取 sel 的事件
while True:
    events = sel.select()
    for key, mask in events:
        # 使用 key 的 data 属性获取为该事件注册的监听函数
        callback = key.data
        # 调用监昕函数，使用 key 的 fileobj 属性获取被监听的 socket 对象
        callback(key.fileobj, mask)

# 上面程序中定义了两个监听器函数 ： accept（）和 read（）， 其中 accept（）函数作为“有客户端连接
# 进来”事件的监昕函数，主程序中的①号粗体字代码负责为 socket 的 selectors.EVENT READ 事件
# 注册该函数； read（）函数则作为“有数据可读”事件的监听函数，如 accept（）函数中的②号粗体字代
# 码所示 。
# 通过上面这种方式，程序避免了采用死循环不断地调用 socket 的 accept（）方法来接受客户端连
# 接，也避免了采用死循环不断地调用 socket 的 recv（）方法来接收数据 。 socket 的 accept（）、 recv（）方
# 法调用都是写在事件监昕函数中的，只有当事件（如“有客户端连接进来”事件、“有数据可读”
# 事件）发生时， accept（）和 recv（）方法才会被调用，这样就避免了阻塞式编程。
# 为了不断地提取 selectors 中的事件，程序最后使用 一个死循环不断地调用 selectors 的 select()
# 方法“监测”事件，每当监测到相应的事件之后，程序就会调用对应的事件监听函数。
