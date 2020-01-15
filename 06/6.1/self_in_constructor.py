#!/usr/bin/env python

# -*- *************** -*-
# @File  : self_in_constructor.py
# @Description :
# @Author: mql
# @Time  : 2020/1/15 13:46
# -*- *************** -*-


class InConstructor:
    def __init__(self):
        foo = 0
        # 使用 self 代表该构造方法正在初始化的对象
        # 下面的代码将会把该构造方法正在初始化的对象的 foo 实例变量设为 6
        self.foo = 6


# 所有使用 InConstructor 创建的对象的 foo 实例变量将被设为 6
print(InConstructor().foo)
