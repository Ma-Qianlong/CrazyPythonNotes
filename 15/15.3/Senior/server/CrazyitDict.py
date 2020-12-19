#!/usr/bin/env python

# -*- *************** -*-
# @File  : CrazyitDict.py
# @Description :
# @Author: mql
# @Time  : 2020/11/20 16:50
# -*- *************** -*-

class CrazyitDict(dict):
    # 根据value查找key
    def key_form_value(self, val):
        # 遍历所有key组成的集合
        for key in self.keys():
            # 如果指定 key 对应的 value 与被搜索的 value 相同，则返回对应的 key
            if self[key] == val:
                return key

    # 根据 value 删除 key
    def remove_by_value(self, val):
        # 遍历所有key组成的集合
        for key in self.keys():
            # 如果指定 key 对应的 value 与被搜索的 value 相同，则返回对应的 key
            if self[key] == val:
                self.pop(key)
                return
