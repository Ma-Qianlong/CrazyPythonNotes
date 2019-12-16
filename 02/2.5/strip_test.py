#!/usr/bin/env python

# -*- *************** -*-
# @File  : strip_test.py
# @Description : 删除空白相关
# @Author: mql
# @Time  : 2019/12/16 23:31
# -*- *************** -*-

s = ' this is a puppy '
# 删除左边空白
print(s.lstrip())
# 删除右边空白
print(s.rstrip())
# 删除两边空白
print(s.strip())
# 输出s s并没有变化， python中的str对象是不可变的，上述生成的都是副本
print(s)

# 删除字符串前后指定字符串
s2 = 'i think it is a scarecrow'
# 删除左边的i、t、o、w字符
print(s2.lstrip("itow"))
# 删除右边的i、t、o、w字符
print(s2.rstrip("itow"))
# 删除两边的i、t、o、w字符
print(s2.strip("itow"))


