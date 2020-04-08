#!/usr/bin/env python

# -*- *************** -*-
# @File  : from_import_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/4/8 18:05
# -*- *************** -*-


# 导入 sys 模块内的 argv，winver 成员， 并未其指定别名
from sys import argv as v, winver as wv

# 使用导入成的语法，直接使用成员的别名访问
print(v[0])
print(wv)  # sys的winver成员记录了当前Python的版本号


# 在使用 frorn...import 语法时也可一次导入指定模块 内的所有成员，例如如下程序。
# 导入sys模块的所有成员
from sys import *
print(argv[0])
print(winver)

# 需要说明的是，一般不推荐使用"frorn 模块 import * " 这种导入指定模块内成员。这样存在潜在的风险(如重名等)
