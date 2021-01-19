#!/usr/bin/env python

# -*- *************** -*-
# @File  : FileInfo.py
# @Description : 
# @Author: mql
# @Time  : 2021/1/19 16:08
# -*- *************** -*-


import time
# import datetime

import os


def TimeStampToTime(timestamp):
    """
    把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12
    :param timestamp: 时间戳(秒)
    :return:
    """
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def getFileSize_byte(filePath):
    '''
    获取文件的大小，单位为byte(字节)
    :param filePath: 文件完整路径
    :return:
    '''
    return os.path.getsize(filePath)


def getFileSize_KB(filePath):
    '''
    获取文件的大小,结果保留两位小数，单位为KB
    :param filePath: 文件完整路径
    :return:
    '''
    # filePath = unicode(filePath, 'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024)
    return round(fsize, 2)


def getFileSize_MB(filePath):
    '''
    获取文件的大小,结果保留两位小数，单位为MB
    :param filePath: 文件完整路径
    :return:
    '''
    # filePath = unicode(filePath, 'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


def get_FileAccessTime(filePath):
    '''
    获取文件的访问时间
    :param filePath:
    :return:
    '''
    # filePath = unicode(filePath,'utf8')
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)


def get_FileCreateTime(filePath):
    '''
    获取文件的创建时间
    :param filePath:
    :return:
    '''
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


def get_FileModifyTime(filePath):
    '''
    获取文件的修改时间
    :param filePath:
    :return:
    '''
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)
