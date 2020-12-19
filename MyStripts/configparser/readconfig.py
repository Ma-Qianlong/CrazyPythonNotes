#!/usr/bin/env python

# -*- *************** -*-
# @File  : readconfig.py
# @Description : 
# @Author: mql
# @Time  : 2020/12/16 22:43
# -*- *************** -*-


import configparser
import os

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            # root_dir = os.path.dirname(os.path.abspath('.'))
            root_dir = os.getcwd()
            configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_db(self, param):
        value = self.cf.get("Mysql-Database", param)
        return value


if __name__ == '__main__':
    test = ReadConfig()
    t = test.get_db("host")
    print(t)