#!/usr/bin/env python

# -*- *************** -*-
# @File  : compare_operator_test.py
# @Description : 比较运算符
# @Author: mql
# @Time  : 2019/12/17 23:33
# -*- *************** -*-


# > >= < <= == != is isnot
# 主要主要，==比较值本身，is及isnot比较值的引用
# is 要求两个变量来自同一个对象

print('1 和 True 是否相等：', 1 == True)
print('0 和 False 是否相等：', 0 == False)
print(True + False)
print(False - True)

import time

# 取当前时间
a = time.gmtime()
b = time.gmtime()
print(a)
print(id(a))  # 用id()方法获取对象的内存地址
print(b)
print(id(b))
print(a == b)
print(a is b)
