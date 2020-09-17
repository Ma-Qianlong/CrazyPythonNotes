#!/usr/bin/env python

# -*- *************** -*-
# @File  : fork_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-17 11:42
# -*- *************** -*-


import os

print('父进程（%s）开始执行' % os.getpid())

# 开始fork一个子进程
# 从这行开始，下面的代码都会被两进程执行
pid = os.fork()
print('进程进入：%s' % os.getpid())
# 如果 pid 为 0， 则表明是子进程
if pid == 0:
    print('子进程， 其ID为（%s）, 父进程ID为（%s）' % (os.getpid(), os.getppid()))
else:
    print('我（%s）创建的子进程ID为（%s）.' % (os.getpid(), pid))
print('进程结束：%s' % os.getpid())

# os.fork（）方法在 Windows 系统上无效 ， 只在 UNIX 及类 UNIX 系统上有效 ， UNIX 及类 UNIX 系统包括 UNIX 、 Linux 和 Mac OS X。
