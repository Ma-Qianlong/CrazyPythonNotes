#!/usr/bin/env python

# -*- *************** -*-
# @File  : else_test2.py
# @Description : 
# @Author: mql
# @Time  : 2020/3/5 22:52
# -*- *************** -*-


def else_test():
    s = input('请输入除数：')
    result = 20 / int(s)
    print('20除以%s的结果是：%g' % (s, result))

def right_main():
    try:
        print('try 块的代码，没有异常')
    except:
        print('程序出现异常')
    else:
        # 将 else_test 放在 else 块中
        else_test()

def wrong_main():
    try:
        print('try 块的代码，没有异常')
        # 将 else_test 放在 try 块的代码的后面
        else_test()
    except:
        print('程序出现异常')


wrong_main()
right_main()

# 放在 else 块中的代间所引发的异常不会被 except 块捕获。
# 所以，如果希望某段代码的异常能被后面的 except 块捕款，那么就应该将这段代码放在 try 块的代码之后；
# 如果希望某段代码的异常能向外传播（不被 except 块捕获〉，那么就应该将这段代码放在else 块中。
