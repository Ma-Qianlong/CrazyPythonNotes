#!/usr/bin/env python

# -*- *************** -*-
# @File  : lambda_in_space.py
# @Description : 
# @Author: mql
# @Time  : 2020/1/16 10:31
# -*- *************** -*-

global_fn = lambda p: print('执行lambda表达式，p参数：', p)
class Category :
    cate_fn = lambda p: print('执行lambda表达式，p参数：', p)

# 调用全局空间内的 global_fn ，为参数 p 传入参数值
global_fn('fkit')

c = Category()
# 调用类命名空间内的 cate_fn, Python 自动绑定第一个参数
c.cate_fn()
