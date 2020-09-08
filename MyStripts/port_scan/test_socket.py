#!/usr/bin/env python

# -*- *************** -*-
# @File  : test_socket.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-08 9:32
# -*- *************** -*-


import socket

print(socket._GLOBAL_DEFAULT_TIMEOUT)

def get_ip_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip, port))
        print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip, port))
    finally:
        server.close()


if __name__ == '__main__':
    host = '10.0.0.11'
    for port in range(20, 100):
        get_ip_status(host, port)