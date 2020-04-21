#!/usr/bin/env python

# -*- *************** -*-
# @File  : billing.py
# @Description : 
# @Author: mql
# @Time  : 2020/4/21 17:37
# -*- *************** -*-


class Item:
    '定义代码商品的Item类'

    def __init__(self, price):
        self.price = price

    def __repr__(self):
        return 'Item[price=%g' % self.price
