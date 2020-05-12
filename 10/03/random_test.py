#!/usr/bin/env python

# -*- *************** -*-
# @File  : random_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/5/12 17:48
# -*- *************** -*-


import random
# 生成范围为 0.0 ≤x< 1.0 的伪随机浮点数
print(random.random())
# 生成范围为 2.5 ≤x< 10.0 的伪随机浮点数
print(random.uniform(2.5, 10.0))
print('%.2f' % random.uniform(2.5, 10.0))

randomStr = '%.2f' % random.uniform(2.5, 10.0);
randomF = float(randomStr)