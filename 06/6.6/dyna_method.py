#!/usr/bin/env python

# -*- *************** -*-
# @File  : dyna_method.py
# @Description : 动态属性
# @Author: mql
# @Time  : 2020/1/19 10:49
# -*- *************** -*-


class Cat:
    def __init__(self, name):
        self.name = name

def walk_func(self):
    print('%s 慢慢的走过一片草地' % self.name)

d1 = Cat('Carfield')
d2 = Cat('Kitty')

# d1.walk() # AttributeError: 'Cat' object has no attribute 'walk'
# 为Cat动态添加walk()方法， 该方法的第一个参数会自动绑定
Cat.walk = walk_func
# d1、d2调用walk()方法
d1.walk()
d2.walk()