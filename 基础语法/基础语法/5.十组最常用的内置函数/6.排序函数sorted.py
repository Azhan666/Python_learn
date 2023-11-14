# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 排序是比较常见的需求。排序函数sorted()不会改变被排序列表的数据结构，而是返回一个新的排序
# 结果。这一点和列表对象的sort()方法不同。列表对象的sort()方法改变了列表自身，且无返回值。

# 以下代码演示了sorted()函数的用法，其中用到了lambda函数。关于lambda函数，Python高手修炼
# 之道2.27小节有详细讲解。

sorted([3,2,7,1,5]) # 一维列表排序
print(sorted([3,2,7,1,5]))

sorted([3,2,7,1,5], reverse=True) # 一维列表排序,逆序输出
print(sorted([3,2,7,1,5], reverse=True))  # reverse:v. 颠倒；撤销；反转；

a = [[6,5],[3,7],[2,8]]
sorted(a,key=lambda x:x[0]) # 根据每一行的首元素排序
print(sorted(a,key=lambda x:x[0]))

sorted(a,key=lambda x:x[-1]) # 根据每一行的尾元素排序
print(sorted(a,key=lambda x:x[-1]))

a = [{'name':'C', 'age':18},{'name':'A', 'age':20},{'name':'B', 'age':19}]
sorted(a,key=lambda x:x['name']) # 根据name键排序
print(sorted(a,key=lambda x:x['name']))

sorted(sorted(a,key=lambda x:x['age'])) # 根据age键排序
print(sorted(a,key=lambda x:x['age']))