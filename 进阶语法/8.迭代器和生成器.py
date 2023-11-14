# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 2.2.8 迭代器和生成器

# 写在前面：
# 迭代器（iterator）是一种可遍历元素的对象，这样遍历只能从第一个元素开始，逐一向后直至结束，
# 不能后退，也不能跳过未遍历的元素。Python的内置函数iter()可以将列表、字典等可迭代对象转为
# 迭代器。内置函数next()可以取得迭代器的下一个元素，每调用一次，就会返回下一个元素；若迭代
# 器已空，则返回一个StopIteration类型的异常，其代码如下：

# it = iter([1,2])
# next(it)           # it:信息技术(Information Technology) 意大利 计算机
# print(next(it))
# 2 # 遍历到2

#next(it)
#print(next(it))    # 迭代器已空,返回一个StopIteration类型的异常

# *********************************我是分割线***************************************

# 写在前面：
# 生成器（generator）是一种特殊的迭代器，通过生成器函数产生。生成器函数看上去类似普通函数，
# 但是用yield代替了return。和return返回结果后结束函数不同，yield返回一个结果，但不会结束
# 函数，而是将函数挂起，等待下一次的迭代。

# 下面用一个简单的例子演示一个生成器的应用场景，假如要写一个函数，返回从0到正整数n的所有整
# 数的平方，一般情况下代码写法如下：

# def get_square(n):  # square:平方 正方形 广场
#     result = list() # 结果为列表形式
#     for i in range(n):
#         result.append(pow(i,2)) # 在列表添加i的平方 # pow():计算平方函数
#         # 计算i的2次方
#     return result
#
# print(get_square(5))
# [0, 1, 4, 9, 16]
# 但是，如果计算1亿以内的所有整数的平方，这个函数将返回长度为1亿的数组，且后面元素的数值接
# 近10的16次方，内存消耗巨大。这种情况下，生成器就可以“大显身手”了。

def get_square(n):
    for i in range(n):
        yield(pow(i,2))

grator = get_square(100)
for i in grator:
    print(i, end=',')

