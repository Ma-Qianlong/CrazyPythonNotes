#!/usr/bin/env python

# -*- *************** -*-
# @File  : PurePath_test2.py
# @Description : 
# @Author: mql
# @Time  : 2020/5/4 15:10
# -*- *************** -*-

from pathlib import *

# UNIX风格路径， 区分大小写
print(PurePosixPath('info') == PurePosixPath("INFO"))  # False
# Windows风格路径，不区分大小写
print(PureWindowsPath('info') == PureWindowsPath("INFO"))  # True
print(PureWindowsPath('info') in {PureWindowsPath("INFO")})

# UNIX 风格的路径区分大小写，所以 ’ D ： ’小于 ’ c :'
print(PurePosixPath('D:') < PurePosixPath("c:"))  # True
# Windows 风格的路径不区分大小写，所 以’ d ：’ （ D ： ）大于 ’ c ：’
print(PureWindowsPath('D:') > PureWindowsPath("c:"))  # True

# 对于不 同风格的 PurePath ， 它们依然可 以比较是否相等（结果总是返回 False ）， 但不能 比较大小，否则会引发错误 。
# 不同风格的路径可以判断是否相等（总不相等〕
print(PureWindowsPath('c') == PurePosixPath("c"))  # False
# 不同风格的路径不能判断大小，否则会引发错误
# print(PureWindowsPath ('info') < PurePosixPath ('info')) # TypeError

pp = PureWindowsPath('abc')
# 将多个路径连接起来（ Windows 风格的路径〕
print(pp / 'xyz' / 'waa')

pp = PurePosixPath('abc')
# 将多个路径连接起来（ UNIX 风格的路径）
print(pp / 'xyz' / 'waa')  # abc/xyz/waa
pp2 = PurePosixPath('haha', 'hehe')
# 将pp、 pp2 两个路径连接起来
print(pp / pp2)  # abc/haha/hehe


# PurePath 的本质其实就是字符串，因此程序可使用 str（）将它们 恢复成字符串对象。在恢复成字
# 符串对象时会转换为对应平台风格的字符串。
print(str(pp2))
