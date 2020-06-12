#!/usr/bin/env python

# -*- *************** -*-
# @File  : readline_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-12 17:23
# -*- *************** -*-

import codecs

# 指定使用UTF-8字符集来读取文件内容
f = codecs.open("readline_test.py", 'r', 'utf-8', buffering=True)
while True:
    # 每次读取一行
    line = f.readline()
    if not line: break
    print(line, end='')
f.close()

# 上面程序使用 UTF-8 字符集打开 readline test.py 文件 这是由于该 Python 源文件是采用 UTF-8
# 字符集保存的 ， 因此，如果直接用普通的 open（）函数打开文件，则会引发 UnicodeDecodeError 异常。