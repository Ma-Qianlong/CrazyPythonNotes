#!/usr/bin/env python

# -*- *************** -*-
# @File  : with_theory.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-29 16:57
# -*- *************** -*-


# 下面我们自定义一个实现上下文管理协议的类，并使用 with 语句来管理它。

class FkResource:
    def __init__(self, tag):
        self.tag = tag
        print('构造器，初始化资源：%s' % tag)
    # 定义__enter__方法，它是在with代码执行之前执行的方法
    def __enter__(self):
        print('[__enter__ %s]:' % self.tag)
        # 该返回值将作为 as 子句后变量的值
        return 'fkit' # 可以返回任意类型的值
    # 定义__exit__方法，它是在with代码执行之前执行的方法
    def __exit__(self, exc_type, exc_val, exc_traceback):
        print('[__exit__ %s]:' % self.tag)
        # exc_traceback 为 None 代表没有异常
        if exc_traceback is None:
            print('没有异常时关闭资源')
        else:
            print('遇到异常时关闭资源')
            return False # 可以省略，默认返回None也被看作时False

with FkResource('孙悟空') as dr:
    print(dr)
    print('[with代码块]没有异常')
print('---------------------------------')
with FkResource('白骨精') as dr:
    print('[with代码块]异常之前的代码')
    raise Exception
    print('[with代码块]~~~~~~~~~~~异常之后的代码')