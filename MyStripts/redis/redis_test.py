#!/usr/bin/env python

# -*- *************** -*-
# @File  : redis_test.py
# @Description : 参考：https://www.cnblogs.com/john-xiong/p/12089103.html
# @Author: mql
# @Time  : 2020/12/16 22:03
# -*- *************** -*-


# from redis import StrictRedis
#
# redis = StrictRedis(host='localhost', port=6379, db=0)
# redis.set('name', 'Bob')
# print(redis.get('name'))

from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)
redis.set('name', 'my name is Bob')
print(redis.get('name'))

redis.mset({'name1': 'Durant', 'name2': 'James'})
print(redis.mget(['nn','name', 'name1', 'name2']))
