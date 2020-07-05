#!/usr/bin/env python

# -*- *************** -*-
# @File  : guiTest.py
# @Description : 
# @Author: mql
# @Time  : 2020-07-03 20:19
# -*- *************** -*-

import tkinter.messagebox as msgbox
from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建容器
        fm1 = Frame(self.master)
        # 改容器放上面排列
        fm1.pack(side=TOP, fill=BOTH, expand=YES)
        # label 文本
        Label(fm1, text="HOST：", font=18, width=10, anchor=NE, padx=5, pady=15).pack(side=LEFT)
        # 输入框
        self.e_host = Entry(fm1, width=50)
        self.e_host.pack(side=LEFT, fill=X, expand=YES)
        self.e_host.insert(0,"192.168.5.249")

        # port
        fm_port = Frame(self.master)
        fm_port.pack(side=TOP, fill=BOTH, expand=YES)
        Label(fm_port, text="PORT：", font=18, width=10, anchor=NE, padx=5, pady=15).pack(side=LEFT)
        self.e_port = Entry(fm_port, width=50)
        self.e_port.pack(side=LEFT, fill=X, expand=YES)

        # user
        fm_user = Frame(self.master)
        fm_user.pack(side=TOP, fill=BOTH, expand=YES)
        Label(fm_user, text="USER：", font=18, width=10, anchor=NE, padx=5, pady=15).pack(side=LEFT)
        self.e_port = Entry(fm_user, width=50)
        self.e_port.pack(side=LEFT, fill=X, expand=YES)

        # pwd
        fm_pwd = Frame(self.master)
        fm_pwd.pack(side=TOP, fill=BOTH, expand=YES)
        Label(fm_pwd, text="PASSWORD：", font=18, width=10, anchor=NE, padx=5, pady=15).pack(side=LEFT)
        self.e_port = Entry(fm_pwd, width=50)
        self.e_port.pack(side=LEFT, fill=X, expand=YES)

        # db
        fm_db = Frame(self.master)
        fm_db.pack(side=TOP, fill=BOTH, expand=YES)
        Label(fm_db, text="DATABASE：", font=18, width=10, anchor=NE, padx=5, pady=15).pack(side=LEFT)
        self.e_port = Entry(fm_db, width=50)
        self.e_port.pack(side=LEFT, fill=X, expand=YES)

        # bn
        fm_bn = Frame(self.master)
        fm_bn.pack(side=TOP, fill=BOTH, expand=YES)
        bn = Button(fm_bn, text='开始转换', command=self.change)
        bn.pack()

    # 定义事件处理方法
    def change(self):
        print("点击了转换按钮")
        print(self.e_host.get())
        if(msgbox.askokcancel(title="warning", message='确认要开始转换吗？')):
            pass
        else:
            print('用户点击了取消')

    def hit(self):
        # box系列
        # tk.messagebox.showinfo(title='hi',message='so this is a msgbox')
        # tk.messagebox.showwarning(title='warning', message='so this is a warningbox')
        # tk.messagebox.showerror(title='hi', message='No! the program is about to crash!')

        # ask系列
        # tk.messagebox.askquestion(title='hi', message='Are you sure to cancel it?') #返回'yes'或'no'
        # tk.messagebox.askyesno(title='hi', message='Are you sure to cancel it?')  #返回True或者False
        # tk.messagebox.askquestion(title='hi', message='Are you sure to cancel it?')  #
        self.master.messagebox.askquestion(title='hi', message='Are you sure to cancel it?')  #


root = Tk()
root.title("图标库多条件配置升级转换器")
display = App(root)
root.mainloop()