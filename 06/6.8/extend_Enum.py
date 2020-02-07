#!/usr/bin/env python

# -*- *************** -*-
# @File  : extend_Enum.py
# @Description : 通过继承 Enum 来派生枚举类
# @Author: mql
# @Time  : 2020/1/30 21:35
# -*- *************** -*-

# 如果要定义更复杂的枚举，则可通过继承 Enum 来派生枚举类，
# 在这种方式下程序就可以为枚举额外定义方法了。

import enum


class Orientation(enum.Enum):
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'

    def info(self):
        print("这是一个代表方向【%s】的枚举" % self.value)


print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
# 通过枚举变量名访问枚举
print(Orientation['WEST'])
# 通过枚举值名访问枚举
print(Orientation('西'))
# 调用枚举的 info （）方法
print(Orientation.EAST.info())
# 遍历 Orientation 枚举的所有成员
for name, member in Orientation.__members__.items():
    print(name, '=>', member, ',', member.value)

# 上面程序通过继承 Enum 派生了 Orientation 枚举类，
# 通过这种方式派生的枚举类既可额外定义方法，
# 如上面的 info（）方法所示，
# 也可为枚举指定 value ( value 的值默认是 l 、 2 、 3 、…）。
