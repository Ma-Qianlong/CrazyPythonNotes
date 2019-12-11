# 复数

ac1 = 3 + 0.2j
print(ac1)
print(type(ac1))

ac2 = 4 - 0.1j
print(ac2)

# 复数运行
print(ac1 + ac2)

# 导入cmath模块,cmath为Python下的模块，包含了各种支持复数运算的函数
import cmath
# sqrt() 是cmath模块下的函数，用于计算平方根
ac3 = cmath.sqrt(-1)
print(ac3)