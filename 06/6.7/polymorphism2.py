#!/usr/bin/env python

# -*- *************** -*-
# @File  : polymorphism2.py
# @Description : 多态2
# @Author: mql
# @Time  : 2020/1/21 18:23
# -*- *************** -*-

# 多态是一种非常灵活的编程机制。
# 假如我们要定义一个 Canvas （画布 〉类，
# 这个画布类定义一个 draw_pic（）方法，该方法负责绘制各种图形 。
# 该 Canvas 类的代码如下 。

class Canvas:
    def draw_pic(self, shape):
        print('--开始绘图--')
        shape.draw(self)

# 从上面代码可以看出，Canvas 的 draw_pic（）方法需要传入一个 shape 参数，
# 该方法就是调用 shape参数的 draw（）方法将 自己绘制到画布上。

# Canvas 的 draw_pic（）传入的参数对象只要带一个 draw（）方法就行，
# 至于该方法具有何种行为 （到底执行怎样的绘制行为），
# 这与 draw_pic（）方法是完全分离的， 这就为编程增加了很大的灵活性。

# 下面程序定义了三个图形类，并为它们都提供了 draw（）方法，
# 这样它们就能以不同的行为绘制在画布上————这就是多态的实际应用。

class Rectangle:
    def draw(self, canvas):
        print('在%s上绘制矩形' % canvas)
class Triangle:
    def draw(self, canvas):
        print('在%s上绘制三角形' % canvas)
class Circle:
    def draw(self, canvas):
        print('在%s上绘制圆形' % canvas)

c = Canvas()
# 传入Rectangle参数，绘制矩形
c.draw_pic(Rectangle())
# 传入Triangle参数，绘制三角形
c.draw_pic(Triangle())
# 传入Circle参数，绘制圆形
c.draw_pic(Circle())

# 从上面这个例子可以体会到 Python 多态的优势。当程序涉及 Canvas 类的 draw_pic（）方法时，
# 该方法所需的参数是非常灵活的，程序为该方法传入的参数对象只要具有指定方法就行，至于该方
# 法呈现怎样的行为特征，则完全取决于对象本身，这大大提高了 draw_pic（）方法的灵活性。
