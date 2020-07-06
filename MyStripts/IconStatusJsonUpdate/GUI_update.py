#!/usr/bin/env python

# -*- *************** -*-
# @File  : GUI_update.py
# @Description : 
# @Author: mql
# @Time  : 2020-07-03 20:19
# -*- *************** -*-

import tkinter.messagebox as msgbox
from tkinter import *
from SightIconStatusJsonUpdate import *
from mycolorlog import logger

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
        self.e_host.insert(0, "127.0.0.1")

        # port
        fm_port = Frame(self.master)
        fm_port.pack(side=TOP, fill=BOTH, expand=YES)
        Label(fm_port, text="PORT：", font=18, width=10, anchor=NE, padx=5, pady=15).pack(side=LEFT)
        self.e_port = Entry(fm_port, width=50)
        self.e_port.pack(side=LEFT, fill=X, expand=YES)
        self.e_port.insert(0, 3136)

        # user
        fm_user = Frame(self.master)
        fm_user.pack(side=TOP, fill=BOTH, expand=YES)
        Label(fm_user, text="USER：", font=18, width=10, anchor=NE, padx=5, pady=15).pack(side=LEFT)
        self.e_user = Entry(fm_user, width=50)
        self.e_user.pack(side=LEFT, fill=X, expand=YES)
        self.e_user.insert(0, 'root')

        # pwd
        fm_pwd = Frame(self.master)
        fm_pwd.pack(side=TOP, fill=BOTH, expand=YES)
        Label(fm_pwd, text="PASSWORD：", font=18, width=10, anchor=NE, padx=5, pady=15).pack(side=LEFT)
        self.e_pwd = Entry(fm_pwd, width=50)
        self.e_pwd.pack(side=LEFT, fill=X, expand=YES)
        self.e_pwd.insert(0, 'root')

        # db
        fm_db = Frame(self.master)
        fm_db.pack(side=TOP, fill=BOTH, expand=YES)
        Label(fm_db, text="DATABASE：", font=18, width=10, anchor=NE, padx=5, pady=15).pack(side=LEFT)
        self.e_db = Entry(fm_db, width=50)
        self.e_db.pack(side=LEFT, fill=X, expand=YES)
        self.e_db.insert(0, 'db-deepctrls-wxcs-dev')

        # bn
        fm_bn = Frame(self.master)
        fm_bn.pack(side=TOP, fill=BOTH, expand=YES)
        bn = Button(fm_bn, text='开始转换', command=self.change)
        bn.pack()

    # 定义事件处理方法
    def change(self):
        logger.info("点击了转换按钮")
        host = self.e_host.get()
        port = self.e_port.get()
        u = self.e_user.get()
        p = self.e_pwd.get()
        db = self.e_db.get()
        logger.info("host:%s, prot:%s, user:%s, pwd:%s, database:%s" %(host, port, u, p, db))
        if (msgbox.askokcancel(title="warning", message='确认要开始转换吗？')):
            try:
                ss = time.time()
                logger.info("###sssss### backend update iconJson ")
                doUpdate(host, int(port), u, p, db)
                ss1 = time.time()
                logger.info("###eeeee### backend update iconJson 耗时: %s \n" % (ss1 - ss))

                logger.info("###sssss### sight update iconJson ")
                doUpdate(host, int(port), u, p, db, True)
                ss2 = time.time()
                logger.info("###eeeee### sight update iconJson 耗时: %s \n" % (ss2 - ss1))

                logger.info("执行耗时（s）:%f" % (ss2 - ss))
                msgbox.showinfo("SUCCESS", '执行成功，耗时（s）:%f' % (ss2 - ss))
                logger.info("当前进程使用CPU时间(ms): %f" % (time.process_time_ns() / 1000000))
            except Exception as e:
                msgbox.showerror("ERROR", '执行失败，请检查数据库信息及网络连接等是否正确')
        else:
            logger.info('用户点击了取消')

    # def hit(self):
    #     # box系列
    #     # tk.messagebox.showinfo(title='hi',message='so this is a msgbox')
    #     # tk.messagebox.showwarning(title='warning', message='so this is a warningbox')
    #     # tk.messagebox.showerror(title='hi', message='No! the program is about to crash!')
    #
    #     # ask系列
    #     # tk.messagebox.askquestion(title='hi', message='Are you sure to cancel it?') #返回'yes'或'no'
    #     # tk.messagebox.askyesno(title='hi', message='Are you sure to cancel it?')  #返回True或者False
    #     # tk.messagebox.askquestion(title='hi', message='Are you sure to cancel it?')  #
    #     self.master.messagebox.askquestion(title='hi', message='Are you sure to cancel it?')  #

if __name__ == '__main__':
    root = Tk()
    root.title("图标库多条件配置升级转换器")
    sw = root.winfo_screenwidth()  # 得到屏幕宽度
    sh = root.winfo_screenheight()  # 得到屏幕高度
    root.geometry('+%d+%d' % (sw / 2 - 230, sh / 2 - 230))
    display = App(root)
    root.mainloop()
