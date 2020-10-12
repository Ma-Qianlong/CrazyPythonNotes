#!/usr/bin/env python

# -*- *************** -*-
# @File  : urlopen_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-10 11:44
# -*- *************** -*-


from urllib.request import *

# 打开 URL 对应的资源
result = urlopen('https://fkjava.org/categories/Python/')
# 按字节读取数据
data = result.read(327)
# 将字节数据恢复成字符串
print(data.decode('utf-8'))

# 用 context manager 来管理打开的 URL 资源
with urlopen('http://www.baidu.com/') as f:
    # 按字节读取数据
    # 按字节读取数据
    data = f.read(327)
    # 将字节数据恢复成字符串
    print(data.decode('utf-8'))