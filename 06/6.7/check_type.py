#!/usr/bin/env python

# -*- *************** -*-
# @File  : check_type.py
# @Description : 检查类型
# @Author: mql
# @Time  : 2020/1/21 18:35
# -*- *************** -*-


# Python 提供了如下两个函数来检查类型。
# >> issubclass(cls, class or_tuple） ：检查 cls 是否为后一个类或元组包含的多个类中任意类的子类。
# >> isinstance(obj , class_or_tuple）：检查 obj 是否为后一个类或元组包含的多个类中任意类的对象。

# 通过使用上面两个函数，程序可以方便地先执行检查，然后才调用方法，

# 这样可以保证程序不会出现意外情况。

# 定义一个字符串
hello = "Hello"
#  “Hello” 是 str 类的实例，输出 True
print('“Hello” 是否是 str 类的实例：', isinstance(hello, str))
#  “Hello”  是 object 类的子类的实例，输出 True
print('"Hello是否是object类的子类："', isinstance(hello, object))
# str 是 object 类的子类，输出 True
print('str 是否是 object 类的子类：', issubclass(str, object))
# " Hello ”不是 tuple 类及其子类的实例，输出 False
print('” Hello ” 是否是 tuple 类的实例 ： ', isinstance(hello, tuple))
# " str ”不是 tuple 类的子类的实例，输出 False
print('str 是否是 tuple 类的子类 ： ', isinstance(str, tuple))

# 定义一个列表
my_list = [2, 4]
# [2, 03]是 list 类的实例，输出True
print('[2, 03]是否是 list 类的实例：', isinstance(my_list, list))
# [2, 03]是 object 类的子类的实例，输出True
print('[2, 03]是否是 object 类及其子类的实例：', isinstance(my_list, object))

# list 是 object 的子类， 输出True
print('list 是否是 object 的子类', issubclass(list, object))
# [2 , 03 ］不是 tuple 类及其子类及其子类的实例，输出 False
print('[2 , 03］是否是 tuple 类及其子类及其子类的实例:', isinstance(my_list, tuple))
#  list 不是 tuple 类的子类，输出 False
print('list 是否是 tuple 的子类', issubclass(list, tuple))
