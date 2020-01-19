#!/usr/bin/env python

# -*- *************** -*-
# @File  : slots_test.py
# @Description : 动态属性与 __slots__
# @Author: mql
# @Time  : 2020/1/19 10:55
# -*- *************** -*-


# Python 的这种动态性固然有其优势 ，但也给程序带来了一定的隐患：
# 程序定义好的类，完全有可能在后面被其他程序修改，这就带来了一些不确定性。
# 如果程序要限制为某个类动态添加属性和方法，则可通过 slots 属性来指定 。

# __slots__属性的值是一个元组，该元组的所有元素列出了该类的实例允许动态添加的所有属性
# 名和方法名（对于 Python 而言，方法相当于属性值为函数的属性） 。 例如如下程序 。

class Dog:
    __slots__ = ('walk', 'age', 'name')

    def __init__(self, name):
        self.name = name

    def test():
        print('预先定义的test方法')


d = Dog('Snoopy')
from types import MethodType
# 只允许为实例动态添加 walk、 age 、 name 这三个属性或方法
d.walk = MethodType(lambda self: print('%s正在慢慢地走' % self.name), d)
d.age = 5
d.walk()
# d.foo = 30 # AttributeError: 'Dog' object has no attribute 'foo'

# 需要说明 的是， __slots__ 属性并不限制通过类来动态添加属性或方法，因此下面代码是合法的。
Dog.bar = lambda self: print('abc')
d.bar()

# 此外 ， __slots__ 属性指定的限制只对当前类的实例起作用，对该类派生出来的子类是不起作用的。
class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)
        pass

gd = GunDog('Puppy')
# 完全可以为 GunDog 实例动态添加属性
gd.speed = 99
print(gd.speed)

# 如果要限制子类的实例动态添加属性和方法，则需要在子类中也定义 slots 属性，
# 这样，子类的实例允许动态添加属性和方法就是子类的__slots__元组加上父类的__slots__元组的和。
