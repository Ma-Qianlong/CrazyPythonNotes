#!/usr/bin/env python

# -*- *************** -*-
# @File  : Request_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-10 13:31
# -*- *************** -*-


from urllib.request import *

params = {'test': "put"}
params = str(params).encode('utf-8')
# 创建request对象， 设置使用 PUT 请求方式
req = Request(url='http://www.baidu.com/',
              data=params, method='GET')  # PUT
with urlopen(req) as f:
    print(f.status)
    print(f.read().decode('utf-8'))

# 可以使用 Request 对象来添加请求头
req = Request(url='http://www.baidu.com/')
# 添加请求头
req.add_header('Referer', 'https://www.test.com/')
with urlopen(req) as f:
    print(f.status)
    print(f.read().decode('utf-8'))


