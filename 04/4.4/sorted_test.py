#!/usr/bin/env python

# -*- *************** -*-
# @File  : sorted_test.py
# @Description : 工具函数 reversed()、sorted()
# @Author: mql
# @Time  : 2020/1/5 22:13
# -*- *************** -*-


# reversed()
# 有些时候 ， 程序需要进行反向遍历，此时可通过 reversed（）函数，
# 该函数可接收各种序列（元组、列表、区间等）参数，然后返回一个“反序排列”的法代器，
# 该函数对参数本身不会产生任何影响
a = range(10)
print([x for x in reversed(a)])
print(a)

print()
# reversed（） 当然也可以对列表、元组进行反转 。
b = ['a', 'fkit', 20, 3.4, 50]
print([x for x in reversed(b)])

print()
# 前面提到过，str其实也是序列，因此也可通过该函数实现在不影响字符串本身的前提下，对字符串进行反序遍历
c = 'Hello, World'
print([x for x in reversed(c)])
print(c)

print()
# sored()
# 与reversed（）函数类似的还有 sorted（）函数，该函数接收一个可迭代对象作为参数，返回 一个对元素排序的列表。
a = [20, 30. -1.2, 3.5, 90, 3.6]
print(sorted(a))
print(a)
# 从上面的运行过程来看， sorted（）函数也不会改变所传入的可迭代对 象 ， 该函数只是返回一个新的 、 排序好的列表。
# 在使用 so1ted（）函数时，还可传入一个 reverse 参数，如果将该参数设置为 True，则表示反向排序
print(sorted(a, reverse=True))

# 在调用 sorted（）函数时，还可传入一个 key 参数，该参数可指定一个函数来生成排序的关键值 。
# 比如希望根据字符串长度排序，则可为 key 参数传入 Jen 函数
b = ['fkit', 'crazyit', 'Charlie', 'fox', 'Emily']
print(sorted(b, key=len))

print()
# 通过 sorted（）函数的帮助，程序可对可迭代对象按照由小到大的顺序进行遍历。
for s in sorted(b, key=len):
    print(s)