# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""我们在学习python类的时候，总会碰见书上的类中有__init__()
这样一个函数，很多同学百思不得其解，其实它就是python的构造方法。
"""
""" 构造方法类似于类似init()
这种初始化方法，来初始化新创建对象的状态，在一个对象呗创建以后会立即调用，比如像实例化一个类：
f = FooBar() # FooBar:程序员常用变量名（类名）表示示例
f.init()
# 使用构造方法就能让它简化成如下形式：
f = FooBar()
你可能还没理解到底什么是构造方法，什么是初始化，下面我们再来举个例子：

class FooBar: # 定义一个示例类
    def __init__(self): # 类的初始化
     self.somevar = 42 # 类属性
f = FooBar()
f.somevar
# 这里调用somevar直接得出42

    我们会发现在初始化FooBar中的somevar的值为42之后，实例化直接就能够调用somevar的值；
如果说你没有用构造方法初始化值得话，就不能够调用，明白了吗？
在明白了构造方法之后，我们来点进阶的问题，那就是构造方法中的初始值无法继承的问题。

例子：
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print
            'Ahahahah'
        else:
            print
            'No thanks!'
            
class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk'
    def sing(self):
        print
        self.song()


sb = SongBird()
sb.sing()  # 能正常输出
sb.eat()  # 报错，因为songgird中没有hungry特性
那解决这个问题的办法有两种：
1、调用未绑定的超类构造方法（多用于旧版python阵营）

class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk'
    def sing(self):
        print
        self.song()

原理：在调用了一个实例的方法时，该方法的self参数会自动绑定到实例上（称为绑定方法）；
如果直接调用类的方法（比如Bird.__init__），那么就没有实例会被绑定，可以自由提供需要的
self参数（未绑定方法）。

2、使用super函数（只在新式类中有用）

class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk'
    def sing(self):
        print
        self.song()

"""
# 原理：它会查找所有的超类，以及超类的超类，直到找到所需的特性为止。

# 注意： 关于多继承 
# - 在Python中，如果父类和子类都重新定义了构造方法init( )，在进行子类实例化的时候，子类的构造
# 方法不会自动调用父类的构造方法，必须在子类中显示调用。 
# - Python的类可以继承多个类，Java和C#中则只能继承一个类 
# - Python的类如果继承了多个类，那么其寻找方法的方式有两种，分别是：深度优先和广度优先 
# - 当类是经典类时，多继承情况下，会按照深度优先方式查找，当类是新式类时，多继承情况下，会按照
# 广度优先方式查找
#
# 经典类和新式类，从字面上可以看出一个老一个新，新的必然包含了跟多的功能，也是之后推荐的写法，
# 从写法上区分的话，如果 当前类或者父类继承了object类，那么该类便是新式类，否则便是经典类。


# 3、多态（Polymorphism）

# 首先Python不支持多态，也不用支持多态，python是一种多态语言，崇尚鸭子类型。
#
# 在程序设计中，鸭子类型（英语：duck
# typing）是动态类型的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定。这个概念的名字来源于由James
# Whitcomb
# Riley提出的鸭子测试，“鸭子测试”可以这样表述： 
# “当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
#
# 在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的。例如，在不使用鸭子类型的语言中，我们可以编写一个函数，它接受一个类型为鸭的对象，并调用它的走和叫方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的走和叫方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。任何拥有这样的正确的走和叫方法的对象都可被函数接受的这种行为引出了以上表述，这种决定类型的方式因此得名。
#
# 鸭子类型通常得益于不测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用。从静态类型语言转向动态类型语言的用户通常试图添加一些静态的（在运行之前的）类型检查，从而影响了鸭子类型的益处和可伸缩性，并约束了语言的动态特性。
#
# 例子：
#
# class A:
#     def prt(self):
#         print
#         "A"
#
#
# class B(A):
#     def prt(self):
#         print
#         "B"
#
#
# class C(A):
#     def prt(self):
#         print
#         "C"
#
#
# class D(A):
#     pass
#
#
# class E:
#     def prt(self):
#         print
#         "E"
#
#
# class F:
#     pass
#
#
# def test(arg):
#     arg.prt()
#
#
# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
# f = F()
#
# test(a)
# test(b)
# test(c)
# test(d)
# test(e)
# test(f)
#
# # 结果
# A
# B
# C
# A
# E
# Traceback(most
# recent
# call
# last):
# File
# "/Users/shikefu678/Documents/Aptana Studio 3 Workspace/demo/demo.py", line
# 33, in < module >
# test(a), test(b), test(c), test(d), test(e), test(f)
# File
# "/Users/shikefu678/Documents/Aptana Studio 3 Workspace/demo/demo.py", line
# 24, in test
# arg.prt()
# AttributeError: F
# instance
# has
# no
# attribute
# 'prt'
# 没有谁规定test方法是接收的参数是什么类型的。test方法只规定，接收一个参数，调用这个参数的prt方法。在运行的时候如果这个参数有prt方法，python就执行，如果没有，python就报错，因为abcde都有prt方法，而f没有，所以得到了上边得结果，这就是python的运行方式。

""" 三、面向对象的各种方法

1、静态方法  (用这个装饰器来表示  @staticmethod  )
意思是把 @staticmethod 下面的函数和所属的类截断了，这个函数就不属于这个类了，没有类的属性了，
只不是还是要通过类名的方式调用  

看个小例子："""

# 错误示例：

# class Person(object): # 定义类
#     def __init__(self,name): # 类初始化
#         self.name = name # 类名变量
#
#     @staticmethod # 把eat方法变为静态变量
#     def eat(self):
#         print("%s is eating"%(self.name))
# d = Person("xiaoming")
# d.eat()

# 结果报错找不到self属性，这是因为@staticmethod把eat()方法与person类割断了，eat方法就没有
# 类的属性了，所以获取不到self.name这个变量

# 正确示例：
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#     @staticmethod
#     def eat(x):
#         print("%s is eating"%(x))
# d = Person("xiaoming")
# d.eat("jack")
# 就把eat方法当作一个独立的变量给他传参就行了
"""2.类方法（用这个装饰器来表示 @classmethod）
    类方法只能访问类变量，不能访问实例变量
看个例子："""
# 错误示例：
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#     @staticmethod
#     def eat(self):
#         print("%s is eating"%(self.name))
# d = Person("xiaoming")
# d.eat()

# 结果报错还是找不到self.name变量，这是因为self.name是通过实例化这个类传递进去的，
# 而类方法是不能访问实例变量的，只能访问类里面定义的变量

# 正确示例：

# class Person(object):
#     name = "杰克"
#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def eat(self):
#         print("%s is eating"%(self.name))
# d = Person("xiaoming")
# d.eat()

"""3.属性方法
    把一个方法变成一个静态属性，属性就不需要再加小括号的那样去调用了
看个例子："""

# 错误示例：
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#     @property
#     def eat(self):
#         print("%s is eating"%(self.name))
# d = Person("xiaoming")
# d.eat()
# 错误原因：此时eat已经变成一个属性了，不是一个方法了，调用它就把不需要括号了，直接变量名.调用即可

# 正确示例：

# class Person(object):
#     def __init__(self,name):
#         self.name = name
#     @property
#     def eat(self):
#         print("%s is eating"%(self.name))
# d = Person("xiaoming")
# d.eat

"""四、高级面向对象
    1、成员修饰符
    python的类中只有私有成员和公有成员两种，不像c++中的类有公有成员（public），私有成员
(private)和保护成员(protected).并且python中没有关键字去修饰成员，默认python中所有的成员都是
公有成员，但是私有成员是以两个下划线开头的名字标示私有成员，私有成员不允许直接访问，只能通过内
部方法去访问，私有成员也不允许被继承。
"""
# 光说不行，来，吃个栗子：

# class a: # 说明父类的私有成员无法在子类中继承
#     def __init__(self):
#         self.ge = 123
#         self.__gene = 256
# class b(a):
#     def __init__(self,name):
#         self.name = name
#         self.__age = 18
#         super(b,self).__init__() # 这一行会报错
#     def show(self):
#         print(self.name)
#         print(self.__age)
#         print(self.ge)
#         print(self.__gene) # 这一行也会报错
# obj = b("xiaoming")
# print(obj.name)
# print(obj.ge)
# # print(obj.__gene) 这个也会报错
# obj.show()

# __双下线下标私有成员，不可继承

"""2、特殊成员
1.__init__

__init__方法可以简单的理解为类的构造方法（实际并不是构造方法，只是在类生成对象之后就会被执行），
之前已经在上一篇博客中说明过了。

2.__del__

__del__方法是类中的析构方法，当对象消亡的时候（被解释器的垃圾回收的时候会执行这个方法）这个方
法默认是不需要写的，不写的时候，默认是不做任何操作的。因为你不知道对象是在什么时候被垃圾回收掉，
所以，除非你确实要在这里面做某些操作，不然不要自定义这个方法。

3.__call__

__call__方法在类的对象被执行的时候（obj()或者 类()()）会执行。

4.__int__

__int__方法，在对象被int()包裹的时候会被执行，例如int(obj)如果obj对象没有、__int__方法，那么
就会报错。在这个方法中返回的值被传递到int类型中进行转换。

5.__str__

__str__方法和int方法一样，当对象被str(obj)包裹的时候，如果对象中没有这个方法将会报错，如果有
这个方法，str()将接收这个方法返回的值在转换成字符串。

6.__add__

__add__方法在两个对象相加的时候，调用第一个对象的__add__方法，将第二个对象传递进来，至于怎么
处理以及返回值，那是程序员自定义的，就如下面的例子：
"""
# class abc:
#     def __init__(self, age):
#         self.age = age
#     def __add__(self, obj):
#         return self.age+obj.age
#
# a1 = abc(18)
# a2 = abc(20)
# print(a1+a2)

""" 7.__dict__

__dict__方法在类里面有，在对象里面也有，这个方法是以字典的形式列出类或对象中的所有成员。就像
下面的例子："""

# class abc:
#     def __init__(self, age):
#         self.age = age
#     def __add__(self, obj):
#         return self.age+obj.age
# a1 = abc(18)
# print(abc.__dict__)
# print(a1.__dict__)

"""8.__getitem__ __setitem__ __delitem__

__getitem__方法匹配 对象[索引] 这种方式，__setitem__匹配 对象[索引]=value 这种方式，
__delitem__匹配 del 对象[索引] 这种方式，例子如下:"""

# class Foo:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def __getitem__(self, item): # 匹配：对象[item]这种形式
#         return item+10
#     def __setitem__(self, key, value): # 匹配：对象[key]=value这种形式
#         print(key,value)
#     def __delitem__(self, key): # 匹配：del 对象[key]这种形式
#         print(key)
#
# li = Foo("alex",18)
# print(li[10])
# li[10] = 100
# del li[10]

# 执行结果：
# 20
# 10 100
# 10

""" 10.__iter__

    类的对象如果想要变成一个可迭代对象，那么对象中必须要有__iter__方法，并且这个方法返回的是
一个迭代器。
    for 循环的对象如果是一个可迭代的对象，那么会先执行对象中的__iter__方法，获取到迭代器，然后
再执行迭代器中的__next__方法获取数据。如果for循环的是一个迭代器，那么直接执行迭代器中的
__next__方法。
"""

# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __iter__(self):
#         return iter([1,2,3,4,5]) # 返回的是一个迭代器
# li = Foo("alex",18)

# 1.如果li中有__iter__方法，那么它返回的就是可迭代对象
# 2.对象.iter()的返回值是一个迭代器
# 3.for循环的如果是迭代器，那么直接执行.next()方法
# 4.for循环的如果是可迭代对象，那么先执行.iter(),获取迭代器再执行next

# for i in li:
#     print(i)

""" 11.isinstance和issubclass

    之前讲过isinstance可以判断一个变量是否是某一种数据类型，其实，isinstance不只可以判断数据
类型，也可以判断对象是否是这个类的对象或者是这个类的子类的对象，代码如下："""

# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Son(Foo):
#     pass
# obj = Son("xiaoming",18)
# print(isinstance(obj,Foo))
# 执行结果：True

# issubclass用来判断一个类是否是某个类的子类，返回的是一个bool类型数据，代码如下：

# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Son(Foo):
#     pass
# obj = Son("xiaoming",18)
# print(issubclass(Son,Foo))
# 执行结果：True

""" 3、类与对象
__new__和__metaclass__

在python中，一切皆对象，我们定义的类其实。。。也是一个对象，那么，类本身是谁的对象呢？
在python2.2之前（或者叫经典类中），所有的类，都是class的对象，但是在新式类中，为了将类型
（int,str,float等）和类统一，所以，所有的类都是type类型的对象。当然，这个规则可以被修改，
在类中有一个属性 __metaclass__ 可以指定当前类该由哪个类进行实例化。而创建对象过程中，其实
构造器不是__init__方法，而是__new__方法，这个方法会返回一个对象，这才是对象的构造器。下面
是一个解释类实例化对象内部实现过程的代码段：
"""
# class Mytype(type):
#     def __init__(self, what, bases=None, dict=None):
#         super(Mytype, self).__init__(what, bases, dict)
#     def __call__(self, *args, **kwargs):
#         obj=self.__new__(self)
#         self.__init__(obj, *args, **kwargs)
#         return obj
#
# class Foo:
#     __metaclass__ = Mytype # __metaclass__ 指定当前类该由Mytype类进行实例化
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls)
# obj = Foo("xiaoming",18)
# print(obj.name,obj.age)
# 执行结果：xiaoming 18

""" 4、异常处理
python中使用try except finally组合来实现异常扑捉，不像java中是使用try catch finally....
..其中，except中的Exception是所有异常的父类，下面是一个异常处理的示例："""

# try:
#     int("aaa") # 可能出现异常的代码
# except IndexError as e: # 捕捉索引异常的子异常，注意，这里的as e在老版本的py中可以写成，
# # e但是新版本中用as e,",e"未来可能会淘汰
#     print("IndexError:",e)
# except ValueError as e:  # 捕捉value错误的子异常
#     print("ValueError:",e)
# except Exception as e:  # 如果上面两个异常没有捕获到，那么使用Exception捕获，
# # Exception能够捕获所有的异常
#     print("Exception",e)
# else:  # 如果没有异常发生，执行else中的代码块
#     print("true")
# finally:  # 不管是否发生异常，在最后都会执行finally中的代码，假如try里面的代码正常执行，
# 先执行else中的代码，再执行finally中的代码
#     print("finally")
# 执行结果：
# ValueError: invalid literal for int() with base 10: 'aaa'
# finally

# 那么既然Exception是所有异常的父类，我们可以自已定义Exception的子类，实现自定义异常处理，
# 下面就是实现例子：

# class OldBoyError(Exception):  # 自定义错误类型
#     def __init__(self,message):
#         self.message = message
#     def __str__(self): # 打印异常的时候会调用对象里面的__str__方法返回一个字符串
#         return self.message
# try:
#     raise OldBoyError("我没错，别抛弃我") # raise是主动抛出异常，可以调用自定义的异常抛出异常
# except OldBoyError as e:
#     print(e)
# 执行结果：我没错，别抛弃我

"""异常处理里面还有一个断言，一般用在判断执行环境上面，只要断言后面的条件不满足，那么就抛出
异常，并且后面的代码不执行了。"""

# print(123)
# assert 1==2  # 断言，故意抛出异常，做环境监测用，环境监测不通过，报错并结束程序
# print("456")
# 执行结果：
#     assert 1==2  # 断言，故意抛出异常，做环境监测用，环境监测不通过，报错并结束程序
# 123
# AssertionError

"""5、反射/自省
python中的反射/自省的实现，是通过hasattr、getattr、setattr、delattr四个内置函数实现的，其实这四个内置函数不只可以用在类和对象中，也可以用在模块等其他地方，只是在类和对象中用的很多，所以单独提出来进行解释。

hasattr(key)返回的是一个bool值，判断某个成员或者属性在不在类或者对象中
getattr(key,default=xxx)获取类或者对象的成员或属性，如果不存在，则会抛出AttributeError异常,如果定义了default那么当没有属性的时候会返回默认值。
setattr(key,value)假如有这个属性，那么更新这个属性，如果没有就添加这个属性并赋值value
delattr(key)删除某个属性
注意，上面的key都是字符串，而不是变量，也就是说可以通过字符串处理类中的成员或者对象中的属性。下面是一个例子代码：
"""
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        return self.name,self.age
obj=Foo("xiaoming",18)
print(getattr(obj,"name"))
setattr(obj,"k1","v1")
print(obj.k1)
print(hasattr(obj,"k1"))
delattr(obj,"k1")
show_fun=getattr(obj,"show")
print(show_fun())
# 执行结果：
# xiaoming
# v1
# True
# ('xiaoming', 18)

# 反射/自省能够直接访问以及修改运行中的类和对象的成员和属性，这是一个很强大的功能，并且并不像
# java中效率很低，所以用的很多。

# 反射：是用字符串类型的名字 取获取变量方法操作
# hasattr()
# getattr()
# delattr()
# setattr()

# demo:
# isinstance(obj,cls) 检查是否obj是否是类 cls的对象
class Lo(object):
       pass
aa=Lo()
print(isinstance(aa,Lo))

# issubclass(sub,super) 检查sub类是否是super的派生类(子类)
class A:pass
class B(A):pass
print(issubclass(B,A))
print(issubclass(A,B))

"""1.getattr()"""

class Da(object):
    cc="188888"
    def __init__(self,name):
        self.name=name

    def aa(self):
        print("反射!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11")
f=Da("张三")

cc=getattr(f,'aa')
cc()
print("**********************************************")
f.aa()

class A:
    def fun(self):
        print("哈哈哈哈哈哈!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
a=A()
a.name="张三"
a.age=25

# 反射对象的属性
ret=getattr(a,"name")  # 通过字符串取到的值
print(ret)
print("**********************")
# 反射对象的方法
r=getattr(a,"fun")
r()
print(a.__dict__)

# 反射类的方法 classmethod staticmethod
class B:
    bb=20
    @classmethod
    def fun(self):
        print("!!!!!!!!!!")

print(B.bb)# 20

# 反射类属性
ret=getattr(B,"bb")
print(ret)# 20

# 反射类方法
re=getattr(B,"fun")
re()  # !!!!!!!!!!




# 下面是一个反射/自省用在模块级别的例子：

"""反射模块"""

# my.py 文件

day='Monday' #  周一

def Gun():
    print("模块中！！！！！！！！！！！！！！反射")

# 模块
# 反射模块的属性
import my
r=getattr(my,"day")
print(r)
# 反射模块的方法
ret=getattr(my,'Gun')
ret()

import  sys
# 内置模块也能用
# 反射自己模块中的变量(就是本模块)
def Gn():
    print("44444444444444")
ye=1111111111
print(sys.modules['__main__'].ye)
k=getattr(sys.modules['__main__'],"ye")
print(k)
# 反射自己模块中的方法(函数）
t=getattr(sys.modules['__main__'],"Gn")
t()
ff=input(">>>>")
gg=getattr(sys.modules['__main__'],ff)
print(gg)
# 把自己变成自己的模块import  sysaa=sys.modules[__name__]print(aa)x=122222222222print(hasattr(aa,"x"))# Trueprint(getattr(aa,"x"))# 122222222222

"""6、单例模式
这里介绍一个设计模式，设计模式在程序员写了两三年代码的时候，到一定境界了，才会考虑到设计模式对于程序带来的好处，从而使用各种设计模式，这里只是简单的介绍一个简单的设计模式：单例模式。在面向对象中的单例模式就是一个类只有一个对象，所有的操作都通过这个对象来完成，这就是面向对象中的单例模式，下面是实现代码：
"""
class Foo:  # 单例模式
    __v=None
    @classmethod
    def ge_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v=Foo()
            return cls.__v
obj1=Foo.ge_instance()
print(obj1)
obj2=Foo.ge_instance()
print(obj2)
obj3=Foo.ge_instance()
print(obj3)
# 执行结果：
# <__main__.Foo object at 0x000001D2ABA01860>
# <__main__.Foo object at 0x000001D2ABA01860>
# <__main__.Foo object at 0x000001D2ABA01860>

"""可以看到，三个对象的内存地址都是一样的，其实，这三个变量中存储的都是同一个对象的内存地址，
这样有什么好处呢？能够节省资源，就比如在数据库连接池的时候就可以使用单例模式，只创建一个类的
对象供其他程序调用，还有在web服务中接收请求也可以使用单例模式来实现，节省资源。"""

"""勇气通往天堂，怯懦通往地狱。"""


















