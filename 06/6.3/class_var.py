#!/usr/bin/env python

# -*- *************** -*-
# @File  : class_var.py
# @Description : 类变量和实例变量1
# @Author: mql
# @Time  : 2020/1/16 10:37
# -*- *************** -*-


# 在类命名空间内定义的变量就属于类变量 ， Python 可以使用类来读取、修改类变量。

class Address:
    detail = '广州'
    post_code = '510660'
    def info(self):
        # 尝试直接访问类变量，报错
        # print(detail)
        # 通过类访问类变量
        print(Address.detail)
        print(Address.post_code)

# 通过类来访问Address类的变量
print(Address.detail)
addr = Address()
addr.info()
# 修改Address类的类变量
Address.detail = '佛山'
Address.post_code = '460110'
addr.info()

# 对于类变量而言，它们就是属于在类命名空间内定义的变量 ，因此程序不能直接访问这些变量，
# 程序必须使用类名来调用类变量。不管是在全局范围内还是函数内访问这些类变量，都必须使用类
# 名进行访问。


