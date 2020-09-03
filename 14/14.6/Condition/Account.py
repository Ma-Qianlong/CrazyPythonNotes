#!/usr/bin/env python

# -*- *************** -*-
# @File  : Account.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-03 10:50
# -*- *************** -*-


import threading

class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号和余额两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.cond = threading.Condition()
        # 定义代表是否已经存钱的旗标
        self._flag = False

    # 因账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalbace(self):
        return self._balance

    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁，相当于调用Condition绑定的Lock的acquire()
        self.cond.acquire()
        try:
            # 如果 self._flag 为 False ，表明账户中还没有人存钱进去，取钱方法被阻塞
            if not self._flag:
                self.cond.wait()
            else:
                # 执行取钱操作
                print(threading.current_thread().name + "取钱： " + str(draw_amount))
                self._balance -= draw_amount
                print("账户余额为：" + str(self._balance), end="\n\n*********\n")
                # 将表明账户中是否有存款的旗标设为False
                self._flag = False
                # 唤醒其他线程
                self.cond.notify_all()
        # 使用finally块来释放锁
        finally:
            self.cond.release()

    def deposit(self, deposit_amount):
        self.cond.acquire()
        try:
            if self._flag:
                self.cond.wait()
            else:
                print(threading.current_thread().name\
                      + "存款：" + str(deposit_amount))
                self._balance += deposit_amount
                print("账户余额为：" + str(self._balance), end="\n\n")
                self._flag = True
                self.cond.notify_all()
        finally:
            self.cond.release()
