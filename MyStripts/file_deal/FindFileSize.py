#!/usr/bin/env python

# -*- *************** -*-
# @File  : FindFileSize.py
# @Description : 
# @Author: mql
# @Time  : 2021/1/19 16:45
# -*- *************** -*-


import os

filename = "name-size(byte).txt"

if __name__ == '__main__':
    print("开始执行...")
    file_path = "./"
    all_files = []
    files_size = []

    # 读取当前路径下所有文件
    # for root, dirs, files in os.walk(file_path):
    #     if root == file_path:  # 仅取当前目录下的
    #         all_files += files
    # print("now files: ", all_files)

    print("all files:")
    for files in os.listdir(file_path):
        if os.path.isfile(files):
            print(files)
            all_files.append(files)

    # 获取所有文件大小(byte)
    for file_name in all_files:
        ss = os.path.getsize(file_name)
        sstr = (file_name + '@' + str(ss))
        files_size.append(sstr)

    print("files @ size: ", files_size)

    # 将信息写入文件
    with open(filename, 'w') as file_object:
        for one in files_size:
            file_object.write(one + '\n')

    print("执行结束。")
