#!/usr/bin/env python

# -*- *************** -*-
# @File  : gobang.py
# @Description : 使用 try...except 捕获异常
# @Author: mql
# @Time  : 2020/3/3 18:06
# -*- *************** -*-

inputStr = input("请输入坐标， 应以x,y的格式:\n")
while inputStr != None :
    try:
        # 将用户输入的字街串以逗号（，）作为分隔符，分隔成两个字符串
        x_str, y_str = inputStr.split(sep=",")

        int(x_str)
        int(y_str)

    except Exception:
        inputStr = input("输入的坐标不合法，请重新输入，应以x,y的格式:\n")
        continue

    print("OK!")
    break