#!/usr/bin/env python

# -*- *************** -*-
# @File  : read_test4.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-12 17:19
# -*- *************** -*-


# 下面程序使用 codecs 模块的 open （） 函数来打开文件，此时可以显式指定字符集。

import codecs
# 指定使用utf-8字符集读取文件内容
f = codecs.open('read_test4.py', 'r', 'utf-8', buffering=True)
try:
    while True:
        # 每次读取一个字符
        ch = f.read(1)
        if not ch: break
        print(ch, end="")
finally:
    f.close()

