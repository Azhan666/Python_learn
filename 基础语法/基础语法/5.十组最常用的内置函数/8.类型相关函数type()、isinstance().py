# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 对于初学者来说，运行代码时出现问题是最头疼的事情，因为根本不知道发生了什么，又该从何处入手
# 来解决问题。如果不是缩进或找不到模块这类初级错误，那么查看变量的类型，也许是最值得一试的
# 调试方法。type()函数是用于查看对象类型的函数。

type(5)
print(type(5))

type('ssdf')
print(type('ssdf'))

type([])
print(type([]))

type(print)
print(type(print))

type(range(5))
print((type(range(5))))

# 很多初学者在了解了type()函数后，喜欢用它来做类型判断，这是不正确的。用于类型判断的是
# isinstance()函数。

a = [3,4,5]
b = ['x','y']
c = dict()
d = 'python'
isinstance(a,list)
print(isinstance(a,list))

isinstance(b,list)
print(isinstance(b,list))

isinstance(c,(dict,str))
print(isinstance(c,(dict,str)))

isinstance(d,(dict,str))
print(isinstance(d,(dict,str)))

isinstance(b,(dict,str))
print(isinstance(b,(dict,str)))

