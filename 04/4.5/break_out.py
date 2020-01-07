#!/usr/bin/env python

# -*- *************** -*-
# @File  : break_out.py
# @Description : 
# @Author: mql
# @Time  : 2020/1/7 18:37
# -*- *************** -*-

# 为了使用 break 语句跳出嵌套循环的外层循环，
# 可先定义 bool 类型的变量来标志是否需要跳出外层循环，
# 然后在内层循环、外层循环中分别使用两条 break 语句来实现。

exit_flag = False

# 外层循环
for i in range(0 ,5):
    # 内层循环
    for j in range(0, 3):
        print("i的值为：%d, j的值为：%d" % (i ,j))
        if j == 1:
            exit_flag = True
            # 跳出内层循环
            break
    # 如果exit_flag为True，则跳出外层循环
    if exit_flag:
        break

# 上面程序在内层循环中判断 j 是否等于 1 ，当 j 等于 1 时，程序将 exit_flag 设为 True,并跳出内层循环 ；、
# 接下来程序开始执行外层循环的剩下语句 ，由于 exit_flag 为 True，因此也会执行外层循环的 break 语句来跳出外层循环
