#!/usr/bin/env python

# -*- *************** -*-
# @File  : for_expr.py.py
# @Description : for 表达式
# @Author: mql
# @Time  : 2020/1/3 9:56
# -*- *************** -*-


# for 表达式用于利用其他区间、元组、列表等可迭代对象创建新的列表。
# for 表达式的语法格式如下：
# ［表达式 for 循环计数器且可法代对象］


a_range = range(10)
# 对 a_range 执行 for 表达式
a_list = [x * x for x in a_range]
print(a_list)

# 还可以在 for 表达式后面添加 if 条件，这样 for 表达式将只迭代那些符合条件的元素。例如:
b_list = [x * x for x in a_range if x % 2 == 0]
print(b_list)

# 如果将 for 表达式的方括号改为圆括号， for 表达式将不再生成列表，而是生成一个生成器
# (generator），该生成器同样可使用 for 循环选代。
# 对于使用圆括号的 for 表达式，它最终返回的是生成器，因此这种 for 表达式也被称为生成器
# 推导式。例如如下代码。

# 使用for表达式创建生成器
c_generator = (x * x for x in a_range if x % 2 == 0)
print(c_generator)
# 用for循环迭代生成器
for i in c_generator:
    print(i, end='\t')
print()

print()
# 在前面看到的 for 表达式都只有一个循环，实际上 for 表达式可使用多个循环，就像嵌套循环
# 一样。例如如下代码。
d_list = [(x, y) for x in range(5) for y in range(4)]
print(d_list)

# 上面的 for 表达式相当于如下嵌套循环 。
dd_list = []
for x in range(5):
    for y in range(4):
        dd_list.append((x, y))
print(dd_list)

# 当然，也支持类似于三层嵌套的 for 表达式，例如如下代码。
e_list = [[x, y, z] for x in range(5) for y in range(4) for z in range(6)]
print(e_list)

print()
# 对于包含多个循环的 for 表达式，同样可指定 if 条件。假如我们有一个需求：程序要将两个列
# 表中的数值按“能否整除”的关系配对在一起。比如 src_a 列表中包含 30, src_b 列表中包含 5,
# 其中 30 可以整除 5 ，那么就将 30 和 5 配对在一起 。 对于上面的需求使用 for 表达式来实现非常简
# 单，例如如下代码。
src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b = [3, 5, 7, 11]
# 只要 y 能整除 x，就将它们配对在一起
result = [(x, y) for x in src_b for y in src_a if y % x == 0]
print(result)
