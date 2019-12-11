#!/usr/bin/env python

# -*- *************** -*-
# @File  : hex_test.py
# @Coding: utf-8
# @Time  : 2019/12/8 23:07
# @Author: mql
# -*- *************** -*-

# 十六进制整数 以0x或0X开头
hex_val1 = 0x13
hex_val2 = 0xaF
print("hexVal1的值为： {}".format(hex_val1))
print("hexVal2的值为： {}".format(hex_val2))

# 二进制整数 以0b或0B开头
bin_val = 0B111
print("bin_val的值为： {}".format(bin_val))
bin_val = 0b101
print("bin_val的值为： {}".format(bin_val))

# 八进制整数 以0o或0O开头
oct_val = 0o54
print("oct_val的值为： {}".format(oct_val))
oct_val = 0O17
print("oct_val的值为： {}".format(oct_val))

# 在数值中使用下划线（python3）
one_million = 1_000_000
print(one_million)
price = 234_234_234  # price实际值为234234234
android = 1234_1234.12  # android实际值为1234_1234.12
print(price)
print(android)