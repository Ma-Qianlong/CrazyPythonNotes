#!/usr/bin/env python

# -*- *************** -*-
# @File  : test_ping.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-09 17:27
# -*- *************** -*-


# import os

# ip = '192.168.5.60'
# callback = os.system('ping -c 1 -w 1 %s' % ip) # ping命令,
# print(type(callback))
# print(callback)

# ipList = ['192.168.5.60', '192.168.2.22', '192.168.2.3', '192.168.254']
# def ping(ip):
#     r = os.system("ping "+ip)
#     if r == 0:
#         print("ping" + ip + "is ok")
#     else:
#         print("ping" + ip + "is not ok")
#     return r
#
# for ip in ipList:
#     pr = ping(ip)
#     ping(pr)

# coding=utf-8

import os, time
import sys

start_Time = int(time.time())
ip_True = open('ip_True.txt', 'w+')
ip_False = open('ip_False.txt', 'w+')
IPhost = []
IPbegin = input(u'请输入起始查询IP： ')
IPend = input(u'请输入终止查询IP： ')
IP1 = IPbegin.split('.')[0]
IP2 = IPbegin.split('.')[1]
IP3 = IPbegin.split('.')[2]
IP4 = IPbegin.split('.')[-1]
IPend_last = IPend.split('.')[-1]
count_True, count_False = 0, 0
for i in range(int(IP4) - 1, int(IPend_last)):
    ip = str(IP1 + '.' + IP2 + '.' + IP3 + '.' + IP4)
    int_IP4 = int(IP4)
    int_IP4 += 1
    IP4 = str(int_IP4)
    return1 = os.system('ping -n 1 -w 2 %s' % ip)
    if return1:
        print('ping %s is fail' % ip)
        ip_False.write(ip + '\n')
        count_False += 1
    else:
        print('ping %s is ok' % ip)
        ip_True.write(ip + '\n')
        count_True += 1
ip_True.close()
ip_False.close()
end_Time = int(time.time())
print("time(秒)：", end_Time - start_Time, "s")
print("ping通的ip数：", count_True, "   ping不通的ip数：", count_False)
