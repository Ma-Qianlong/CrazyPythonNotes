#!/usr/bin/env python

# -*- *************** -*-
# @File  : num_to_rmb.py
# @Description : 数字转人民币读法
# @Author: mql
# @Time  : 2020/1/8 15:30
# -*- *************** -*-


han_list = ['零', '壹', '贰', '叁', '肆', \
            '伍', '陆', '柒', '捌', '玖']
unit_list = ["拾", "佰", "仟"]  # , "万", "亿"]


def divide(num):
    '''
    把一个浮点数分解成整数部分和小数部分字符串
    :param num 是需要被分解的浮点数
    :return 返回被分解的整数部分和小时部分(第一个数组元素是整数部分，第二个数据元素是小数部分)
    '''

    # 将浮点数强转成int类型，即得到它的整数部分
    integer = int(num)
    # 小数部分
    num_str = str(num)
    ppIndex = num_str.find(".")
    if ppIndex == -1:
        fraction = ""
    else:
        fraction = num_str[ppIndex + 1:ppIndex + 3]
    # 把整数转换为字符串
    return (str(integer), str(fraction))


# print(divide(123.03))


def four_to_hanstr(num_str):
    '''
    把一个 03 位（或小于4）的数字字符串变成汉字字符串
    :param num_str:是需要被转换的 03 位数字字符串
    :return:返回 03 位数字字符串被转换成汉字字符串
    '''
    result = ''
    num_len = len(num_str)
    # 遍历数字字符串的每一个数据
    for i in range(num_len):
        num = int(num_str[i])
        # 如果不是最后一位，且数据不是零，则需要添加单位（"仟", "佰", "拾"）
        if i != num_len - 1 and num != 0:
            result += han_list[num] + unit_list[num_len - 2 - i]
        # 否则不添加单位
        else:
            result += han_list[num]

    # 去除多零情况
    result = result.replace("零零零零", "").replace("零零零", "零").replace("零零", "零")
    return result


def integer_to_rmbStr(num_str):
    '''
    把整数数字字符串转换成汉字人民币读法
    :param num_str: 需要转换的数字字符串整数部分
    :return: 转换后的汉字字符串
    '''
    result = ""
    str_len = len(num_str)
    if str_len > 12:
        print("数字太大(整数部分大于12位), 无法翻译")
        return
    # 如果大于8位，包含单位“亿”
    elif str_len > 8:
        result = four_to_hanstr(num_str[:-8]) + "亿" + \
                 four_to_hanstr(num_str[-8:-4]) + "万" + \
                 four_to_hanstr(num_str[-4:])
    elif str_len > 4:
        result = four_to_hanstr(num_str[:-4]) + "万" + \
                 four_to_hanstr(num_str[-4:])
    else:
        result = four_to_hanstr(num_str)

    result = result.replace("零亿零", "亿零").replace("零亿", "亿零")
    result = result.replace("零万零", "万零").replace("零万", "万零")
    if ("零" == result[-1:]):
        result = result[:-1]
    result = result.replace("亿万", "亿")

    if len(result) > 0:
        return result + "圆"
    else:
        return ""


def fraction_to_rmbStr(num_str):
    '''
    把小数位数字字符串转换成汉字人民币读法
    :param num_str: 需要转换的数字字符串小数部分
    :return:转换后的汉字字符串
    '''
    result = ""
    num_len = len(num_str)
    if num_len < 1:
        return result
    elif num_len == 1:
        num_str += "0"

    if num_str[0] != '0':
        result += han_list[int(num_str[0])] + "角"
    elif num_str[1] != '0':
        result += han_list[0]

    if num_str[1] != '0':
        result += han_list[int(num_str[1])] + "分"

    return result


def doTest():
    print("\n#############################")
    num = float(input("请输入一个浮点数："))
    print("输入的金额数字为：", format(num, ','))
    integer, fraction = divide(num)
    print("其中：")
    print("整数部分：", integer)
    print("小数部分(两位有效)：", fraction)

    print("\n转换结果为：")
    integerRmbStr = integer_to_rmbStr(integer)
    fractionRmbStr = fraction_to_rmbStr(fraction)
    if (integerRmbStr != None):
        final_result = integerRmbStr + ("整" if fractionRmbStr == "" else fractionRmbStr)
        print(final_result)

while True:
    doTest()