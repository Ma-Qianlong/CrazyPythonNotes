#!/usr/bin/env python

# -*- *************** -*-
# @File  : zip_test.py
# @Description : 工具函数 zip()
# @Author: mql
# @Time  : 2020/1/5 22:00
# -*- *************** -*-

# zip()
# 使用 zip（）函数可以把两个列表“压缩” 成一个 zip 对象（可法代对象〉，这样就可以使用一个
# 循环并行遍历两个列表.
# zip（）函数压缩得到的可迭代对象所包含的元素是由原列表元素组成的元组(Python3.x)。
a = ['a', 'b', 'c']
b = [1, 2, 3]
print([x for x in zip(a, b)])

# 如果 zip（）函数压缩的两个列表长度不相等 ， 那么 zip（）函数将以长度更短的列表为准
c = [0.1, 0.2]
print([x for x in zip(a, c)])

# zip（）函数不仅可以压缩两个列表 ， 也可以压缩多个列表; 如果使用 zip（）函数压缩 N 个列表，那么 zip（）函数返回的可选代对象的
# 元素就是长度为 N 的元组。
print([x for x in zip(a, b, c)])

print()
# 下面代码示范了使用 zip（）函数来实现并行遍历的效果
books = ['疯狂 Kotlin 讲义', '疯狂 Swift 讲义', '疯狂 Python 讲义']
prices = [79, 69, 89]
# 使用 zip （）函数压缩两个列表，从而实现并行遍历
for book, price in zip(books, prices):
    print('%s 的价格谁: %5.2f' % (book, price))

