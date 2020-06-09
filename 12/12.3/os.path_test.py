#!/usr/bin/env python

# -*- *************** -*-
# @File  : os.path_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-08 17:02
# -*- *************** -*-


from pathlib import *
import fnmatch

# 遍历当前目录下的所有的文件和目录
for file in Path('.').iterdir():
    # 访问所有以_test.py结尾的文件
    if fnmatch.fnmatch(file, '*_test.PY'):
        print(file)

names = ['a.py', 'b.py', 'c.py', 'd.py']
# 对 names 列表进行过滤
sub = fnmatch.filter(names, '[ac].py')
print(sub)  # ['a.py', 'c.py']

print(fnmatch.translate('?.py'))  # (?s:.\.py)\Z
print(fnmatch.translate('[ac].py'))  # (?s:[ac]\.py)\Z
print(fnmatch.translate('[a-c].py'))  # (?s:[a-c]\.py)\Z
