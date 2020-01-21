#!/usr/bin/env python

# -*- *************** -*-
# @File  : metaclass_test.py
# @Description : 使用 metaclass
# @Author: mql
# @Time  : 2020/1/19 15:00
# -*- *************** -*-


# 如果希望创建某一批类全部具有某种特征， 则可通过 metaclass 来实现。使用 rnetaclass 可以在
# 创建类时动态修改类定义 。

# 为了使用 metaclass 动态修改类定义，程序需要先定义 metaclass, metaclass 应该继承 type 类，
# 并重写__new__（）方法 。
# 下面程序定义了 一个 metaclass 类 。

# 定义ItemMetaClass, 继承 type
class ItemMetaClass(type):
    # cls 代表被动态修改的类
    # name 代表被动态修改的类名
    # basses 代表被动态修改类的所有父类
    # attr 代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, basses, attrs):
        # 为该类动态添加一个cal_price方法
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, basses, attrs)


# metaclass 类的 new 方法的作用是：
# 当程序使用 class 定义新类时，如果指定了 metaclass,
# 那么 metaclass 的 new 方法就会被自动执行。
# 例如，如下程序使用 metaclass 定义了两个类

# 定义Book类
class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


# 定义CellPhone类
class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '_discount')

    def __init__(self, price):
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount

# ItemMetaClass 类的__new__ 方法会为目标类动态添加 cal_price 方法，
# 因此，虽然在定义 Book 、CellPhone 类时没有定义 cal_price （）方法，
# 但这两个类依然有 cal_price（）方法。
# 如下程序测试了 Book 、CellPhone 两个类的 cal_price（）方法
b = Book("疯狂Python讲义", 89)
b.discount = 0.76
# 调用Book对象的cal_price()方法
print(b.cal_price())

cp = CellPhone(2399)
cp.discount = 0.85
# 调用CellPhone对象的cal_price()方法
print(cp.cal_price())

# 通过使用 metaclass 可以动态修改程序中的一批类，对它们集中进行某种修改。

# 这个功能在开发一些基础性框架时非常有用，程序可以通过使用 metaclass 为某一批需
# 要具有通用功能的类添加方法。
