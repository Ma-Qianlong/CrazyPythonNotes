#!/usr/bin/env python

# -*- *************** -*-
# @File  : from_import_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/03/8 18:05
# -*- *************** -*-


# 导入 sys 模块内的 argv，winver 成员
from sys import argv, winver
# 使用导入成的语法，直接使用成员名访问
print(argv[0])
print(winver) # sys的winver成员记录了当前Python的版本号
