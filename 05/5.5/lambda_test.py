#!/usr/bin/env python

# -*- *************** -*-
# @File  : lambda_test.py
# @Description : 使用 lambda 表达式代替局部函数
# @Author: mql
# @Time  : 2020/1/14 14:34
# -*- *************** -*-


# 如果使用 lambda 表达式来简化 function_return_test.py，则可以将程序改写成如下形式。

def get_math_func(type):
    result = 1
    # 该函数返回的是lambda表达式
    if type == 'square':
        return lambda n: n * n
    elif type == "cube":
        return lambda n: n * n * n
    else:
        return lambda n: (1 + n) * n / 2  # 1+2+3+...+n的总和

# 调用 get_math_func （），程序返回一个嵌套函数
math_func = get_math_func("cube")  # 得到 cube 函数
print(math_func(5))  # 125
math_func = get_math_func("square")  # 得到 square 函数
print(math_func(5))  # 25
math_func = get_math_func("other")  # 得到 factorial 函数
print(math_func(5))  # 15.0

# 由于 lambda 表达式只 能是单行表达式，不允许使用更复杂的函数形式，因此上 ~
# 面①号粗体字代码处改为计算 1+2+3＋…切的总和。

# lambda 表达式的语法格式如下：
#   lambda [parameter_list ］ ： 表达式

# lambda 表达式的几个要点。
# 》 lambda 表达式必须使用 lambda 关键字定义 。
# 》在 lambda 关键字之后、冒号左边的是参数列表，可以没有参数，也可以有多个参数 。 如果
#   有多个参数， 则 需要用逗号隔开，冒号右边是该 lambda 表达式的返回值 。

# 实际上， lambda 表达式的本质就是匿名的、单行函数体的函数。因此， lambda 表达式可以写
# 成函数的形式。例如，对于如下 lambda 表达式。
# lambda x , y:x + y
# 可改写为如下函数形式 。
# def add(x, y): return x+ y
# 上面定义函数H才使用了简化语法：当函数体只有一行代码时，可以直接把函数体的代码放在与
# 函数头同一行。

# 总体来说，函数比 lambda 表达式的适应性更强， lambda 表达式只能创建简单的函数对象（它
# 只适合函数体为单行的情形）。但 lambda 表达式依然有如下两个用途 。
# 〉对于单行函数，使用 lambda 表达式可以省去定义函数的过程，让代码更加简洁。
# 》对于不需要多次复用的函数 ， 使用 lambda 表达式可以在用完之后立即释放，提高了性能 。