#!/usr/bin/env python

# -*- *************** -*-
# @File  : print_shape.py
# @Description : 
# @Author: mql
# @Time  : 2020/4/8 22:51
# -*- *************** -*-


# 编写一个 Python 模块文件，并将该文件复制在 lib\site-packages 路径下。

'''
简单的模块， 该模块包含以下内容
my_list: 保存列表的变量
print_triangle: 打印由星号组成的三角形的函数
'''
my_list = ['Python', 'Kotlin', 'Swift']


def print_triangle(n):
    '''打印由星号组成的三角形'''
    if n <= 0:
        raise ValueError('n 必须大于 0 ')
    for i in range(n):
        print(" " * (n - i - 1), end='')
        print('*' * (2 * i - 1), end='')
        print('')


# ====以下是测试代码====
def test_print_triangle():
    print_triangle(3)
    print_triangle(5)
    print_triangle(7)
    print_triangle(10)


if __name__ == '__main__': test_print_triangle()


# ，把该模块文件拷贝到 lib\site”packages 路径下，
# 就相当于为 Python 扩展了一个 print_shape 模块，这样任何 Python 程序都可使用该模块 。
