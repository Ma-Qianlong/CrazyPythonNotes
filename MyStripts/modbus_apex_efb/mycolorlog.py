#!/usr/bin/env python

# -*- *************** -*-
# @File  : mycolorlog.py
# @Description : 
# @Author: mql
# @Time  : 2020/5/20 17:58
# -*- *************** -*-


#!/usr/bin/env python

# -*- *************** -*-
# @File  : MyLoggingColorlogCfg01.py
# @Description : logger 同时输出到控制台（颜色不同）和文件
# @Author: mql
# @Time  : 2020/5/20 17:50
# -*- *************** -*-


import logging
import logging.handlers
import colorlog

log_colors_config = {
    'DEBUG': 'white',  # cyan white
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red'
}

logger = logging.getLogger('modbus_apex_efb')
# 输出到控制台
console_handler = logging.StreamHandler()
# 输出到文件
# file_handler = logging.FileHandler(filename='mylog.log', mode='a', encoding='utf8')
file_handler = logging.handlers.TimedRotatingFileHandler(filename='modbus_apex_efb.log', when='D', interval=1, backupCount=30, encoding=None, delay=False, utc=False)
# 设置后缀名称，跟strftime的格式一样
# 注意：filehanlder.suffix的格式必须这么写，才能自动删除旧文件，如果设定是天，就必须写成“%Y-%m-%d.log”，写成其他格式会导致删除旧文件不生效。这个配置在源码里能看出来，但是在官方文档并没有说明这一点！！！！！！！！！！
# file_handler.suffix = "%Y-%m-%d_%H-%M-%S.log"
file_handler.suffix = "%Y-%m-%d.log"

# 日志级别，logger 和 handler以最高级别为准，不同handler之间可以不一样，不相互影响
logger.setLevel(logging.DEBUG)
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

fmt1 = '%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s'
fmt2 = '[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s'
fmt2_color ='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s'
fmt_my = '%(asctime)s.%(msecs)03d - PID:%(thread)d - [%(threadName)s] [%(levelname)s] %(filename)s -> %(funcName)s[line:%(lineno)d] - %(message)s'
fmt_my_color = '%(log_color)s%(asctime)s.%(msecs)03d - PID:%(thread)d - [%(threadName)s] [%(levelname)s] %(filename)s -> %(funcName)s[line:%(lineno)d] - %(message)s'

# 日志输出格式
file_formatter = logging.Formatter(
    #fmt='[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
    fmt=fmt_my,
    datefmt='%Y-%m-%d  %H:%M:%S'
)
console_formatter = colorlog.ColoredFormatter(
    #fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
    fmt=fmt_my_color,
    datefmt='%Y-%m-%d  %H:%M:%S',
    log_colors=log_colors_config
)
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# 重复日志问题：
# 1、防止多次addHandler；
# 2、loggername 保证每次添加的时候不一样；
# 3、显示完log之后调用removeHandler
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

console_handler.close()
file_handler.close()


if __name__ == '__main__':
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')