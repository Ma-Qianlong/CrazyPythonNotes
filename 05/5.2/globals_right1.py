#!/usr/bin/env python

# -*- *************** -*-
# @File  : globals_right1.py
# @Description : 1.访问被遮蔽的全局变量
# @Author: mql
# @Time  : 2020/1/14 10:56
# -*- *************** -*-


# 通过 globals（）函数来实现
name = 'Charlie'
def test():
    # 通过globals()函数访问name全局变量
    print(globals()['name']) # Charlie
    name = '孙悟空'
test()
print(name) # Charlie