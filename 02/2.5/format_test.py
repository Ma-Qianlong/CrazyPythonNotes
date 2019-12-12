#!/usr/bin/env python

# -*- *************** -*-
# @File  : format_test.py
# @Description : 字符串格式化test
# @Author: mql
# @Time  : 2019/12/12 22:32
# -*- *************** -*-

# %s转换说明符，用str()函数转换
price = 108
print("the book's price is %s" % price)

user = "Charli"
age = 8
# 格式化字符串中有两个占位符，第三部分也应该提供两个变量或值
print("%s is a %s year old boy" % (user, age))

num = -28
print("num is: %i" % num)  # 转换为带符号的十进制
print("num is: %6i" % num)  # 转换为带符号的十进制（指定了字符串的最小宽度为6）
print("num is: %6d" % num)  # 转换为带符号的十进制
print("num is: %6o" % num)  # 转换为带符号的八进制
print("num is: %6x" % num)  # 转换为带符号的十六进制
print("num is: %6X" % num)  # 转换为带符号的十六进制
print("num is: %6s" % num)  # 转换为字符串 用str()
print("num is: %6r" % num)  # 转换为字符串 用repr()
print("num is: %6e" % num)  # 转换为科学计数法表示的浮点数
print("num is: %6E" % num)  # 转换为科学计数法表示的浮点数
print("num is: %6f" % num)  # 转换为十进制形式的浮点数
print("num is: %6F" % num)  # 转换为十进制形式的浮点数
print("num is: %6g" % num)  # 智能选择e或f格式
print("num is: %6G" % num)  # 智能选择E或F格式
# print("num is: %6C" % num)  # 转换为单字符（只接受整数或单字符字符串）

num2 = 30
# 最小宽度为6， 左边补0
print("num2 is: %06d" % num2)
# 最小宽度为6， 左边补0, 总是带上符号
print("num2 is: %+06d" % num2)
# 最小宽度为6， 左对齐
print("num2 is: %-6d" % num2)

# 精度值处理，被放在最小宽度之后，中间用点（.）来分割。
my_value = 3.1415926535
# 最小宽度为8， 小数点后保留3位
print("my_value is: %8.3f" % my_value)
# 最小宽度为8， 小数点后保留3位, 左边补0
print("my_value is: %08.3f" % my_value)
# 最小宽度为8， 小数点后保留3位, 左边补0, 始终带符号
print("my_value is: %+08.3f" % my_value)
the_name = 'Cahrlie'
# 只保留3个字符
print("the name is: %.3s" % the_name)
# 只保留2个字符, 最小宽度为10
print("the name is: %10.2s" % the_name)
