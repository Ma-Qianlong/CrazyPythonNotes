#!/usr/bin/env python

# -*- *************** -*-
# @File  : all_module.py
# @Description : 
# @Author: mql
# @Time  : 2020/03/21 16:23
# -*- *************** -*-


'测试__all__变量的模块'


def hello():
    print("Hello, Python")


def world():
    print("Python World is funny")


def test():
    print('--test--')


# 定义__all__变量，默认只导入 hello 和 world 两个程序单元
__all__ = ['hello', 'world']
