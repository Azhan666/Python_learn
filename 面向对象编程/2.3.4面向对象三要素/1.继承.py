# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Rewrite the date：2021-11-02
# target：根据书籍《Python语言及其应用》'Introducing Python'
# ([美］Bill Lubanovic 著
# 丁嘉瑞　梁杰　禹常隆 译)深入学习面向对象
# 丁嘉瑞：“耶鲁大学计算机硕士，曾就读于北京理工大学。主要研究方向为机器学习，
# 曾从事iOS开发。个人博客：Jiarui-blog.com”
# creator：Mr_He

# 写在前面：
# 面向对象有三大要素：继承、封装和多态。这里面概念非常多，往往越讲读者越糊涂。为了不误导读者，
# 此处尽可能不做解释，只给出例子，请读者自行揣摩。

# 1.继承
# 继承是指类之间共享属性和操作的机制

# 如果派生类只有一个父类，就是单继承；如果派生类有多个父类，那就是多继承。如果父类的构造函数
# 需要参数，则应该显式的调用父类的构造函数，或使用super()函数，其代码如下：

# class Animal:
#     def eat(self):
#         print('我能吃东西')

# class Fash(Animal): # 单继承 Animal是其父类
#     def __init__(self, name): # __init__ ：面向对象初始化函数
#         self.name = name # 调用函数name
#     def swim(self):
#         print('我会游泳')

# class Bird(Animal): # 单继承，继承animal
#     def __init__(self, name):
#         self.name = name
#     def who(self):
#         print('我是%s'%self.name)
#     def fly(self):
#         print('我会飞')

# class Batman(Bird): # 单继承，显式地调用父类的构造函数
#     def __init__(self, name, color):
#         Bird.__init__(self, name)
#         self.color = color
#     def say(self):
#         print('我会说话，喜欢%s'%self.color)

# class Ultraman(Fash, Batman): # 多继承，有两个父类
#     def __init__(self, name, color, region):
#         super(Ultraman, self).__init__(name)
#         super(Fash, self).__init__(name, color)
#         self.region = region
#     def where(self):
#         print('我来自%s'%self.region)
# uman = Ultraman('奥特曼', '红色', '火星')
# uman.who()
# uman.where()
# uman.say()
# uman.eat()
# uman.fly()
# uman.swim()
# print(uman)

"""
    继承：
"""
# class Car(): # 创建一个空类
#     pass
#
# class Yugo(Car): # 继承自Car
#     pass
"""
    为每一个类创建一个实例对象：
"""
# give_me_a_car = Car()
# gi_me_a_yugo = Yugo()

"""
    子类是父类的一种特殊情况，它属于父类。在面向对象的术语里，我们经常称Yugo是一个(is-a)Car。
对象give_me_a_yugo是Yugo类的一个实例，但它同时继承了Car能做到的所有事情。当然，上面的例子中
Car和Yugo就像潜艇上的甲板水手一样起不到任何实际作用。我们来更新一下类的定义，让它们发挥点作用：
"""
# class Car():
#     def exclaim(self):
#         print("I'm a Car!")
# class Yugo(Car):
#     pass
# 最后，为每一个类各创建一个对象，并调用刚刚声明的exclaim方法：
# give_me_a_car = Car()
# gi_me_a_yugo= Yugo()
# give_me_a_car.exclaim()
# gi_me_a_yugo.exclaim()
# I'm a Car!
# I'm a Car!

"""
    覆盖方法：
"""

"""
    就像上面的例子展示的一样，新创建的子类会自动继承父类的所有信息。接下来将看到子
类如何替代——更习惯说覆盖（override）——父类的方法。Yugo 和 Car 一定存在着某些区
别，不然的话，创建它又有什么意义？试着改写一下 Yugo 中 exclaim() 方法的功能：
"""
# class Car():
#     def exclaim(self):
#         print("I'm a Car！")
# class Yugo(Car):
#     def exclaim(self):
#         print("I'm a Yugo ! Much like a Car, but more Yugo-ish.")
#
# # 现在为每个类创建一个对象：
# give_me_a_car = Car().exclaim()
# give_me_a_yugo = Yugo().exclaim()

"""
    在上面的例子中，我们覆盖了父类的 exclaim() 方法。在子类中，可以覆盖任何父类的方
法，包括 __init__()。下面的例子使用了之前创建过的 Person 类。我们来创建两个子类，
分别代表医生（MDPerson）和律师（JDPerson）:
"""
# class Person():
#     def __init__(self, name):
#         self.name = name
# class MDPerson(Person):
#     def __init__(self, name):
#         self.name = "Doctor" + name
# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name + ", Esquire"

"""
    在上面的例子中，子类的初始化方法 __init__() 接收的参数和父类 Person 一样，但存储
到对象内部 name 特性的值却不尽相同：
# """
# person = Person('Fudd')
# doctor = MDPerson('Fudd')
# lawyer = JDPerson('Fudd')
# print(person.name)
# print(doctor.name)
# print(lawyer.name)

"""
    添加新方法：

    子类还可以添加父类中没有的方法。
"""
# class Car():
#     def exclaim(self):
#         print("I'm a Car!")
# class Yugo(Car):
#     def exclaim(self):
#         print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
#         # 添加一个新方法：
#     def need_a_push(self):
#         print("A little help here?")
# # 接着，创建实例对象：
# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
# # Yugo类的对象可以响应need_a_push()方法：
# give_me_a_yugo.need_a_push()
# A little help here?
# 但比它更广义的Car无法响应该方法：
# give_me_a_car.need_a_push()
"""
Traceback (most recent call last):
  File "D:/python_learn/Python基础阶段/Python高手修炼之道/面向对象编程/2.3.4面向对象三要素/1.继承.py", line 152, in <module>
    give_me_a_car.need_a_push()
AttributeError: 'Car' object has no attribute 'need_a_push'
"""
# 至此，Yugo终于可以做一些Car做不到的事情了，它的与众不同的特征开始体现了出来。
# 这个方法是在子类中新定义的，父类中没有定义，父类也无法使用这个方法。

"""
    使用super从父类得到帮助：
"""

"""
    我们已经知道如何在子类中覆盖父类的方法，但如果想要调用父类的方法怎么办？
“哈哈！终于等到你问这个了。”super() 站出来说道。下面的例子将定义一个新的类
EmailPerson，用于表示有电子邮箱的 Person。首先，来定义熟悉的 Person 类：
"""
# class Person():
#     def __init__(self, name):
#         self.name = name
#
# # 下面是子类的定义，注意，子类的初始化方法__init__()中添加了一个额外的email参数：
# class EmailPerson(Person):
#     def __init__(self, name, email):
#         super().__init__(name)
#         self.email = email
"""
    在子类中定义__init__()方法时，父类的__init__()方法会被覆盖。
也称作“类的初始化”，因此，在子类中，父类的初始化并不会被自动调用，
我们必须显式调用它。以上代码实际上做了这样几件事情。
    •通过super()方法获取了父类Person的定义。
    •子类的__init__()调用了Person.__init__()方法。它会自动
将self参数传递给父类。因此，你只需传入其余参数即可。上面的例子中，
Person()能接受的其余参数指的是
name。
    • self.email = email 这行新的代码才真正起到了将 EmailPerson 与 Person 区分开的作用。

    接下来，创建一个EmailPerson类的对象：
"""
# bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
# # 我们即可以访问name特性，也可以访问email特性：
# bob.name
# bob.email
# """
#     为什么不像下面这样定义EmailPerson类呢？
# """
# class EmailPerson(Person):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
"""
    确实可以这么做，但这样有悖（bei）于我们使用继承的初衷。我们应该使用super()
来让Person完成它应该做的事情，就像任何一个单纯的Person对象一样。
    除此之外，不这么写还有另一个
好处：如果 Person 类的定义在未来发生改变，使用 super() 可以保证这些改变会自动反映
到 EmailPerson 类上，而不需要手动修改。
子类可以按照自己的方式处理问题，但如果仍需要借助父类的帮助，使用 super() 是最佳
的选择（就像现实生活中孩子与父母的关系一样）
"""
"""
    还记得前面例子中的Car类吗？再次调用exclaim()方法：
"""
# car = Car()
# car.exclaim()
# I'm a Car!
"""
    Python在背后做了以下两件事情：
    ·查找car对象所属的类（Car）；
    ·把car对象作为self参数传给Car类所包含的exclaim()方法。
    
    了解调用机制后，为了好玩，我们甚至可以像下面这样进行调用，这与普通的调用语法
(car.exclaim())效果完全一致；
Car.exclaim(car)
I'm a Car!
    当然，我们没有理由使用这种臃肿的方法。
"""

"""
    使用属性对特性进行访问和设置：
"""
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#     name = property(get_name, set_name)

"""
    这两个新方法在最后一行之前都与普通的 getter 和 setter 方法没有任何区别，而最后一行
则把这两个方法定义为了 name 属性。property() 的第一个参数是 getter 方法，第二个参
数是 setter 方法。现在，当你尝试访问 Duck 类对象的 name 特性时，get_name() 会被自动
调用：
"""
# fowl = Duck('Howard')
# # print(fowl.name)
# # inside the getter
# # Howard
#
# # 也可以显式调用get_name()方法，它就像普通的getter方法一样：
# fowl.get_name()
# # inside the getter
#
# # 当对name特性执行赋值操作时，set_name()方法会被调用：
# fowl.name = 'Daffy'
# print(fowl.name)
# # inside the getter
# # Daffy
#
# # 也可以显式调用set_name()方法：
# fowl.set_name('Daffy')
# print(fowl.name)
# # inside the getter
# # Daffy

# 另一种定义属性的方式是是使用修饰符（decorator）。下一个例子会定义两个不同的方法，
# 他们都叫name(),但包含不同的修饰符：
# property, 用于指示getter方法;
# name.setter, 用于指示setter方法.

# demo:
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.hidden_name
#     @name.setter
#     def name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
"""
    你仍然可以向之前访问特性一样访问name,但这里没有了显式的get_name()和
set_name()
"""
# fowl = Duck('Howard')
# print(fowl.name)
# fowl.name = 'Donald'
# print(fowl.name)

"""
    实际上，如果有人能猜到我们在类的内部用的特性名是 hidden_name，他仍
然可以直接通过 fowl.hidden_name 进行读写操作。下一节将看到 Python 中
特有的命名私有特性的方式。
"""

"""
    在前面几个例子中，我们都使用 name 属性指向类中存储的某一特性（在我们的例子中是
hidden_name）。除此之外，属性还可以指向一个计算结果值。我们来定义一个 Circle 类，
它包含 radius 特性以及一个计算属性 diameter:
"""
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#     @property
#     def diameter(self):
#         return 2 * self.radius
# # 创建一个Circle对象,并给radius赋予一个初值:
# c = Circle(5)
# print(c.radius)
# # 可以像访问特性(例如radius)一样访问属性diameter:
# print(c.diameter)

"""
    真正有趣的还在后面.我们可以随时改变radius特性的值,计算属性diameter会自动1根据新的值更新自己:
"""
# c.radius = 7
# print(c.diameter)
#
# """
#     如果你没有指定某一特性的setter属性(@diameter.setter),那么将无法从类得外部对它
# 的值进行设置.这对于那些只读的特性非常有用:
# """
# c.diameter = 20
"""
Traceback (most recent call last):
  File "D:/python_learn/Python基础阶段/Python高手修炼之道/面向对象编程/2.3.4面向对象三要素/1.继承.py", line 340, in <module>
    c.diameter = 20
AttributeError: can't set attribute
# 不能设置属性
"""
"""
    与直接访问特性相比,使用property还有一个巨大的优势:如果你改变了某个特性的定义,
只需要在类定义里修改相关代码即可,不需要在每一处调用修改.
"""

"""
    使用名称重整保护私有特性:
    
    前面的 Duck 例子中，为了隐藏内部特性，我们曾将其命名为 hidden_name。其实，Python
对那些需要刻意隐藏在类内部的特性有自己的命名规范：由连续的两个下划线开头（__）。
我们来把 hidden_name 改名为 __name，如下所示：
"""
# class Duck():
#     def __init__(self, input_name):
#         self.__name = input_name
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.__name
#     @name.setter
#     def name(self, input_name):
#         print('inside the setter')
#         self.__name = input_name
# # 看看代码是否还能正常工作:
# fowl = Duck('Howard')
# print(fowl.name)
# fowl.name = 'Donald'
# print(fowl.name)
# inside the getter
# Howard
# inside the setter
# inside the getter
# Donald

# 看起来不错！现在，你无法在外部访问 __name 特性了：
# fowl.__name
"""
Traceback (most recent call last):
  File "d:/python_learn/Python基础阶段/Python高手修炼之道/面向对象编程
/2.3.4面向对象三要素/1.继承.py", line 383, in <module>
    fowl.__name
AttributeError: 'Duck' object has no attribute '__name'
"""

"""
    这种命名规范本质上并没有把特性变成私有，但 Python 确实将它的名字重整了，让外部
的代码无法使用。如果你实在好奇名称重整是怎么实现的，我可以偷偷地告诉你其中的奥
秘，但不要告诉别人哦：
"""
# fowl.Duck__name
# Donald

"""
    如前面例子中，假如我们需要把特性 hidden_name 的名字改成 in_class_name。不设置属性（property）
的话，我们需要在每一处访问 hidden_name 的地方将它替换成 in_class_name；而设置了属性的话，仅
需在类的内部修改，其余部分的访问仍直接通过属性 name 即可。——译者注
"""
"""
发现了吗？我们并没有得到 inside the getter，成功绕过了 getter 方法。尽管如我们所
见，这种保护特性的方式并不完美，但它确实能在一定程度上避免我们无意或有意地对特
性进行直接访问。
"""
"""
    方法的类型：

    实例方法：self.xxx

    有些数据（特性）和函数（方法）是类本身的一部分，还有一些是由类创建的实例的一部分。
在类的定义中，以 self 作为第一个参数的方法都是实例方法（instance method）。它们在
创建自定义类时最常用。实例方法的首个参数是 self，当它被调用时，Python 会把调用该
方法的对象作为 self 参数传入。

    类方法：@classmethod

    与之相对，类方法（class method）会作用于整个类，对类作出的任何改变会对它的所有实
例对象产生影响。在类定义内部，用前缀修饰符 @classmethod 指定的方法都是类方法。与
实例方法类似，类方法的第一个参数是类本身。在 Python 中，这个参数常被写作 cls，因
为全称 class 是保留字，在这里我们无法使用。下面的例子中，我们为类 A 定义一个类方
法来记录一共有多少个类 A 的对象被创建
"""
# class A():
#     count = 0
#     def __init__(self):
#         A.count += 1
#     def exclaim(self):
#         print("I'm a A!")
#     @classmethod
#     def kids(cls):
#         print("A has", cls.count, "little objects.")

# easy_a = A()
# breezy_a = A()
# wheezy_a = A()
# print(A.kids())

"""
    注意，上面的代码中，我们使用的是 A.count（类特性），而不是 self.count（可能是对象
的特性）。在 kids() 方法中，我们使用的是 cls.count，它与 A.count 的作用一样.

    类定义中的方法还存在着第三种类型，它既不会影响类也不会影响类的对象。它们出现在
类的定义中仅仅是为了方便，否则它们只能孤零零地出现在代码的其他地方，这会影响代
码的逻辑性。这种类型的方法被称作静态方法（static method），用 @staticmethod 修饰，
它既不需要 self 参数也不需要 class 参数。下面例子中的静态方法是一则 CoyoteWeapon
的广告：
"""
# class CoyoteWeapon():
#     @staticmethod # 静态方法
#     def commercial():
#         print('This CoyoteWeapon has been brought to you by Acme')
# CoyoteWeapon.commercial()
# This CoyoteWeapon has been brought to you by Acme
"""
    注意，在这个例子中，我们甚至都不用创建任何 CoyoteWeapon 类的对象就可以调用这个方
法，句法优雅不失风格！
"""

"""
    鸭子类型：
    
    Python 对实现多态（polymorphism）要求得十分宽松，这意味着我们可以对不同对象调用
同名的操作，甚至不用管这些对象的类型是什么。
我们来为三个 Quote 类设定同样的初始化方法 __init__()，然后再添加两个新函数：
• who() 返回保存的 person 字符串的值；
• says() 返回保存的 words 字符串的内容，并添上指定的标点符号。
它们的具体实现如下所示：
"""
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'
class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'
class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

"""
    我们不需要改变 QuestionQuote 或者 ExclamationQuote 的初始化方式，因此没有覆盖它们
的 __init__() 方法。Python 会自动调用父类 Quote 的初始化函数 __init__() 来存储实例
变量 person 和 words，这就是我们可以在子类 QuestionQuote 和 ExclamationQuote 的对象
里访问 self.words 的原因。

    接下来创建一些对象：
"""
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunter1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunter1.who(), 'says:', hunter1.says())

hunter2 = ExclamationQuote('Daffy Duck', "Is's rabbit season")
print(hunter2.who(), 'says:', hunter2.says())
# Elmer Fudd says: I'm hunting wabbits.
# Bugs Bunny says: What's up, doc?
# Daffy Duck says: Is's rabbit season!


