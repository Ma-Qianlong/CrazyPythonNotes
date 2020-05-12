#!/usr/bin/env python

# -*- *************** -*-
# @File  : exec_ddl.py
# @Description : 
# @Author: mql
# @Time  : 2020/5/12 15:18
# -*- *************** -*-


# 导入访问MySQL的模块
import pymysql

# 1. 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3136, user="root", password="root",
                       database='python')

# 1. 获取游标
c = conn.cursor()
# 3. 执行DDL语句建表
c.execute('''create table user_tb(
        user_id integer primary key auto_increment,
        name varchar(255),
        pass varchar(255),
        gender varchar(255))''')

c.execute("""create table order_tb(
        order_id integer  primary key auto_increment,
        item_name varchar(255),
        item_price double,
        item_number double,
        user_id int,
        foreign key(user_id) references user_tb(user_id))""")

# 03. 关闭游标
c.close()
# 5. 关闭连接
conn.close()