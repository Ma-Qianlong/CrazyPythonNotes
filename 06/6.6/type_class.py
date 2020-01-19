#!/usr/bin/env python

# -*- *************** -*-
# @File  : type_class.py
# @Description : 使用 type（）函数定义类
# @Author: mql
# @Time  : 2020/1/19 14:35
# -*- *************** -*-


# 实际上 Python 完全允许使用 type（）函数（相当于 type 类的构造器函数）来创建 type 对象，
# 又由于 type 类的实例就是类，因此 Python 可以使用 type（）函数来动态创建类 。 例如如下程序。

def fn(self):
    print('fn函数')
# 使用type()定义Dog类
Dog = type('Dog', (object,),dict(walk=fn, age=6))
# 创建Dog对象
d = Dog()
# 分别查看d、Dog的类型
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)

# 上面粗体字代码使用 type（）定义了 一个 Dog 类。在使用 type（）定义类时可指定三个参数。
# 》参数一 ：创建的类名。
# 》参数二 ： 该类继承的父类集合。由于 Python 支持多继承，因此此处使用元组指定它的多个
#   父类。即使实际只有一个父类， 也需要使用元组语法（必须要多一个逗号〉。
# 》参数三 ： 该宇典对象为i豆类绑定 的类变量和方法。其中字典的 key 就是类变量或方法名 ，
#   如果字典的 value 是普通值，那就代表类变量 ； 如果字典的 value 是函数，则代表方法 。
#   由此可见，上面粗体字代码定义了 一个 Dog 类 ， 该类继承了 object 类，还为i豆类定义了 一个
#   walk （）方法和一个 age 类变量。

# 从上面的输出结果可以看出，使用 type（）函数定义的类与直接使用 class 定义的类井没有任何区别。
# 事实上 ， Python 解释器在执行使用 class 定义的类时，其实依然是使用 type（）函数来创建类
# 的 。因此，无论通过哪种方式定义类，程序最终都是创建一个 type 的实例。