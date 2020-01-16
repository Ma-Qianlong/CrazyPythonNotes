#!/usr/bin/env python

# -*- *************** -*-
# @File  : instance_access_classvar.py
# @Description : 类变量和实例变量2
# @Author: mql
# @Time  : 2020/1/16 10:44
# -*- *************** -*-


# 实际上， Python 完全允许使用对象来访 问 该对象所属类的类变量（当然还是推荐使用类访问类变量）。

class Record:
    # 定义两个类变量
    item = '鼠标'
    date ='2016-06-16'
    def info(self):
        print('info方法中，', self.item)
        print('info方法中，', self.date)

rc = Record()
print(rc.item)
print(rc.date)
rc.info()

print()
# 由于通过对象访 问类变量的本质还是通过类名在访 问， 因此如果类变量发生了改变 ， 当程序访
# 问这些类变量时也会读到修改之后的值 。

# 修改 Record 类的两个类变量
Record.item = '键盘'
Record.date = '2016-08-18'
# 调用info（) 方法
rc.info()
# 从上面的输出结果可以看到，通过实例访问类变量的本质依然是通过类名在访问 。

