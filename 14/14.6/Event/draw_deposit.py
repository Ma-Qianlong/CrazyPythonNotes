#!/usr/bin/env python

# -*- *************** -*-
# @File  : draw_deposit.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-03 11:06
# -*- *************** -*-


import threading
import Account

# 定义一个函数，模拟重复 max 次执行取钱操作
def draw_many(account, draw_amount, max):
    for i in range(max):
        account.draw(draw_amount)

# 定义一个函数，模拟重复 max 次执行存款操作
def deposit_many(account, deposit_amount, max):
    for i in range(max):
        account.deposit(deposit_amount)

# 创建一个账号
acct = Account.Account("1234567", 0)
# 创建并启动一个取钱线程
threading.Thread(name="取钱者", target=draw_many, args=(acct, 800, 100)).start()
# 创建并启动一个存款线程
threading.Thread(name="存款者甲", target=deposit_many, args=(acct, 800, 100)).start()
threading.Thread(name="存款者乙", target=deposit_many, args=(acct, 800, 100)).start()
threading.Thread(name="存款者丙", target=deposit_many, args=(acct, 800, 100)).start()