# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 2.2.7 lambda函数

# 写在前面：
# lambda函数听起来很高级，但其实指的就是匿名函数。如果一个函数非常简单，且仅在定义这个函数的地
# 方使用，那就最适合使用匿名函数了。下面是一个求和的匿名函数，有两个输入参数x和y，函数体就是x+y
# ，省略了return关键字。

# lambda x,y: x+y
# print(lambda x,y: x+y)
#
# (lambda x,y: x+y) (3, 4) # 因为匿名函数没有名字，是用的时候要用括号把它括起来
# print((lambda x,y: x+y) (3, 4))
#
# f = lambda x,y: x+y # 也可以给匿名函数取个名字，像普通函数那样进行调用
# f(3, 4)
# print(f(3, 4))

# 一般情况下，以函数为参数的函数，如过滤函数filter()、映射函数map()、排序函数sorted()等，
# 多使用匿名函数做参数。下面的例子使用排序函数sorted()对元素类型为字典的列表进行排序，就
# 使用了lambada函数指定排序规则。

# a = [{'name':'B', 'age':50}, {'name':'A', 'age':30}, {'name':'C', 'age':40}]
# sorted(a, key=lambda x:x['name']) # 按姓名排序
#
# [{'name':'A', 'age':30}, {'name':'B', 'age':50}, {'name':'C', 'age':40}]
# sorted(a, key=lambda x:x['age']) # 按年龄排序
#
# print(sorted(a, key=lambda x:x['name']))
# print(sorted(a, key=lambda x:x['age']))

"""example:"""
f = lambda x,y: x + y
f(1, 2)
print(f(1, 2))
# 3
# or :
p = (lambda x,y: x+y) (3, 4)
print(p)
# 7