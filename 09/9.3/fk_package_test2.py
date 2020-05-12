#!/usr/bin/env python

# -*- *************** -*-
# @File  : fk_package_test2.py
# @Description : 
# @Author: mql
# @Time  : 2020/03/21 18:37
# -*- *************** -*-


# 导入 fk_package 包，实际上就是导入该包下的＿__init__.py 文件
import fk_package

# 直接使用 fk_package. 前缀即可调用它所包含的模块内的程序单元
fk_package.print_blank_triangle(5)
im = fk_package.Item(4.5)
print(im)
fk_package.print_multiple_chart(5)