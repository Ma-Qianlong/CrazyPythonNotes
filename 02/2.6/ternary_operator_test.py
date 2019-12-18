#!/usr/bin/env python

# -*- *************** -*-
# @File  : ternary_operator_test.py
# @Description : 三目运算符
# @Author: mql
# @Time  : 2019/12/18 11:23
# -*- *************** -*-


# 三目语法：True_statements if expression else False_statements
a = 5
b = 3
st = "a大于b" if a > b else "a不大于b"
print(st)
print("a大于b" if a > b else "a不大于b")

# True_statements 或 False_statements 中可以放置多条语句
# 以下两种方式：
# 1.多条语句以英文逗号(",")分隔：每条语句都会执行，程序返回多条语句返回值组成的元组
# 2.多条语句以英文分号(";")分隔：每条语句都会执行，程序程序只返回第一条语句的返回值

# 1 英文逗号(",")分隔
st = print("cracyit"), 'a大于b' if a > b else "a不大于b"
print(st, end="\n\n")

st = "cracyit", 'a大于b' if a > b else "a不大于b"
print(st, end="\n*********\n\n")

# 2 英文分号(";")分隔
st = print("cracyit");'a大于b' if a > b else "a不大于b"
print(st, end="\n\n")

st = "cracyit";'a大于b' if a > b else "a不大于b"
print(st)

print()
# 三目运算符支持嵌套
c = 5
d = 5
print("c大于d") if c > d else (print("c小于d") if c < d else print("c等于d"))
