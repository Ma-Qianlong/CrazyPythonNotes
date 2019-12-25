#!/usr/bin/env python

# -*- *************** -*-
# @File  : pass_test.py
# @Description : pass语句，就是空语句
# @Author: mql
# @Time  : 2019/12/25 23:31
# -*- *************** -*-


# pass空语句不做任何事，仅仅占个位

s = input("请输入一个整数：")
s = int(s)
if s > 5:
    print("大于5")
elif s < 5:
    # 空语句，相当于站位符
    pass
else:
    print("等于5")
