#!/usr/bin/env python

# -*- *************** -*-
# @File  : module1.py
# @Description : 
# @Author: mql
# @Time  : 2020/03/8 18:22
# -*- *************** -*-

'''
    这是我们编写的第一个模块，该模块包含以下内容
    my_book ： 字符串变量
    say_hi ： 简单的函数
    User ：代表用户的类
'''

print('this is module 1')
my_book = 'Crazy Python Notes'


def say_hi(user):
    print('%s, 您好， 欢迎学习 Python' % user)


class User:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('%s 正在慢慢地走路' % self.name)

    def __repr__(self):
        return "User[name=%s]" % self.name


# ***** 以下部分我测试代码 ***
def test_my_book():
    print(my_book)


def test_say_hi():
    say_hi('孙悟空')
    say_hi(User('Carlie'))


def test_User():
    u = User('白骨精')
    u.walk()
    print(u)


# 对于实际开发的项目，对每个函数、类可能都需要使用更多的测试用例进行测试，
# 这样才能达到各种覆盖效果 （比如语句 覆盖、条件覆盖等 ）。

# 如果只是简单地调用上面的测试程序，则会导致一个问题 ： 当其他程序每次导入该模块时，这
# 三个测试函数都会自动运行 ，这显然不是我们期望看到的结果 。 此时希望实现的效果是：如果直接
# 使用 python 命令运行该模块（相当于测试），程序应该执行该模块的测试函数：如果是其他程序导
# 入该模块，程序不应该执行该模块的测试函数。

# 此时可借助于所有模块内置的__name__变量进行区分，如果直接使用 python 命令来运行一个
# 模块， __name__ 变量的值为 __mian__ ；如果该模块被导入其他程序中，__name__ 变量的值就是模
# 块名。因此，如果希望测试函数只有在使用 python 命令直接运行时才执行，则可在调用测试函数
# 时增加判断：只有当__name__属性为 __mian__ 时才调用测试函数。为模块增加如下代码即可

# 当__name__为“__mian__”(直接使用Python运行改模块)时执行如下代码
if __name__ == '__main__':
    test_my_book()
    test_say_hi()
    test_User()
