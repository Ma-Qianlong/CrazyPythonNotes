#!/usr/bin/env python

# -*- *************** -*-
# @File  : append_test.py
# @Description : 增加列表元素
# @Author: mql
# @Time  : 2019/12/23 15:40
# -*- *************** -*-


a_list = ['crazyit', 20, -2]
print(a_list)
# 追加元素
a_list.append('fkit')
print(a_list)


# 追加元组，元组被当成是一个元素
a_tuple = (3.4, 5.6)
a_list.append(a_tuple)
print(a_list)

# 追加列表，列表被当做是一个元素
a_list.append(['a', 'b'])
print(a_list)

# 若不想追加的列表被当做一个元素，仅追加列表中元素，使用extend()方法
b_list = ['a', 30]
print(b_list)
# 追加元组中的所有元素
b_list.extend((-1, 3))
print(b_list)
# 追加列表中的所有元素
b_list.extend(['c', 'R', 'A'])
print(b_list)
# 追加区间中的所有元素
b_list.extend(range(97, 100))
print(b_list)

# 使用列表的insert()可插入元素
c_list = list(range(1, 6))
print(c_list)
# 3 处 插入字符串
c_list.insert(3, 'CRAZY')
print(c_list)
# 3 处插入元组，元组被当做一个yuans
c_list.insert(3, tuple('crazy'))
print(c_list)