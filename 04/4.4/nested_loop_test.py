#!/usr/bin/env python

# -*- *************** -*-
# @File  : nested_loop_test.py
# @Description : 嵌套循环
# @Author: mql
# @Time  : 2019/12/29 22:03
# -*- *************** -*-


# 外层循环
for i in range(0, 5):
    j = 0
    # 内层循环
    while j < 3:
        print("i的值位：%d , j的值为：%d" % (i, j))
        j += 1
