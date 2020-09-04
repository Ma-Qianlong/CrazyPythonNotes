#!/usr/bin/env python

# -*- *************** -*-
# @File  : plot_bkmd_kpa.py
# @Description : 必康美德报警器压力数据获取
# @Author: mql
# @Time  : 2020-09-04 10:08
# -*- *************** -*-

import re
from urllib.request import *
from mycolorlog import logger


# 读取网页
def get_html(url):
    request = Request(url)
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41')
    response = urlopen(request)
    return response.read().decode('utf-8')


# OXYGEN  # MEDICAL AIR # VACUUM

def getOneMeterDate(url):
    rrr = None
    try:
        html = get_html(url)
        # 将相应的html拼接起来
        text = "".join(html.split())

        # 氧气压力
        patten_OXYGEN = re.compile('<td>OXYGEN</td><td>(.*?)KPA</td>')
        # 空气压力
        patten_MEDICALAIR = re.compile('<td>MEDICALAIR</td><td>(.*?)KPA</td>')
        # 真空压力
        patten_VACUUM = re.compile('<td>VACUUM</td><td>(.*?)KPA</td>')

        lis_O = re.findall(patten_OXYGEN, text)
        lis_M = re.findall(patten_MEDICALAIR, text)
        lis_V = re.findall(patten_VACUUM, text)

        rrr = {"oxy": lis_O[0], "mda": lis_M[0], "vac": lis_V[0]}
    except Exception as e:
        print()
        logger.error("get url: "+url+" data error, 获取不到数据")

    logger.info("url: %s, result: %s" % (url, str(rrr)))
    return rrr


if __name__ == '__main__':
    print(getOneMeterDate("http://127.0.0.1/bkmd/192.168.10.40.html"))
    print(getOneMeterDate("http://127.0.0.1/bkmd/192.168.10.41.html"))
    print(getOneMeterDate("http://127.0.0.1/bkmd/192.168.10.441.html"))
    print(getOneMeterDate("http://127.0.0.1/bkmd/192.168.10.46.html"))
    print(getOneMeterDate("http://127.0.0.1/bkmd/192.168.10.47.html"))
