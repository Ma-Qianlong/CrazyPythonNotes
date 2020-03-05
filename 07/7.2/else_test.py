#!/usr/bin/env python

# -*- *************** -*-
# @File  : else_test.py
# @Description : else 块
# @Author: mql
# @Time  : 2020/3/5 22:43
# -*- *************** -*-


# 在 Python 的异常处理流程中还可添加一个 else 块 ，当 try 块没有出现异常时，程序会执行 else 块。

s = input('请输入除数：')
try:
    result = 20 / int(s)
    print('20除以%s的结果是：%g' % (s, result))
except ValueError:
    print('值错误，你必须输入整数值')
except ArithmeticError:
    print('算术错误，您不能输入0')
else:
    print('没有异常')