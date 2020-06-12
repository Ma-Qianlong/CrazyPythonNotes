#!/usr/bin/env python

# -*- *************** -*-
# @File  : readlines_test.py.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-12 17:28
# -*- *************** -*-

# 使用 readlines（）方法一次读取文件 内所有行 。
import codecs

# 指定使用UTF-8字符集来读取文件内容
f = codecs.open("readlines_test.py", 'r', 'utf-8', buffering=True)
# 使用readlines() 读取所有行，返回所有组成的列表
for l in f.readlines():
    print(l, end='')
f.close()