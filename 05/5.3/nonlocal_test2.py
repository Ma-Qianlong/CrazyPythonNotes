#!/usr/bin/env python

# -*- *************** -*-
# @File  : nonlocal_test2.py
# @Description : 局部函数2
# @Author: mql
# @Time  : 2020/1/14 10:48
# -*- *************** -*-


# 为了声明 bar（）函数中的“ name＝’孙悟空”’ 赋值语句不是定义新的局部变量，只是访问它所在foo（）函数内的 name 局部变量 ，
# Python 提供了 nonlocal 关键字，通过 nonlocal 语句即可声明访问赋值语句只是访问该函数所在函数内的局部变量。
# 将上面程序改为如下形式。

def foo():
    # 局部变量name
    name = 'Charlie'

    def bar():
        nonlocal name  # ***
        # 访问bar函数所在的foo函数内的name变量
        print("bar1:", name)  # Charlie
        name = '孙悟空'
        print("bar2:", name)  # 孙悟空
    bar()
    print("foo:", name)

foo()


# nonlocal 和前面介绍的 global 功能大致相似，
# 区别只是 global 用于声明访问全局变量，而 nonlocal 用于声明访问当前函数所在函数内的局部变量。