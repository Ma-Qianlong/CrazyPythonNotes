#!/usr/bin/env python

# -*- *************** -*-
# @File  : autocommit_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/5/12 16:20
# -*- *************** -*-


# 需要说明的是， MySQL 数据库模块的连接对象有一个 autoconunit 属性，如果将该属性设为
# True ，则 意 味着关闭该连接的事务支持 ， 程序每次执行 DML 语句之后都会自动提交，这样程序就
# 无须调用连接对象的 commit（）方法来提交事务了。

# 对于pymysql 库没有用。 mysql.connector 有用

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3136, user="root", password="root",
                       database='python')

conn.autocommit = True

cursor = conn.cursor()

cursor.execute('insert into order_tb values(null, %s, %s, %s, %s)',
               ('键盘', 34.2, 3, 2))
cursor.close()
conn.close()
