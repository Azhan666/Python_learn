# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 遍历列表、字符串等可迭代对象时，如果想同时得到元素的索引序号，enumerate()函数就可以派上用
# 场了。因为enumerate()函数会返回可迭代对象的索引和元素组成的元祖的可迭代对象，所以不用担心
# 该函数的效率和资源消耗情况。

for index, item in enumerate([True,False,None]):
    print(index,item,sep='->')
# sep: 默认是空格，表示两个字符串之间用什么分割。eg: 空格  sep="  "
# 类似于：end: 默认是换行，表示两个字符串最后以什么结尾。eg: 换行  end="\n"
# 0->True
# 1->False
# 2->None

for index in enumerate('xyz'):
    print(index,item,sep='->')

# 0->x
# 1->y
# 2->z

# **********************************我是分割线**************************************

# zip()函数可以将两个等长列表的对应元素组合成元组后返回一个迭代器。zip()函数的典型应用场
# 景是同时遍历多个列表。

a = ['x','y','z']
b = [3,4,5]
for k, v in zip(a,b):
    print(k, v, sep='->')

# x->3
# y->4
# z->5

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
#
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
#
# zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
#
# 如果需要了解 Pyhton3 的应用，可以参考 Python3 zip()。
#
# 语法
# zip 语法：
#
# zip([iterable, ...])
# 参数说明：
#
# iterabl -- 一个或多个迭代器;
# 返回值
# 返回元组列表。
#
# 实例
# 以下实例展示了 zip 的使用方法：
#
# >>>a = [1,2,3]
# >>> b = [4,5,6]
# >>> c = [4,5,6,7,8]
# >>> zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]
# Python 内置函数 Python 内置函数

# **********************************我是分割线**************************************

# map()函数可以对列表中的每一个元素做一次计算，这个计算由函数参数指定。这个作为参数的函
# 数既可以是普通的函数，也可以是lambda匿名函数。下面以对列表中各元素开3次方为例演示map
# ()函数的用法。

def extract(x): # 开3次方 extract：提取 抽出 抽取
    return pow(x,1/3)
    p = pow(x,1/3)
    print(p)
result = map(extract, [7,8,9]) # extract()函数对列表元素逐一运算，返回迭代对象
list(result) # 将迭代对象转为list
print(result)

list(map(lambda x:pow(x,1/3), [7,8,9])) # 使用lambda匿名函数更简洁
print(list((map(lambda x:pow(x,1/3), [7,8,9]))))

# pow()
# 方法返回
# xy（x
# 的
# y
# 次方） 的值。
#
# 语法
# 以下是
# math
# 模块
# pow()
# 方法的语法:
#
# import math
#
# math.pow(x, y)
# 内置的
# pow()
# 方法
#
# pow(x, y[, z])
# 函数是计算
# x
# 的
# y
# 次方，如果
# z
# 在存在，则再对结果进行取模，其结果等效于
# pow(x, y) % z。
#
# 注意：pow()
# 通过内置的方法直接调用，内置方法会把参数作为整型，而
# math
# 模块则会把参数转换为
# float。
#
# 参数
# x - - 数值表达式。
# y - - 数值表达式。
# z - - 数值表达式。
# 返回值
# 返回
# xy（x的y次方） 的值。
# 实例
# 以下展示了使用
# pow()
# 方法的实例：
#
# 实例
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import math  # 导入 math 模块
#
# print
# "math.pow(100, 2) : ", math.pow(100, 2)
# # 使用内置，查看输出结果区别
# print
# "pow(100, 2) : ", pow(100, 2)
#
# print
# "math.pow(100, -2) : ", math.pow(100, -2)
# print
# "math.pow(2, 4) : ", math.pow(2, 4)
# print
# "math.pow(3, 0) : ", math.pow(3, 0)
# 以上实例运行后输出结果为：
#
# math.pow(100, 2): 10000.0
# pow(100, 2): 10000
# math.pow(100, -2): 0.0001
# math.pow(2, 4): 16.0
# math.pow(3, 0): 1.0
# Python
# 数字
# Python
# 数字

# **********************************我是分割线**************************************

# chr()函数返回ASCII编码值对应的字符，order()函数返回字符串对应的ASCII编码值，二者是
# 互逆的操作。

chr(65)
print(chr(65))

ord('Z')
print(ord('Z'))

for i in range(26):
    print(chr(65+i), sep='', end='')

# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
#
# 语法
# 以下是 chr() 方法的语法:
#
# chr(i)
# 参数
# i -- 可以是10进制也可以是16进制的形式的数字。
# 返回值
# 返回值是当前整数对应的 ASCII 字符。
#
# 实例
# 以下展示了使用 chr() 方法的实例：
#
# >>>print chr(0x30), chr(0x31), chr(0x61)   # 十六进制
# 0 1 a
# >>> print chr(48), chr(49), chr(97)         # 十进制
# 0 1 a
# Python 内置函数 Python 内置函数




