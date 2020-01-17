#!/usr/bin/env python

# -*- *************** -*-
# @File  : multiple_inherit.py
# @Description : 关于多继承
# @Author: mql
# @Time  : 2020/1/17 21:34
# -*- *************** -*-


# 大部分面向对象的编程语言（除了 C＋＋）都只支持单继承，而不支持多继承，
# 这是由于多继承不仅增加了编程的复杂度，而且很容易导致一些莫名的错误。

# Python 虽然在语法上明确支持多继承，但通常推荐：
# 如果不是很有必要，则尽量不要使用多继承，
# 而是使用单继承，这样可以保证编程思路更清H忻，而且可以避免很多麻烦。

# 当一个子类有多个直接父类时一，该子类会继承得到所有父类的方法，
# 这一点在前面示例中己经做了示范。
# 现在的问题是 ：如果多个父类中包含了同名的方法，此时会发生什么呢？
# 此时排在前面的父类中的方法会“遮蔽”排在后面的父类中的同名方法。

class Item:
    def info(self):
        print("Item中的方法：", '这是一个商品')
class Product:
    def info(self):
        print("Product中的方法：", '这是一个工业产品')

class Mouse(Item, Product): # ①
    pass
m = Mouse()
m.info()

# 上面程序中 Item 和 Product 两个父类中都包含 了 info（）方法，当 Mouse 子类对象调用 info（）方
# 法时一一子类中没有定义 info（）方法，因此 Python 会从父类中寻找 info（）方法，此时优先使用第一
# 个父类 item 中的 info（）方法 。
# 运行上面程序，将看到如下输出结果。
#   Item 中方法 ： 这是一个商品
# 如果将上面粗体字代码改为如下形式。
#   class Mouse(Product, Item): # ①
# 此时 Product 父类的优先级高于 Item 父类，因此 Product 中的 info（）方法将会起作用 。
# 运行上面程序，将会看到如下输出结果 。
#   Product 中方法 ： 这是一个工业产品