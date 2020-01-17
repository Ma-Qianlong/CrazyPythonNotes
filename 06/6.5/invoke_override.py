#!/usr/bin/env python

# -*- *************** -*-
# @File  : invoke_override.py
# @Description : 使用未绑定方法调用被重写的方法
# @Author: mql
# @Time  : 2020/1/17 21:49
# -*- *************** -*-

# 如果在子类中调用重写之后的方法， Python 总是会执行子类重写的方法，不会执行父类中被
# 重写的方法。如果需要在子类中调用父类中被重写 的实例方法，那该怎么办呢？

# Python 类相当于类空间，因此 Python 类中的方法本质上相当于类空间内的函数。
# 所以，即使是实例方法，Python 也允许通过类名调用。
# 区别在于 ：
# 在通过类名调用实例方法时 ，Python 不会为实例方法的第一个参数 self 自动绑定参数值，
# 而是需要程序显式绑定第一个参数 self。这种机制被称为未绑定方法。

# 通过使用未绑定方法即可在子类中再次调用父类中被重写的方法。例如如下程序。

class BaseClass:
    def foo(self):
        print('父类中定义的foo方法')


class SubClass:
    # 重写foo方法
    def foo(self):
        print("子类重写父类中的 foo 方法 ")

    def bar(self):
        print('执行 bar 方法')
        # 直接执行 foo 方法，将会调用子类重写之后的 foo （）方法
        self.foo()
        # 使用类名调用实例方法〈未绑定方法）调用父类被重写的方法
        BaseClass.foo(self)


sc = SubClass()
sc.bar()
