# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 元组（tuple）可以理解为限制版的列表，也是元素的有序集合，但这个集合一旦创建，就不允许增加、
# 删除和修改元素。通常元组用于表示特定的概念，如坐标、矩形区域等。

a = (3,4)
a = tuple([3,4])
a.count(3)
print(a.count(3))

a.index(3)
print(a.index(3))