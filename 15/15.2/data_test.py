#!/usr/bin/env python

# -*- *************** -*-
# @File  : data_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-10 13:15
# -*- *************** -*-


from urllib.request import *

# 向 https://localhost/cgi-bin/test.cgi 发送请求数据
# with urlopen(url='https://localhost/cgi-bin/test.cgi',
with urlopen(url='http://www.baidu.com',
             data='测试数据'.encode('utf-8')) as f:
    # 读取服务器全部响应数据
    print(f.read().decode('utf-8'))

print("\n######################################")
# 如果使用 urlopen（）函数向服务器页面发送 GET 请求参数 ，则无须使用 data 属性，直接把请求
# 参数附加在 URL 之后即可 。
import urllib.parse

param = urllib.parse.urlencode({'name': 'fkit', 'password': '123888'})
# 将请求参数添加到URL后面
url = 'http://www.baidu.com/?%s' % param
print(url)
with urlopen(url=url) as f:
    # 读取服务器全部响应数据
    print(f.read().decode('utf-8'))

print("\n######################################")
# 如果想通过 urlopen（）函数发送 POST 请求参数，则同样可通过 data 属性来实现。
params = urllib.parse.urlencode({'name': 'fkit', 'password': '123888'})
params = params.encode('utf-8')
# 只用data指定请求参数
with urlopen("http://www.baidu.com/", data=params) as f:
    print(f.read().decode('utf-8'))
