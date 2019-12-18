#!/usr/bin/env python

# -*- *************** -*-
# @File  : seq_packing.py
# @Description : 序列分包和序列解包
# @Author: mql
# @Time  : 2019/12/18 21:26
# -*- *************** -*-

# 序列封包, 多值封装成元组
vals = 10, 20, 30
print(vals)
print(type(vals))
print(vals[1])

print(end="\n\n")
# 序列解包，元组
a_tuple = tuple(range(1, 10, 2))
a, b, c, d, e = a_tuple
print(a, b, c, d, e)

print(end="\n\n")
# 序列解包，列表
a_list = ['fkit', 'crazyit']
a_str, b_str = a_list;
print(a_str, b_str)

print(end="\n\n")
# 同时使用序列封包及解包机制
x, y, z = 20, 15, 10
print(x, y, z)
# 上述代码实际执行过程如下
xyz = 20, 15, 10
x, y, z = xyz
print(x,y,z)

print(end="\n\n")
# 序列解包 是只赋值部分元素，剩余的用列表保存
# 被赋值变量前加*表示一个列表
first, second, *rest = range(1,10)
print(first)
print(second)
print(rest)

*begin, last = range(10)
print(begin)
print(last)

first, *middle, last = range(10)
print(first)
print(middle)
print(last)