# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 字典（dict）也是Python语言最强大的工具之一。字典的本质是无序的键值对，字典类封装了很多
# 有用的方法，用起来非常顺手。

d = dict() # 虽然可以写成 d = {}, 但是我更喜欢这样写，就像我更喜欢你一样
d = dict(a=1,b=2)
print(d)

d = dict([('a',1),('b',2)])
print(d)

d.update({'c':3}) # 用赋值语句也可以插入和更新字典，但不如这样写优雅
print(d)

d.pop('c') # 删除元素
print(d)

list(d.items()) # items：项目、记录
[('a',1),('b',2)]
list(d.keys()) # 键
['a','b']
list(d.values()) # 值
[1,2]
for key in d: # 遍历字典的标准写法
    print(key,d[key])

dict.fromkeys('xyz',0) # fromkeys是字典类的静态方法，实例也可以调用
                       # fromkeys：生成一个字典|方法|快速创建字典
print(dict.fromkeys('xyz',0))

