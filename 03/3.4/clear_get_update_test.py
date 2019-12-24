#!/usr/bin/env python

# -*- *************** -*-
# @File  : clear_get_update_test.py
# @Description : 字典的 clear(), get(), update()
# @Author: mql
# @Time  : 2019/12/24 16:39
# -*- *************** -*-


# clear()
cars = {'BMW': 8.5, 'BENS': 8.3, "AUDI": 3.8}
print(cars)
cars.clear()
print(cars)

print(end='\n')
# get(),据key获取value,不存在不会包KeyError错误，方括号获取会报
cars11 = [['BMW', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
cars1 = dict(cars11)
print(cars1)
print(cars1.get('BMW'))
print(cars1.get('BMW2'))
# print(cars1['BMW2']) # KeyError

print(end='\n')
# update()
cars1.update({"BMW": 4.5, 'PORSCHE': 9.3})
print(cars1)
