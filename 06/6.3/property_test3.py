#!/usr/bin/env python

# -*- *************** -*-
# @File  : property_test3.py
# @Description : 使用 property 函数定义属性3
# @Author: mql
# @Time  : 2020/1/16 22:36
# -*- *************** -*-


# ***提示***
# 在某些编程语言中，类似于这种 proerty 合成的属性被称为计算属性。
# 这种属性并不真正存储任何状态，它的值其实是通过某种算法计算得到的。
# 当程序对该属性赋值时，被赋的值也会被存储到其他实例变量中 。

# 还可使用＠property 装饰器来修饰方法，使之成为属性 。

class Cell:
    # 使用@property修饰方法，相当于为该属性设置getter方法
    @property
    def state(self):
        return self._state
    # 为state属性设置setter方法
    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    # 为 is_dead 属性设置 getter 方法
    # 只有 getter 方法的属性是只读属性
    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'

c = Cell()
c.state = 'Alive'
print(c.state)
print(c.is_dead)