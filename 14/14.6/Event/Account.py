#!/usr/bin/env python

# -*- *************** -*-
# @File  : Account.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-03 14:21
# -*- *************** -*-


import threading

class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号和余额两个成员变量
        self.account_no = account_no
        self._balance = balance

        self.lock = threading.Lock()
        self.event = threading.Event()

    # 因账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalbace(self):
        return self._balance

    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        # 如果Event内部旗标为True，则表明账户中已有人存钱进去
        if self.event.is_set():
            # 执行取钱操作
            print(threading.current_thread().name + "取钱： " + str(draw_amount))
            self._balance -= draw_amount
            print("账户余额为：" + str(self._balance), end="\n\n*********\n")

            # 将Event内部旗标设置为False
            self.event.clear()
            # 释放锁
            self.lock.release()
            # 阻塞当前线程
            self.event.wait()
        else:
            # 释放锁
            self.lock.release()
            # 阻塞当前线程
            self.event.wait()

    def deposit(self, deposit_amount):
        self.lock.acquire()
        if not self.event.is_set():
            print(threading.current_thread().name \
                  + "存款：" + str(deposit_amount))
            self._balance += deposit_amount
            print("账户余额为：" + str(self._balance), end="\n\n")

            self.event.set()
            self.lock.release()
            self.event.wait()
        else:
            self.lock.release()
            self.event.wait()
