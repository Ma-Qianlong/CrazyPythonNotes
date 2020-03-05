#!/usr/bin/env python

# -*- *************** -*-
# @File  : multi_exception_test.py
# @Description : 多异常捕获
# @Author: mql
# @Time  : 2020/3/3 18:28
# -*- *************** -*-


# Python 的一个 except 块可以捕获多种类型的异常。
# 在使用一个 except 块捕获多种类型的异常时，只要将多个异常类用圆括号括起来，中间用逗号隔开即可——其实就是构建多个异常类的元组。

import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except (IndexError, ValueError, ArithmeticError):
    print("程序发生了数组越界、数字格式异常、算术异常之一 ")
except:
    print("未知异常")


# 上面程序中代码使用了（IndexError, ValueError, ArithmeticError）来指定所捕获的异常类型，这就表明该 except 块可以同时捕获这三种类型的异常 。
# 代码倒数第二行， 这行代码只有 except 关键字，并未指定具体要捕获的
# 异常类型，这种省略异常类的 except 语句也是合法的，它表示可捕获所有类型的异常， 一般会作
# 为异常捕获的最后一个 except 块 。


