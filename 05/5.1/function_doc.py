#!/usr/bin/env python

# -*- *************** -*-
# @File  : function_doc.py
# @Description : 为函数提供文档
# @Author: mql
# @Time  : 2020/1/13 14:44
# -*- *************** -*-


def my_max(x, y):
    '''
    获取两个数值之间较大数的函数

    my max(x, y)
        返回 x 、 y 两个参数之间较大的那个数
    '''
    # 定义一个变量 z ，该变量等于 x 、 y 中较大的值
    z = x if x > y else y
    # 返回变量 z 的值
    return z

# 使用 help （）函数查看 my_max 的帮助文档
help(my_max)
# 通过函数的__doc__属性访问函数的说明文挡
print(my_max.__doc__)