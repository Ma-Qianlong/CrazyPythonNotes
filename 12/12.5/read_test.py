#!/usr/bin/env python

# -*- *************** -*-
# @File  : read_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-12 17:02
# -*- *************** -*-


f = open("test.txt", 'r', True)
try:
    while True:
        # 每次读取一个字符
        ch = f.read(1)  # 如果在调用 read（）方法时不传入参数，该方法默认会读取全部文件内容。
        # 如果没有读取到了数据，则跳出循环
        if not ch: break
        # 输出 ch
        print(ch, end='')
finally:
    f.close()

# 当使用 open（） 函数打开文本文件时 ，程序使用的是那种字符集昵？
# 总是使用当前操作系统的字符集， 比如 Windows 平台 ， open（）函数总是使用 GBK 宇符集。
# 因此，上面程序读取的 test.txt 也必须使用 GBK 字符集保存 ； 否则，程序就会出 UnicodeDecodeError 错误 。
# 如果要读取 的文件所使用 的字符集和 当前操作系统的字符集不匹配， 则有两种解决方式 。
# 》使用 二进制模式读取 ， 然后用 bytes 的 decode（）方法恢复成字符串 。
# 》利用 codecs 模块的 open（）函数来打开文件， 该函数在打开文件时允许指定字符集 。