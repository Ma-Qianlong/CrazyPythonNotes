#!/usr/bin/env python

# -*- *************** -*-
# @File  : handle_mysql.py
# @Description : 
# @Author: mql
# @Time  : 2020/12/31 10:47
# -*- *************** -*-


import time
from mycolorlog import logger
import pymysql
import json

class doDbOpt:
    '''
    数据库操作类
    '''

    def __init__(self, host, port, user, password, database):
        '''
        初始化数据库连接
        :param host:
        :param port: int
        :param user:
        :param password:
        :param database:
        '''
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                    database=self.database)
        if self.conn is not None:
            logger.info("MySQL 数据库连接正常")
        else:
            logger.error("MySQL 数据库连接失败!")

    def closeConn(self):
        '''
        关闭数据库连接
        '''
        if (self.conn is not None):
            self.conn.close()

    def insertFaultRecData(self, assetName, faultCode, faultTime, faultRec=0, faultData=None):
        '''
        保存故障及录波数据
        :param assetName:   str 设备名
        :param faultCode:   int 故障码
        :param faultTime:   str 故障时间
        :param faultRec:    int 是否有录波数据
        :param faultData:   srt 录波数据
        :return:
        '''
        try:
            logger.debug("【insertFaultRecData】 ('%s', '%d', '%s', '%d', '%s')" % (assetName, int(faultCode), faultTime, int(faultRec), faultData))
            cursor = self.conn.cursor()
            affRows = cursor.execute("insert into t_efb_fault_rec_data(assetName, faultCode, faultTime, faultRec, recData) "
                                     "values (%s, %s, %s, %s, %s) ",
                                     (assetName, faultCode, faultTime, faultRec, faultData))
            logger.debug("【insertFaultRecData】 Number of affected rows: %d \n" % affRows)
            self.conn.commit()
        except Exception as e:
            logger.error("【insertFaultRecData】 error, args: %s" % e.args)
            self.conn.rollback()
        finally:
            cursor.close()


if __name__ == '__main__':
    db = doDbOpt(host='127.0.0.1', port=3136, user='root', password='root', database='db-deepctrls-ay2fy')
    db.insertFaultRecData("d01", 1, "2020-12-31 00:00:00", faultRec=1, faultData="dafasfda")