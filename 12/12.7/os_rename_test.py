#!/usr/bin/env python

# -*- *************** -*-
# @File  : os_rename_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-30 17:59
# -*- *************** -*-


import os

path = 'my_dir'
# 直接删除当前目录下的子目录
os.rename(path, 'you_dir')

path = 'abc/xyz/wawa'
# 递归删除目录
os.renames(path, 'foo/bar/haha')