#!/usr/bin/env python

# -*- *************** -*-
# @File  : Dog.py
# @Description : 
# @Author: mql
# @Time  : 2020/1/15 13:46
# -*- *************** -*-


class Dog:
    def jump(self):
        print("正在执行jump()方法")

    def run(self):
        # 使用self参数引用调用run方法的对象
        self.jump()
        print("正在执行run方法")

# 当 Python 对象的一个方法调用另 一个方法时，不可以省略 self。
# Python 语言的设计来看，Python 的类、对象有点类似于一个命名空间，因此在
# 调用类、对象的方法时，一定要加上“类.”或“对象.”的形式。
# 如果直接调用某个方法，这种形式属于调用函数。
