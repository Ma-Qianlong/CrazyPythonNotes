#!/usr/bin/env python

# -*- *************** -*-
# @File  : break_else.py
# @Description : 对于带else 块的 for 循环 ，
#               如果使用 break 强行中止循环，
#               程序将不会执行 else 块
# @Author: mql
# @Time  : 2020/1/7 18:33
# -*- *************** -*-


for i in range(0,10):
    print("i 的值是：", i)
    if i == 2:
        break
    else:
        print('else块', i)