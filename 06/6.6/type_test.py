#!/usr/bin/env python

# -*- *************** -*-
# @File  : type_test.py
# @Description : 使用 type（）函数定义类
# @Author: mql
# @Time  : 2020/1/19 14:29
# -*- *************** -*-


#
class Role:
    pass


r = Role()

# 查看变量 r 的类型
print(type(r))  # <class '__main__.Role'>
# 查看 Role 类本身的类型
print(type(Role))  # <class 'type'>

# 从上面的输出结果可以看到， Role 类本身的类型是type。
# 这句话有点拗口，怎样理解 Role 类的类型是 type?

# 从 Python 解释器的角度来看，当程序使用 class 定义 Role 类时，也可理解为定义了 一个特殊
# 的对象 (type 类的对象)，并将该对象赋值给 Role 变量。
# 因此，程序使用 class 定义的所有类都是 type 类的实例 。

# 实际上 Python 完全允许使用 type（）函数（相当于 type 类的构造器函数）来创建 type 对象，
# 又、由于 type 类的实例就是类，因此 Python 可以使用 type（）函数来动态创建类 。
