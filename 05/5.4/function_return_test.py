#!/usr/bin/env python

# -*- *************** -*-
# @File  : function_return_test.py
# @Description : 使用函数作为返回值
# @Author: mql
# @Time  : 2020/1/14 13:53
# -*- *************** -*-


# Python 还支持使用函数作为其他函数的返回值。例如如下程序 。

def get_math_func(type):
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

    # 返回局部函数
    if type == "square":
        return square
    elif type == "cube":
        return cube
    else:
        return factorial


# 调用 get_math_func （），程序返回一个嵌套函数
math_func = get_math_func("cube")  # 得到 cube 函数
print(math_func(5))  # 125
math_func = get_math_func("square")  # 得到 square 函数
print(math_func(5))  # 25
math_func = get_math_func("other")  # 得到 factorial 函数
print(math_func(5))  # 120
