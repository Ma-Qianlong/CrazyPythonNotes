#!/usr/bin/env python

# -*- *************** -*-
# @File  : function_test.py
# @Description : 定义函数和调用函数
# @Author: mql
# @Time  : 2020/1/13 14:32
# -*- *************** -*-


# 在使用函数之前必须先定义函数，定义函数的语法格式如下：
# def 函数名（形参列表）
#   //由零条到多条可执行语句组成的函数
#   [return ［返回值门


# 定义一个函数，声明两个形参
def my_max(x, y):
    z = x if x > y else y
    return z

# 定义一个函数，声明一个形参
def say_hi(name):
    print("===正在执行say_hi()函数===")
    return  name + ",您好！"

a = 6
b = 9

result = my_max(a, b)
print("result:", result)
print(say_hi("孙悟空"))