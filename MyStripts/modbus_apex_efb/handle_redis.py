#!/usr/bin/env python

# -*- *************** -*-
# @File  : handle_redis.py
# @Description : 
# @Author: mql
# @Time  : 2020/12/17 22:54
# -*- *************** -*-


from redis import StrictRedis, ConnectionPool


class HandleRedis:
    def __init__(self, host="127.0.0.1", port=6379, db=0, key_prefix="ACQDATA_R_"):
        pool = ConnectionPool(host=host, port=port)
        print("redis connect ok !")
        self.redis = StrictRedis(connection_pool=pool, db=db)
        self.key_prefix = key_prefix

    def getRedis(self):
        return self.redis

    def putRTData(self, list):
        if list is None:
            return
        pushdict = {}
        for ii in list:
            key = self.key_prefix + ii.get('tag')
            val = ii.get('tag') + ",0," + ii.get('time') + "," + str(ii.get('val')) + ",0"
            pushdict[key] = val
        self.redis.mset(pushdict)

# pool = ConnectionPool(host='localhost', port=6379, db=0)
# redis = StrictRedis(connection_pool=pool)
# redis.set('name', 'my name is Bob')
# print(redis.get('name'))
#
# redis.mset({'name1': 'Durant', 'name2': 'James'})
# print(redis.mget(['nn', 'name', 'name1', 'name2']))
