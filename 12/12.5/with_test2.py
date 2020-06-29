#!/usr/bin/env python

# -*- *************** -*-
# @File  : with_test2.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-29 14:07
# -*- *************** -*-


# 程序也可 以使用 with 语句来处理通过 fileinput.input 合并的多个文件，例如如下程序 。

import fileinput
# 使用with语句打开文件，该语句会负责关闭文件
with fileinput.input(files=('test.txt', 'info.txt')) as f:
    for line in f:
        print(line, end='')