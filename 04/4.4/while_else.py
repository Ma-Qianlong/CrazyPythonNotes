#!/usr/bin/env python

# -*- *************** -*-
# @File  : while_else.py
# @Description :  while 循环使用else代码块
# @Author: mql
# @Time  : 2019/12/26 17:31
# -*- *************** -*-


# Python 的循环都可以定义 else 代码块，当循环条件为 False 时，程序会执行 else 代码块
# 如下，while 循环定义else代码块
count_i = 0
while count_i < 5:
    print('cout_i小于5：', count_i)
    count_i += 1
else:
    print('count_i 大于或等于5：', count_i)

print("---------------")
# 简单来说，程序在结束循环之前，会先执行 else 代码块。
# 从这个角度来看， else 代码块其实没有太大的价值一一将 else 代码块直接放在循环体之外即可 。
# 也就是说，上面的循环其实可改为如下形式
count_i = 0
while count_i < 5:
    print('cout_i小于5：', count_i)
    count_i += 1
print('count_i 大于或等于5：', count_i)