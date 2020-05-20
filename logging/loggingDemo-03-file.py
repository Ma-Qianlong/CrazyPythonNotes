#!/usr/bin/env python

# -*- *************** -*-
# @File  : loggingDemo-03-file.py
# @Description :  格式配置--第三种 logging.config.fileConfig 读取配置文件
# @Author: mql
# @Time  : 2020/5/20 17:35
# -*- *************** -*-


# 配置文件为logging.conf
import logging.config
logging.config.fileConfig('./logging.conf')
log = logging.getLogger(name='rotatingFileLogger')
log.debug('log debug')
log.info('log info')
log.warning('log warning')
log.error('log error')
log.critical('log critical')