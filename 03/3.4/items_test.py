#!/usr/bin/env python

# -*- *************** -*-
# @File  : items_test.py
# @Description :字典的 items()、 keys() 、 values()使用
# @Author: mql
# @Time  : 2019/12/24 16:47
# -*- *************** -*-


# items()、 keys() 、 values()分别用于获取字典 中的所有key-value对、所有key、所有value。
# 这三个方法依次返 回 dict_items 、 dict_keys 和 dict_values 对象，
# Python 不希望用户直接操作这几个方法，但可通过 list（）函数把它们转换成列表。

cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 获取字典中的所有键值对
ims = cars.items()
print(type(ims))
# 将dict_items转换成列表
print(list(ims))
# 访问第二个键值对
print(list(ims)[1])
print(list(ims)[1][0])
print(list(ims)[1][1])

# 获取字典中的所有的key
kys = cars.keys()
print(type(kys))
# 将dict_keys转换成列表
print(list(kys))
# 访问第二个key
print(list(kys)[1])

# 获取字典中的所有value
vals = cars.values()
print(vals)
# 将dict_values转换成列表
print(list(vals))
print(list(vals)[1])

