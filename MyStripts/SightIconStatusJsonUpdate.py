#!/usr/bin/env python

# -*- *************** -*-
# @File  : SightIconStatusJsonUpdate.py
# @Description : 
# @Author: mql
# @Time  : 2020-07-02 20:54
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
        :param port:
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
            logger.info("数据库连接正常")
        else:
            logger.error("数据库连接失败!")

    def closeConn(self):
        '''
        关闭数据库连接
        '''
        if (self.conn is not None):
            self.conn.close()

    def updateStatusJson(self, id, statusJsonStr):
        '''
        据id更新图标判断条件相关json字符串数据
        :param id:
        :param statusJsonStr:
        '''
        try:
            logger.debug("【updateStatusJson】 id:%s,  statusJson:%s" % (id, statusJsonStr))
            cursor = self.conn.cursor()
            affRows = cursor.execute('UPDATE thinkbos_backend_icon set statusJson = %s WHERE id = %s ',
                                     (statusJsonStr, id))
            logger.debug("【updateStatusJson】 Number of affected rows: %d \n" % affRows)
            self.conn.commit()
        except Exception as e:
            logger.error("【updateStatusJson】 error, args: %s" % e.args)
            self.conn.rollback()
        finally:
            cursor.close()

    def selectIconsHasStatusJson(self):
        '''
        查询所有的有状态json数据的图标数据
        :return:
        '''
        cursor = self.conn.cursor()
        try:
            cursor.execute('select id, statusJson FROM thinkbos_backend_icon WHERE statusJson <> "" ')

            # logger.debug('---------------------------------------------')
            # a = 0;
            # for dd in cursor.description:
            #     logger.debug(a)
            #     a += 1
            #     logger.debug(dd)
            # logger.debug('---------------------------------------------')

            logger.debug('共查询到：%d条数据。' % cursor.rowcount)

            # 查询所有数据，返回结果默认以元组形式，所以可以进行迭代处理
            # for i in cursor.fetchall():
            #     logger.debug(i)

            # 获取第一行数据
            # result_1 = cursor.fetchone()
            # logger.debug(result_1)

            # 获取前n行数据
            # result_3 = cursor.fetchmany(3)
            # logger.debug(result_3)

            return cursor.fetchall()
        except Exception as e:
            logger.error("【selectIconsHasStatusJson】 error, args: %s" % e.args)
        finally:
            cursor.close()


    def updateStatusJson_sight(self, id, statusJsonStr):
        '''
        据id更新图标判断条件相关json字符串数据
        :param id:
        :param statusJsonStr:
        '''
        try:
            logger.debug("【updateStatusJson_sight】 id:%s,  statusJson:%s" % (id, statusJsonStr))
            cursor = self.conn.cursor()
            affRows = cursor.execute('UPDATE thinkbos_page_asset_icon set statusJson = %s WHERE id = %s ',
                                     (statusJsonStr, id))
            logger.debug("【updateStatusJson_sight】 Number of affected rows: %d \n" % affRows)
            self.conn.commit()
        except Exception as e:
            logger.error("【updateStatusJson_sight】 error, args: %s" % e.args)
            self.conn.rollback()
        finally:
            cursor.close()

    def selectIconsHasStatusJson_sight(self):
        '''
        查询所有的有状态json数据的图标数据
        :return:
        '''
        cursor = self.conn.cursor()
        try:
            cursor.execute('select id, statusJson FROM thinkbos_page_asset_icon WHERE statusJson <> "" ')

            # logger.debug('---------------------------------------------')
            # a = 0;
            # for dd in cursor.description:
            #     logger.debug(a)
            #     a += 1
            #     logger.debug(dd)
            # logger.debug('---------------------------------------------')

            logger.debug('共查询到：%d条数据。' % cursor.rowcount)

            return cursor.fetchall()
        except Exception as e:
            logger.error("【selectIconsHasStatusJson_sight】 error, args: %s" % e.args)
        finally:
            cursor.close()


def chenageJsonStr(rstJson):
    logger.info('#######################################')
    logger.info('原始字符串：%s' % rstJson)
    jArr = json.loads(rstJson)

    newArr = []
    for obj in jArr:
        logger.debug("原始OBJ：%s", obj)

        if ('list' in obj['status']):
            logger.warning(">>>>>>> 此对象已经被转化过了")
            continue

        statusList = []
        statusListObj1 = {'pointId': obj['status']['type'], 'equal': obj['status']['equal'],
                          'isOpen': obj['status']['isOpen']}
        # statusListObj1 = {'pointId': obj['status']['type']}
        # if('equal' in obj['status']):
        #     statusListObj1['equal'] = obj['status']['equal']
        # else:
        #     logger.warning(">>>>>>>>> 无【equal】属性")
        # if ('isOpen' in obj['status']):
        #     statusListObj1['isOpen'] = obj['status']['isOpen']
        # else:
        #     logger.warning(">>>>>>>>> 无【isOpen】属性")

        statusListObj2 = {}
        if ('add' in obj['status'] and obj['status']['add'] != 'no'):
        # if ('add' in obj['status']):
            statusListObj1['add'] = obj['status']['add']
            if ('addEqual' in obj['status'] and 'addOpen' in obj['status']):
                statusListObj2 = {'pointId': obj['status']['type'], 'equal': obj['status']['addEqual'], 'isOpen': obj['status']['addOpen'], 'add': 'no'}
                # statusListObj2 = {'pointId': obj['status']['type'], 'equal': obj['status']['addEqual'], 'isOpen': obj['status']['addOpen']}

        statusList.append(statusListObj1)
        if (len(statusListObj2) > 0):
            statusList.append(statusListObj2)

        statusObj = {'imageUrl': obj['status']['imageUrl'], 'type': obj['status']['type'], 'list': statusList}
        if ('flash' in obj['status']):
            statusObj['flash'] = obj['status']['flash']
        newObj = {'defaultStatus': obj['defaultStatus'], 'status': statusObj}
        logger.info("新的OBJ：%s", newObj)

        newArr.append(newObj)

    newStr = json.dumps(newArr)
    logger.info('结果字符串：%s \n ' % newStr)
    return newStr


def doUpdate(host, port, user, pwd, database, isSight = False):
    try:
        db = doDbOpt(host, port, user, pwd, database)
        dataRows = db.selectIconsHasStatusJson() if isSight is False else db.selectIconsHasStatusJson_sight()
        for row_tuples in dataRows:
            logger.debug("ID:" + row_tuples[0])
            if (row_tuples[1].startswith("[") and row_tuples[1].endswith("]")):
                logger.warning('@@@@@@ stausJson 数组对象：')
                rStr = chenageJsonStr(row_tuples[1])
                if(rStr and '[]' != rStr):
                    db.updateStatusJson(row_tuples[0], rStr) if isSight is False else db.updateStatusJson_sight(row_tuples[0], rStr)
            else:
                logger.warning('@@@@@@ stausJson 【非】数组对象： \n')
    finally:
        db.closeConn()


if __name__ == '__main__':
    ss = time.time()
    # db = doDbOpt('192.168.5.249', 3136, 'root', 'root', 'db-deepctrls-wxcs-dev')
    # db.selectIconsHasStatusJson()
    # db.closeConn()

    # chenageJsonStr('[{"defaultStatus":true,"status":{"equal":"1","isOpen":"0","imageUrl":"/backend/9d74ce4f-b0aa-4b7c-98ab-11102e0014ee_水泵_关闭.png","type":"default"}},{"defaultStatus":true,"status":{"equal":"1","isOpen":"1","imageUrl":"/backend/4d8793bf-9f30-41ac-80e7-b101f2c217ed_水泵_开启.png","type":"open"}},{"defaultStatus":true,"status":{"equal":"1","isOpen":"0","imageUrl":"/backend/a8677357-a6b7-4d28-9143-397f9038bafc_水泵_故障.png","add":"no","addEqual":"","addOpen":"","type":"fault","flash":false}},{"defaultStatus":true,"status":{"equal":"1","isOpen":"1","imageUrl":"/backend/aa8a1d00-1ad5-454c-a615-67dde7549259_水泵_报警.png","add":"or","addEqual":"1","addOpen":"1","type":"alarm","flash":false}},{"defaultStatus":true,"status":{"equal":"1","isOpen":"0","imageUrl":"/backend/b8ff9930-ab67-467c-8782-f4adcbbf9e96_水泵_关闭.png","type":"status"}}]')

    logger.info("###sssss### backend update iconJson ")
    doUpdate('192.168.5.249', 3136, 'root', 'root', 'db-deepctrls-wxcs-dev')
    ss1 = time.time()
    logger.info("###eeeee### backend update iconJson 耗时: %s \n" % (ss1 - ss))

    logger.info("###sssss### sight update iconJson ")
    doUpdate('192.168.5.249', 3136, 'root', 'root', 'db-deepctrls-wxcs-dev', True)
    ss2 = time.time()
    logger.info("###eeeee### sight update iconJson 耗时: %s \n" % (ss2 - ss1))

    logger.info("执行耗时（s）:%f" % (ss2 - ss))
    logger.info("当前进程使用CPU时间(ms): %f" % (time.process_time_ns() / 1000000))
