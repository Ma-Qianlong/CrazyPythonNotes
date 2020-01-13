#!/usr/bin/env python

# -*- *************** -*-
# @File  : multi_return.py
# @Description : 多个返回值
# @Author: mql
# @Time  : 2020/1/13 14:49
# -*- *************** -*-

# 如果程序需要有多个返回值，则既可将多个值包装成列表之后返回，也可直接返回多个值 。
# 如果 Python 函数直接返回多个值， Python 会自动将多个返回值封装成元组。

def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        # ＃如果元素 e 是数值
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count


my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]
# 获取 sum and avg 函数返回的多个值，多个返回值被封装成元组
tp = sum_and_avg(my_list)
print(tp)

# 使用序列解包来获取多个返回值
s, avg = sum_and_avg(my_list)
print(s)
print(avg)