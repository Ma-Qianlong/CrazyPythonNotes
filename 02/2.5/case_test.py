#!/usr/bin/env python

# -*- *************** -*-
# @File  : case_test.py
# @Description : 大小写相关
# @Author: mql
# @Time  : 2019/12/16 23:18
# -*- *************** -*-

# 在交互式解释其中可以用两个帮助函数查看python文档
# 用dir() 和 help()配合使用
# 如dir(str) help(str.title)

a = 'our domain is mydomain.com.cn'
# 每个词首字母大写
print(a.title())
print(str.title(a))
# 每个字母小写
print(a.lower())
# 每个字母大写
print(a.upper())
print("a is: %s" % a)

