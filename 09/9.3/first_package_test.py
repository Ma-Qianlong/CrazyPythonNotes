#!/usr/bin/env python

# -*- *************** -*-
# @File  : first_package_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/4/21 16:46
# -*- *************** -*-


# 导入first_package包（模块）
import first_package

print('==========')
print(first_package.__doc__)
print(type(first_package))
print(first_package)

# 从上面的输出结果可以看出，在导入 first_package 包时，程序执行了该包所对应的文件夹下的
# __init__.py；从倒数第二行输出可以看到，包的本质就是模块；
# 从最后一行输出可以看到，使用 import first_package 导入包的本质就是加载井执行该包下的__init__.py 文件，然后将整个文件内容赋值给
# 与包同名的变量，该变量的类型是 module。
