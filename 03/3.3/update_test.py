#!/usr/bin/env python

# -*- *************** -*-
# @File  : update_test.py
# @Description : 修改列表元素
# @Author: mql
# @Time  : 2019/12/23 17:16
# -*- *************** -*-


a_list = [2, 4, -3.4, 'crazyit', 23]
print(a_list)
# 对第3个元素赋值
a_list[2] = 'fkit'
print(a_list)
# 对倒数第二个元素赋值
a_list[-2] = 9999
print(a_list)

print(end='\n')
# 通过slice语法对其中一部分赋值，并不要求元素数一致
b_list = list(range(1, 5))
print(b_list)
# 将2到4（不包含）元素赋值为新列表的元素
b_list[1: 3] = ['a', 'b']
print(b_list)
# 将第3到3(不包含)元素赋值为新列表的元素，相当于在索引2处插入元素
b_list[2: 2] = ['x', 'y']
print(b_list)
# 赋值为空列表，就相当于删除元素
b_list[2: 5] = []
print(b_list)
# slice 语法赋值时，不能使用单个值；若是字符串，将自动当做序列处理
b_list[1:3] = 'Charlie'
print(b_list)
# slice 语法，可指定step参数，若指定了，则要求所赋值列表与被替换列表元素个数一致
c_list = list(range(1, 10))
c_list[2:9:2] = ['a', 'b', 'c', 'd']
print(c_list)
