#!/usr/bin/env python

# -*- *************** -*-
# @File  : varargs.py
# @Description : 参数收集（个数可变的参数）
# @Author: mql
# @Time  : 2020/1/13 21:12
# -*- *************** -*-


#  Python 允许在形参前面添加一个星号(*)，这样就意味着该参数可接收多个参数
# 值，多个参数值被当成元组传入
print("test1")
# test1
# 定义了支持参数收集的函数
def test(a, *books):
    print(books)
    # books 被当成元组处理
    for b in books:
        print(b)
    # 输出变量a
    print(a)


# 调用test()函数
test(5, "疯狂 iOS 讲义", "疯狂 Android 讲义")
# 从上面的运行结果可 以看出，当调用 test（）函数时， books 参数可以传入多个字符串作为参数值 。
# 从 test（）的函数体代码来看，参数收集的本质就是一个元组 ： Python 会将传给 books 参数的多个值
# 收集成一个元组 。

print("\ntest2")
# test2
# Python 允许个数可变的形参可以处于形参列表的任意位置（不要求是形参列表的最后一个参数〉，
# 但 Python 要求一个函数最多只能带一个支持“普通”参数收集的形参。例如如下程序。
# 定义了支持参数收集的函数
def test2(*books, num):
    print(books)
    # books 被当成元组处理
    for b in books:
        print(b)
    # 输出变量num
    print(num)


# 调用test()函数
test2("疯狂 iOS 讲义", "疯狂 Android 讲义", num=5)
# 如从上面程序中所看到的， test（）函数的第一个参数就是个数可变的形参，
# 由于该参数可接收个数不等的参数值，因此如果需要给后面的参数传入参数值，
# 则必须使用关键字参数 ；
# 否则 ，程序会把所传入的多个值都当成是传给 books 参数的 。

print("\ntest3")
# test3
# Python 还可以收集关键宇参数，此时 Python 会将这种关键宇参数收集成字典。为了让 Python
# 能收集关键宇参数，需要在参数前面添加两个星号（**）。在这种情况下，一个函数可同时包含一个支持
# “普通”参数收集的参数和一个支持关键字参数收集的参数
def test3(x, y, z=3, *books, **scores):
    print(x, y, z)
    print(books)
    print(scores)


test3(1, 2, 3, "疯狂 iOS 讲义", "疯狂 Android 讲义", 语文=89, 数学=94)
# 上面程序在调用 test（）函数时 ，前面的 l 、 2 、 3 将会传给普通参数 x 、 y 、 z ；
# 接下来的两个字符串将会由 books 参数收集成元组；最后的两个关键字参数将会被收集成字典

# 对于以上面方式定义的 test（）函数 ， 参数 z 的默认值几乎不能发挥作用 。
# 比如按如下方式调用test（） 函数 。
test3(1, 2,  "疯狂 iOS 讲义", "疯狂 Android 讲义", 语文=89, 数学=94)
# 上面代码在调用 t巳st（）函数时，前面的 l 、 2 、"疯狂 iOS 讲义"将会传给普通参数x,y,z;
# 接下来的一个字符串将会由 books 参数收集成元组 ； 最后的两个关键宇参数将会被收集成宇典。

# 如果希望让 z 参数的默认值发挥作用， 则 需要只传入两个位置参数。例如如下调用代码 。
test3(1, 2,  语文=89, 数学=94)
# 上面代码在调用 test（）函数时，前面的 l 、 2 将会传给普通参数 x、 y，此时 z 参数将使用默认的
# 参数值 3, books 参数将是一个空元组 ； 接下来的两个关键字参数将会被收集成字典。