#!/usr/bin/env python

# -*- *************** -*-
# @File  : return_self.py
# @Description : 
# @Author: mql
# @Time  : 2020/1/15 14:12
# -*- *************** -*-


#  当 self 参数作为对象的默认引用时，程序可 以像访问普通变量一样来访 问这个 self 参数，
#  甚至可以把 self 参数当成实例方法的返回值。

class ReturnSelf:
    def grow(self):
        if hasattr(self, 'age'):
            self.age += 1
        else:
            self.age = 1

        # return self 返回调用该方法的对象
        return self


rs = ReturnSelf()
# 可以连续调用向一个方法
rs.grow().grow().grow()
print('rs的age属性值是：', rs.age)

# 从上面程序中可以看出，如果在某个方法中把 self 参数作为返回值 ，则可以多次连续调用同一
# 个方法，从而使得代码更加简洁。但是这种把 self 参数作为返回值的方法可能会造成实际意义的模
# 糊，例如上面的 grow 方法用于表示对象的生长，即 age 属性的值加 1 ， 实际上不应该有返回值 。

# ###注意：使用 self 参数作为方法的返回值可以让代码更加简洁，但可能造成实际意义的模糊。
