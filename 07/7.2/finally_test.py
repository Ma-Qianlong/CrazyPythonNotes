#!/usr/bin/env python

# -*- *************** -*-
# @File  : finally_test.py
# @Description : 使用 finally 回收资源
# @Author: mql
# @Time  : 2020/3/5 22:58
# -*- *************** -*-


# 有些时候，程序在 try 块里打开了 一些物理资源（例如数据库连接、网络连接和磁盘文件等〉，这些物理资源都必须被显式回收。

# Python 的垃圾回收机制不会回收任何物理资源，只能回收堆内存中对象所占用的内存。

# 在异常处理语法结构中，只有 try 块是必需的，
# 也就是说，如果没有 try 块，则不能有后面的except 块和 finally 块 ；
# except 块和 finally 块都是可选的，但 except 块和 finally 块至少出现其中之一，也可以同时出现；
# 可以有多个except 块，但捕获父类异常的 except 块应该位于捕获子类异常的 except 块的后面；
# 不能只有 try 块，既没有 except 块，也没有 finally 块：
# 多个 except 块必须位于 try 块之后， finally 块必须位于所有的 except 块之后。

import os
def test():
    fis = None
    try:
        fis = open("a.txt")
    except OSError as e:
        print(e.strerror)
        # return 语句强制方法返回
        return # 1
        os._exit(1) # 2, 强制退出python解释器
    finally:
        # 关闭磁盘文件，回收资源
        if fis is not None:
            try:
                # 关闭资源
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print("执行 finally 块里的资源回收!")

test()


# 上面的运行结果表明在方法返回之前执行了 finally 块的代码。
# 将①处的 return 语句注释掉，取消②处代码的注释，即在异常处理的 except 块中使用 os._exit(1）语句来退出 Python 解释器。
# 运行上面代码，将看到如下运行结果。
# No such file or directory
# 上面的运行结果表明 finally 块没有被执行 。
# 如果在异常处理代码中使用 os._exit(1）语句来退出Python 解释器，则 finally 块将失去执行的机会。

# ** 注意：
# 除非在try块 、 except 块中调用了退出 Python 解释器的方法，
# 否则不管在 try 块、except 块中执行怎样的代码，出现怎样的情况，异常处理的 finally 块总会被执行。
# 调用 sys.exit（）方法退出程序不能阻止 finally 块的执行，这是因为 sys.exit（）方法本身就是通过引发 SystemExit 异常来退出程序的。