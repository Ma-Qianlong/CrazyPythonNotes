#!/usr/bin/env python

# -*- *************** -*-
# @File  : exec_insert.py
# @Description : 
# @Author: mql
# @Time  : 2020/5/12 15:58
# -*- *************** -*-


import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3136, user="root", password="root",
                       database='python')

cursor = conn.cursor()

cursor.execute('insert into user_tb values (3, %s, %s, %s)',
               ('孙悟空', '123456', 'male'))
conn.commit()
cursor.execute('insert into order_tb values(null, %s, %s, %s, %s)',
               ('鼠标', 34.2, 3, 1))
conn.commit()
cursor.close()
conn.close()