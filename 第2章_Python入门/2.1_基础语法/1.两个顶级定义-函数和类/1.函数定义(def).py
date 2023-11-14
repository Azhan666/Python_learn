# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：和所有编程语言一样，Python的函数既可以有参数，也可以无参数；既可以有返回值，
# 也可以无返回值。关键字def用来定义一个函数，使用关键字return返回函数结果（如果需要）。
# 以下是两个函数定义的示例：

# def say_hello(): # 函数可以没有参数
#     print('hello')
#
# say_hello() # 调用函数say_hello()
#
# def adder(x, y): # 函数有两个参数
#     return x + y # 使用关键字return返回结果
#
# adder(3, 4) #调用函数adder()

# 因为Python3中返回值需要手动取出，所以在此要加上取出操作。
# a = adder(3, 4)
# print(a)
# 或者这样：
# print(adder(3, 4))

""" 以上代码定义了两个参数，say_hello()函数没有参数，也没有返回值，adder()函数有两个参数，
返回值是两个参数的和，需要注意的是，定义和调用函数时，即使没有参数，函数名后面的圆括号也不能省略。
"""

# 有了上面的example，我们来自己定义一些函数：

def eat_meal(): # meal:饭 定义了函数
    print('eat')

    eat_meal() # 调用函数

def multiplication(x, y): # multiplication:乘，乘法 # 定义一个乘法，传入两个待乘参数

    return x * y

multiplication(3, 4) # 调用乘法函数传入实参
print(multiplication(3, 4))
12
"""ok,我们已经学会了函数的定义和调用！"""

""" Python的函数参数非常有特色，除了常规的参数之外，还支持默认参数、可变参数和关键字参数。
关于函数参数的更多知识，详见本书2.2.1小节。"""

