# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面:
# 抽象类不能被实例化，只能作为父类被其他类继承，且派生类必须实现抽象类中所有的成员函数。
# 抽象类的应用场景是什么呢？我曾经做过很多下载数据的脚本插件，针对不同的数据源使用不同的
# 脚本，而这些脚本的使用必须保持相同的API（Application Programming Interface,应用程序接口）
# ，即每个脚本定义的下载类的成员必须使用相同的名字，此时抽象类就派上用场了。

# Python的内置模块abc是专门用来定义抽象类的，该模块提供了名为abstractmethod的装饰器函数，
# 绑定在抽象类的每一个成员函数上。如果派生类没有重写抽象类的成员函数，实例化派生类时将会抛出
# 异常。

import abc

class A(object, metaclass=abc.ABCMeta): # 定义抽象类，定义了两个成员函数
    @abc.abstractmethod
    def f1(self):
        pass
    @abc.abstractmethod
    def f2(self):
        pass

class B(A): #继承抽象类，重写了两个成员函数
    def f1(self):
        print('重写f1')
    def f2(self):
        print('重写f2')

class C(A): #继承抽象类，只重写了一个成员函数
    def f1(self):
        print('重写f1')

b = B()
c = C()

# 以上代码定义了一个抽象类A，并以A为基类，派生了B类和C类。其中B类重写了A类的全部方法，
# C类仅重写了A类的一个方法。实例化B类时没有问题，但实例化C类时抛出了异常。

