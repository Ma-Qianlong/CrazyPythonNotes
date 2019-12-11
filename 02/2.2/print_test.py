#!/usr/bin/env python

# -*- *************** -*-
# @File  : print_test.py.py
# @Coding: utf-8
# @Time  : 2019/12/5 22:16
# @Author: mql
# -*- *************** -*-

user_name = 'mql'
user_age = 27
# 同时输出多个变量和字符串
print('读者名：', user_name, "年龄：", user_age)

# 同时输出多个变量和字符串,指定分隔符
print('读者名：', user_name, "年龄：", user_age, sep="|")

# 设置end参数，指定输出后不再换行
print(40, "\t", end="")
print(50, "\t", end="")
print(60, "\t", end="")

# 输出到文件，默认为控制台sys.stdout
f = open("poem.txt", "w")  # 打开文件以便写入
print("呵呵哒", file=f)
print("哈哈哈", file=f)
