# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 当父类有多个派生类，且派生类都实现了同一个成员函数时，可以实现多态，其代码如下：

# class H2O:
#     def who(self):
#         print("I'm H20")
#
# class Water:
#     def who(self):
#         print("I'm water")
#
# class Ice: # ice:冰
#     def who(self):
#         print("I'm ice")
#
# class Vapor(H2O): #vapor:蒸汽
#     def who(self):
#         print("I'm vapor")
#
# def who(obj):
#     obj.who()
#
# objs = [H2O(), Water(), Ice(), Vapor()]
# for obj in objs:
#     who(obj)

"""
    鸭子类型：

    Python 对实现多态（polymorphism）要求得十分宽松，这意味着我们可以对不同对象调用
同名的操作，甚至不用管这些对象的类型是什么。
我们来为三个 Quote 类设定同样的初始化方法 __init__()，然后再添加两个新函数：
• who() 返回保存的 person 字符串的值；
• says() 返回保存的 words 字符串的内容，并添上指定的标点符号。
它们的具体实现如下所示：
"""


# class Quote():
#     def __init__(self, person, words):
#         self.person = person
#         self.words = words
#
#     def who(self):
#         return self.person
#
#     def says(self):
#         return self.words + '.'
#
#
# class QuestionQuote(Quote):
#     def says(self):
#         return self.words + '?'
#
#
# class ExclamationQuote(Quote):
#     def says(self):
#         return self.words + '!'


"""
    我们不需要改变 QuestionQuote 或者 ExclamationQuote 的初始化方式，因此没有覆盖它们
的 __init__() 方法。Python 会自动调用父类 Quote 的初始化函数 __init__() 来存储实例
变量 person 和 words，这就是我们可以在子类 QuestionQuote 和 ExclamationQuote 的对象
里访问 self.words 的原因。

    接下来创建一些对象：
"""
# hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
# # print(hunter.who(), 'says:', hunter.says())
#
# hunter1 = QuestionQuote('Bugs Bunny', "What's up, doc")
# # print(hunter1.who(), 'says:', hunter1.says())
#
# hunter2 = ExclamationQuote('Daffy Duck', "Is's rabbit season")
# print(hunter2.who(), 'says:', hunter2.says())
# Elmer Fudd says: I'm hunting wabbits.
# Bugs Bunny says: What's up, doc?
# Daffy Duck says: Is's rabbit season!

"""
    三个不同版本的 says() 为上面三种类提供了不同的响应方式，这是面向对象的语言中多态
的传统形式。Python 在这方面走得更远一些，无论对象的种类是什么，只要包含 who() 和
says()，你便可以调用它。我们再来定义一个 BabblingBrook 类，它与我们之前的猎人猎
物（Quote 类的后代）什么的没有任何关系：
"""
# class BabblingBrook():
#     def who(self):
#         return 'Brook'
#     def says(self):
#         return 'Babble'
# brook = BabblingBrook()
#
# """
#     现在，对不同对象执行who()和says()方法，其中有一个（brook）与其它类型的对象毫无关联：
# """
# def who_says(obj):
#     print(obj.who(), 'says', obj.says())
# who_says(hunter)
# who_says(hunter1)
# who_says(hunter2)
# who_says(brook)
# Elmer Fudd says I'm hunting wabbits.
# Bugs Bunny says What's up, doc?
# Daffy Duck says Is's rabbit season!
# Brook says Babble
"""
    这种方式有时被称为鸭子类型（duck typing），这个命名源自一句名言：
    如果它像鸭子一样走路，像鸭子一样叫，那么它就是一只鸭子。
                                          ———— 一位智者

    源于“鸭子测试”。在鸭子类型中，并不关注对象本身的具体类型，只关注它能实现的功能。
——译者注 
"""

"""
    特殊方法：
    
    到目前为止，你已经能创建并使用基本对象了。现在再往深钻研一些。
当我们输入像 a = 3 + 8 这样的式子时，整数 3 和 8 是怎么知道如何实现 + 的？同样，a
又是怎么知道如何使用 = 来获取计算结果的？你可以使用 Python 的特殊方法（special 
method），有时也被称作魔术方法（magic method），来实现这些操作符的功能。别担心，
不需要甘道夫 8 的帮助，它们一点也不复杂。
"""
"""
    这些特殊方法的名称以双下划线（__）开头和结束。没错，你已经见过其中一个：__
init__，它根据类的定义以及传入的参数对新创建的对象进行初始化。
假设你有一个简单的 Word 类，现在想要添加一个 equals() 方法来比较两个词是否一致，
忽略大小写。也就是说，一个包含值 'ha' 的 Word 对象与包含 'HA' 的是相同的。
下面的代码是第一次尝试，创建一个普通方法 equals()。self.text 是当前 Word 对象所包
含的字符串文本，equals() 方法将该字符串与 word2（另一个 Word 对象）所包含的字符串
做比较：
"""
# class Word():
#     def __init__(self, text):
#         self.text = text
#     def equals(self, word2):
#         return self.text.lower() == word2.text.lower()
# 借着创建三个包含不同字符串的Word对象：
# first = Word('ha')
# second = Word('HA')
# third = Word('eh')
# 当字符串 'ha' 和 'HA' 被转换为小写形式再进行比较时（我们就是这么做的），它们应该是
# 相等的：
# print(first.equals(second))
# True
# 但字符串 'eh' 无论如何与 'ha' 也不会相等：
# print(first.equals(third))
# False

"""
    我们成功定义了 equals() 方法来进行小写转换并比较。但试想一下，如果能通过 if first 
== second 进行比较的话岂不更妙？这样类会更自然，表现得更像一个 Python 内置的类。
好的，来试试吧，把前面例子中的 equals() 方法的名称改为 __eq__()（请先暂时接受，后
面我会解释为什么这么命名）：
"""

# class Word():
#     def __init__(self, text):
#         self.text = text
#     def __eq__(self, word2):
#         return self.text.lower() == word2.text.lower()
# # 修改到此结束，来看看新的版本能否正常工作：
# first = Word('ha')
# second = Word('HA')
# third = Word('eh')
# print(first == second)
# # True
# print(first == third)
# # False

"""
    太神奇了！是不是如同魔术一般？仅需将方法名改为 Python 里进行相等比较的特殊方法名
__eq__() 即可。表 6-1 和表 6-2 列出了最常用的一些魔术方法。
"""

"""
表6-1：和比较相关的魔术方法
方法名                使用
__eq__(self, other) self == other
__ne__(self, other) self != other
__lt__(self, other) self < other
__gt__(self, other) self > other
__le__(self, other) self <= other
__ge__(self, other) self >= other
"""

"""
表6-2：和数学相关的魔术方法
方法名                  使用
__add__(self, other) self + other
__sub__(self, other) self - other
__mul__(self, other) self * other
__floordiv__(self, other) self // other
__truediv__(self, other) self / other
__mod__(self, other) self % other
__pow__(self, other) self ** other
"""
"""
    不仅数字类型可以使用像 +（魔术方法 __add__()）和 -（魔术方法 __sub__()）的数学运算
符，一些其他的类型也可以使用。例如，Python 的字符串类型使用 + 进行拼接，使用 * 进
行复制。关于字符串的魔术方法还有很多，你可以在 Python 3 在线文档的 Special method 
names（https://docs.python.org/3/reference/datamodel.html#special-method-names）里找到，其中
最常用的一些参见下面的表 6-3
"""

"""
表6-3：其他种类的魔术方法
方法名           使用
__str__(self) str(self)
__repr__(self) repr(self)
__len__(self) len(self)
"""

"""
    除了 __init__() 外，你会发现在编写类方法时最常用到的是 __str__()，它用于定义如何
打印对象信息。print() 方法，str() 方法以及你将在第 7 章读到的关于字符串格式化的相
关方法都会用到 __str__()。交互式解释器则用 __repr__() 方法输出变量。如果在你的类
既没有定义 __str__() 也没有定义 __repr__()，Python 会输出类似下面这样的默认字符串：
"""
# first = Word('ha')
# print(first)
# <__main__.Word object at 0x1006ba3d0>
# print(first)
# <__main__.Word object at 0x1006ba3d0>

# 我们将 __str__() 和 __repr__() 方法都添加到 Word 类里，让输出的对象信息变得更好看些：
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return Word(self.text)
first = Word('ha')
print(first) # uses __repe__
# ha
print(first) # uses __str__
# ha
# 更 多 关 于 魔 术 方 法 的 内 容 请 查 看 Python 在 线 文 档（https://docs.python.org/3/reference/
# datamodel.html#special-method-names）