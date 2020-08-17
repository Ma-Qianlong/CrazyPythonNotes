#!/usr/bin/env python

# -*- *************** -*-
# @File  : Account1.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-13 14:15
# -*- *************** -*-


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账号编号和账号和账户余额两个成员变量
        self.account_no = account_no
        self.balance = balance