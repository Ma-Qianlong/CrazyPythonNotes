#!/usr/bin/env python

# -*- *************** -*-
# @File  : os_rmdir_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-30 17:57
# -*- *************** -*-


import os

path = 'my_dir'
# 直接删除当前目录下的子目录
os.rmdir(path)

path = 'abc/xyz/wawa'
# 递归删除目录
os.removedirs(path)