#!/usr/bin/env python

# -*- *************** -*-
# @File  : os_chdir_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-30 17:49
# -*- *************** -*-


import os

# 获取当前目录
print(os.getcwd())

# 改变当前目录
print(os.chdir('../12.6'))
# 再次获取当前目录
print(os.getcwd())