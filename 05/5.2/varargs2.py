#!/usr/bin/env python

# -*- *************** -*-
# @File  : varargs2.py
# @Description : 逆向参数收集
# @Author: mql
# @Time  : 2020/1/14 9:39
# -*- *************** -*-


# 所谓逆向参数收集，指的是在程序己有列表、元组、 宇典等对象的前提下，把它们的元素“拆开”后传给函数的参数 。
# 逆向参数收集需要在传入的列表、元组参数之前添加一个星号 ， 在字典参数之前添加两个星号。

def test(name, message):
    print("用户是：", name)
    print("欢迎消息：", message)


my_list = ['孙悟空', "欢迎来到疯狂软件"]
test(*my_list)


# 程序中的 my_list 列表包含两个元素，为了让程序将 my_list 列表的两个元素传给 test（）函数，程序在传入的 my一list 参数之前添加 了一个星号。

print()
# 实际上，即使是支持收集的参数，如果程序需要将一个元组传给该参数，那么同样需要使用逆
# 向收集。例如如下代码:
def foo(name, *nums):
    print("name参数：", name)
    print("nums参数：", nums)
my_tuple = (1,2,3)
# 使用逆向收集，将 my_tuple 元组的元素传给 nums 参数
foo('fkit', *my_tuple)
# 使用逆向收集，将 my_tuple 元组的第一个元素传给 name 参数，剩下元素传给 nums 参数
foo(*my_tuple)
# 不使用逆向收集， my_tuple 元组整体传给name 参数
foo(my_tuple)

print()
# 字典也支持逆向收集，字典将会以关键宇参数的形式传入。如如下代码
def bar(book, price, desc):
    print(book, " 这本书的价格是：", price)
    print('描述信息:', desc)

my_dict = {'price':89, 'book':'疯狂Python讲义', 'desc':'这是一本系统全面的Python学习图书'}
# 按逆向收集的方式将 my_dict 的多个 key-value 对传给 bar（）函数
bar(**my_dict)