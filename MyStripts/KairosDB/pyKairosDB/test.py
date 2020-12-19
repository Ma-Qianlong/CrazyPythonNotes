#!/usr/bin/env python

# -*- *************** -*-
# @File  : test.py
# @Description : 
# @Author: mql
# @Time  : 2020/11/24 23:02
# -*- *************** -*-


import connection

c = connection.KairosDBConnection("127.0.0.1", "8080", False)
print(c)