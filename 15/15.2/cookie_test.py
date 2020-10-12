#!/usr/bin/env python

# -*- *************** -*-
# @File  : cookie_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-12 15:42
# -*- *************** -*-


from urllib.request import *
import http.cookiejar, urllib.parse

# 以指定文件创建 CookieJar 对象 ， 该对象可 以把 cookie 信息保存在文件中
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 创建 HTTPCookieProcessor 对象
cookie_processor = HTTPCookieProcessor(cookie_jar)
# 创建 OpenerDirector 对象
openner = build_opener(cookie_processor)

# 定义模拟 Chrome 浏览器的 User-Agent
user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
# 定义请求头
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

# ---------------------- 以下为登录的POST请求 ----------------------
# 定义系统登录参数
params = {'name': 'crazyit.org', 'pass': 'leegang', 'p': 'dp_2020'}
postdata = urllib.parse.urlencode(params).encode()
# 创建向登录页面发送 POST 请求的 Request
request = Request('http://127.0.0.1/sight/deepctrls/login',  # http://localhost:8888/test/login.jsp
                  data=postdata, headers=headers)
# 使用 OpenerDirector 发送POST请求
response = openner.open(request)
print(response.read().decode('utf-8'))

# 将cookie 信息写入文件中
cookie_jar.save(ignore_discard=True, ignore_expires=True)  # ①

# ------------------------ 下面代码发送访问被保护资源的 GET 请求 ---------------------------------------
# 创建向被保护页面发送 GET 请求 的 Request
request = Request('http://127.0.0.1/sight/deepctrls/sightIndex#/subWayIndex', # 'http://localhost:8888/test/secret.jsp',
                  headers=headers)
response = openner.open(request)
print(response.read().decode())
