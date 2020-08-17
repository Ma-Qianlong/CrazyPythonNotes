#!/usr/bin/env python

# -*- *************** -*-
# @File  : Account1.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-17 14:15
# -*- *************** -*-


import threading
import time

class Account1:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号和账户余额两个变量
        self.account_no = account_no
        self._blance = balance
        self.lock = threading.RLock() # 注意此处括号

    # 因为账户余额不允许随便修改，所以只为self.blance提供getter方法
    def getBalance(self):
        return self._blance

    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            if self._blance >= draw_amount:
                print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + " " + threading.current_thread().name \
                      + "取钱成功！吐出钞票：" + str(draw_amount))
                time.sleep(1)  # 此处为黑体
                # 修改余额
                self._blance -= draw_amount
                print("\t余额为：" + str(self._blance))

            else:
                print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + " " + threading.current_thread().name \
                      + "取钱失败！余额不足！")
        finally:
            # 修改完成，释放锁
            self.lock.release()
