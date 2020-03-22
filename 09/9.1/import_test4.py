#!/usr/bin/env python

# -*- *************** -*-
# @File  : import_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/3/22 23:12
# -*- *************** -*-


# 导入sys,os两个模块, 并分别指定别名s, o
import sys as s, os as o

# 使用模块别名作为前缀来访问模块中的成员
print(s.argv[0])
print(o.sep)
