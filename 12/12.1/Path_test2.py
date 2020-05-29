#!/usr/bin/env python

# -*- *************** -*-
# @File  : Path_test2.py
# @Description : 
# @Author: mql
# @Time  : 2020-05-26 15:01
# -*- *************** -*-


from pathlib import *

p = Path('a_test.txt')
# 指定以 GBK 字符集输出文本内容
result = p.write_text('''有一个美丽的新世界
它在远方等我
那里有天真的孩子
还有姑娘的酒窝''', encoding='GBK')
# 返回输出的字符数
print(result)

# 指定以GBK字符集读取文本内容
content = p.read_text(encoding='GBK')
# 输出所读取的文本内容
print(content)

# 读取字节内容
bb = p.read_bytes()
print(bb)
 