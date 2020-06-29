#!/usr/bin/env python

# -*- *************** -*-
# @File  : with_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-22 18:25
# -*- *************** -*-


# 程序使用 with 语句来读取文件 。

import codecs
# 使用 with 语句打开文件，该语句会负责关闭文件
with codecs.open('readlines_test.py', 'r', 'utf-8', buffering=True) as f:
    for line in f:
        print(line, end="")