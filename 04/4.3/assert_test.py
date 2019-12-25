#!/usr/bin/env python

# -*- *************** -*-
# @File  : assert_test.py
# @Description : assert断言
# @Author: mql
# @Time  : 2019/12/25 23:37
# -*- *************** -*-


# asser断言，它对一个bool表达式进行断言
# 如果bool表达式位True,程序继续执行；否则程序引发AssertinError错误

s_age = input("请输入您的年龄：")
age = int(s_age)
assert 20 < age < 80
print("您输入的年龄在20和80之间")

