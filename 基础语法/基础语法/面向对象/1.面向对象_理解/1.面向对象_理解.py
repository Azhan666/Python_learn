# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""一.对面向对象的理解

    1.面向对象的编程---object oriented programming

简称：OOP，是一种编程的思想。OOP把对象当成一个程序的基本单元，一个对象包含了数据和
操作数据的函数。面向对象的出现极大的提高了编程的效率，使其编程的重用性增高。
"""
""" 2.面向对象的重要术语
      1.多态（polymorphism）：一个函数有多种表现形式，调用一个方法有多种形式，
但是表现出的方法是不一样的，这就是“多态”
      2.继承（inheritance）：子项继承父项的某些功能，在程序中表现某种联系
      3.封装（encapsulation）：把重用的函数或功能封装，方便其它程序直接调用
      4.类：对具有相同数据或方法的一组对象的集合
      5.对象：对象是一个类的具体实例
      6.实例化：是一个对象实例化的具体实现
      7.标识：每一个对象的实例都需要一个可以唯一标识这个实例的标记
      8.实例属性：一个对象就是一组属性的集合
      9.实例方法：所有存储或更新某个实例一条或多条属性函数的集合
      10.类属性：属于一个类中所有对象的属性
      11.类方法：那些无须特定的对性实例就能够工作的从属于类的函数。
                Python 类方法和实例方法相似，它最少也要包含一个参数，只不过类方法中
通常将其命名为 cls，Python 会自动将类本身绑定给 cls 参数（注意，绑定的不是类对象）。
也就是说，我们在调用类方法时，无需显式为 cls 参数传参。
和 self 一样，cls 参数的命名也不是规定的（可以随意命名），只是 Python 程序员约定俗
称的习惯而已。
"""
# 类方法举例：
# class CLanguage:
#     #类构造方法，也属于实例方法
#     def __init__(self):
#         self.name = "www.csdncsdn"
#         self.add = "https://.net"
#     #下面定义了一个类方法
#     @classmethod
#     def info(cls):
#         print("正在调用类方法",cls)
# # 注意，如果没有 ＠classmethod，则 Python 解释器会将 fly() 方法认定为实例方法，
# # 而不是类方法。
# # 类方法推荐使用类名直接调用，当然也可以使用实例对象来调用（不推荐）。例如，在上面 CLanguage 类的基础上，在该类外部添加如下代码：
#
# #使用类名直接调用类方法：
# CLanguage.info()
# #使用类对象调用类方法：
# clang = CLanguage()
# clang.info()

# 运行结果为：
# 正在调用类方法 <class '__main__.CLanguage'>
# 正在调用类方法 <class '__main__.CLanguage'>

"""Python类静态方法
# 静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间
（类命名空间）中，而函数则定义在程序所在的空间（全局命名空间）中。

# 静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数
做任何类或对象的绑定。也正因为如此，类的静态方法中无法调用任何类属性和类方法。

# 静态方法需要使用＠staticmethod修饰，例如："""
# class CLanguage:
#     @staticmethod
#     def info(name,add):
#         print(name,add)
# """""""# 静态方法的调用，既可以使用类名，也可以使用类对象，例如："""
# #使用类名直接调用静态方法：
# CLanguage.info("C语言中文网","http://c.biancheng.net")
# #使用类对象调用静态方法：
# clang = CLanguage()
# clang.info("Python教程","http://c.biancheng.net/python")
# 运行结果为：
# C语言中文网 http://c.biancheng.net
# Python教程 http://c.biancheng.net/python

""" 在实际编程中，几乎不会用到类方法和静态方法，因为我们完全可以使用函数代替它们实现
想要的功能，但在一些特殊的场景中（例如工厂模式中），使用类方法和静态方法也是很不错的
选择。"""

"""3、函数和面向对象编程的区别:
　　相同点：都是把程序进行封装、方便重复利用，提高效率。

　　不同点：函数重点是用于整体调用，一般用于一段不可更改的程序。仅仅是解决代码重用性
的问题。

　　而面向对象除了代码重用性。还包括继承、多态等。使用上更加灵活。
"""

"""二、封装、继承、多态

    1、封装（Encapsulation）
    封装，顾名思义就是将内容封装到某个地方，以后再去调用被封装在某处的内容。 
对于面向对象的封装，其实就是使用构造方法，将内容封装到 对象 中，然后通过对象
直接或self.间接获取被封装的内容。
"""
# demo：

# class Foo: # (出于四分之一程序员之间的“默契”，我也来个Foo变量名(类名)，哈哈！)
#     def __init__(self,name, age, gender): # 初始化可不能少，面向对象的灵魂。
#         self.name = name # 开启self.无限调用变量模式。
#         self.age  = age
#         self.gender = gender
#         # 现在把我们所需要的变量名都调用完了，下面我们来给它“技能”。
#
#     def eat(self): # 定义技能函数1：eat，从小就是干饭人哈哈。
#         print("%s,%s岁,%s,干奶"%(self.name, self.age, self.gender))
#     def he(self): # 从小就要养成多喝水的好习惯。
#         print("%s,%s岁,%s,喝水"%(self.name,self.age,self.gender))
#     def shui(self): # 睡觉很重要，我也想晚上多睡会儿，打个哈欠，困了哈哈。
#         print("%s,%s岁,%s,睡觉"%(self.name,self.age,self.gender))
#         # 就这些吧，小孩子不用一生下来就会太多，后天学习很重要。
#
# """ 好了，上面的这些其实就是我们的封装过程，我们把小宝宝的天生技能封装在一起，
# 下面小宝宝出生的时候就可以直接给他们“赋天赋点”，就是直接拿取它，便于使用。
# """
# # 两位小宝贝呱呱坠地啦：
# # 男宝宝a：
# a = Foo('jack',1,'男') # 传入宝宝信息参数
# # 给男宝宝拿技能（“变量名.技能”）：
# a.eat()
# a.he()
# a.shui()
#
# b = Foo('lisa',1,'女')
# # 给女宝宝拿技能（“变量名.技能”）：
# b.eat()
# b.he()
# b.shui()

"""2、继承（Inheritance）
    继承，面向对象中的继承和现实生活中的继承相同，即：子可以继承父的内容。

例如：
猫可以：喵喵叫、吃、喝、拉、撒

狗可以：汪汪叫、吃、喝、拉、撒

公共的部分就是 吃、喝、拉、撒

如下实现:"""

class Animal: # 定义动物类

    def eat(self): # 定义动物技能函数
        print("%s 吃"%(self.name)) # self.name(传入了参数name，使用name调用这个技能函数)
    def drink(self):
        print("%s 喝"%(self.name))
    def shit(self):
        print("%s 拉"%(self.name))
    def pee(self):
        print("%s 撒"%(self.name))

class Cat(Animal):# 子类1
    def __init__(self,name): # 使用构造方法（初始化新创建对象的状态）
        self.name = name
        self.breed = '猫' # (breed:种类)
    def cry(self):
        print('喵喵叫')

class Dog(Animal): # 子类2
    def __init__(self,name):
        self.name = name
        self.breed = '狗'
    def cry(self):
        print('汪汪叫')

c1 = Cat('猫one')
c1.eat()

c2 = Cat('猫two')
c2.drink()

d1 = Dog('狗one')
d1.shit()








