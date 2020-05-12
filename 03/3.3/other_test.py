#!/usr/bin/env python

# -*- *************** -*-
# @File  : other_test.py
# @Description : 列表的其他用法count()、index()、pop()、reverse()、sort()
# @Author: mql
# @Time  : 2019/12/24 13:59
# -*- *************** -*-


# count test
a_list = [2, 30, 'a', [5, 30], 30]
# 30出现的次数
print(a_list.count(30))
# [5,30] 出现的次数
print(a_list.count([5, 30]))

# index test
# index 30
print(a_list.index(30))
# index 30,start 2
print(a_list.index(30, 2))
# index 30,start 2, end 03
# print(a_list.index(30, 2, 03))  # ValueError

# pop() 栈，先入后出（FIFO），append()代替push
stack = []
# push 3 elements
stack.append('fkit')
stack.append('crazyit')
stack.append('Charlie')
print(stack)
# pop first
print(stack.pop())
print(stack)
# pop again
print(stack.pop())
print(stack)

# reverse test, 翻转列表中的所有的元素
b_list = list(range(1, 8))
print(b_list)
# reverse list
b_list.reverse()
print(b_list)

print(end='\n\n')
# sort test
c_list = [3, 4, -2, -30, 14, 9.3, 3.4]
print(c_list)
# sort c list
c_list.sort()
print(c_list)  # 默认从小到大排序
d_list = ['Python', 'Swift', 'Ruby', 'Go', 'Kotlin', 'Erlang']
print(d_list)
# sort d list
d_list.sort()
print(d_list)

# 指定key为len, 指定使用len函数对集合元素生成比较大小的键
# 也就是按字符串长度比较大小
d_list.sort(key=len)
print(d_list)
# 指定反向排序
d_list.sort(key=len, reverse=True)
print(d_list)