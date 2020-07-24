#!/usr/bin/env python

# -*- *************** -*-
# @File  : os_readwrite_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-07-24 11:08
# -*- *************** -*-


import os

# 以读写、创建的方式打开文件
f = os.open('abc.txt', os.O_RDWR | os.O_CREAT)
# 写入文件内容
len1 = os.write(f, '水晶潭底银鱼跃，\n'.encode('utf-8'))
len2 = os.write(f, '清徐风中碧竿横。\n'.encode('utf-8'))
# 将文件指针移动到开始处
os.lseek(f, 0, os.SEEK_SET)
# 读取文件内容
data = os.read(f, len1 + len2)
# 打印所读取到的字节串
print(data)
# 将字节串恢复成字符串
print(data.decode("utf-8"))
os.close(f)