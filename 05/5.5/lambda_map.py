#!/usr/bin/env python

# -*- *************** -*-
# @File  : lambda_map.py
# @Description :
# @Author: mql
# @Time  : 2020/1/14 14:42
# -*- *************** -*-

# 下面代码示范了通过 lambda 表达式来调用 Python 内置的 map（）函数 。

# 传入计算平方的lambda表达式作为参数
x = map(lambda x: x * x, range(8))
print([e for e in x])  # [0, 1, 4, 9, 16, 25, 36, 49]
# 传入计算平方的 lambda 表达式作为参数
y = map(lambda x: x * x if x % 2 == 0 else 0, range(8))
print([e for e in y]) # [0, 0, 4, 0, 16, 0, 36, 0]
