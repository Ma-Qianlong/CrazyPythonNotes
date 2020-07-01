#!/usr/bin/env python

# -*- *************** -*-
# @File  : os.chmod_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-30 19:06
# -*- *************** -*-


import os, stat

# 将 os.chmod_test.py 文件改为只读的
os.chmod('os.chmod_test.py', stat.S_IREAD)
# 判断是否可写
ret = os.access("os.chmod_test.py", os.W_OK)
print("os.W_OK - 返回值：", ret)