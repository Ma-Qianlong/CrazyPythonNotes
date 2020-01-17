#!/usr/bin/env python

# -*- *************** -*-
# @File  : inherit.py
# @Description : 继承的语法
# @Author: mql
# @Time  : 2020/1/17 21:22
# -*- *************** -*-


# Python 子类继承父类的语法是在定义子类时，将多个父类放在子类之后的圆括号里。
# 语法格式如下：
# class Subclass (SuperClassl , SuperClass2 , .. . )
#   ＃类定义部分
# 从上面的语法格式来看，定义子类的语法非常简单，只需在原来的类定义后增加圆括号，
# 并在圆括号中添加多个父类，即可表明该子类继承了这些父类。

# 从子类的角度来看，子类扩展（ extend ）了父类 ：
# 但从父类的角度来看 ， 父类派生（ derive)出子类。
# 也就是说，扩展和派生所描述的是同一个动作，只是观察角度不同而己。
# 下面程序示范了子类继承父类的特点 。 下面是 Fruit 类的代码。

class Fruit:
    def info(self):
        print("我是一个水果！ 重%g克" % self.weight)

class Food:
    def taste(self):
        print("不同的食物的口感不同")

# 定义Apple类，继承了Fruit类和Food类
class Apple(Fruit, Food):
    pass

# 创建Apple对象
a = Apple()
a.weight = 5.6
# 调用Apple对象的info方法
a.info()
# 调用Apple对象的taste方法
a.taste()
