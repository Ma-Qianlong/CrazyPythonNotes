#!/usr/bin/env python

# -*- *************** -*-
# @File  : property_test.py
# @Description : 使用 property 函数定义属性1
# @Author: mql
# @Time  : 2020/1/16 11:03
# -*- *************** -*-


# 如果为 Python 类定义了 getter 、 seeter 等访问器方法，则可使用 property（）函数将它们定义成属
# 性（相当于实例变量 ）。
# property（）函数的语法格式如下 ：
#   property(fget=None , fset=None , fdel=None , doc=None)
# 从上面的语法格式可以看出，在使用 property（）函数时，可传入 4 个参数，分别代表 getter 方
# 法 、 setter 方法、del 方法和 doc ， 其中 doc 是一个文档字符串，用于说明该属性 。
# 当然，开发者调用 property 也可传入 0 个（既不能读，也不能写的属性）、 1 个（只读属性）、 2 个（读写属性、 3
# 个（读写属性，也可删除〉和 4 个（读写属性，也可删除，包含文档说明〉参数 。

# 例如，如下程序定义了 一个 Rectangle 类，该类使用 property（）函数定义了一个 size 属性 。

