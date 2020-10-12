#!/usr/bin/env python

# -*- *************** -*-
# @File  : urlparse_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-10-10 10:53
# -*- *************** -*-


from urllib.parse import *

# 解析 URL 字符串
result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(result)

# 通过属性名和索引来获取 URL 的各部分
print('scheme:', result.scheme, result[0])
print('主机和端口：', result.netloc, result[1])
print("主机：", result.hostname)
print('端口：', result.port)
print('资源路径：', result.path, result[2])
print('参数：', result.params, result[3])
print('查询字符串：', result.query, result[4])
print('fragment:', result.fragment, result[5])
print(result.geturl())

print("\n***********************************")
# 如果使用 url unparse（）函数 ，则可 以把一个 ParseResult 对象或元组恢复成 URL 字街串
result = urlunparse(('http', 'www.crazyit.org:80', 'index.php', 'yeeku', 'name=fkit', 'frag'))
print('URL为：', result)

# 如果被解析的 URL 以双斜线（//）开头 ，那么 urlparse（） 函数可以识别出主机， 只是缺少 scheme
# 部分。但如果被解析的 URL 既没有 scheme ，也没有以双斜线（//）开头 ，那么 urlparse（）函数将会
# 把这些 URL 都当成资源路径。
print("\n***********************************")
# 解析以双斜线（//）开头的 URL
result = urlparse('//www.crazyit.org:80/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口：', result.netloc, result[1])
print('资源路径：', result.path, result[2])
print('---------------')
# 解析没有 scheme ，也没有以双斜线（//）开头的 URL
# 从开头部分开始就会被当成资源路径
result = urlparse('www.crazyit.org:80/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口：', result.netloc, result[1])
print('资源路径：', result.path, result[2])


# parse＿qs()和 parse_qsl() （这个 l 代表 list ） 两个 函数都用于解析 查 询字符串 ， 只不 过返回值不
# 同而已 parse_qsl（）函数的返回值是 list（正如该函数名所暗示的。 url_encode（）则是它们的逆函数。
print("\n***********************************")
# 解析查询字符串， 返回 dict
result = parse_qs('name=fkit&name=%E7%96%AF%E7%8B%82%20java&age=12')
print(result)
# 解析查询字符串， 返回 list
result = parse_qsl('name=fkit&name=%E7%96%AF%E7%8B%82%20java&age=12')
print(result)
# 将列表形式的请求参数恢复成字符审
print(urlencode(result))


print("\n***********************************")
# 被拼接的 URL 不以斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', 'help.html')
print(result)
result = urljoin('http://www.crazyit.org/users/login.html', 'book/list.html')
print(result)

# 被拼接的 URL 以斜线（代表根路径 path ）开头
result = urljoin('http://www.crazyit.org/users/login.html', '/help.html')
print(result)
# 被拼接的 URL 以双斜线（代表绝对路径 path ）开头
result = urljoin('http://www.crazyit.org/users/login.html', '//help.html')
print(result)
