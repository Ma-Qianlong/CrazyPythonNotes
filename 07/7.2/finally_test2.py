
#!/usr/bin/env python

# -*- *************** -*-
# @File  : finally_test2.py
# @Description : 
# @Author: mql
# @Time  : 2020/3/5 23:16
# -*- *************** -*-


# 在通常情况下，不要在 finally 块中使用如 return 或 raise 等导致方法中止的语句，
# 一旦在 finally 块中使用了 return 或 raise 语句，将会导致 try 块、 except 块中的 return、raise 语句失效。

def test():
    try:
        # 因为 finally 块中包含了 return 语句
        # 所以下面的 return 语句失去作用
        return True
    finally:
        return False
a = test()
print(a)

# 如果 Python 程序在执行町块、 except 块时遇到了 return 或 raise 语句，这两条语句都会导致该方法立即结束，
# 那么系统执行这两条语句并不会结束该方法，而是去寻找该异常处理流程中的finally 块，
# 如果没有找到 finally 块，程序立即执行 return 或 rais巳语句，方法中止；
# 如果找到 finally 块，系统立即开始执行 finally 块——只有当 finally 块执行完成后，
# 系统才会再次跳回来执行 try 块、except 块里的 return 或 rais巳语句;
# 如果在 finally 块里也使用了 return 或 raise 等导致方法中止的语句， finally 块己经中止了方法，系统将不会跳回去执行 t可块、 except 块里的任何代码。

# ** 注意
# 尽量避免在 finally 块里使用 return 或 raise 等导致方法中止的语句，否则可能出现一些很奇怪的情况。