#!/usr/bin/env python

# -*- *************** -*-
# @File  : encapsule.py
# @Description : 隐藏和封装
# @Author: mql
# @Time  : 2020/1/17 14:53
# -*- *************** -*-


# 如下程序示范了 Python 的封装机制。

class User:
    def __hide(self):
        print('示范隐藏的hide方法')

    def getname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3~8之间')
        self.__name = name

    name = property(getname, setname)

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户年龄必须在18~20之间')
        self.__age = age

    def getage(self):
        return self.__age

    age = property(getage, setage)


#
u = User()
# 对name属性赋值， 实际上是调用setname()方法
# u.name = 'fk'  # 引发 ValueError 错误：用户名长度必须在 3-8 之间

# 上面程序将 User 的两个实例变量分别命名为＿name 和＿age ， 这两个实例变量就会被隐藏起
# 来 ，这样程序就无法直接访 问＿name、＿age 变量 ，只能通过 setname（）、 getname（）、 setage（）、 getage()。
# 这些访问器方法进行访问，而 setnam巳（） 、 setage（）会对用户设置的 name 、 age 进行控制，只有符合
# 条件的 name 、 age 才允许设置。

u.name = 'fkit'
u.age = 25
print(u.name)
print(u.age)

# 从该程序可以看出封装的好处，程序可以将 User 对象的实现细节隐藏起来，程序只能通过暴
# 露出来的 setnam巳（）、 setage（）方法来改变 User 对象的状态，而这两个方法可以添加自己的逻辑控制，
# 这种控制对 User 的修改始终是安全 的 。

# 上面程序还定义了一个 hide（）方法，这个方法默认是隐藏的。如果程序尝试执行如下代码：
# 尝试调用隐藏的 hide （）方法
# u.__hide()
# 将会提示如下错误。
# AttributeError: 'User' object has no attribute '__hide'

# 最后需要说明的是， Python 其实没有真正的隐藏机制 ，双下画线只是 Python 的一个小技巧 ：
# Python 会 “偷偷”地 改变 以双下画线开头的方法名，会在这些方法名前添加单下画线和类名 。 因
# 此上面的一hide（）方法其实可以按如下方式调用（通常并不推荐这么干）。
# 调用隐藏的 hide （）方法
u._User__hide()  # 示范隐藏的hide方法

# 通过上面调用可以看出 ， Python 并没有实现真正的隐藏。
# 类似的是 ， 程序也可通过为隐藏的实例变量添加下画线和类名的方式来访问或修改对象的实例
# 变量。通过这种方式可“绕开” setname（）方法的检查逻辑 ， 直接对 User 对象的 name 属性赋值 。
# 例如如下代码。

# 对隐藏的 name 属性赋值
u._User__name = 'fk'
# 访问 User 对象的 name 属性（实际上访问的是一name 实例变量）
print(u.name)

