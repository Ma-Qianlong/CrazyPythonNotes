#!/usr/bin/env python

# -*- *************** -*-
# @File  : for_tuple_list.py
# @Description : 使用for-in遍历列表和元组
# @Author: mql
# @Time  : 2019/12/26 16:52
# -*- *************** -*-

# for-in 遍历 元组
a_tuple = ('fkit', 'crazyit', 'Charlie')
for ele in a_tuple:
    print('当前元素是：', ele)

print(end='\n')
# for-in 遍历 列表
# isinstance（）用于判断某个变量是否指定数据类型的实例
src_list = [12, 45, 3.4, 13, 'a', 4, 56, 'crazyit', 109.5]
my_sum = 0
my_count = 0
for ele in src_list:
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)
        my_sum += ele
        my_count += 1;
print('总和:', my_sum)
print('平均数:', my_sum / my_count)

print(end='\n')
# 可以通过循环计数器来访问列表元素
a_list = [330, 1.4, 50, 'fkit', -3.5]
# 遍历0到len(a_list)的范围
for i in range(0, len(a_list)):
    # 据索引访问列表元素
    print("第%02d个元素是: %s" % (i, a_list[i]))
