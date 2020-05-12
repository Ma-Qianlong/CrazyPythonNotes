#!/usr/bin/env python

# -*- *************** -*-
# @File  : exec_many.py
# @Description : 
# @Author: mql
# @Time  : 2020/5/12 16:16
# -*- *************** -*-


import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3136, user="root", password="root",
                       database='python')

cursor = conn.cursor()

# executemany（）方法重复执行一条 SQL 语句。
cursor.executemany('insert into user_tb values (null , %s, %s, %s)',
               (('sun', '123456', 'male'),
                ('bai', '123456', 'female'),
                ('zhu', '123456', 'male'),
                ('niu', '123456', 'male'),
                ('tang', '123456', 'male')))
conn.commit()
cursor.close()
conn.close()
