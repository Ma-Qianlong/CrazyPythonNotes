#!/usr/bin/env python

# -*- *************** -*-
# @File  : DirListInfo.py
# @Description : 
# @Author: mql
# @Time  : 2021/1/19 16:28
# -*- *************** -*-


import os


# 对于os.walk会遍历指定目录下的所有子文件夹和子文件夹中的所有文件
def file_name_walk(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print('root', root)  # 当前目录路径
        print('dirs', dirs)  # 当前目录下的所有子目录
        print('files', files)  # 当前路径下所有非空目录子文件


# 返回指定路径下所有的文件和文件夹列表,但是子目录下文件不遍历。
def file_name_listdir(file_dir):
    for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
        print("files", files)


# 通过os.path.splitext指定文件类型
# 选取特定文件类型
# 选取文件名中所有txt后缀名的文本文件
def file_name(file_dir):
    File_Name = []
    for files in os.listdir(file_dir):
        if os.path.splitext(files)[1] == '.txt':
            File_Name.append(files)
    return File_Name


if __name__ == '__main__':
    file_name_walk("./")
    print("------------")
    file_name_listdir("./")
    print("------------")
    txt_file_name = file_name(".")
    print("txt_file_name", txt_file_name)

    filename = "test_text.txt"
    with open(filename, 'w') as file_object:
        file_object.write("Add a word\n")
        file_object.write("Add two words\n")
