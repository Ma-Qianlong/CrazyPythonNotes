#!/usr/bin/env python

# -*- *************** -*-
# @File  : while_tuple_list.py
# @Description : 利用while遍历元组和列表
# @Author: mql
# @Time  : 2019/12/26 15:42
# -*- *************** -*-

# while 遍历元组
a_tuple = ('fkit', 'crazyit', 'Charlie')
i = 0
while i < len(a_tuple):
    print(a_tuple[i])
    i += 1

print(end="\n")

# while 遍历列表
src_list = [12, 45, 34, 13, 100, 24, 56, 75, 109]
a_list = []  # 定义保存整除3
b_list = []  # 定义保存除3余1
c_list = []  # 定义保存除3余2
# 只要src_list中有元素，就执行
while len(src_list) > 0:
    # pop 弹出最后一个元素
    ele = src_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print("整除3的有：", a_list)
print("除3余1的有：", b_list)
print("除3余2的有：", c_list)
