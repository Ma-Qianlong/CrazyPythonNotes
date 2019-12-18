#!/usr/bin/env python

# -*- *************** -*-
# @File  : index_and_slice_test.py
# @Description : list and tuple 使用索引
# @Author: mql
# @Time  : 2019/12/18 13:55
# -*- *************** -*-


a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
a_list = ('crazyit1', 20.0, 5.60, 'fkit1', -17.1)
print(a_tuple)
print(a_list)

# 访问元素
print(a_tuple[0])
print(a_list[0])
print(a_tuple[2])
print(a_list[2])

print(a_tuple[-1])
print(a_list[-1])
print(a_tuple[-2])
print(a_list[-2])

# 用slice方法，格式如下：[start: end: step]

print(a_tuple[1:3])
print(a_tuple[-3:-1])
print(a_tuple[1:-2])
print(a_tuple[-3:4])

b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b_tuple[2:8:2])
print(b_tuple[2:8:3])
print(b_tuple[2:-2:2])
