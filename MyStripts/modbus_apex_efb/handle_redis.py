#!/usr/bin/env python

# -*- *************** -*-
# @File  : handle_redis.py
# @Description : 
# @Author: mql
# @Time  : 2020/12/17 22:54
# -*- *************** -*-


from redis import StrictRedis, ConnectionPool


class HandleRedis:
    def __init__(self, host="127.0.0.1", port=6379, db=0, key_prefix="ACQDATA_R_", fault_rec_prefix="APEX_REC_"):
        pool = ConnectionPool(host=host, port=port)
        self.redis = StrictRedis(connection_pool=pool, db=db)
        if self.redis.ping():
            print("'ping -> pong', redis connect success !")
        self.key_prefix = key_prefix
        self.fault_rec_prefix = fault_rec_prefix

    def getRedis(self):
        return self.redis

    def putRTData(self, list):
        if list is None and len(list) > 0:
            return
        pushdict = {}
        for ii in list:
            key = self.key_prefix + ii.get('tag')
            val = ii.get('tag') + ",0," + ii.get('time') + "," + str(ii.get('val')) + ",0"
            pushdict[key] = val
        self.redis.mset(pushdict)

    def putFaultRecData(self, list):
        if list is None and len(list) > 0:
            return
        pushdict = {}
        for ii in list:
            key = self.fault_rec_prefix + ii.get('tag')
            val = str(ii).replace("'", "\"").replace('(', '').replace(')', '')
            pushdict[key] = val
        self.redis.mset(pushdict)

# pool = ConnectionPool(host='localhost', port=6379, db=0)
# redis = StrictRedis(connection_pool=pool)
# redis.set('name', 'my name is Bob')
# print(redis.get('name'))
#
# redis.mset({'name1': 'Durant', 'name2': 'James'})
# print(redis.mget(['nn', 'name', 'name1', 'name2']))
