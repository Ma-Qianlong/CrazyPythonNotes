#!/usr/bin/env python

# -*- *************** -*-
# @File  : open_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-09 18:00
# -*- *************** -*-


# 以默认方式打开文件
f = open('open_test.py')
# 所访问文件的编码方式
print(f.encoding)
# 所访问文件的访问模式
print(f.mode)
# 所访问文件是否已经关闭
print(f.closed)
# 所访问文件对象打开的文件名
print(f.name)
