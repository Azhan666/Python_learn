# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 2.2.4 列表推导式

# 写在前面：
# 列表推导式是Python语言独有的语法特色，可以让代码更加简练。列表推导式在中高级Python程序员的
# 代码中出现频率非常高。例如，求列表各元素的平方，初级程序员的写法一般如下（当然也有其他写法
# ，如使用map()函数）。

# a = [1, 2, 3, 4, 5]
# result = list()
# for i in a:
#     result.append(i*i)
#     result
# print(result)
# #
# # # 如果使用列表推导式，看起来就简单多了，代码如下：
# #
# a = [1, 2, 3, 4, 5]
# [i*i for i in a]
# print([i*i for i in a])
#
# # 列表推导式还可以配合条件语句，实现更复杂的功能。不过请注意，如果条件只有if，必须放在for循
# # 环之后。如果条件类似于三元表达式，则必须置于for循环之前。
#
# [i for i in range(10) if i%2==0]
# print([i for i in range(10) if i%2==0])
#
# [i if i%2==0 else -1*i for i in range(10)]
# print([i if i%2==0 else -1*i for i in range(10)])

# b = [9,8,7,6,5,4,3,2,1]
# result = list()
# for i in b:
#     result.append(i*i)
#     result
# print(result)

# 列表推导式：
# b = [9,8,7,6,5,4,3,2,1]
# [i*i for i in b]
# print([i*i for i in b])
# [81, 64, 49, 36, 25, 16, 9, 4, 1]