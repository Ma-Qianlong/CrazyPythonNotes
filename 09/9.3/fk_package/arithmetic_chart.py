#!/usr/bin/env python

# -*- *************** -*-
# @File  : arithmetic_chart.py
# @Description : 
# @Author: mql
# @Time  : 2020/4/21 17:30
# -*- *************** -*-


def print_multiple_chart(n):
    '打印乘法口诀的函数'
    for i in range(n):
        for j in range(i + 1):
            print('%d * %d = %-2d' % ((j + 1), (i + 1), (j + 1) * (i + 1)), end='  ')
        print('')


def test_print_multiple_chart():
    print_multiple_chart(9)


__all__ = ['print_multiple_chart']

if __name__ == "__main__":
    test_print_multiple_chart()
