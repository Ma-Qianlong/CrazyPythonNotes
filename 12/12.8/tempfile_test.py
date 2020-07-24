#!/usr/bin/env python

# -*- *************** -*-
# @File  : tempfile_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-07-24 11:36
# -*- *************** -*-


import tempfile

# 创建临时文件
fp = tempfile.TemporaryFile()
print(fp.name)
fp.write('两情若是久长时，'.encode('utf-8'))
fp.write('又岂在朝朝暮暮。'.encode('utf-8'))
# 将文件指针移到开始处，准备读取文件
fp.seek(0)
print(fp.read().decode('utf-8'))  # 输出刚才写入的内容
# 关闭文件，该文件将会被自动删除
fp.close()

# 通过with语句创建临时文件，with会自动关闭临时文件
with tempfile.TemporaryFile() as fp:
    # 写入内容
    fp.write(b'I Love Python!')
    # 将文件指针移到开始处，准备读取文件
    fp.seek(0)
    # 读取文件内容
    print(fp.read())  # b'I Love Python!'

# 通过with语句创建临时目录
with tempfile.TemporaryDirectory() as tmpdirname:
    print('创建临时目录', tmpdirname)

# 上面程序 以两种方式来创建临时文件 。
# 》第一种方式是手动创建临时文件，读写临时文件后需要主Zj:}］关闭它，当程序关闭该临时文
# 件时，该文件会被自动删除 。
# 》第二种方式则是使用 with 语句创建临时文件，这样 with 语句会自动关闭临时文件。
# 上面程序最后还创建了临时目录 。 由于程序使用 with 语句来管理临时目录 ，因此程序也会自动删除该临时目录。
