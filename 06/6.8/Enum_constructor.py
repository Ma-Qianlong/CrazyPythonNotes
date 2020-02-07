#!/usr/bin/env python

# -*- *************** -*-
# @File  : Enum_constructor.py
# @Description : 枚举的构造器
# @Author: mql
# @Time  : 2020/2/7 22:32
# -*- *************** -*-


# 枚举也是类，因此枚举也可以定义构造器。
# 为枚举定义构造器之后，在定义枚举实例时必须为构造器参数设置值。

import enum


class Gender(enum.Enum):
    MALE = '男', '阳刚之力'
    FEMALE = '女', '柔顺之美'

    def __init__(self, cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc

    @property
    def desc(self):
        return self._desc

    @property
    def cn_name(self):
        return self._cn_name


# 访问 FEMALE 的 name
print('访问 FEMALE 的 name:', Gender.FEMALE.name)
# 访问 FEMALE 的 value
print('访问 FEMALE 的 value:', Gender.FEMALE.value)

# 访问 自定义的 en_name 属性
print('FEMALE 的 cn_name:', Gender.FEMALE.cn_name)
# 访问自定义的 desc 属性
print('FEMALE 的 desc:', Gender.FEMALE.desc)


# 上面程序定义了 Gender 枚举类，并为它定义了一个构造器，调用该构造器需要传入 en name
# 和 desc 两个参数，因此程序使用如下代码来定义 Gender 的枚举值 。
#     MALE = '男', '阳刚之力'
#     FEMALE = '女', '柔顺之美'

# 上面代码为 MALE 枚举指定的 value 是'男', '阳刚之力'这两个字符串，其实它们会被自动封装
# 成元组后传给 MALE 的 value 属性；而且此处传入的 '男', '阳刚之力'这两个参数值正好分别传给cn_name 和 desc 两个参数。

# 简单来说，枚举的构造器需要几个参数，此处就必须指定几个值。


