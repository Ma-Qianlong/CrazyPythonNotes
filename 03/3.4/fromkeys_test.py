#!/usr/bin/env python

# -*- *************** -*-
# @File  : fromkeys_test.py
# @Description : dict的fromkeys()方法
# @Author: mql
# @Time  : 2019/12/24 17:09
# -*- *************** -*-

# 使用列表创建包含两个key的字典
a_dict = dict.fromkeys(['a', 'b'])
print(a_dict)
# 使用元组创建包含两个key的字典
b_dict = dict.fromkeys((13, 17))
print(b_dict)
# 使用元组创建包含两个key的字典, 指定默认的value
c_dict = dict.fromkeys((13, 17), 'good')
print(c_dict)
