#!/usr/bin/env python

# -*- *************** -*-
# @File  : recursive.py
# @Description : 递归函数
# @Author: mql
# @Time  : 2020/1/13 14:54
# -*- *************** -*-

# 在一个函数体内调用它自身，被称为函数边归 。 函数递归包含了 一种隐式的循环 ， 它会重复执
# 行某段代码，但这种重复执行无须循环控制。
# 例如有如下数学题 。 己知有一个数列 ： f〔0) = 1, f(1)=4，只f(n + 2) = 2*(n+1) +f(n） ，
# 其中 n 是大于 0 的整数，求只 f(10）的值 。这道题可以使用递归来求得 。
# 下面程序将定义一个 fn（）函数，用于计算f(1O）的值

def fun(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        # 在函数体中调用它自身，就是函数递归
        return 2 * fun(n - 1) + fun(n - 2)


# 输出 fn (10 ）的结果
print("fun(10）的结果是：", fun(10))


# 己知有一个数列 ：f(20)=1, f(21)=4 ，f(n + 2) = 2 *f(n+1) + f(n)
# 其中 n 是大于 0 的整数，求 f(10）的值

def fn(n):
    if n == 20:
        return 1
    elif n == 21:
        return 4
    else:
        return fn(n + 2) - 2 * fn(n + 1)


# fn 的参数必须小于等于20
print("fn(10):", fn(10))
