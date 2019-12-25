#!/usr/bin/env python

# -*- *************** -*-
# @File  : if_expr.py
# @Description : if条件的类型
# @Author: mql
# @Time  : 2019/12/25 23:07
# -*- *************** -*-


# if条件不仅仅是只能使用bool类型
# 除了False本身，各种代表‘空’的None、空字符串、空元组、空列表、空字典都会被当成False处理
# False、None、0、""、()、[]、{} 最为bool表达式时，会被解释器当做False处理

# 定义空字符串
s = ''
if s:
    print('s 不是空字符串')
else:
    print('s 是空字符串')

# 定义空列表
my_list = []
if my_list:
    print('my_list is not empty')
else:
    print('my_list is empty')

# 定义空字典
my_dict = {}
if my_dict:
    print('my_dict is not empty')
else:
    print('my_dict is empty')

