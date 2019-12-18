#!/usr/bin/env python

# -*- *************** -*-
# @File  : plus_and_multiple_and_translate_test.py
# @Description : 列表或元组的加法，乘法及示例
# @Author: mql
# @Time  : 2019/12/18 14:10
# -*- *************** -*-


# plus
a_tuple = ('crazyit', 20, -1.2)
b_tuple = (127, 'crazyit', 'fkit', 3.33)

sum_tuple = a_tuple + b_tuple
print('sum_tuple:', sum_tuple)
print('a_tuple:', a_tuple)
print('b_tuple:', b_tuple)

print(a_tuple + (-22, -23))
# 元组和列表不能直接相加
# print(a_tuple + [22, 23]) # 报错

a_list = ['sb', 'ad', 23, 553]
b_list = ["232", 23, 323, 55, 6543]
print(a_list + b_list)

# muitiple
mul_tuple = a_tuple * 3
print(mul_tuple)
mul_list = a_list * 3
print(mul_list)

# translate
print(end="\n\n\n")
# 同时对元组使用加法和乘法
order_endings = ('st', 'nd', 'rd')\
    + ('th',) * 17 + ('st', 'nd', 'rd')\
    + ('th',) * 7 + ('st',)
print(order_endings)

day = input("输入日期（1-31）：")
day_int = int(day)
print(day + order_endings[day_int-1])

