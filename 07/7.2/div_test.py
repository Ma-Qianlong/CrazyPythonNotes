#!/usr/bin/env python

# -*- *************** -*-
# @File  : div_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/3/3 18:20
# -*- *************** -*-

# Python 的所有异常类的基类是 BaseException，但如果用户要实现自定义异常，则不应该继承这个基类，而是应该继承 Exception 类。
# BaseException 的主要子类就是 Exception ，不管是系 统的异常类，还是用户自定义的异常类，都应该从 Exception 派生 。
# 下面看几个简单的异常捕获的例子 。

import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except IndexError:
    print("索引错误 ： 运行程序时输入的参数个数不够")
except ValueError:
    print("数值错误 ： 程序只能接收整数参数")
except ArithmeticError:
    print("算术错误")
except Exception:
    print("未知错误")

# 上面程序，导入了 sys 模块，并通过 sys 模块的 argv 列表来获取运行 Python 程序时提供的参数 。
# 其中通常sys.argv[0]代表正在运行的Python程序名，sys.argv[1]代表运行程序所提供的第一个参数，sys.argv[2]代表运行程序所提供的第 二 个参数 ·…· ·依此类推。
