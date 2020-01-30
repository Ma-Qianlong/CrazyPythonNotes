#!/usr/bin/env python

# -*- *************** -*-
# @File  : polymorphism.py
# @Description : 多态1
# @Author: mql
# @Time  : 2020/1/21 18:18
# -*- *************** -*-

class Bird:
    def move(self, field):
        print('鸟在%s 上自由地飞翔' % field)

class Dog:
    def move(self, field):
        print('狗在%s 里飞快地奔跑' % field)

# x变量被赋值为Bird对象
x = Bird()
# 调用x变量的move()方法
x.move('天空') # 鸟在天空 上自由地飞翔

# x变量被赋值为Dog对象
x = Dog()
# 调用x变量的move()方法
x.move('草地') # 狗在草地 里飞快地奔跑

# 从上面的运行结果可以看出，
# 同一个变量 x 在执行同一个 move（）方法时，由于 x 指向的对象不同，
# 因此它呈现出不同的行为特征，这就是多态 。

