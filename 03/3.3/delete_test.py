#!/usr/bin/env python

# -*- *************** -*-
# @File  : delete_test.py
# @Description : 删除列表数据
# @Author: mql
# @Time  : 2019/12/23 15:53
# -*- *************** -*-

a_list = ['crazyit', 20, -2.4, (3, 4), 'fkit']
print(a_list)
# 删除第3个元素
del a_list[2]
print(a_list)
# 删除第2到第4个(不包含)元素
del a_list[1: 3]
print(a_list)

b_list = list(range(1, 10))
print(b_list)
# 删除第3个到倒数第2个（不包含）元素,间隔为2
del b_list[2: -2: 2]
print(b_list)
# 删除slice语法列表
del b_list[2: 4]
print(b_list)

# del 删除普通变量
name = 'crazyit'
print(name)
# 删除
del name
# print(name)  # NameError
print(end='\n\n')

# remove() 方法删除，据元素本身删除，只删除第一个找到的元素，找不到包ValueError错误
c_list = [20, 'crazyit', 30, -4, 'crazyit', 3.4]
print(c_list)
# 删除30
c_list.remove(30)
print(c_list)
# 删除第一个crazyit
c_list.remove('crazyit')
print(c_list)

# clear() ，清空列表
c_list.clear()
print(c_list)