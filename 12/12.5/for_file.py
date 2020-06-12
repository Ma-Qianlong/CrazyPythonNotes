#!/usr/bin/env python

# -*- *************** -*-
# @File  : for_file.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-12 17:39
# -*- *************** -*-


# 实际上，文件对象本身就是可遍历的（就像一个序列一样），因此，程序完全可以使用 for 循
# 环来遍历文件内容。
# 使用 for 循环读取文件内容。

import codecs
# 指定使用utf-8字符集读取文件内容
f = codecs.open('read_test4.py', 'r', 'utf-8', buffering=True)
# 使用for循环遍历文件对象
for line in f:
    print(line, end='')
f.close()

# 如果有需要 ， 程序也可以使用 list（） 函数将文件转换成 list 列表，就像文件对象的 readlines（）方
# 法的返回值一样。例如如下代码（程序清单间上）。

# 将文件对象转换为list列表
print(list(codecs.open('for_file.py', 'r', 'utf-8',buffering=True)))