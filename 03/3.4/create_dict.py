#!/usr/bin/env python

# -*- *************** -*-
# @File  : create_dict.py
# @Description : 创建字典
# @Author: mql
# @Time  : 2019/12/24 16:12
# -*- *************** -*-


scores = {'语文': 89, '数学': 92, '英语': 93}
print(scores)
# 空字典
empty_dict = {}
print(empty_dict)
# 使用元组作为字典的key,列表不能作为字典的key, 因为dict要求key值为不可变类型
dict2 = {(20, 30): 'good', 30: 'bad'}
print(dict2)
# 多个列表或元组参数作为key-value对
vagetables = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 1.29)]
print(vagetables)
# 创建3个key-value对的字典
dict3 = dict(vagetables)
print(dict3)
cars = [['BMW', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
print(cars)
dict4 = dict(cars)
print(dict4)
# 创建空字典
dict5 = dict();
print(dict5)

# 指定关键字参数创建字典，此时key不允许使用表达式
dict6 = dict(spinach=1.39, cabbage=2.59)
print(dict6)
