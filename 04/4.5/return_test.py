#!/usr/bin/env python

# -*- *************** -*-
# @File  : return_test.py
# @Description : 使用 return 结束方法
# @Author: mql
# @Time  : 2020/1/7 18:48
# -*- *************** -*-

# return 用于从包 围它的最直接方法、函数或匿名函数返回 。
# 当函数或方法执行到一条 return 语句时，这个函数或方法将被结束 。

# Python 程序中的大部分循环都被放在函数或方法中执行，
# 一旦在循环体内执行到一条 return 语句时， return 语句就会结束该函数或方法，循环自然也随之结束。

def test():
    # 外层循环
    for i in range(10):
        for j in range(10):
            print("i的值是：%d, j的值是：%d" % (i, j))
            if (1 == j):
                return
            print("return 后输出的语句")


test()


# 运行上面程序，循环只能执行到 1 等于 0 、 j 等于 1 时 ，
# 当 j 等于 1 时程序将完全结束（当 test()函数结束时，也就是 Python 程序结束时） 。
# 从这个运行结果来看，虽然 return 并不是专门用于控制循环结构的关键字 ，但通过 return 语句确实可 以结束一个循环 。
# 与 continue 和 break 不同的是， return直接结束整个函数或方法，而不管 return 处于多少层循环之内 。
