#!/usr/bin/env python

# -*- *************** -*-
# @File  : function_param_test.py
# @Description : 使用函数作为函数形参
# @Author: mql
# @Time  : 2020/1/14 13:35
# -*- *************** -*-


# 有时候需要定义一个函数，该函数的大部分计算逻辑都能确定，但某些处理逻辑暂时无法确定，
# 这意昧着某些程序代码需要动态改变，如果希望调用函数时能动态传入这些代码，那么就需
# 要在函数中定义函数形参，这样即可在调用该函数时传入不同的函数作为参数，从而动态改变这段代码 。

# Python 支持像使用其他参数一样使用函数参数，例如如下程序 。

# 定义函数类型的形参，其中fn是一个函数
def map(data, fn):
    result = []
    # 遍历 data 列表中的每个元素，并用 fn 函数对每个元素进行计算
    # 然后将计算结果作为新数组的元素
    for e in data:
        result.append(fn(e))
    return result


# 定义一个计算平方的函数
def square(n):
    return n * n


# 定义一个计算立方的函数
def cube(n):
    return n * n * n


# 定义一个计算阶乘的函数
def factorial(n):
    result = 1
    for index in range(2, n + 1):
        result *= index
    return result


data = [3, 4, 9, 5, 8]
print("原数据：", data)
# 下面程序代码调用 map （）函数三次，每次调用时传入不同的函数
print("计算数组元素的平方")
print(map(data, square))
print("”计算数组元素的立方”")
print(map(data, cube))
print("计算数组元素的阶乘")
print(map(data, factorial))
print(type(map))