# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 很多人是在学习for循环时认识range()函数的。range()函数可以返回一个整数序列，只是无法看到
# 这个序列的全貌，也不能访问其中的某个元素，只能从头开始依次遍历每一个元素。range()函数可以
# 接受一个、两个或三个整型参数。

# 以下代码演示了range()函数的用法。

type(range(5))
print(type(range(5)))

for i in range(5): # 默认从0开始，步长为1
    print(i,end=',')

for i in range(5,10): # 在[5,10]区间内生成序列，步长为1
    print(i,end=',')

for i in range(5,10,2): # 在[5,10]区间生成序列，步长为2
    print(i,end=',')

list(range(5)) # 将range类转成list类
print(list(range(5)))

