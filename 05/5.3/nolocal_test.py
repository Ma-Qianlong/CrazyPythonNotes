#!/usr/bin/env python

# -*- *************** -*-
# @File  : nolocal_test.py
# @Description : 局部函数2
# @Author: mql
# @Time  : 2020/1/14 10:41
# -*- *************** -*-


# 局部函数内的变量也会遮蔽它所在函数内的局部变量（这句话有点拗口），请看如下代码 。

def foo():
    # 局部变量name
    name = 'Charlie'
    def bar():
        # 访问bar函数所在的foo函数内的name变量
        print(name) # Charlie
        name = '孙悟空'
    bar()
foo()

# 运行上面代码，会导致如下错误。
# UnboundLocalError: local variable 'name' referenced before assignment
# 该错误是由局部变量遮蔽局部变量导致的，在 bar（）函数中定义的 name 局部变量遮蔽了它所在
# foo（）函数内的 name 局部变量，因此导致程序中粗体字代码报错。

# 解决方式见next

# next: nonlocal_test2.py