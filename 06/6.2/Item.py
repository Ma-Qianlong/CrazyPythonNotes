#!/usr/bin/env python

# -*- *************** -*-
# @File  : Item.py
# @Description : 
# @Author: mql
# @Time  : 2020/1/16 10:28
# -*- *************** -*-

# Python 同样允许在类范围内放置可执行代码——当 Python 执行该类
# 定义肘，这些代码同样会获得执行的机会。
class Item:
    # 直接在类命名空间中放置可执行代码
    print('正在定义Item类')
    for i in range(10):
        if i % 2 == 0:
            print('偶数：', i)
        else:
            print('奇数：', i)
