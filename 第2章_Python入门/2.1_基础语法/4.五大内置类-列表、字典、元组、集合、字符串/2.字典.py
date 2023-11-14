# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 字典（dict）也是Python语言最强大的工具之一。字典的本质是无序的键值对，字典类封装了很多
# 有用的方法，用起来非常顺手。

# d = dict() # 虽然可以写成 d = {}, 但是我更喜欢这样写，就像我更喜欢你一样
# d = dict(a=1,b=2)
# print(d)
# {'a': 1, 'b': 2} 字典形式，即键值对

# d = dict([('a',1),('b',2)])
# print(d)
# {'a': 1, 'b': 2} # 也可以直接指定键值对
#
# d.update({'c':3}) # 用赋值语句也可以插入和更新字典，但不如这样写优雅
# print(d)
#
# d.pop('c') # 删除元素
# print(d)
#
# list(d.items()) # items：项目、记录
# [('a',1),('b',2)]
# list(d.keys()) # 键
# ['a','b']
# list(d.values()) # 值
# [1,2]
# for key in d: # 遍历字典的标准写法
#     print(key,d[key])
#
# dict.fromkeys('xyz',0) # fromkeys是字典类的静态方法，实例也可以调用
#                        # fromkeys：生成一个字典|方法|快速创建字典
# print(dict.fromkeys('xyz',0))
# {'x': 0, 'y': 0, 'z': 0}
# Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有
# 键对应的初始值。记住是“所有键”
# fromkeys()方法语法：
# dict.fromkeys(seq[, value])
# seq -- 字典键值列表。
# value -- 可选参数, 设置键序列（seq）的值。
# 返回值：
# 该方法返回一个新字典。
# 关于fromkeys：https://www.runoob.com/python/att-dictionary-fromkeys.html

"""我们依照教程写一个fromkeys的example："""
# seq = ('丢掉','幻想','准备','斗争')
# dict = dict.fromkeys(seq)
# print("新字典为：%s"%str(dict))
# # 新字典为：{'丢掉': None, '幻想': None, '准备': None, '斗争': None}
# dict = dict.fromkeys(seq[:3]) # 列表切片，从0到3
# print("新字典为：%s"%str(dict))
# 新字典为：{'丢掉': None, '幻想': None, '准备': None}

# dict = {} # 创建一个空字典
#
# # print(dict.fromkeys('123',1))
# print(dict.fromkeys((1,2,3),'number'))
# # {1: 'number', 2: 'number', 3: 'number'}
# print(dict)
# {}

"""为什么会出现dict还是空字典呢？
    这是因为fromkeys 方法只用来创建新字典，不负责保存。当通过一个字典来调用 fromkeys 方法时，
如果需要后续使用一定记得给他复制给其他的变量。"""

# 复制给其他变量即可解决：
# dict_2 = dict.fromkeys((1,2,3),'number')
# print(dict_2)
# {1: 'number', 2: 'number', 3: 'number'}

