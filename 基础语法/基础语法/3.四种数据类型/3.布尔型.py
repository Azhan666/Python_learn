# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# Python语言定义了两个常量True和False，用来表示布尔型的真和假。True表示真、非空、非零等概念，
# False表示假、空、零等概念。

a = bool(0)
b = bool(None)
c = bool('')
d = bool([])
e = bool(5)
f = bool('x')
g = bool([False])
print(a,b,c,d,e,f,g)
