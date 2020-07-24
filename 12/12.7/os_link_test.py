#!/usr/bin/env python

# -*- *************** -*-
# @File  : os_link_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-07-24 11:19
# -*- *************** -*-


import os

# 为 os.link_test.py 文件创建快捷方式
os.symlink("os_link_test.py", 'tt')
# 为 os.link_test.py 文件创建硬链接(在Windows系统中就是复制文件)
os.link('os_link_test.py', 'dst')
