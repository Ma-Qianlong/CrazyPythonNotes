#!/usr/bin/env python

# -*- *************** -*-
# @File  : list_test.py
# @Description : 创建列表，及转换
# @Author: mql
# @Time  : 2019/12/18 21:53
# -*- *************** -*-


a_tuple = ('crazyit', 20, -1.2)
# 将元组转换成列表
a_list = list(a_tuple)
print(a_list)
# 使用range()函数创建区间（range）对象
a_range = range(1, 5)
print(a_range)
# 将区间转换成列表
b_list = list(a_range)
print(b_list)
# 创建区间时指定了步长
c_list = list(range(1, 40, 3))
print(c_list)

# tuple()函数可以将列表及区间等对象转换成元组
print(end="\n\n")
# 将列表转换成元组
a_tuple = tuple(a_list)
print(a_tuple)
b_tuple = tuple(a_range)
print(b_tuple)
c_tuple = tuple(range(4, 40, 3))
print(c_tuple)
