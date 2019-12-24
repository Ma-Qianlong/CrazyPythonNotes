#!/usr/bin/env python

# -*- *************** -*-
# @File  : pop_popitem_test.py
# @Description : dict的pop()及popitem()方法
# @Author: mql
# @Time  : 2019/12/24 16:58
# -*- *************** -*-

# 获取指定的key-value,并从字典中删除
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.pop('AUDI'))
print(cars)

# popitem（）方法用于随机弹出字典中的 一个 key-value对
# 随机是假的，其实还是弹出最后一个元素
# popitem() 弹出的是一个元组，可通过序列解包的方式去key和value
print(cars.popitem())
print(cars)
# 将弹出的值赋给 k 和 v
k, v = cars.popitem()
print(k, v)

