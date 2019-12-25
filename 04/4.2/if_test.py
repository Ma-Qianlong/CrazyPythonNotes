# !/usr/bin/env python

# -*- *************** -*-
# @File  : if_test.py
# @Description : 
# @Author: mql
# @Time  : 2019/12/25 21:49
# -*- *************** -*-


s_age = input("请输入年龄：")
age = int(s_age)
if age > 20:
    # age大于20时，下面整体缩进代码块才会执行
    print("年龄已经大于20岁了")
    print("20岁以上的人应该学会承担责任...")
