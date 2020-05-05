#!/usr/bin/env python

# -*- *************** -*-
# @File  : PurePath_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/5/4 14:54
# -*- *************** -*-

from pathlib import *

# 实际上为PureWindowPath
pp = PurePath("setup.py")
print(type(pp))

pp = PurePath('/carzyit', 'some/path', 'info')
print(pp)

# 明确指定创建 PurePosixPath
pp = PurePosixPath('carzyit', 'some/path', 'info')
print(pp)

# 默认当前路径
pp = PurePath()
print(pp)

# 如果传入的参数包含多个根路径 ，则只有最后一个根路径及后面的子路径生效
pp = PurePosixPath('/etc', '/usr', 'lib64')
print(pp)
pp = PureWindowsPath('c:Windows', 'd:info')
print(pp)

# 路径字符串中多出来的斜杠和点号（代表当前路径）都会被忽略
pp = PurePath('foo//bar')
print(pp)
pp = PurePath('foo/./bar')
print(pp)

pp = PurePath('foo/../bar')
print(pp) # foo\ .. \bar ，相当于找和 foo 同一级的 bar 路径