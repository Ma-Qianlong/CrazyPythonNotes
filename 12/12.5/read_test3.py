#!/usr/bin/env python

# -*- *************** -*-
# @File  : read_test3.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-12 17:15
# -*- *************** -*-


# 下面程序使用二进制模式来读取文本文件 。

# 指定使用二进制模式读取文件内容
f = open('read_test3.py', 'rb', True)
try:
    # 直接读取文件的全部内容， 并调用bytes的decode()方法将字节内容恢复成字符串
    print(f.read().decode('utf-8'))
finally:
    f.closed()