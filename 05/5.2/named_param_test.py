#!/usr/bin/env python

# -*- *************** -*-
# @File  : named_param_test.py
# @Description : 关键字（ keyword ）参数
# @Author: mql
# @Time  : 2020/1/13 20:44
# -*- *************** -*-


# Python 函 数的参数名不是无意义的， Python 允许在调用函数时通过名字来传入参数值。
# 因此，Python 函数的参数名应该具有更好的语义——程序可以立刻明确传入函数的每个参数的含义。
# 按照形参位置传入的参数被称为位置参数。
# 如果使用位置参数的方式来传入参数值，则必须严格按照走义函数时指定的顺序来传入参数值：
# 如果根据参数名来传入参数值，则无须遵守定义形参的顺序，这种方式被称为关键字（keyword）参数。

# 定义一个函数
def girth(width, height):
    print("width:", width)
    print("height:", height)
    return 2 * (width + height)


# 传统函数调用的方式，根据位置传入参数
print(girth(3.5, 4.8))
# 根据关键字传入参数值
print(girth(width=3.5, height=4.8))
# 在使用关键字传参是可以调换位置
print(girth(height=4.8, width=3.5))
# 部分使用关键字参数，部分使用位置参数
print(girth(3.5, height=4.8))

# 需要说明的是，如果希望在调用函数时混合使用关键字参数和位置参数，则关键字参数必须位
# 于位置参数之后 。 换句话说，在关键字参数之后的只能是关键字参数 。 例如如下代码是错误的。

# 必须将位置参数放在关键字参数之前，下面代码错误
# print(girth(width=3.5, 4.8))