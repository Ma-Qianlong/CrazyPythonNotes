#!/usr/bin/env python

# -*- *************** -*-
# @File  : fk_package_test1.py
# @Description : 
# @Author: mql
# @Time  : 2020/4/21 17:58
# -*- *************** -*-


# 导入 fk_package 包，实际上就是导入包下的__init__.py 文件
# import fk_package  # 在fk_package文件夹下没有__init__.py 文件时，此处代码无效

# 导入 fk_package 包下的 print_shape 模块
# 实际上就是导入 fk_package 目录下的 print_shape.py
import fk_package.print_shape
# 导入 fk package 包下的 billing 模块
# 实际上就是导入 fk_package 目录下的 billing.py
from fk_package import billing
# 导入 fk_package 包下的 arithmetic_chart 模块
# 实际上就是导入 fk_package 目录下的 arithmetic_chart.py
import fk_package.arithmetic_chart

fk_package.print_shape.print_blank_triangle(5)
im = billing.Item(5.5)
print(im)
fk_package.arithmetic_chart.print_multiple_chart(9)