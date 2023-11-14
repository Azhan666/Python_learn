# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 有人说Python是强类型语言，也有人不认同这个观点。关于这一点，我们姑且不论。但在逻辑层面和
# 操作层面上，还是很有必要讲一讲数据类型的，因为Python要处理的数据是分类型的。Python将数据
# 分为整型、浮点型、布尔型和字符串这四种类型，并提供了int类、float类、bool类和str类这四个
# 内置类与之对应。这也体现了Python“万物皆对象”的特点。下面的代码生成了四种类型的数据对象，
# 使用type()函数可以看到它们各自的类名。

# i, f, b, s = 5, 3.14, True, 'xyz'
# type(i), type(f), type(b), type(s)
#
# print(type(i),type(f),type(b),type(s))

# **************************************我是分割线***********************************

# 写在前面：
# 整型数据就是数学上的整数，包括正整数、负整数和零。Python的整型不像C语言和C++语言那样分了长
# 短很多种，几乎不用担心整数超过系统限制。下面这个计算阶乘的函数，很容易就算出了100的阶乘，其
# 结果位数长达158位。

def factorial(n): # factorial:阶乘
    if n == 0: # 出口条件
        return 1
    return n*factorial(n-1) # 返回n的阶乘 因为factorial()参数为n
factorial(100) # 调用已定义的函数
# 因为Python3中返回值需要手动取出，所以在此要加上取出操作。
# a = factorial(100)
# print(a)

# 或者这样：
print(factorial(100)) # 计算100的阶乘