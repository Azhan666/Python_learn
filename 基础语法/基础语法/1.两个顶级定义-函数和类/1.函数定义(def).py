# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：和所有编程语言一样，Python的函数既可以有参数，也可以无参数；既可以有返回值，
# 也可以无返回值。关键字def用来定义一个函数，使用关键字return返回函数结果（如果需要）。
# 以下是两个函数定义的示例：

def say_hello(): # 函数可以没有参数
    print('hello')

say_hello() # 调用函数say_hello

def adder(x, y): # 函数有两个参数
    return x + y # 使用关键字return返回结果

adder(3, 4) #调用函数adder

# 因为Python3中返回值需要手动取出，所以在此要加上取出操作。
a = adder(3, 4)
print(a)