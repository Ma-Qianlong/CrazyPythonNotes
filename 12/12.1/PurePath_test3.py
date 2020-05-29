#!/usr/bin/env python

# -*- *************** -*-
# @File  : PurePath_test3.py
# @Description : 
# @Author: mql
# @Time  : 2020-05-25 11:37
# -*- *************** -*-


from pathlib import *

# 访问 drive 属性
print(PureWindowsPath('c:/Program Files/').drive)  # c:
print(PureWindowsPath('/Program Files/').drive)  # ''
print(PurePosixPath('/etc').drive)  # ''

# 访问 root 属性, 该属性返回路径字符串中的根路径。
print(PureWindowsPath('c:/Program Files/').root)  # \
print(PureWindowsPath('c:Program Files/').root)  # ''
print(PurePosixPath('/etc').root)  # /

# 访问 anchor 属性, 该属性返回路径字符串中的盘符和根路径。
print(PureWindowsPath('c:/Program Files/').anchor)  # c:\
print(PureWindowsPath('c:Program Files/').anchor)  # c:
print(PurePosixPath('/etc').anchor)  # /

# 访问 parents 属性, 该属性返回当前路径 的全部父路径。
pp = PurePath('abc/xyz/wawa/haha')
print(pp.parents(0))  # abc\xyz\wawa
print(pp.parents(1))  # abc\xyz
print(pp.parents(2))  # abc
print(pp.parents[3])  # .
# 访问 parent 属性
print(pp.parent)  # abc\xyz\wawa

# 访问 name 属性
print(pp.name)  # haha
pp = PurePath('abc/wawa/bb.txt')
print(pp.name)  # bb.txt

pp = PurePath('abc/wawa/bb.txt.tar.zip')
# 访问 suffixes 属性
print(pp.suffixes[0])  # .txt
print(pp.suffixes[1])  # .tar
print(pp.suffixes[2])  # .zip

# 访问 suffix 属性, 该属性返回当前路径中的文件后缀名。相当于 suffixes 属性返回的列表的最后一个元素。
print(pp.suffix)  # .zip
print(pp.stem)  # bb.txt.tar

pp = PurePath('abc', 'xyz', 'wawa', 'haha')
print(pp)  # abc\xyz\wawa\haha
# 转换成 UNIX 风格的路径
print(pp.as_posix())  # abc/xyz/wawa/haha
# 将相对路径转换成 URI 引发异常
# print(pp.as_uri()) # ValueError
# 创建绝对路径
pp = PurePath('d:／', 'Python', 'Python3.6')
# 将绝对路径转换成 URI
print(pp.as_uri())  # file:///d:/Python/Python3.6

# 判断当前路径是否匹配指定通配符
print(PurePath('a/b.py').match('女.py'))  # True
print(PurePath('/a/b/c.py').match('b/*.py'))  # True
print(PurePath('/a/b/c.py').match('a/*.py'))  # False

pp = PurePosixPath('c:/abc/xyz/wawa')
# 测试 relative_to 方法, 获取当前路径中去除基准路径之后的结果。
print(pp.relative_to('c:/'))  # abc\xyz\wawa
print(pp.relative_to('c:/abc'))  # xyz\wawa
print(pp.relative_to('c:/abc/xyz'))  # wawa

# 测试 with_name 方法, 将当前路径中的文件名替换成新文件名 。 如果当前路径中没有文件名，则会引发 ValueError。
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz ')
print(p.with_name('fkit.py'))  # e:\Downloads\fkit.py
p = PureWindowsPath('c:/')
# print (p.with_name('fkit.py')) # ValueError

# 测试 with_suffix 方法, 将当前路径中的文件后缀名替换成新的后缀名 。 如果当前路径中没有后缀名，则会添加新的后缀名。
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_suffix('.zip'))  # e:\Downloads\pathlib.tar.zip
p = PureWindowsPath('README')
print(p.with_suffix('.txt'))  # README.txt
