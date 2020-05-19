#!/usr/bin/env python

# -*- *************** -*-
# @File  : all_module_test.py
# @Description : 
# @Author: mql
# @Time  : 2020/03/21 16:29
# -*- *************** -*-


# 导入all_module模块中的所有成员
from all_module import *
hello()
world()
test() # 会提示找不到 test（）函数

# 事实上， __all__ 变量的意义在于为模块定义了一个开放的公共接口 。
# 通常来说，只有__all__变量列出的程序单元，才是希望该模块被外界使用的程序单元 。
# 因此，为模块设置__all__变量还是比较有用的 。
# 比如一个实际的大模块可能包含了大量其他程序不需要使用的变量、函数和类，那么通过__all__变量即可把它们自动过滤掉，这还是非常酷的。
#
# 如果确实希望程序使用模块内 __all__ 列表之外的程序单元，有两种解决方法。
# 〉第一种是使用“ import 模块名”来导入模块。在通过这种方式导入模块之后，总可以通过
# 模块名前缀（如果为模块指定了別名，则可以使用模快的别名作为前缀）来调用模块内的成员 。
# 〉第二种是使用＂ from 模块名 import 程序单元”来导入指定程序单元。在这种方式下，即
# 使想导入的程序单元没有位于 all 列表中，也依然可以导入 。