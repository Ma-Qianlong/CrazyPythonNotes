#!/usr/bin/env python

# -*- *************** -*-
# @File  : loggingDemo-01-direct.py
# @Description : 格式配置--第一种：显式调用操作
# @Author: mql
# @Time  : 2020/5/20 16:37
# -*- *************** -*-


# 显式创建 Logger记录器、Handler处理器 和 Formatter格式化器，并进行相关设置
import logging.config
# create logger
logger_name = "example"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# create stream handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler
log_path = "./loggingDemo-01-direct.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARNING)

# create formatter
fmt = '%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('log debug')
logger.info('log info')
logger.warning('log warning')
logger.error('log error')
logger.critical('log critical')