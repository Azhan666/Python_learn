# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 2.3.3 静态变量和实例变量
# 写在前面：
# 类的成员变量分为两种：静态变量和实例变量
# 静态变量一般定义在类的开始位置，独立于构造函数。静态变量既可以用<对象名.变量名>的方式访问，
# 也可以用<类名.变量名>的方式访问。通常，类的静态变量用于保存类的静态属性，该属性可被类的方
# 法使用，但不应该被类的方法修改。

# 在构造函数中定义的变量称为实例变量。实例变量只能在实例化后使用<对象名.变量名>的方式访问，
# 不能使用<类名.变量名>的方式访问。

class A:
    static_x = 10 # 静态变量
    def __init__(self): # 定义构造函数
        self.instance_y = 5 # 实例变量

a = A() # 实例化
a.static_x # 使用实例名a访问静态变量
print(a.static_x)

a.instance_y # 使用实例名a访问实例变量
print(a.instance_y)

A.static_x # 使用类名名A访问静态变量
print(A.static_x)

A.instance_y # 使用类名名A访问实例变量
print(A.instance_y)