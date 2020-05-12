#!/usr/bin/env python

# -*- *************** -*-
# @File  : __init__.py
# @Description : 
# @Author: mql
# @Time  : 2020/03/21 17:56
# -*- *************** -*-

# 从当前包导入 print_shape 模块
from . import print_shape
# 从.print_shape中导入所有程序单元到fk_package中
from .print_shape import *

# 从当前包导入billing模块
from . import billing
# 从.billing中导入所有程序单元到fk_package中
from .billing import *

# 从当前包中导入 arithmetic_chart 模块
from . import arithmetic_chart
# 从.arithmetic_chart 中导入所有程序单元到fk_package中
from .arithmetic_chart import *


# 该程序的代码基本上差不多，都是通过如下两行代码来处理导入的。
# ＃从当前包中导入 print_shape 模块
# from . import print_shape
# ＃从 . print shape 中导入所有程序单元到 fk_package 中
# from .print_shape import *

# 上面第 一行 from...import 用于 导入当 前包（模块） 中的 print_shape （模块) ， 这样即可在
# tk_package 中使用 print_shape模块 。 但这种导入方式是将 print_shape 模块导入了 fk_package 包中，
# 因此当其他程序使用 print_shape 内的成员 时， 依然需要通过 fk_package.print_shape 前缀进行调用 。
# 第二行导入语句用于将print_shape 模块内的所有程序单元导入 fk_package 模块中，这样以后只要
# 使用 fk_package.前缀就可以使用三个模块内的程序单元。


