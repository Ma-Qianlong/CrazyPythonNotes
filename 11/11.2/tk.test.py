#!/usr/bin/env python

# -*- *************** -*-
# @File  : tk.test.py
# @Description : 
# @Author: mql
# @Time  : 2020/4/22 20:12
# -*- *************** -*-

# Python 2.x 使用这行
# from Tkinter import *
# Python 3.x 使用这行
from tkinter import *

# 创建Tk对象，Tk代表窗口
root = Tk()
# 设置窗口标题
root.title('窗口标题')
# 创建Label对象，（用于显亦不可编辑的文本或图标）， 第一个参数指定将Label放入root内
w = Label(root, text="Hello Tkinter!")
# 调用pack进行布局
w.pack()
# 启动主窗口
root.mainloop()

# 上面程序主要创建了两个对象： Tk 和 Label。其中 Tk 代表顶级窗口， Label 代表一个简单的文
# 本标签，因此需要指定将该 Label 放在哪个容器内。上面程序在创建 Label 时第一个参数指定了 root,
# 表明该 Label 要放入 root 窗口内 。
