#!/usr/bin/env python

# -*- *************** -*-
# @File  : exercise.py
# @Description : 绕圈圈
# @Author: mql
# @Time  : 2020/1/9 22:34
# -*- *************** -*-

# 以输入5为例，输入如下
# 01 16 15 14 13
# 02 17 24 23 12
# 03 18 25 22 11
# 04 19 20 21 10
# 05 06 07 08 09


SIZE = int(input("请输入一个整数："))

array = [[0] * SIZE]
# 创建一个长度为SIZE*SIZE的二维数组
for i in range(SIZE - 1):
    array += [[0] * SIZE]

# orient 代表绕圈的方向
# down-向下， right-向右，left-向左，up-相上
orient = 'down'
# 控制将1~SIZE*SIZE-1的数值填入二维数组中
# 其中 j 控制行索引， k 控制列缩影
j = 0
k = 0
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i
    # ①号转弯线（j+k = SIZE - 1 ）
    if j + k == SIZE - 1:
        # j>k,在左下角
        if j > k:
            orient = 'right'
        # 在右上角
        else:
            orient = 'left'
    # ②号转弯线
    elif j == k and k >= SIZE / 2:
        orient = 'up'
    # ③号转弯线
    elif j == k - 1 and k <= SIZE / 2:
        orient = 'down'

    # 据方向来控制行、列索引的改变
    if orient == 'down':
        j += 1
    elif orient == 'right':
        k += 1
    elif orient == 'left':
        k -= 1
    elif orient == 'up':
        j -= 1

# 遍历输出二维数组
for i in range(SIZE):
    for j in range(SIZE):
        print('%02d ' % array[i][j], end="")
    print()
