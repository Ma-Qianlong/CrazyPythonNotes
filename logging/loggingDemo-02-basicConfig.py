#!/usr/bin/env python

# -*- *************** -*-
# @File  : loggingDemo-02-basicConfig.py
# @Description : 格式配置--第二种：logging.basicConfig() 配置
# @Author: mql
# @Time  : 2020/5/20 17:09
# -*- *************** -*-


# key	描述
# filename	指定使用指定的文件名，而不是StreamHandler创建FileHandler。
# filemode	如果指定了文件名，请在此模式下打开文件。 默认为'a'。
# format	格式化字符串
# datefmt	格式化日期/时间格式
# style	引用样式，默认'%', 即'%()s'
# level	logger 的 等级
# stream	使用指定的流初始化StreamHandler。 注：此参数与filename不兼容 - 如果两者都存在，则引发ValueError。
# handlers	如果指定，则应该是已创建的处理程序的可迭代，以添加到根记录器。 任何没有格式化程序集的处理程序都将被分配在此函数中创建的默认格式化程序。 请注意，此参数与filename或stream不兼容 - 如果两者都存在，则引发ValueError。

import logging.config

logging.basicConfig(
    filename='loggingDemo-02-basicConfig.log',
    level=logging.DEBUG,
    format= '%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug('log debug')
logging.info('log info')
logging.warning('log warning')
logging.error('log error')
logging.critical('log critical')