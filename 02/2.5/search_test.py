#!/usr/bin/env python

# -*- *************** -*-
# @File  : search_test.py
# @Description : 查找、替换相关方法
# @Author: mql
# @Time  : 2019/12/17 22:36
# -*- *************** -*-


s = 'crazyit.org is a good site b'
# 是否已crazyit开头
print(s.startswith('crazyit'))

print(s.endswith("site"))

# 出现“org”的位置
print(s.find("org"))
print(s.index("org"))
print(s.find('org', 9))  # find找不到返-1
# print(s.index('org', 9)) # index找不到报错

# 替换
print(s.replace("org", "xxxx"))
print(s.replace('org', 'xxxx', 1))
# 定义翻译映射表
table = {97: 945, 98: 946, 116: 964}
print(s.translate(table))

# 可以用maketrans()方法创建翻译映射表
# 翻译映射表不能直接用字符串本身，而是其编码
table = str.maketrans('abt啊', 'αβτa')
print(table)

table = str.maketrans("abc", '123')
print(table)