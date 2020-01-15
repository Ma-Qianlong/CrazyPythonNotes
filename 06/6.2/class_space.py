#!/usr/bin/env python

# -*- *************** -*-
# @File  : class_space.py
# @Description : 
# @Author: mql
# @Time  : 2020/1/15 14:25
# -*- *************** -*-

# Python 的类在很大程度上是一个命名空间——当程序在类体中定义变量、
# 定义方法时，与前面介绍的定义变量、定义函数其实并没有太大的不同

# 定义全局空间的foo函数
def foo():
    print("全局空间的foo函数")


# 定义全局变量的bar变量
bar = 20


class Bird:
    # 定义Bird空间的foo函数
    def foo():
        print("Bird空间的foo方法")

    # 定义bar空间的bar变量
    bar = 200


# 调用全局空间的函数和变量
foo()
print(bar)

# 调用Bird空间的函数和变量
Bird.foo()
print(Bird.bar)


# ***注意***
# Python 的类可以调用实例方法，但使用类调用实例方法时， Python 不会自动 为
# 方法的第一个参数 self 绑定参数值；程序必须显式地为第一个参数 self传入方法调用
# 者。 这种调用方式被称为“未绑定方法”。
