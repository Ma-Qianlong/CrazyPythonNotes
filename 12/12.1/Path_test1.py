#!/usr/bin/env python

# -*- *************** -*-
# @File  : Path_test1.py
# @Description : 
# @Author: mql
# @Time  : 2020-05-26 14:30
# -*- *************** -*-


from pathlib import *

# 获取当前目录
p = Path('.')
# 遍历当前目录下的所有文件和子目录
for x in p.iterdir():
    print(x)

# 获取上级目录
p = Path('../')
# 获取上级目录及所有子目录下的.py文件
for x in p.glob("**/*.py"):
    print(x)

# 获取 D:\ProgramDevelop\PycharmProjects\CrazyPythonNotes\12\12.1 对应的目录
p = Path("D:\ProgramDevelop\PycharmProjects\CrazyPythonNotes")
for x in p.glob("**/Path_test1.py"):
    print(x)
