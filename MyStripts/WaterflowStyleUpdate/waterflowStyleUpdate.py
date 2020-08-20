#!/usr/bin/env python

# -*- *************** -*-
# @File  : waterflowStyleUpdate.py
# @Description : 
# @Author: mql
# @Time  : 2020-08-18 16:52
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

    def findBackWaterflowById(self, backId):
        '''
        据id获取 backend 水流相关样式 信息
        :param backId:
        :return:
        '''
        cursor = self.conn.cursor()
        try:
            cursor.execute('select waterFlowName, styleJson FROM thinkbos_backend_waterflow WHERE id = %s ', (backId,))

            # logger.debug('---------------------------------------------')
            # a = 0;
            # for dd in cursor.description:
            #     logger.debug(a)
            #     a += 1
            #     logger.debug(dd)
            # logger.debug('---------------------------------------------')

            return cursor.fetchone()
        except Exception as e:
            logger.error("【findBackWaterflowById】 error, args: %s" % e.args)
        finally:
            cursor.close()

    def findPageWaterflowBybackId(self, backId):
        '''
        据backend水流id获取 页面水流相关 信息
        :param backId:
        :return:
        '''
        cursor = self.conn.cursor()
        try:
            cursor.execute('select * FROM thinkbos_page_waterflow WHERE backWaterflowId = %s ', (backId,))

            # logger.debug('---------------------------------------------')
            # a = 0;
            # for dd in cursor.description:
            #     logger.debug(a)
            #     a += 1
            #     logger.debug(dd)
            # logger.debug('---------------------------------------------')

            return cursor.fetchall()
        except Exception as e:
            logger.error("【findPageWaterflowBybackId】 error, args: %s" % e.args)
        finally:
            cursor.close()

    def updatePageWaterflowStyle(self, id, paramsJsonStr, x, y):
        '''
        据id更新水流样式相关json字符串数据
        :param id:
        :param paramsJsonStr:
        '''
        try:
            logger.debug("【updatePageWaterflowStyle】 id:%s,  paramsJsonStr:%s, x:%s, y:%s" % (id, paramsJsonStr, str(x), str(y)))
            cursor = self.conn.cursor()
            affRows = cursor.execute('UPDATE thinkbos_page_waterflow set params = %s, toLeft = %s, toTop = %s WHERE id = %s ',
                                     (paramsJsonStr, str(x), str(y), id))
            logger.debug("【updatePageWaterflowStyle】 Number of affected rows: %d \n" % affRows)
            self.conn.commit()
        except Exception as e:
            logger.error("【updatePageWaterflowStyle】 error, args: %s" % e.args)
            self.conn.rollback()
        finally:
            cursor.close()


def doStyleUpdate(pWaterflowStyle, backStyle, x, y):
    pWaterflowStyle['stroke'] = backStyle['flow']['color']
    pWaterflowStyle['background'] = backStyle['piping']['color']
    pWaterflowStyle['pipeline'] = backStyle['pipeline_frame']['color']
    pWaterflowStyle['defaultStatic'] = backStyle['defaultStatic']
    pWaterflowStyle['staticStyleObj'] = backStyle['staticStyleObj']


    angle = pWaterflowStyle['angle'] % 360
    if(pWaterflowStyle['height'] != 6 and pWaterflowStyle['height']!= 6):
        if (angle == 0 or angle == 180):
            y += 2;
        if (angle == 90 or angle == 270):
            x += 2;

    if(pWaterflowStyle['height'] is None or pWaterflowStyle['height'] == 8 or pWaterflowStyle['height'] == 7):
        pWaterflowStyle['height'] = 6

    if (pWaterflowStyle['width'] is None or pWaterflowStyle['width'] == 8 or pWaterflowStyle['width'] == 7):
        pWaterflowStyle['width'] = 6


# 改回去了
    # angle = pWaterflowStyle['angle'] % 360
    # #if(pWaterflowStyle['height'] != 6 and pWaterflowStyle['height']!= 6):
    # if (angle == 0 or angle == 180):
    #     y -= 2;
    # if (angle == 90 or angle == 270):
    #     x -= 2;
    #
    # if(pWaterflowStyle['height'] is None or int(pWaterflowStyle['height']) < 8):
    #     pWaterflowStyle['height'] = 8
    #
    # if (pWaterflowStyle['width'] is None or int(pWaterflowStyle['width']) < 8):
    #     pWaterflowStyle['width'] = 8




    return (pWaterflowStyle,x,y)



def doUpdate(host, port, user, pwd, database, backWaterflowId):
    try:
        db = doDbOpt(host, port, user, pwd, database)
        backWaterflow = db.findBackWaterflowById(backWaterflowId)
        print("backWaterflow:" + str(backWaterflow))
        pageWaterflows = db.findPageWaterflowBybackId(backWaterflowId)
        for row_tuple in pageWaterflows:
            pWaterflowId = row_tuple[0]
            pWaterflowStyle_new = doStyleUpdate(json.loads(row_tuple[7]), json.loads(backWaterflow[1]), row_tuple[8], row_tuple[9])
            print("pWaterflowStyle_new: " + str(pWaterflowStyle_new))
            db.updatePageWaterflowStyle(pWaterflowId, json.dumps(pWaterflowStyle_new[0]), pWaterflowStyle_new[1], pWaterflowStyle_new[2])

    except Exception as e:
        logger.info(e)
        logger.error(e.args)
        return e.args
    finally:
        db.closeConn()

if __name__ == '__main__':
    ss = time.time()
    # db = doDbOpt('192.168.5.249', 3136, 'root', 'root', 'db-deepctrls-wxcs-dev')
    # db.selectIconsHasStatusJson()
    # db.closeConn()

    # chenageJsonStr('[{"defaultStatus":true,"status":{"equal":"1","isOpen":"0","imageUrl":"/backend/9d74ce4f-b0aa-4b7c-98ab-11102e0014ee_水泵_关闭.png","type":"default"}},{"defaultStatus":true,"status":{"equal":"1","isOpen":"1","imageUrl":"/backend/4d8793bf-9f30-41ac-80e7-b101f2c217ed_水泵_开启.png","type":"open"}},{"defaultStatus":true,"status":{"equal":"1","isOpen":"0","imageUrl":"/backend/a8677357-a6b7-4d28-9143-397f9038bafc_水泵_故障.png","add":"no","addEqual":"","addOpen":"","type":"fault","flash":false}},{"defaultStatus":true,"status":{"equal":"1","isOpen":"1","imageUrl":"/backend/aa8a1d00-1ad5-454c-a615-67dde7549259_水泵_报警.png","add":"or","addEqual":"1","addOpen":"1","type":"alarm","flash":false}},{"defaultStatus":true,"status":{"equal":"1","isOpen":"0","imageUrl":"/backend/b8ff9930-ab67-467c-8782-f4adcbbf9e96_水泵_关闭.png","type":"status"}}]')

    logger.info("###sssss### backend update iconJson ")
    doUpdate('192.168.5.249', 3136, 'root', 'root', 'db-deepctrls-ay2fy', '4028b88173f2abe80173ff6431ef312e')