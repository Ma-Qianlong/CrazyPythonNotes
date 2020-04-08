#!/usr/bin/env python

# -*- *************** -*-
# @File  : from_import_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/4/8 18:05
# -*- *************** -*-


# 导入 sys 模块内的 argv 成员, 并未其指定别名
from sys import argv as v
# 使用导入成的语法，直接使用成员的别名访问
print(v[0])
