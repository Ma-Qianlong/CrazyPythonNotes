#!/usr/bin/env python

# -*- *************** -*-
# @File  : auction_test.py
# @Description : except 和 raise 同时使用
# @Author: mql
# @Time  : 2020/3/11 22:35
# -*- *************** -*-

class AuctionException(Exception): pass


class AuctionTest:
    def __init__(self, init_price):
        self.init_price = init_price

    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            # 此处仅简单打印异常信息
            print("转换出异常", e)
            # 再次引发自定义异常
            raise AuctionException('竞拍价必须是数值，不能包含其他字符！')
            # 或进行异常转译（包装）
            # raise AuctionException(e)
            # 或再次引发当前激活的异常
            # raise
        if self.init_price > d:
            raise AuctionException('竞拍价比起拍价低，不允许竞拍！')
        initPrice = d


def main():
    at = AuctionTest(20.4)
    try:
        at.bid("df")
    except Exception as ae:
        # 再次捕获到 bid （）方法中的异常，并对该异常进行处理
        print('main 函数捕获的异常：', ae)


main()
