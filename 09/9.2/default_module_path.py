#!/usr/bin/env python

# -*- *************** -*-
# @File  : default_module_path.py
# @Description : 
# @Author: mql
# @Time  : 2020/03/8 22:44
# -*- *************** -*-

import sys, pprint
pprint.pprint(sys.path)

# 上面代码使用 pprint 模块下的 pprint（）函数代替普通的 print（）函数，这是因为如果要打印的内容
# 很多，使用 pprint 可以显示更友好的打印结果。

# 上面的运行结果列出的路径都是 Python 默认的模块加载路径 ，但通常来说，我们应该将 Python
# 的扩展模块添加在 lib\site-packages 路径下 ， 它专 门用 于存放 Python 的扩展模块和包 。


