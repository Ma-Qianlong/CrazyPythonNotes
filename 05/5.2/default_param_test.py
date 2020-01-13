#!/usr/bin/env python

# -*- *************** -*-
# @File  : default_param_test.py
# @Description : 参数默认值
# @Author: mql
# @Time  : 2020/1/13 20:53
# -*- *************** -*-


# 在某些情况下，程序需要在定义函数时为一个或多个形参指定默认值——这样在调用函数时就
# 可以省略为该形参传入参数值，而是直接使用该形参的默认值。
# 为形参指定默认值的语法格式如下：
#   形参名＝默认值
# 从上面的语法格式可以看出，形参的默认值紧跟在形参之后，中间以英文“＝”隔开。

# 为两个参数指定默认值
def say_hi(name="孙悟空", message="欢迎来到疯狂软件"):
    print(name, "，您好")
    print("消息是：", message)


# 全部使用默认参数
say_hi()

say_hi("白骨精")

say_hi("白骨精", "欢迎学习Python")

say_hi(message="欢迎学习Python")

# 由于 Python 要求在调用函数时关键字参数必须位于位置参数的后面，因此在定义函数时指定
# 了默认值的参数（关键字参数）必须在没有默认值的参数之后 。 例如如下代码。

# 定义一个打印三角形的函数, 有默认值的参数必须放在后面
def printTriangle(char, height=5):
    for i in range(1, height+1):
        # 先打印一排空格
        for j in range(height - i):
            print(' ', end=" ")
        # 再打印一排特殊字符
        for j in range(2 * i - 1):
            print(char, end="")
        print()

printTriangle('@', 6)
printTriangle('#', height=7)
printTriangle(char='*')
