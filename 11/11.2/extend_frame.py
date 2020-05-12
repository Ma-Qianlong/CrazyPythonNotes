#!/usr/bin/env python

# -*- *************** -*-
# @File  : extend_frame.py
# @Description : 
# @Author: mql
# @Time  : 2020/03/22 20:28
# -*- *************** -*-


# 此外，还有一种方式是不直接使用 Tk，只要创建 Frame 的子类，它的子类就会自动创建 Tk 对象作为窗口。

# Python 2.x 使用这行
# from Tkinter import *
# Python 3.x 使用这行
from tkinter import *


# 定义继承Frame 的 Application 类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # 调用 initWidgets()方法初始化界面
        self.initWidgets()

    def initWidgets(self):
        # 创建Label对象，（用于显亦不可编辑的文本或图标）， 第一个参数指定将Label放入root内
        w = Label(self)
        # 创建一个位图
        bm = PhotoImage(file='serial.png')
        # 必须用一个不会被释放的变量引用该图片，否则该图片会被回收
        w.x = bm
        # 设置显示的图片是bm
        w['image'] = bm
        w.pack()
        # 创建Button对象， 第一个参数指定将该 Button 放入 root 内
        okButton = Button(self, text="确定")
        okButton['background'] = 'yellow'
        # okButton.configure(background='yellow') # 与上一行作用一样
        # okButton.configure(image=bm)
        okButton.pack()


# 创建Application对象
app = Application()
# Frame 有一个默认的 master 属性，该属性值是 Tk 对象（窗口）
print(type(app.master))
# 通过master属性来设置窗口标题
app.master.title('窗口标题')
# 启动主窗口消息循环
app.mainloop()
