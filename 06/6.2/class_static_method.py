#!/usr/bin/env python

# -*- *************** -*-
# @File  : class_static_method.py
# @Description : 类方法与静态方法
# @Author: mql
# @Time  : 2020/1/15 14:46
# -*- *************** -*-


# 实际上， Python 完全支持定义类方法，甚至支持定义静态方法 。
# Python 的类方法和静态方法很相似，它们都推荐使用类来调用（其实也可使用对象来调用〕。
# 类方法和静态方法的区别在于 ：
#   Python 会自动绑定类方法的第一个参数，类方法的第一个参数（通常建议参数名为 cls）会自动绑
#   定到类本身：但对于静态方法则不会自动绑定。

# 使用＠classmethod 修饰的方法就是类方法：使用＠staticmethod 修饰的方法就是静态方法。

class Bird:
    # 使用@classmethod 修饰的方法是类方法
    @classmethod
    def fly(cls):
         print('类方法：', cls)

    # 使用@staticmethod 休书的方法是静态方法
    @staticmethod
    def info(p):
        print('静态方法info: ', p)

# 调用类方法， Bird 类会自动绑定到第一个参数
Bird.fly()
# 调用静态方法，不会自动绑定，因此程序必须手动绑定第一个参数
Bird.info("crazyit")

# 创建Bird 对象
b = Bird()
# 使用对象调用 fly （）类方法，其实依然还是使用类调用的
# 因此第一个参数依然被自动绑定到 Bird 类
b.fly()
# 使用对象调用 info （）静态方法，其实依然还是使用类调用的
# 因此程序必须为第一个参数执行绑定
b.info('fkit')

# 在使用 Python 编程时， 一般不需要使用类方法或静态方法，程序完全可以使用函数来代替类
# 方法或静态方法。但是在特殊的场景（比如使用工厂模式）下，类方法或静态方法也是不锚的选择 。
