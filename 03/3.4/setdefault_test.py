#!/usr/bin/env python

# -*- *************** -*-
# @File  : setdefault_test.py
# @Description : dict的setdefault()方法
# @Author: mql
# @Time  : 2019/12/24 17:05
# -*- *************** -*-


cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 设置默认值，该 key 在 dict 中不存在 ， 新增 key-value 对
print(cars.setdefault('PORSCHE', 9.2))
print(cars)
# 设置默认值，该 key 在 dict 中存在，不会修改 dict 内容
print(cars.setdefault("BMW", 3.4))
print(cars)