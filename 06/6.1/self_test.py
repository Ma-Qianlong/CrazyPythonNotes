#!/usr/bin/env python

# -*- *************** -*-
# @File  : self_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/1/15 14:08
# -*- *************** -*-


# 需要说明的是，自动绑定的 self 参数并不依赖具体的调用方式，不管是以方法调用还是 以函数
# 调用的方式执行它， self 参数一样可以自动绑定。
class User:
    def test(self):
        print('self参数：', self)

u = User()
# 以方法形式调用 test （）方法
u.test()
# 将以user对象的凡是调用 test（）方法

foo = u.test
# 过 foo 变量（函数形式〉调用 test （）方法、
foo()
