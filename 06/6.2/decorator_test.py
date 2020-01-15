#!/usr/bin/env python

# -*- *************** -*-
# @File  : decorator_test.py
# @Description : ＠函数装饰器
# @Author: mql
# @Time  : 2020/1/15 15:45
# -*- *************** -*-

# 前面介绍的＠staticmethod 和＠classmethod 的本质就是函数装饰器，
# 其中 staticmethod 和 classmethod 都是 Python 内置的函数 。
# 使用＠符号引用己有的函数（比如＠staticmethod、＠c lassmethod ）后，可用于修饰其他函数，
# 装饰被修饰的函数 。
# 那么我们是否可以开发自定义的函数装饰器呢？答案是肯定的 。
# 当程序使用“＠函数’＇ （比如函数 A ）装饰另 一个函数（比如函数 B ）时 ， 实际上完成如下两步。
# ① 将被修饰的函数（函数B）作为参数传给＠符号引用的函数（函数A）。
# ② 将函数B 替换（装饰）成第①步的返回值。

# 从上面介绍不难看出，被“＠函数”修饰的函数不再是原来的函数，而是被替换成一个新的东西。

def funA(fn):
    print('a')
    fn()  # 执行传入的fn参数
    return 'fkit'


'''
下面的装饰效果相当于 funA(funB)
funB 将会被替换（装饰）成该语句的返回值
由于 funA 函数返回 fkit ，因此 funB 就是 fkit
'''


@funA
def funB():
    print('B')


print(type(funB))
print(funB)  # fkit

print()

# 被修饰的函数总是被替换成＠符号所引用的函数的返回值，
# 因此被修饰的函数会变成什么，完全由于＠符号所引用的函数的返回值决定
# ——如果＠符号所引用的函数的返回值是函数，那么被修饰的函数在替换之后还是函数。

# 下面程序示范了更复杂的函数装饰器。
def foo(fn):
    def bar(*args):
        print('===1===', args)
        n = args[0]
        print('===2===', n * (n - 1))
        # 查看传给foo函数的fn函数
        print(fn.__name__)
        fn(n * (n - 1))
        print("*" * 15)
        return fn(n * (n - 1))

    return bar


'''
下面的装饰效果相当于 foo(my_test)
my test 将会被替换（装饰〉成该语句的返回值
由于 foo （）函数返回 bar 函数，因此 funB 就是 bar
'''
@foo
def my_test(a):
    print("==my_test 函数==", a)


# 打印 my_test 函数，：｜每看到实际上是 bar 函数
print(my_test)
# 下面代码看上去是调用 my_test （），其实是调用 bar （）函数
my_test(10)
my_test(6, 5)

print()
# 通过＠符号来修饰函数是 Python 的一个非常实用的功能，它既可以在被修饰函数的前面添加
# 一些额外的处理逻辑（比如权限检查），也可以在被修饰函数的后面添加－些额外的处理逻辑（ 比
# 如记录日志〉，还可以在目标方法抛出异常时进行一些修复操作……这种改变不需要修改被修饰函
# 数的代码，只要增加一个修饰即可。

# 上面介绍的这种在被修饰函数之前、之后、抛出异常后制啊处理逻辑的方式，
# 就是其他编程语言中的 AOP (Aspect Orient Programming，面向切面编程）。

# 下面例子示范了如何通过函数装饰器为函数添加权限检查的功能。

def auth(fn) :
    def auth_fn(*args):
        # 用一条语句模拟执行权限检查
        print("------模拟执行权限检查------")
        # 回调被修饰的目标函数
        fn(*args)
    return auth_fn

@auth
def test(a, b):
    print("执行test函数, 参数a:%s, 参数b:%s " % (a, b))

# 调用 test （）函数，其实是调用修饰后返回的 auth_fn 函数
test(20, 15)
