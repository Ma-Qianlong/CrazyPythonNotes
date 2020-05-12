#!/usr/bin/env python

# -*- *************** -*-
# @File  : module1_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/03/8 22:28
# -*- *************** -*-


# 两次导入 module1 ，并指定其别名为md
import module1 as md
import module1 as md

print(md.__doc__)
print(md.my_book)
md.say_hi('mmm')
print(md.User)
user = md.User('孙悟空')
print(user)
user.walk()

# 这里为什么要两次导入 module1 模块呢？其实完全没必要，此处两次导入只是为了说明一点 ：
# Python 很智能。
# 虽然上面程序两次导入了 module1 模块，但最后运行程序，我们看到输出语句只输出一条“这
# 是 module1飞这说明第二次导入的 module ！ 模块并没有起作用，这就是 Python 的“智能”之处。
# 当程序重复导入同一个模块时 ， Python 只会导入一次。
