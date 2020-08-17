#!/usr/bin/env python

# -*- *************** -*-
# @File  : draw_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-17 14:59
# -*- *************** -*-


import threading
import Account1

# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 直接调用account对象的drew方法来执行取钱操作
    account.draw(draw_amount)
# 创建一个账户
acct = Account1.Account1("1234567", 1000)
# 使用两个线程模拟从同一个账户中取钱

for i in range(5):
    print("\n### 开始第 %d 轮取钱：" % (i+1))
    th1 = threading.Thread(name="甲", target=draw, args=(acct, 130))
    th2 = threading.Thread(name="乙", target=draw, args=(acct, 200))
    th1.start()
    th2.start()
    th1.join()
    th2.join()