#!/usr/bin/env python

# -*- *************** -*-
# @File  : draw_thread.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-13 14:21
# -*- *************** -*-


import threading
import time
import Account


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 账户余额大于取钱数目
    if account.balance >= draw_amount:
        # 吐出钞票
        print(threading.current_thread().name \
              + "取钱成功！吐出钞票：" + str(draw_amount))

        time.sleep(0.001)  # 此处为黑体
        # 修改余额
        account.balance -= draw_amount
        print("\t余额为：" + str(account.balance))
    else:
        print(threading.current_thread().name \
              + "取钱失败！余额不足！")


# 创建一个账户
acct = Account.Account('1234567', 1000)
# 使用两个线程模拟从同一个账户中取钱
threading.Thread(name="甲", target=draw, args=(acct, 800)).start()
threading.Thread(name="乙", target=draw, args=(acct, 800)).start()
