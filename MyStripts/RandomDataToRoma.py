#!/usr/bin/env python

# -*- *************** -*-
# @File  : RandomDataToRoma.py
# @Description : 向MySQL数据库模拟随机数据
# @Author: mql
# @Time  : 2020/5/12 17:47
# -*- *************** -*-


from datetime import datetime, timedelta
import random
import pymysql
import time


# 获取俩浮点数之间的伪随机数
def getRandomFloat(sF, eF):
    randomStr = '%.2f' % random.uniform(sF, eF)
    return float(randomStr)


# 获取每几分钟数据
def getEveryMinute(begin_time, end_time, durion):
    '''
    获取每几分钟数据
    :param begin_time: string 开始时间
    :param end_time: string 结束时间
    :param durion: integer 分钟间隔
    :return: list 时间字符串列表
    '''
    time_list = []
    begin_time = datetime.strptime(begin_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    while begin_time <= end_time:
        time_str = begin_time.strftime('%Y-%m-%d %H:%M:%S')
        time_list.append(time_str)
        begin_time += timedelta(minutes=durion)
    return time_list


# 向数据库写数据，datas元组
def exec_many(datas, host='192.168.5.249', port=3136, user="root", password="root",
              database='db-deepctrls-cecep-roma'):
    conn = pymysql.connect(host=host, port=port, user=user, password=password,
                           database=database)
    cursor = conn.cursor()
    try:
        affRows = cursor.executemany('insert into cecep_huawei_roma_test values (%s, %s, %s)', datas)
        print("【insert】 Number of affected rows: %d" % affRows)
        conn.commit()
    except Exception as e:
        print("execute many error, args: %s" % e.args)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def exec_del(tagnameList, sTime, eTime, host='192.168.5.249', port=3136, user="root", password="root",
             database='db-deepctrls-cecep-roma'):
    conn = pymysql.connect(host=host, port=port, user=user, password=password,
                           database=database)
    cursor = conn.cursor()
    try:
        argList = [];
        for tagname in tagnameList:
            # sql = 'delete from cecep_huawei_roma_test where id = \'%s\' and time between \'%s\' and \'%s\'' % ('test_test_test_test_test', '2020-05-10 00:00:00', '2020-05-13 23:59:59')
            # print(sql)
            # affRows = cursor.execute(sql)
            # affRows = cursor.execute("delete from cecep_huawei_roma_test where id = 'test_test_test_test_test' and time between '2020-05-10 00:00:00' and '2020-05-13 23:59:59'")
            # affRows = cursor.execute("delete from cecep_huawei_roma_test where id = %s and time between %s and %s ", ('test_test_test_test_test', '2020-05-10 00:00:00', '2020-05-13 23:59:59'))
            # affRows = cursor.executemany("delete from cecep_huawei_roma_test where id = %s and time between %s and %s ", [('test_test_test_test_test', '2020-05-10 00:00:00', '2020-05-13 23:59:59')])
            # print("Number of affected rows: %d" % affRows)
            argList.append((tagname, sTime, eTime))
        affRows = cursor.executemany("delete from cecep_huawei_roma_test where id = %s and time between %s and %s ",
                                     argList)
        print("【delete】 Number of affected rows: %d" % affRows)
        conn.commit()
    except Exception as e:
        print("execute many Delete error, args: %s" % e.args)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# 模拟单个tagname的值到MySQL数据库
def oneTagDataToMySQL(tagname, sT, eT):
    timeList = getEveryMinute(sT, eT, 5)
    lastTupleList = []
    for time in timeList:
        tupleD = (tagname, time, getRandomFloat(0, 255))
        lastTupleList.append(tupleD)
    print('data list for 【%s】 size: %d' % (tagname, len(lastTupleList)))
    exec_many(tuple(lastTupleList))


# 模拟多个tagname的值到MySQL数据库
def manyTagDataToMySQL(tagnames, sT, eT, minVal=0, maxVal=255):
    sRT = datetime.now()
    print(sRT.timestamp())
    if tagnames == None or len(tagnames) < 1:
        raise ValueError('tagname 不能为空，多个用英文逗号分隔')
    tagList = tagnames.split(",")

    # 先删除
    print(">>>>>1. 删除已有的满足当前条件的数据，防冲突")
    exec_del(tagList, sTime, eTime)

    timeList = getEveryMinute(sT, eT, 5)
    toSubmitList = []
    count = 0
    print(">>>>>2. 开始组织数据写入。。。")
    for tag in tagList:
        for time in timeList:
            tupleD = (tag, time, getRandomFloat(minVal, maxVal))
            tupleDel = (tag, time)

            toSubmitList.append(tupleD)
            count += 1
            if count % 10000 == 0:
                exec_many(tuple(toSubmitList))
                toSubmitList.clear()

    if len(toSubmitList) > 0:
        exec_many(tuple(toSubmitList))
    print(datetime.now().timestamp())
    print(">>>>>3. 模拟随机数据写入完成, 共写入 %d 条数据, 模拟及写入耗时(s)：%f" % (count, datetime.now().timestamp() - sRT.timestamp()))


# 模拟多个tagname的值到指定的 MySQL 数据库
def manyTagDataToMySQL2(tagnames, sTime, eTime, minVal=0, maxVal=255,
                        isFixedVal = 'no',
                        host='192.168.5.249', port=3136, user="root",
                        password="root",
                        database='db-deepctrls-cecep-roma'):
    '''
    :param tagnames:
    :param sTime:
    :param eTime:
    :param minVal:
    :param maxVal:
    :param isFixedVal: 是否固定值，yes-是（取maxVal为固定值）；no-否(默认, 取伪随机)
    :param host:
    :param port:
    :param user:
    :param password:
    :param database:
    :return:
    '''
    sRT = datetime.now()
    print(sRT.timestamp())
    if tagnames == None or len(tagnames) < 1:
        raise ValueError('tagname 不能为空，多个用英文逗号分隔')
    tagList = tagnames.split(",")

    # 先删除
    print(">>>>>1. 删除已有的满足当前条件的数据，防冲突")
    exec_del(tagList, sTime, eTime, host=host, port=port, user=user, password=password, database=database)

    timeList = getEveryMinute(sTime, eTime, 5)
    toSubmitList = []
    count = 0
    print(">>>>>2. 开始组织数据写入。。。")
    for tag in tagList:
        for time in timeList:
            tupleD = (tag, time, maxVal)

            if isFixedVal == 'no':
                tupleD = (tag, time, getRandomFloat(minVal, maxVal))

            toSubmitList.append(tupleD)
            count += 1
            if count % 10000 == 0:
                exec_many(tuple(toSubmitList), host=host, port=port, user=user, password=password, database=database)
                toSubmitList.clear()

    if len(toSubmitList) > 0:
        exec_many(tuple(toSubmitList), host=host, port=port, user=user, password=password, database=database)
    print(datetime.now().timestamp())
    print(">>>>>3. 模拟随机数据写入完成, 共写入 %d 条数据, 模拟及写入耗时(s)：%f" % (count, datetime.now().timestamp() - sRT.timestamp()))


# oneTagDataToMySQL("test_test_test_test_test", '2020-05-10 00:00:00', '2020-05-10 23:00:00')
# exec_del(['test_test_test_test_test'], '2020-05-10 00:00:00', '2020-05-13 23:59:59')

if __name__ == "__main__":
    print('------------------欢迎使用MySQL历史数据模拟(5分钟间隔)-------------------')
    print('注：此处会将相同tagname及时间的值覆盖', end='\n\n')
    tagnames = input("请输入tagname, 多个应英文逗号（','）分隔：")
    sDate = input("请输入开始日期(yyyy-MM-dd)：")
    eDate = input("请输入结束日期(yyyy-MM-dd)：")

    sTime = sDate + " 00:00:00"
    eTime = eDate + " 23:59:59"

    manyTagDataToMySQL(tagnames, sTime, eTime)

    print("当前进程使用CPU时间(ms): %f" % (time.process_time_ns() / 1000000))

# conn = pymysql.connect(host='192.168.5.249', port=3136, user="root", password="root",
#                            database='db-deepctrls-cecep-roma')
# cursor = conn.cursor()
# sql = 'delete from cecep_huawei_roma_test where id = \'%s\' and time between \'%s\' and \'%s\'' % ('test_test_test_test_test', '2020-05-10 00:00:00', '2020-05-13 23:59:59')
# print(sql)
# # affRows = cursor.execute(sql)
# # affRows = cursor.execute("delete from cecep_huawei_roma_test where id = 'test_test_test_test_test' and time between '2020-05-10 00:00:00' and '2020-05-13 23:59:59'")
# # affRows = cursor.execute("delete from cecep_huawei_roma_test where id = %s and time between %s and %s ", ('test_test_test_test_test', '2020-05-10 00:00:00', '2020-05-13 23:59:59'))
# affRows = cursor.executemany("delete from cecep_huawei_roma_test where id = %s and time between %s and %s ", [('test_test_test_test_test', '2020-05-10 00:00:00', '2020-05-13 23:59:59')])
# print("Number of affected rows: %d" % affRows)
# conn.commit()
# cursor.close()
# conn.close()
