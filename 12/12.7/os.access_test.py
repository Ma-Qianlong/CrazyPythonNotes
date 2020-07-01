#!/usr/bin/env python

# -*- *************** -*-
# @File  : os.access_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-30 18:45
# -*- *************** -*-


import os, sys

# 判断当前目录的权限
ret = os.access('.', os.F_OK|os.R_OK|os.W_OK|os.X_OK)
print('os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值:', ret)
# 判读当前文件的权限
ret = os.access('os.assess_test.py', os.F_OK|os.R_OK|os.W_OK)
print("os.F_OK|os.R_OK|os.W_OK - 返回值:", ret)