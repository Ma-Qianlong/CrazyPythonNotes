#!/usr/bin/env python

# -*- *************** -*-
# @File  : for_stdin.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-12 17:43
# -*- *************** -*-


# sys.stdin 也是一个类文件对象（类似于文件的对象， Python 的很多 IO 流都是类文件对
# 象） ， 因此，程序同样可以使用 for 循环遍历 sys.stdin ， 这意味着程序可以通过 for 循环来获取用户
# 的键盘输入。

import sys

# 使用for循环遍历标准输入
for line in sys.stdin:
    print('用户输入：', line, end='')

# 上面代码使用 for 循环遍历 sys.stdin， 这意味着程序可以通过 for 循环来读取用户的键
# 盘输入————用户每输入一行，程序就会输出用户输入的这行。
