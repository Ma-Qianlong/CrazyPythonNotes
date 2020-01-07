#!/usr/bin/env python

# -*- *************** -*-
# @File  : break_test.py
# @Description : break结束循环
# @Author: mql
# @Time  : 2020/1/7 18:30
# -*- *************** -*-

for i in range(0, 10):
    print("i的值是：", i)
    if i == 2:
        # 执行该语句将结束循环
        break
