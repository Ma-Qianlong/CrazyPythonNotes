#!/usr/bin/env python

# -*- *************** -*-
# @File  : raise_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/3/11 22:16
# -*- *************** -*-


# 不管是系统自动引发的异常，还是程序员于动引发的异常，Python 解释器对异常的处理没有任何差别。

# 即使是用户自行引发的异常，也可 以使用 try...except 来捕获它。当然也可以不管它， 让该异常
# 向上（先调用者 〉传播，如果该异常传到 Python 解释器，那么程序就会中止。

def main():
    try:
        # 使用 try...except 来捕获异常
        # 此时即使程序出现异常 ， 也不会传播给 main 函数
        mtd(3)
    except Exception as e:
        print('程序出现异常', e)
    # 不使用 try...except 捕获异常，异常会传播出来导致程序中止
    mtd(3)


def mtd(a):
    if a > 0:
        raise ValueError("a的值大于 0 ，不符合要求")

main()

# **提示
# 第 二次调 用 mtd(3 ）引 发 的 以“ File”开头的三行输出 ，其实显示的就是异常的传播轨迹信息。
# 也就是说，如果程序不对异常进行处理， Pyhon 默认会在控制台输出异常的传播轨迹信息 。