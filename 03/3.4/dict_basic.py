#!/usr/bin/env python

# -*- *************** -*-
# @File  : dict_basic.py
# @Description : 字典的基本用法
# @Author: mql
# @Time  : 2019/12/24 16:26
# -*- *************** -*-


scores = {'语文': 89}
# 通过key访问value
print(scores['语文'])
# 增加键值对
scores['数学'] = 99
scores[92] = 5.5
print(scores)
# 删除键值对
del scores["语文"]
del scores['数学']
print(scores)
# 修改值
cars = {'BMW': 8.5, 'BENS': 8.3, "AUDI": 3.8}
cars['BENS'] = 3.4
cars['AUDI'] = 7.9
print(cars)
# 判读是否包含指定的key
print("AUDI" in cars)
print("AUDIA8" in cars)
print("AUDIA9" not in cars)
