#!/usr/bin/env python

# -*- *************** -*-
# @File  : print_shape.py
# @Description : 
# @Author: mql
# @Time  : 2020/4/21 17:39
# -*- *************** -*-


def print_blank_triangle(n):
    '''
    打印一个有星号组成的空心的三角形
    :param n: 三角形边长
    '''
    if n < 0:
        raise ValueError('n 必须大于0')
    for i in range(n):
        print(' ' * (n - i - 1), end= '')
        print('*', end='')
        if i != n-1:
            print(' ' * (2 * i - 1), end= '')
        else:
            print('*' * (2 * i - 1), end= '')
        if i != 0:
            print('*')
        else:
            print('')

if __name__ == '__main__':
    print_blank_triangle(9)