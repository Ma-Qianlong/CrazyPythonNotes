#!/usr/bin/env python

# -*- *************** -*-
# @File  : chars_test.py
# @Description : 字符串 序列相关
# @Author: mql
# @Time  : 2019/12/13 15:28
# -*- *************** -*-


s = 'crazyit.org is very good'
# 获取字符串中索引为2的字符
print(s[2])

# 获取从右往左，第4个字符
print(s[-4])

# 获取索引3到5(不含)的字串
print(s[3:5])
# 获取索引3到倒数5的子串
print(s[3:-5])
# 获取索引倒数6到倒数3的子串
print(s[-6:-3])
print(s[-3:-6])

# 允许省略起始索引或结束索引
print(s[3:])
print(s[:-5])

# 用in运算符判读是否包含某个子串
print('very' in s)
print('ffdd' in s)

# 用内置函数len()获取字符串长度
print(len(s))
print(len('test'))

# 用全局内置函数min()和max()获取最小字符串和最大字符串
print(max(s))  # z
print(min(s))  # 空格
