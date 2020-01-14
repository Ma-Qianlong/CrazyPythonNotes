#!/usr/bin/env python

# -*- *************** -*-
# @File  : local_function_test.py
# @Description : 局部函数1
# @Author: mql
# @Time  : 2020/1/14 10:33
# -*- *************** -*-


# Python 还支持在函数体内定义函数 ， 这种被放在函数体内定义的函数称为局部函数。
# 在默认情况下 ，局部函数对外部是隐藏的，局部函数只能在其封闭（ enclosing ）函数内有效，
# 其封闭函数也可以返回局部函数，以便程序在其他作用域中使用局部函数 。

# 如果封闭函数没有返回局部函数，那么局部函数只能在封闭函数内部调用，如下面面程序所示。
# 定义函数，该函数会包含局部函数
def get_math_func(type, nn):
    # 定义一个计算平方的局部函数
    def square(n):
        return n * n

    # 定义一个计算立方的局部函数
    def cube(n):
        return n * n * n

    # 定义一个计算阶乘的局部函数
    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    # 调用局部函数
    if type == 'square':
        return square(nn)
    elif type == "cube":
        return cube(nn)
    else:
        return factorial(nn)


print(get_math_func("square", 3))
print(get_math_func("cube", 3))
print(get_math_func("", 3))
# 另外，还会出现一种情况，如果封闭函数将局部函数返回，且程序使用变量保存了封闭函数的
# 返回值，那么这些局部函数的作用域就会被扩大。因此程序完全可以自由地调用它们，就像它们都
# 是全局函数一样 。 下一节(5.4)就会介绍函数返回函数的情况 。


# next: nonlocal_test.py
