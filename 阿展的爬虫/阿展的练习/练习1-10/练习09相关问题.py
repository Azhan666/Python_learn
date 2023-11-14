# # !/usr/bin/env python
# # -*- coding: utf-8 -*-

# 1.通过jsonpath提取英雄id的问题：

# 为什么要用jsonpath
#
# 就跟为什么要用xpath一样，jsonpath的设计灵感来源于xpath。一个强大的json数据提取工具。让用户不用编写脚本就可以提取到相应的json数据。
#
# jsonpath的语法
#
# jsonpath可以什么这两种模式来检索数据：
#
# 以点为分隔
#
# $.store.book[0].title
#
# $.store.book[0,1] #可以取到第一个和第二个book值
#
# $.store.book[*].title #可以取到所的的book值
#
# 以中括号为分隔
#
# $['store']['book'][0]['title']
#
# 对于输入.路径，内中路径将始终使用更通用的中括号模式。 (我猜是因为jsonpath在python中是dict，访问方式刚好是用中括号)
#
# 还支持[start:end:step]模式
#
# "$.store.book[0:3:2].title" #和python中的range步长计算是一致的
#
# @符号表达式：即可以用来代表长度，也可以用来代表name。
#
# $.store.book[(@.length-1)].title #取到最后一个book的title
#
# $.store.book[?(@.price < 10)].title #取到价格小于10的书的title
#
# jsonpath的xpath的语法比较：
#
# XPath
#
# JSONPath
#
# 描述
#
# /
#
# $
#
# 根节点
#
# .
#
# @
#
# 现行节点
#
# /
#
# .or[]
#
# 取子节点
#
# ..
#
# n/a
#
# 取父节点，Jsonpath未支持
#
# //
#
# ..
#
# 就是不管位置，选择所有符合条件的条件
#
# *
#
# *
#
# 匹配所有元素节点
#
# @
#
# n/a
#
# 根据属性访问，Json不支持，因为Json是个Key-value（键值对）递归结构，不需要属性访问。
#
# []
#
# []
#
# 迭代器标示(可以在里边做简单的迭代操作，如数组下标，根据内容选值等)
#
# |
#
# [,]
#
# 支持迭代器中做多选。
#
# []
#
# ?()
#
# 支持过滤操作.
#
# n/a
#
# ()
#
# 支持表达式计算
#
# ()
#
# n/a
#
# 分组，JsonPath不支持
#
# jsonPath的使用示例
#
# ----------------
#
# from jsonpath import jsonpath
#
# data = {...} #这个数据是下面的example data
#
# print(jsonpath(data, "$.store.book[0:3:2].title")) #按步长取，到第1个和第3本书的titile
#
# print(jsonpath(data, "$.store.book[0:2:2].title")) #按步长取到第1本书的titile
#
# print(jsonpath(data, "$.store.book[?(@.price < 10)].title")) #取价格小于10的书的title
#
# print(jsonpath(data, "$..store.book[(@.length -1)].title")) #取最后一本书的title
#
# ----------------
#
# example data:
#
# ----------------
#
# { "store": { "book": [ { "category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95 }, { "category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99 }, { "category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "isbn": "0-553-21311-3", "price": 8.99 }, { "category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings", "isbn": "0-395-19395-8", "price": 22.99 } ], "bicycle": { "color": "red", "price": 19.95 } } }
# ————————————————


# ==================================================================================================================================================================================

# 2.python文件操作a+的问题：

# python文件读写a+_python 文件读写模式r,r+,w,w+,a,a+的区别：

# 模式     可做操作     若文件不存在     是否覆盖
#
# r 　　   只能读           报错    　　　　　 -
#
# r+    　 可读可写        报错     　　　　   是
#
# w     　 只能写           创建     　　　　   是
#
# w+　    可读可写        创建　　　　　　是
#
# a　　   只能写           创建     　　 否，追加写
#
# a+        可读可写        创建     　　否，追加写
#
# 1.只读模式(r)一个存在的文件：
#
# def file_operation():
#
# with open('/wzd/test.txt', mode='r') as f:
#
# # f.write('abc')
#
# r = f.readlines()
#
# print r
#
# print '---done---'
#
# file_operation()
#
# 2.只读模式(r)一个不存在的文件：
#
# def file_operation():
#
# with open('/wzd/test001.txt', mode='r') as f:
#
# # f.write('abc')
#
# r = f.readlines()
#
# print r
#
# print '---done---'
#
# file_operation()
#
# 3.只读模式去写文件：
#
# def file_operation():
#
# with open('/wzd/test.txt', mode='r') as f:
#
# f.write('abc')
#
# r = f.readlines()
#
# print r
#
# print '---done---'
#
# file_operation()

