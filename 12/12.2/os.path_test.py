#!/usr/bin/env python

# -*- *************** -*-
# @File  : os.path_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-05 16:34
# -*- *************** -*-


import os
import time

# 获取绝对路径
print(os.path.abspath("about.txt"))

# 获取共同的前缀名
print(os.path.commonprefix(['/usr/lib', "/usr/local/lib"])) # /usr/l

# 获取共同的路径
print(os.path.commonpath(['/usr/lib', "/usr/local/lib"])) # \usr

# 获取目录
print(os.path.dirname("abc/xyz/README.txt"))

# 判读指定目录是否存在
print(os.path.exists("abc/xyz/README.txt"))

# 获取最近一次的访问时间
print(time.ctime(os.path.getatime('os.path_test.py')))

# 获取最后一次修改时间
print(time.ctime(os.path.getmtime('os.path_test.py')))

# 获取创建时间
print(time.ctime(os.path.getctime('os.path_test.py')))

# 获取文件大小
print(os.path.getsize('os.path_test.py'))

# 判断是否为文件
print(os.path.isfile('os.path_test.py'))

# 判断是否为目录
print(os.path.isdir('os.path_test.py'))

# 判断是否为同一个文件
print(os.path.samefile('os.path_test.py', './os.path_test.py'))