#!/usr/bin/env python

# -*- *************** -*-
# @File  : Person.py
# @Description : 
# @Author: mql
# @Time  : 2020/1/14 15:07
# -*- *************** -*-

class Person:
    'Person 类'
    # 定义变量
    hair = 'black'

    def __init__(self, name='Charlie', age=8):
        # 为Person对象增加两个实例变量
        self.name = name
        self.age = age

    # 定义方法
    def say(self, content):
        print(content)


# 上面的 Person 类代码定义了 一个构造方法，该构造方法只是方法名比较特殊： init ，该方
# 法的第一个参数同样是 self，被绑定到构造方法初始化的对象 。
# 与函数类似的是 ， Python 也允许为类定义说明文挡 ， 该文档同样被放在类声明之后、类体之
# 前，如上面程序中第二行的字符串所示 。
# 在定义类之后，接下来即可使用该类了 。 Python 的类大致有如下作用 。
# 〉定义变量 。
# 〉创建对象 。
# 〉派生子类

# 用 Person 类的构造方法，返回一个 Person 对象
# 将该 Person 对象赋值给 p 变量
p = Person()
print(type(p))
print(p)
print(dir(p))

# 在创建对象之后，接下来即可使用该对象了 。 Python 的对象大致有如下作用 。
# 》操作对象的实例变量 （包括访问实例变量的值、添加实例变量、删除实例变量）。
# 》调用对象的方法 。

# 对象访问方法或变量的语法是 ： 对象．变量｜方法（参数〉 。 在这种方式中，对象是主调者，用于访问该对象的变量或方法。

# 输出p的name、age实例变量
print(p.name, p.age)  # Charlie 8
# 访问 p 的 name 实例变量，直接为该实例变量赋值
p.name = '李刚'
# 调用 p 的 say （）方法，在声明白 say（）方法时定义了两个形参
# 但第一个形参（ self ）是自动绑定的，因此调用该方法只需为第二个形参指定一个值
p.say("Pytho口语言很简单，学习很容易！")
# 次输出 p 的 name 、 age 实例变量
print(p.name, p.age)  # 李刚 8

print()
# 由于 Python 是动态语言，因此程序完全可以为 p 对象动态增加实例变量 只要为它的新变
# 量赋值即可 ；也可以动态删除实例变量一一使用 de！语句即可删除

# 为 p 对象增加一个 skills 实例变量
p.skills = ['programming', 'swimming']
print(p.skills)
# 删除 p 对象的 name 实例变量
del p.name
# 再次访问 p 的 name 实例变量
# print(p.name)  # AttributeError: 'Person' object has no attribute 'name'

print()

# Python 是动态语言，当然也允许为对象动态增加方法。比如上面程序中在定义 Person 类时只
# 定义了 一个 say（）方法，但程序完全可以为 p 对象动态增加方法 。
# 但需要说明的是，为 p 对象动态增加的方法 ， Python 不会自动将调用者自动绑定到第一个参
# 数（即使将第一个参数命名为 self 也没用）。

def info(self):
    print("---info函数---", self)

# 使用 info 对 p 的 foo 方法赋值（动态增加方法）
p.foo = info
# Python 不会自动将调用者绑定到第一个参数
# 因此程序需要手动将调用者绑定到第一个参数
p.foo(p)

# 用 lambda 表达式为 p 对象的 bar 方法赋值（动态增加方法）
p.bar = lambda self: print('---lambda表达式---', self)
p.bar(p)

print()

# 如果希望动态增加的方法也能自动绑定到第一个参数，则可借助于 types 模块下的 MethodType 进行包装
def intro_func(self, content):
    print("我是一个人， 信息为：%s" % content)
# 导入MethodType
from types import MethodType
# 使用 MethodType 对 intro_func 进行包装，将该函数的第一个参数绑定为 P
p.intro = MethodType(intro_func, p)
# 第一个参数已经绑定了，无须传入
p.intro("生活在别处")