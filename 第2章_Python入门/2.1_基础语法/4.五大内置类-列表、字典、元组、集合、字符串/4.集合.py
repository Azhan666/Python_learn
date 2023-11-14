# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 集合（set）有两个特点，一是集合内元素具有唯一性，二是集合内元素无序排列。在学习的初级阶段
# 使用集合的机会不多，但有一个经常使用的经典用法，它最能体现集合的价值，那就是去除列表内重复
# 的元素。

a = set()
a.update({'x','y','z'})
print(a)

a.remove('z')
print(a)

a.add('w')
print(a)

a = {'A','D','B'}
b = {'D','E','C'}
a.difference(b) # 返回a有b没有的元素集合 difference：差异，不同
print(a.difference(b))
a - b # 记不住的话，这样写也行
print((a - b))

a.union(b) # 返回a和b的并集。虽然差集也可以用a-b替代，但并集不能用a+b表示
print(a.union(b))  # union:联合 |并集 |联邦

a.intersection(b) # 返回a和b重复元素的集合  intersection:交集 |十字路口 |交叉点
print(a.intersection(b))

a.symmetric_difference(b) # 返回a和b非重复元素的集合
print(a.symmetric_difference(b)) # symmetric_difference:对称差分

list(set([1,2,5,2,3,4,5,'x',4,'x'])) # 去除数组[1,2,5,2,3,4,5,'x',4,'x']中的重复元素
print(list(set([1,2,5,2,3,4,5,'x',4,'x']))) # 因为集合内元素具有唯一性



