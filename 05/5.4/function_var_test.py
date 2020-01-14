#!/usr/bin/env python

# -*- *************** -*-
# @File  : function_var_test.py
# @Description : 使用函数变量
# @Author: mql
# @Time  : 2020/1/14 13:28
# -*- *************** -*-


# Python 的 函数也是一种值 ： 所有函数都是 function 对象，这意味着可以把函数本身赋值给变量 ，
# 就像把整数、浮点数、列表、元组赋值给变量一样。

# 当把函数赋值给变量之后，接下来程序也可通过该变量来调用函数

# 定义一个计算乘方的函数
def pow(base, exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result


# 将 pow 函数赋值给 my_fun ，则 my_fun 可被当成 pow 使用
my_fun = pow
print(my_fun(3, 4))


# 定义一个计算面积的函数
def area(width, height):
    return width * height


# 将 area 函数赋值给 my_fun ，则 my_fun 可被当成 area 使用
my_fun = area
print(my_fun(3, 4))

# 通过对 my_fun 变量赋值不同的函数 ， 可以让 my_fun 在不同的时间指向不同的函数 ，
# 从而让程序更加灵活。由此可见，使用函数变量的好处是让程序更加灵活 。
