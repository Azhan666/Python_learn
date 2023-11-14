# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# len()函数也是初学者接触最早、最容易记住的函数之一，len是length的缩写。该函数用于返回列
# 表、元组、字典、字符串等可迭代对象的长度（或称为元素数量）。至于什么是可迭代对象，初学者
# 暂时可以不用深究，随着学习的深入会逐步理解的。

# 以下代码演示了len()函数的用法。

len('asdf34g')
print(len('asdf34g'))

len([3,4,5])
print(len([3,4,5]))

len({'x':1,'y':2})
print(len({'x':1,'y':2}))

len(range(5))
print(range(5))