#!/usr/bin/env python

# -*- *************** -*-
# @File  : Enum_test.py
# @Description : 枚举类
# @Author: mql
# @Time  : 2020/1/30 21:15
# -*- *************** -*-

import enum

# 定义Season枚举类
Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
# 程序可直接通过枚举值进行访问，
# 这些枚举值都是该枚举的成员，每个成员都有 name 、 value 两个属性，
# 其中 name 属性值为该枚举值 的变量名，
# value代表该枚举值的序号（序号通常从 1 开始〉。
# 直接访问指定枚举
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)

# 程序除可直接使用枚举之外，还可通过枚举变量名或枚举值来访问指定枚举对象。
# 根据枚举变量名访问枚举对象
print(Season['SUMMER'])  # Season.SUMMER
# 根据枚举值访问枚举对象
print(Season(3))  # Season.FALL

# 此外， Python 还为枚举提供了 一个 __members__ 属性，
# 该属性返回一个 dict 字典 ， 字典包含了该枚举的所有枚举实例。
# 程序可通过遍历 __members__ 属性来访问枚举的所有实例。
# 遍历 Season 枚举的所有成员
print()
print(Season.__members__)
for name, member in Season.__members__.items():
    print(name, '=>', member, ',', member.value)
