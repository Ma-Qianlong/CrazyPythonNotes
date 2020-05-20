#!/usr/bin/env python

# -*- *************** -*-
# @File  : loggingDemo-04-dict.py
# @Description : 格式配置--第四种 logging.config.dictConfig 读取配置信息
# @Author: mql
# @Time  : 2020/5/20 17:41
# -*- *************** -*-


import logging.config
dictConfig = {
    'version': 1,
    'disable_existing_loggers': True,
    'incremental': False,
    'formatters': {
        'master_format': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'filters': {
        'filter_by_name': {
            'class': 'logging.Filter',
            'name': 'fileLogger'
        },
        # 仅 INFO 能输出
        'filter_single_level_pass': {
            'class': 'logging.StreamHandler',
            'pass_level': logging.INFO
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': logging.DEBUG,
            'formatter': 'master_format',
        },
        'fileHandler': {
            'class': 'logging.FileHandler',
            'filename': 'logfile.log',
            'level': logging.INFO,
            'formatter': 'master_format',
            'filters': ['filter_by_name', ],
        },
        'rotatingFileHandler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'rotatingLogfile.log',
            'level': logging.DEBUG,
            'formatter': 'master_format',
            'maxBytes': 256,
            'backupCount': 2
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False
        },
        'fileLogger': {
            'handlers': ['console', 'fileHandler'],
            'filters': ['filter_by_name', ],
            'level': 'DEBUG'
        },
        'rotatingFileLogger': {
            'handlers': ['console', 'rotatingFileHandler'],
            'level': 'INFO'
        }
    }
}
logging.config.dictConfig(dictConfig)
log = logging.getLogger(name='fileLogger')
log.debug('log debug')
log.info('log info')
log.warning('log warning')
log.error('log error')
log.critical('log critical')

log2 = logging.getLogger(name='rotatingFileLogger')
log2.debug('log debug')
log2.info('log info')
log2.warning('log warning')
log2.error('log error')
log2.critical('log critical')