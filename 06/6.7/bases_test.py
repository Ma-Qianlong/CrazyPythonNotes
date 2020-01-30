#!/usr/bin/env python

# -*- *************** -*-
# @File  : bases_test.py
# @Description :  __bases__ 属性
# @Author: mql
# @Time  : 2020/1/30 20:39
# -*- *************** -*-


# Python 为所有类都提供了一个 __bases__ 属性，通过该属性可以查看该类的所有直接父类，
# 该属性返回所有直接父类组成的元组。

class A:
    pass

class B:
    pass

class C(A, B):
    pass

print('类A的所有父类：', A.__bases__)
print('类B的所有父类：', B.__bases__)
print('类C的所有父类：', C.__bases__)

# Python 还为所有类都提供了 一个 __subclass__() 方法，
# 通过该方法可以查看该类的所有直接子
# 类，该方法返回该类的所有子类组成的列表。

print('类A的所有子类：', A.__subclasses__())
print('类B的所有子类：', B.__subclasses__())
print('类C的所有子类：', C.__subclasses__())