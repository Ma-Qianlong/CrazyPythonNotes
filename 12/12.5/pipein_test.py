#!/usr/bin/env python

# -*- *************** -*-
# @File  : pipein_test.py
# @Description : 
# @Author: mql
# @Time  : 2020-06-22 17:57
# -*- *************** -*-

#下面的 Python 程序用于读取 sys.stdin 的输入，并通过正则表达式识别其中包含多少个 E-mail地址。

import sys
import re

# 定义匹配E-mail的正则表达式
# 由r开头引起的字符串就是声明了后面引号里的东西是原始字符串，在里面放任何字符都表示该字符的原始含义。
mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+'\
    + '[\.][a-z]{2,3}([\.][a-z]{2})?'

# 读取标准输入
text = sys.stdin.read()  ### 这是粗体字
# 使用正则表达式执行查找
it = re.finditer(mailPattern, text, re.I)
# 输出所有电子邮件的地址
for e in it:
    print(str(e.span()) + "--->" + e.group())

# 上面程序中粗体字代码使用 sys.stdin 来读取标准输入的内容， 并使用正则表达式匹配所读取字
# 符串中的E-mail 地址。
# 如果程序使用管道输入的方式，就可以把前一个命令的输出当成 pipein——test.py 这个程序的输
# 入 。 例如使用如下命令 。
#   type ad.txt | python pipein_test .py
# 上面的管道命令由两个命令组成 。
# >> type ad.txt ： 该命令使用 type 读取 a d.txt 文件的内容，并将文件内容输出到控制台。但由于
# 使用了管道，因此该命令的输出会传给下一个命令 。
# >> python pipein test.py ： 该命令使用 python 执行 pipein_test.py 程序。由于该命令前面有管道 ，
# 因此它会把前一个命令的输出当成输入 。

# 运行上面的 type ad.txt | python pipein_test.py 命令， pipein_test.py 程序将会把 ad.txt 文件的内容
# 作为标准输入 。