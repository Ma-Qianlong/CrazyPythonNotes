#!/usr/bin/env python

# -*- *************** -*-
# @File  : beautifulsoup_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/8/8 23:17
# -*- *************** -*-

import codecs
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, features="lxml")
# 打印一下 soup 对象的内容，格式化输出
print(soup.prettify())
print("##############2")
# soup2 = BeautifulSoup(codecs.open("C:\\Users\\mql\\Desktop\\bookmarks_2020_7_5.html", 'r', encoding="utf-8"), features="lxml")
# print(soup2.prettify())
print("##############2")


# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
#
#     Tag
#     NavigableString
#     BeautifulSoup
#     Comment

# (1) Tag
print(soup.title)
print(soup.head)
print(soup.a)
print(soup.p)

# 验证一下这些对象的类型
print(type(soup.a)) # <class 'bs4.element.Tag'>

# 对于 Tag，它有两个重要的属性，是 name 和 attrs，下面我们分别来感受一下：
print(soup.name)
print(soup.head.name)
# soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。

# 把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
print(soup.p.attrs)
# 如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么
print(soup.p['class'])
# 还可以这样，利用get方法，传入属性的名称，二者是等价的
print(soup.p.get('class'))