#!/usr/bin/env python

# -*- *************** -*-
# @File  : for_test.py
# @Description : for-in 循环
# @Author: mql
# @Time  : 2019/12/26 15:53
# -*- *************** -*-


# for-in 循环专门用于遍历范围、列表、元素和字典等可迭代对象包含的元素。
# for-in 循环的语法格式如下：
#   for 变量 in 字符串｜范围｜集合等 ：
#       statements
# 对于上面的语法格式有两点说明。
# 1. for-in 循环中的变量的值受 for-in 循环控制，该变量将会在每次循环开始时自动被赋值，
#   因此程序不应该在循环中对该变量赋值 。
# 2. for-in 循环可用于遍历任何可选代对象 。
#   所谓可迭代对象，就是指该对象中包含一个__iter__方法，且该方法的返回值对象具有 next（）方法。

# 使用 for-in 循环来计算指定整数的阶乘
s_max = input("请输入您想计算阶乘的整数：")
mx = int(s_max)
result = 1
# 使用for-in循环遍历范围
for num in range(1, mx + 1):
    result *= num
print(result)