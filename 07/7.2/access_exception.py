#!/usr/bin/env python

# -*- *************** -*-
# @File  : access_exception.py
# @Description :  访问异常信息
# @Author: mql
# @Time  : 2020/3/3 18:36
# -*- *************** -*-


# 如果程序需要在 except 块中访问异常对象的相关信息，则可通过为异常对象声明变量来实现 。
# 当 Python 解释器决定调用某个 except 块来处理该异常对象时，会将异常对象赋值给 except 块后的
# 异常变量，程序即可通过该变量来获得异常对象的相关信息 。
# 所有的异常对象都包含了如下几个常用属性和方法 。
# ~ args：该属性返回异常的错误编号和描述字符串 。
# ~ errno ：该属性返回异常的错误编号。
# ~ strerror：该属性返回异常的描述宇符串。
# ~ with_traceback（）： 通过该方法可处理异常的传播轨迹信息。
# 下面例子演示了程序如何访问异常信息 。

def foo():
    try:
        fis = open("a.txt");
    except Exception as e:
        # 访问异常的错误编号和详细信息
        print(e.args)
        # 访问异常的错误编号
        print(e.errno)
        # 访问异常的详细信息
        print(e.strerror)

foo()

# 从上面程序可以看出，如果要访问异常对象，只要在单个异常类或异常类元组（多异常捕获）之后使用 as 再加上异常变量即可 。