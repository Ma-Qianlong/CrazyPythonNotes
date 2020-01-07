#!/usr/bin/env python

# -*- *************** -*-
# @File  : continue_test.py
# @Description : 使用 continue 忽略本次循环的剩下语句
# @Author: mql
# @Time  : 2020/1/7 18:43
# -*- *************** -*-


# continue 的功能和 break 有点类似，
# 区别是 continue 只是忽略当次循环的剩下语句, 接着开始下一次循环,
# 并不会中止循环；而 break 则是完全中止循环本身

for i in range(0, 3):
    print("i的值是：", i)
    if i == 1:
        # 忽略当次循环剩下的语句
        continue
    print("continue 之后输出语句")


# 从上面的运行结果来看 ， 当 l 等于 1 时，程序没有输出 “ continue 后的输出语句”字符串，
# 因为程序执行到 continue 时 ，忽略了当次循环中 continue 语句后的代码 。
# 从这个意义上看，如果把一条continue 语句放在当次循环的最后一行，
# 那么这条 continue 语句是没有任何意义的 因为它仅仅忽略了一片空白，没有忽略任何程序语句。
