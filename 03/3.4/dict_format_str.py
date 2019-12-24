#!/usr/bin/env python

# -*- *************** -*-
# @File  : dict_format_str.py
# @Description : 使用字典格式化字符串
# @Author: mql
# @Time  : 2019/12/24 17:16
# -*- *************** -*-

# 在字符串模板中使用key
temp = '书名是:%(name)s, 价格是:%(price)010.2f, 出版社:%(publish)s'
book = {'name': '疯狂Python讲义', 'price': 78.9, 'publish': '电子社'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
book = {'name': '疯狂Python讲义', 'price': 88.9, 'publish': '电子社'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
