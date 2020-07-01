#!/usr/bin/env python

# -*- *************** -*-
# @File  : os_mkdir_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-30 17:53
# -*- *************** -*-


import os

path = 'my_dir'
# 直接在当前目录下创建子目录
os.mkdir(path, 0O755)

path = 'abc/xyz/wawa'
# 递归创建目录
os.makedirs(path, 0O755)