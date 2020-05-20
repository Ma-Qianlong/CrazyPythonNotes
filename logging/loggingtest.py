#!/usr/bin/env python

# -*- *************** -*-
# @File  : loggingtest.py
# @Description : loggin 基础使用
# @Author: mql
# @Time  : 2020/5/20 15:24
# -*- *************** -*-


import logging

logging.debug('dubug msg')
logging.info('info msg')
logging.warning('warn msg')
logging.error('error msg')
logging.critical('crictical msg')

# *. 默认 打印等级：WARNING(即只有日志级别高于WARNING的日志信息才会输出)
# *. 默认 打印格式：[%(levelname)s]:[%(name)s]:[%(message)s] 即：[日志等级]:[Logger实例名称]:[日志消息内容]