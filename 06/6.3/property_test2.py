#!/usr/bin/env python

# -*- *************** -*-
# @File  : property_test2.py
# @Description : 使用 property 函数定义属性2
# @Author: mql
# @Time  : 2020/1/16 22:23
# -*- *************** -*-


# 在使用 property（）函数定义属性时，也可根据需要只 传入少量的参数。
# 例如 ，如下代码使用 property（）函数定义了一个读写属性 ，该属性不能删除。

class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def getfullname(self):
        return self.first + "," + self.last
    def setfullname(self, fullname):
        first_last = fullname.rsplit(',')
        self.first = first_last[0]
        self.last = first_last[1]

    # 使用 property（） 函数定义 fullname 属性，只传入两个参数
    # 该属性是一个i卖写属性，但不能删除
    fullname = property(getfullname, setfullname)

u = User('悟空', '孙')
# 访问fullname属性
print(u.fullname)
# 对fullname赋值
u.fullname = '八戒,朱'
print(u.first)
print(u.last)
