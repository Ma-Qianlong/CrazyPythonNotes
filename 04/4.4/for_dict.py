#!/usr/bin/env python

# -*- *************** -*-
# @File  : for_dict.py
# @Description :  for-in 遍历字典表
# @Author: mql
# @Time  : 2019/12/26 17:12
# -*- *************** -*-


my_dict = {'语文': 89, '数学': 92, '英语': 80}
# 通过items()方法遍历所有的key-value对
# 由于items()方法返回的列表元素是key-value对，因此要声明两个变量
for key, value in my_dict.items():
    print('key: %s, value: %d' % (key, value))
print('----------------')
# 通过keys方法遍历所有的key
for key in my_dict.keys():
    print('key:', key)
    # 再通过key获取value
print('----------------')
# 通过values()方法遍历所有的value
for value in my_dict.values():
    print('value:', value)

print(end="\n----统计列表中各元素出现的次数----\n")
src_list = [12, 45, 3.4, 12, 'fkit', 45, 3.4, 12, 'fkit', 45, 3.4, 12, 12]
print("列表：", src_list)
statistics = {}
for ele in src_list:
    if ele in statistics:
        statistics[ele] += 1
    else:
        statistics[ele] = 1
# 遍历dict,打印各元素出现的次数
for ele, count in statistics.items():
    print("%5s 出现的次数为：%d" % (ele, count))
