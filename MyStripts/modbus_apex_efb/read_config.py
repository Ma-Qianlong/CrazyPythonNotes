#!/usr/bin/env python

# -*- *************** -*-
# @File  : read_config.py
# @Description : 
# @Author: mql
# @Time  : 2020/12/19 22:17
# -*- *************** -*-


import configparser
import os


class ReadConfig:
    """读取配置文件类"""

    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            # root_dir = os.path.dirname(os.path.abspath('.'))
            # 在当前路径下获取配置文件
            root_dir = os.getcwd()
            configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_sections(self):
        """
        获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
        :return:
        """
        return self.cf.sections()

    def get_opetions(self, item):
        """
        获取某个section名为item所对应的键
        :param item: 不可为空
        :return:
        """
        return self.cf.options(item)

    def get_items(self, item, param=None):
        """
        获取指定item的配置数据
        :param item: 不可为空
        :param param: 参数key值
        :return: 当param为None时，返回item的所有键值对；反之返回指定参数值
        """
        if param:
            return self.cf.get(item, param)
        else:
            return self.cf.items(item)

    def get_base(self, param=None):
        if param:
            return self.cf.get("BASE", param)  # 获取[BASE]中<param>对应的值
        else:
            return self.cf.items("BASE")  # 获取section名为BASE所对应的全部键值对

    def get_redis(self, param=None):
        if param:
            return self.cf.get("REDIS", param)  # 获取[REDIS]中<param>对应的值
        else:
            return self.cf.items("REDIS")  # 获取section名为REDIS所对应的全部键值对

    def get_mysql(self, param=None):
        if param:
            return self.cf.get("MYSQL", param)  # 获取[MYSQL]中<param>对应的值
        else:
            return self.cf.items("MYSQL")  # 获取section名为MYSQL所对应的全部键值对


if __name__ == '__main__':
    test = ReadConfig()

    t = test.get_redis()
    print(t)

    base = test.get_base()
    print(base)

    base_dict = dict(base)
    print(base_dict)

    for i in range(int(base_dict.get('meter_no'))):
        efb = test.get_items('EFB-'+str(i+1))
        print(dict(efb))
