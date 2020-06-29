#!/usr/bin/env python

# -*- *************** -*-
# @File  : writebytes_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-29 17:51
# -*- *************** -*-


# 如果需要使用指定的字符集来输出文件，
# 则可以来用二进制形式————程序先将所输出的字符串转换成指定字符集对应的二进制数据（字节串），然后输出 二进制数据。
import os
f = open('y.txt', 'wb+')
f.write(('我爱Python'+os.linesep).encode('utf-8'))
f.writelines((('土门壁甚坚，' + os.linesep).encode('utf-8'),
              ('杏园度亦难。' + os.linesep).encode('utf-8'),
              ('势异邺城下，' + os.linesep).encode('utf-8'),
              ('纵死时犹宽。' + os.linesep).encode('utf-8')))

# 上面程序中的粗体字代码以 wb＋模式打开文件，这意味着程序会以二进制形式来输出文件，
# 此时程序输出的必须是宇节串，不能是字符串。 因此，程序调用 encode（）方法将字符串转换成字节串，
# 转换时指定使用 UTF名 字符集，这意味着程序将会以 UTF-8 字符集来保存文件。