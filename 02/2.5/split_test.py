#!/usr/bin/env python

# -*- *************** -*-
# @File  : split_test.py
# @Description : 字符串分割、连接相关方法
# @Author: mql
# @Time  : 2019/12/17 22:51
# -*- *************** -*-


s = 'crazyit.org is a good site'
# 空格分割
print(s.split())
# 空格分割，最多分两词
print(s.split(" ", 2))
print(s.split(None, 2))

# 点分割
print(s.split("."))

mylist = s.split();
# 用分隔符连接
print('/'.join(mylist))
print(str.join('/', mylist))
print(','.join(mylist))