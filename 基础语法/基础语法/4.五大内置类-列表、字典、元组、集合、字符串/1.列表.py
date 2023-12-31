# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 列表(list)是元素的有序集合，列表的元素可以是Python语言支持的任意类型。初学者一般习惯用一对
# 方括号([])来创建列表，标准的写法是用list()来实例化list类。列表的方法有很多，可以实现列表末
# 尾追加元素、指定位置插入元素、删除指定元素或指定索引位置的元素、返回元素索引、排列等操作。
# 此外，列表的索引、切片也非常灵活，很多操作都能给人惊喜。

a = list() # 创建一个空列表，可以传入列表、元组、字符串等迭代对象
a.append(3) # 列表尾部追加元素3
a.extend([4,5,7,4,9]) # 列表后接列表[4,5,7,4,9]
print(a)

a.index(9) # 返回列表值指定元素的索引值
print(a.index(9))

a.count(4) # 返回列表中值为4的元素的个数
print(a.count(4))

a.pop(1) # 删除并返回索引序号为1的元素，如果不指定索引，则删除最后一个元素
print(a.pop(1))

#a.remove(4) # 删除列表中最靠前的元素4（无返回）
#print(a.remove(4))

a.sort() # 排序
print(a.sort())

a[-1] # python引入-1做末尾元素的索引
print(a[-1])

a[1:-1] # “掐头去尾”切片
print(a[1:-1])

a[::2] # 从头开始，隔一个取一个元素
print(a[::2])

a[::-1] # 逆序
print(a[::-1])