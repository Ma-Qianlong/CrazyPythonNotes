#!/usr/bin/env python

# -*- *************** -*-
# @File  : linecache_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-29 17:29
# -*- *************** -*-


import linecache
import random

# 读取random模块源文件的第3行
print(linecache.getline(random.__file__, 3))
# 读取本程序的第3行
print(linecache.getline('linecache_test.py', 3))
# 读取普通文件的第2行
print(linecache.getline('info.txt', 2))