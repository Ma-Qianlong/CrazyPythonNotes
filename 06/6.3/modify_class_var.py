#!/usr/bin/env python

# -*- *************** -*-
# @File  : modify_class_var.py
# @Description : 类变量和实例变量3
# @Author: mql
# @Time  : 2020/1/16 10:50
# -*- *************** -*-


# 要说明的是， Python 允许通过对象访 问类变量 ， 但如果程序通过对象尝试对类变量赋值 ，
# 此时性质就变了一－Python 是动态语言，赋值语句往往意味着定义新变量。
# 因此，如果程序通过对象对类变量赋值，其实不是对“类变量赋值”，而是定义新的实例变量 。

class Inventory:
    # 定义两个类变量
    item = '鼠标'
    quantity = 2000

    # 定义示例方法
    def change(self, item, quantity):
        # 下面的语句不是对类变量赋值，而是定义信息的实例变量
        self.item = item
        self.quantity = quantity


# 创建Inventory对象
iv = Inventory()
iv.change('显示器', 500)

print()
# 访问iv的item和quantity实例变量
print(iv.item)  # 显示器
print(iv.quantity)  # 500

print()
# 访问Inventory的item和quantity实例变量
print(Inventory.item)  # 鼠标
print(Inventory.quantity)  # 2000

print()
# 如果程序通过类修改了两个类变量的值，程序中 Inventory 的实例变量的值也不会受到任何影响 。 例如如下代码 。
Inventory.item = '类变量 item'
Inventory.quantity = '类变量 quantity'
# 访问iv的item和quantity实例变量
print(iv.item)  # 显示器
print(iv.quantity)  # 500

print()
# 同样，如果程序对一个对象的实例变量进行了修改，这种修改也不会影响类变量和其他对象的
# 实例变量。 例如如下代码 。
iv.item = '实例变量 item'
iv.quantity = '实例变量 quantity'
# 访问Inventory的item和quantity实例变量
print(Inventory.item)  # 类变量 item
print(Inventory.quantity)  # 类变量 quantity
