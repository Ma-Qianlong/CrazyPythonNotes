#!/usr/bin/env python

# -*- *************** -*-
# @File  : cookie_load.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-12 16:07
# -*- *************** -*-


import http.cookiejar
from urllib.request import *

# 以指定文件创建 CookieJar 对象 ， 该对象可 以把 cookie 信息保存在文件中
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 直接加载 a.txt 中的cookie 信息
cookie_jar.load('a.txt', ignore_discard=True, ignore_expires=True)
# 遍历 a.txt 中保在的 cookie 信息
for item in cookie_jar:
    print('name = ' + item.name)
    print('Value = ' + item.value)
# 创建 HTTPCookieProcessor 对象
cookie_processor = HTTPCookieProcessor(cookie_jar)
# 创建 OpenerDirector 对象
openner = build_opener(cookie_processor)

# 定义模拟 Chrome 浏览器的 User-Agent
user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
# 定义请求头
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
# ------------------------ 下面代码发送访问被保护资源的 GET 请求 ---------------------------------------
# 创建向被保护页面发送 GET 请求 的 Request
request = Request('http://127.0.0.1/sight/deepctrls/sightIndex#/subWayIndex', # 'http://localhost:8888/test/secret.jsp',
                  headers=headers)
response = openner.open(request)
print(response.read().decode())
