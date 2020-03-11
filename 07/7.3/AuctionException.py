#!/usr/bin/env python

# -*- *************** -*-
# @File  : AuctionException.py
# @Description : 自定义异常类
# @Author: mql
# @Time  : 2020/3/11 22:28
# -*- *************** -*-


# 很多时候 ， 程序可选择引发自定义异常，因为异常的类名通常也包含了该异常的有用信息。
# 所以在引发异常时 ，应该选择合适的异常类，从而可以明确地描述该异常情况 。
# 在这种情形下 ， 应用程序常常需要引发自定义异常。

# 用户自定义异常都应该继承 Exception 基类或 Exception 的子类 ，
# 在自定义异常类时基本不需要书写更多的代码，只要指定自定义异常类的父类即可。
# 下面程序创建了一个自定义异常类。

class AuctionException(Exception): pass

# 上面程序创建了 AuctionException 异常类，该异常类不需要类体定义，因此使用 pass 语句作为占位符即可 。
# 在大部分情况下，创建自定义异常类都可采用与 AuctionException.py 相似的代码来完成，
# 只需改变 AuctionExc巳ption 异常的类名即可，让该异常的类名可以准确地描述该异常。