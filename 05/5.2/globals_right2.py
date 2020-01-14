#!/usr/bin/env python

# -*- *************** -*-
# @File  : globals_right2.py
# @Description : 2. 在函数中声明全局变量
# @Author: mql
# @Time  : 2020/1/14 10:59
# -*- *************** -*-

# 为了避免在函数中对全局变量赋值（不是重新定义局部变量），
# 可使用 global 语句句来声明全局变量。
name = 'Charlie'


def test():
    # 声明 name 是全局变量，后面的赋值语句不会重新定义局部变量
    global name
    print(name)  # Charlie
    name = '孙悟空'


test()
print(name)  # 孙悟空

# 增加了“ global name”声明之后，程序会把 name 变量当成全局变量，这意味着 test（）函数后面
# 对 name 赋值的语句只是对全局变量赋值，而不是重新定义局部变量。