#!/usr/bin/env python

# -*- *************** -*-
# @File  : ifcorrect_test.py
# @Description : if逻辑处理
# @Author: mql
# @Time  : 2019/12/25 23:23
# -*- *************** -*-

# test1

age = 45
if age > 60:
    print("老年人")
elif age > 40:
    print("中年人")
elif age > 20:
    print("青年人")

# 以上程序等同于以下，test2
if age > 60:
    print("老年人")
if age > 40 and not (age > 60):
    print("中年人")
if age > 20 and not (age > 60) and not (age > 40 and not (age > 60)):
    print("青年人")
