# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 编程语言虽然不是自然语言，但是细细琢磨，编程语言其实在很多方面也是符合自然语言规律的。例如，
# 编程语言也讲究词汇学（关键字），结构学（程序结构），句法（语法），语义（代码功能）等；在语
# 言的学习方法上，编程语言和自然语言也高度相似。

# 回想一下学习英语的过程，大多数人都有这样一个阶段：语法都学明白了，词汇量也够了，可就是说不
# 出来，听不明白，急得捶胸顿足。再来看看初学者学习Python语言的情况，是不是也有这样一个阶段呢？
# 基础语法都学完了，可是读别人的代码特别吃力，自己写也不知从何处着手。

# 为什么会这样呢？因为缺乏语感！语感是比较直接迅速地感悟语言的能力，是语言水平的重要组成部分，
# 是对语言分析、理解、体会、吸收全过程的高度浓缩，是一种经验色彩很浓的能力。其中涉及学习经验、
# 生活经验、心理经验、情感经验，包含理解能力、判断能力、联想能力等诸多因素。

# 以上就是编程也要讲“语感训练”的理论基础。语感训练并不等同于语法学习，也不是完整的小项目、小
# 课题练习；而是针对编程实践中经常遇到的字符串处理，文件读写，列表、字典、元组、集合、对象操
# 作等基本技能进行训练，以帮助初学者建立语感。一旦建立起了语感，我们就可以专注于功能的实现，
# 而不会被一些小问题中断思维。

# 此处整理的Python语感训练题涵盖了列表、字典、元组、集合、字符串、类型转换、文件读写、综合
# 应用等类型，共100道练习题。

# =================================================================================
# 开头标注“*”号的为不熟练习题，“*”号越多，需要复习的次数越多！
# =================================================================================

# （1）将元组（1,2,3）和集合{4,5,6}合并成一个列表。

# list((1,2,3)) + list({4,5,6})  # 拼接
# print(list((1,2,3)) + list({4,5,6}))

# （2）在列表[1,2,3,4,5,6]首尾分别添加整型元素7和0.

# a = [1,2,3,4,5,6]
# a.insert(0,7) # insert()方法需添加要插入位置的索引 insert:插入
# a.append(0)   # append()方法默认添加在末尾 append：附加 添加 追加
# print(a)

# （3）反转列表[0,1,2,3,4,5,6,7]。

# a = [0,1,2,3,4,5,6,7]
# a.reverse() # reverse()方法：相反的 倒车档 颠倒的
# print(a)
# a[::-1]     # [::-1]：列表切片，-1为反转
# print(a[::-1])

# （4）反转列表[0,1,2,3,4,5,6,7]后给出其中元素5的索引号。

# [0,1,2,3,4,5,6,7] [::-1].index(5) # index()方法：指数 索引 指标 数据库索引
# print([0,1,2,3,4,5,6,7] [::-1].index(5))

# （5）分别统计列表[True,False,0,1,2]中True、False、0、1、2的元素个数，发现了什么？

# a = [True,False,0,1,2]  # count()方法:计数，统计
# a.count(True),a.count(False),a.count(0),a.count(1),a.count(2)
# print(a.count(True),a.count(False),a.count(0),a.count(1),a.count(2))

# 我发现了count()不区分True和1、False和0，但None、''不会被视为False。

# **（6）从列表[True,1,0,'x',None,'x',False,2,True]中删除元素'x'。

# a = [True,1,0,'x',None,'x',False,2,True]
# for i in range(a.count('x')): # 使用 for i in 的方法判断元素是否在a.count()范围中
#     a.remove('x')  # 使用remove()方法移除元素'x' remove:移除 除去 删除 解除
# print(a)

# （7）从列表[True,1,0,'x',None,'x',False,2,True]中删除索引号为4的元素。

# a = [True,1,0,'x',None,'x',False,2,True]
# a.pop(4) # pop()方法：从列表中删除指定索引的元素
# print(a)

# ***（8）删除列表中索引号为奇数（或偶数）的元素。

# a = list(range(10))
# print(a)
# del a[::2] # 删除索引号为偶数的元素（偶数，包含0）
# print(a)   # del a（n）方法：它的作用是删除掉列表里面的索引号位置为n 的元素，
          # 这里需要注意的是del是一种操作语句
#
# a = list(range(10))
# del a[1::2] # 删除索引号为奇数的元素
# print(a)

# （9）清空列表中的所有元素。

# a = list(range(10))
# print(a)
# a.clear() # clear()方法：清除
# print(a)

# *（10）对列表[3,0,8,5,7]分别进行升序和降序排列。

# a = [3,0,8,5,7]
# a.sort() # sort()方法：排序 （默认升序）
# print(a)
# a.sort(reverse=True)  # 降序 # reverse：相反的 倒车档 颠倒的
# print(a)

# ***（11）将列表[3,0,8,5,7]中大于5的元素置1，其余元素置0.


# ****（12）遍历列表['x','y','z']并打印每一个元素及其对应的索引号。

# for index, value in enumerate(['x','y','z']): # enumerate:枚举
#     print('index={}, value={}'.format(index,value)) # format:格式化输出，类似%d、%s

# ====================================枚举专栏======================================

# 一、Python中的枚举
# Python中的枚举是作为一个类存在的，这是与其他语言的一个较为鲜明的特征，总结它的用法特点如下：
# 1.
# Python枚举作为一个类存在，使用它需要首先导入枚举模块，然后继承并自定义需要的枚举类；
# 2.
# 导入枚举模块可以是Enum(枚举值可以是任意类型)，也可以是IntEnum(枚举值只能是整型)；
# 3.
# 枚举类不允许存在相同的标签；但是允许不同标签的枚举值相同，这样后者相当于前者别名；
# 4.
# 不同的枚举类型，即使枚举名和枚举值都一样，比较结果也是False
# 5.
# 枚举类的值不可以被外界更改
#
# 二、Python枚举的基本用法
# 定义一个枚举如下：
#
# # 第一步：导入枚举类
# from enum import Enum
#
#
# # 第二步：通过继承的方式，定义一个适合我们使用的枚举类
# # 枚举的名字一般都大写
# # 继承Enum后枚举值可以是字符串也可以是整型，如果IntEnum则必须整型
#
# class QQVIP(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
#     BLUE_ALIAS = 3
#     OTHERCOLOR = "othercolor"
#
#
# 1.
# 打印枚举信息

# 1.1打印枚举类型，得到的是一个枚举类型
# print(QQVIP.GREEN)  # 打印结果：QQVIP.GREEN
#
# # 1.2打印枚举名，得到的是一个字符串
# print(QQVIP.GREEN.name)  # 打印结果：GREEN
# print(QQVIP.OTHERCOLOR.name)  # 打印结果：OTHERCOLOR
#
# # 1.3.打印枚举值
# print(QQVIP.GREEN.value)  # 打印结果：2
#
# # 1.4.测试枚举值不可更改，否则报错
# # QQVIP.GREEN = 100
#
# # 1.5.通过枚举名称获取枚举
# print(QQVIP['GREEN'])  # 打印：QQVIP.GREEN
# print(QQVIP['OTHERCOLOR'])  # 打印：QQVIP.OTHERCOLOR
# 2.
# 遍历枚举
#
# # 2.1.由于BLUE与BLUE_ALIAS枚举值相同，BLUE_ALIAS相当于BLUE的别名,所以没有被打印出来
# forvalue
# inQQVIP:
# print(value)
# '''
# 打印结果：
# QQVIP.RED
# QQVIP.GREEN
# QQVIP.BLUE
# QQVIP.OTHERCOLOR
# '''
#
# # 2.2.可以打印出所有的枚举值包括别名,使用__members__
# forvalue
# inQQVIP.__members__:
# print(value)
# '''
# 打印结果：
# RED
# GREEN
# BLUE
# BLUE_ALIAS
# OTHERCOLOR
# '''
#
# # 2.3打印出枚举的所有信息,得到是元组
# forvalue
# inQQVIP.__members__.items():
# print(value)
# '''
# ('RED', <QQVIP.RED: 1>)
# ('GREEN', <QQVIP.GREEN: 2>)
# ('BLUE', <QQVIP.BLUE: 3>)
# ('BLUE_ALIAS', <QQVIP.BLUE: 3>)
# ('OTHERCOLOR', <QQVIP.OTHERCOLOR: 'othercolor'>)
# '''
# 3.
# 枚举的比较
#
# # 3.1两个枚举值可以做等值比较
# result1 = QQVIP.RED == QQVIP.GREEN
# print(result1)  # 打印：False
# result2 = QQVIP.RED == QQVIP.RED
# print(result2)  # 打印：True
#
# # 3.2另一种比较
# result2_1 = QQVIP.RED is QQVIP.RED
# print(result2_1)  # 打印：True
#
# # 3.3两个枚举值不支持大小比较
# # result3 = QQVIP.RED > QQVIP.GREEN
# # print(result3)   #打印：报错
#
# # 3.4：枚举值和对应值比较,并不相等
# result4 = QQVIP.RED == 1
# print(result4)  # 打印 False
# 4.
# 枚举别名
#
# 不同标签但是枚举值相同，后者是前者别名
#
# print(QQVIP.BLUE)
# print(QQVIP.BLUE_ALIAS)  # 打印结果都是BLUE
# 5.
# 枚举转换
#
# 通过具体值得到枚举类型
#
# num = 2
# print(QQVIP(num))  # 打印：QQVIP.GREEN
# 三、枚举的特殊用法
# 创建一个枚举：枚举值只能是整型且不允许设置别名
#
# from enum import IntEnum, unique
#
#
# # 枚举类的的特殊使用
# @unique # unique：独特 唯一 独一无二的 独有
# class Grade(IntEnum):
#     Heigh = 1
#     # Heigh_Alias = 2   #报错重复值，设置unique后，不能设置别名
#     medium = 2
#     Low = 3
#     # Lower = "Lower"  #报错，因为继承IntEnum,所以枚举值只能是Int
#
#
#
# 例一：
# from enum import Enum # 导入枚举模块
#
# # 定义枚举
# class Gender(Enum):
#     MALE = 1
#     FEMALE = 2
#     UNKNOW = 3
#
#
# # 使用枚举
# g = Gender.FEMALE
# g = Gender(1)
# g = Gender['FEMALE']
# print(g)
# print(g.name)
# print(g.value)
#
#
# # 迭代枚举
# for g in Gender:
#     print(g)
#
# # 例二：
# from enum import Enum
#
# # 定义枚举
# #Gender = Enum('Gender', 'MALE FEMALE UNKNOW')
# Gender = Enum('Gender', [('MALE',1), ('FEMALE',2), ('UNKNOW',3)])
#
# # 使用枚举
# g = Gender.FEMALE
# g = Gender(1)
# g = Gender['FEMALE']
# print(g)
# print(g.name)
# print(g.value)
#
#
# # 迭代枚举
# for g in Gender:
#     print(g)
#
# # 例三：自动生成值
# from enum import Enum, auto # auto：汽车 自动 自动模式 全自动
#
# # 如果不关心值，可以自动生成
# class Gender(Enum):
#     MALE = auto()
#     FEMALE = auto()
#     UNKNOW = auto()

# ===============================枚举专栏结束========================================

# （13）将列表[0,1,2,3,4,5,6,7,8,9]拆分为奇数组和偶数组两个列表。

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = a[::2] # 偶数组
# c = a[1::2] # 奇数组
# print(b)
# print(c)

# ****（14）分别根据每一行的首元素和尾元素大小对二维列表[[6,5],[3,7],[2,8]]排序。

# a = [[6,5],[3,7],[2,8]]
# sorted(a, key=lambda x:x[0]) # 根据每一行的首元素排序，默认reverse=False 利用了lambda表达式
# print(sorted(a, key=lambda x:x[0])) # sorted：排序（默认升序）
#
# sorted(a, key=lambda x:x[-1]) # 根据每一行的尾元素排序，默认reverse=True实现逆序
# print(sorted(a, key=lambda x:x[-1]))

# ===================================lambda表达式专栏========================================

# 【1】什么是lambda
#
# 举例如下：
#
# func = lambda x: x + 1
# print(func(1))
# # 2
# print(func(2))
#
#
# # 3
#
# # 以上lambda等同于以下函数
# def func(x):
#     return (x + 1)
#
#
# 可以这样认为, lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x + 1
# 为函数体。在这里lambda简化了函数定义的书写形式。使代码更为简洁，但是使用函数的定义方式更为直观，易理解。
#
# 【2】语法
#
# 在Python中，lambda的语法是唯一的。其形式如下：
#
# lambda argument_list: expression
#
# 其中，lambda是Python预留的关键字，argument_list和expression由用户自定义。具体介绍如下。
# 导入模块：keyword，使用方法keyword.kwlist,即可列出所有内置的关键字
# argument_list是参数列表。它的结构与Python中函数(function)
# 的参数列表是一样的。具体来说，argument_list可以有非常多的形式。例如：
#
# a, b
#
# a = 1, b = 2
#
# *args
#
# ** kwargs
#
# a, b = 1, *args
#
# 空
#
# ......
#
# expression是一个关于参数的表达式。表达式中出现的参数需要在argument_list中有定义，并且表达式只能是单行的。
#
# lambda argument_list: expression表示的是一个函数。这个函数叫做lambda函数。
#
#
# 【3】特性
#
# lambda函数有如下特性：
#
# lambda函数是匿名的：所谓匿名函数，通俗地说就是没有名字的函数。lambda函数没有名字。
#
# lambda函数有输入和输出：输入是传入到参数列表argument_list的值，输出是根据表达式expression计算得到的值。
#
# lambda函数一般功能简单：单行expression决定了lambda函数不可能完成复杂的逻辑，只能完成非常简单的功能。由于其实现的功能一目了然，甚至不需要专门的名字来说明。
# expression：表达式
# 下面是一些lambda函数示例：
#
# lambda x, y: x * y；函数输入是x和y，输出是它们的积x * y
#
# lambda: None；函数没有输入参数，输出是None
#
# lambda *args: sum(args);
# 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
#
# lambda **kwargs: 1；输入是任意键值对参数，输出是1
#
# 【4】用法
#
# 由于lambda语法是固定的，其本质上只有一种用法，那就是定义一个lambda函数。在实际中，根据这个lambda函数应用场景的不同，可以将lambda函数的用法扩展为以下几种：
#
# （1）将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。
#
# 例如，执行语句add = lambda x, y: x + y，定义了加法函数lambda
# x, y: x + y，并将其赋值给变量add，这样变量add便成为具有加法功能的函数。例如，执行add(1, 2)，输出为3。
#
# （2）将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。
#
# 例如，为了把标准库time中的函数sleep的功能屏蔽(Mock)，我们可以在程序初始化时调用：time.sleep = lambda
#     x: None。这样，在后续代码中调用time库的sleep函数将不会执行原有的功能。例如，执行time.sleep(3)
# 时，程序不会休眠3秒钟，而是什么都不做。
#
# （3）将lambda函数作为其他函数的返回值，返回给调用者。
#
# 函数的返回值也可以是函数。例如return
# lambda x, y: x + y返回一个加法函数。这时，lambda函数实际上是定义在某个函数内部的函数，称之为嵌套函数，或者内部函数。对应的，将包含嵌套函数的函数称之为外部函数。内部函数能够访问外部函数的局部变量，这个特性是闭包(
#     Closure)
# 编程的基础，在这里我们不展开。
#
# （4）将lambda函数作为参数传递给其他函数。
#
# 部分Python内置函数接收函数作为参数。典型的此类内置函数有这些：
#
# filter函数。此时lambda函数用于指定过滤列表元素的条件。例如filter(lambda x: x % 3 == 0, [1, 2, 3])
# 指定将列表[1, 2, 3]
# 中能够被3整除的元素过滤出来，其结果是[3]。
#
# sorted函数。此时lambda函数用于指定对列表中所有元素进行排序的准则。例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5 - x))
# 将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]
# 按照元素与5距离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。
#
# map函数。此时lambda函数用于指定对列表中每一个元素的共同操作。例如map(lambda x: x + 1, [1, 2, 3])
# 将列表[1, 2, 3]
# 中的元素分别加1，其结果[2, 3, 4]。
#
# reduce函数。此时lambda函数用于指定列表中两两相邻元素的结合条件。例如reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
# 将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]
# 中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，其结果是
# '1, 2, 3, 4, 5, 6, 7, 8, 9'。
#
# 另外，部分Python库函数也接收函数作为参数，例如gevent的spawn函数。此时，lambda函数也能够作为参数传入。
#
# 【5】争议
#
# 事实上，关于lambda在Python社区是存在争议的。Python程序员对于到底要不要使用lambda意见不一致。
#
# 支持方认为使用lambda编写的代码更紧凑，更“pythonic”。
#
# 反对方认为，lambda函数能够支持的功能十分有限，其不支持多分支程序if... elif ... else ...
# 和异常处理程序try...except...。并且，lambda函数的功能被隐藏，对于编写代码之外的人员来说，理解lambda代码需要耗费一定的理解成本。他们认为，使用for循环等来替代lambda是一种更加直白的编码风格。
#
# 关于lambda的争执没有定论。在实际中，是否使用lambda编程取决于程序员的个人喜好。

# ===================================lambda表达式专栏结束======================================

# *（15）从列表[1,4,7,2,5,8]中索引号为3的位置开始，依次插入列表['x','y','z']的所有元素。

# a = [1,4,7,2,5,8]
# a[3:3] = ['x','y','z'] # 如果写成a[3:4],索引为3的元素2被替换成'x','y','z'
# print(a)

# *（16）快速生成由[5,50)区间内的整数组成的列表。

# 和py2不同，py3的range()函数返回的是<class 'range'>,而不是<class 'list'>
# list(range(5,50))
# print(list(range(5,50)))

# **（17）若a = [1,2,3],令b=a，执行b[0] = 9,a[0]也被改变。为什么，如何避免？

# a = [1,2,3]
# b = a
# id(a) == id(b) # 对象a和对象b在内存中是同一个，所以会出现关联
# print(id(a) == id(b))
#
# b = a.copy() # 正确的做法是复制一个新的对象
# id(a) == id(b)
# print(id(a) == id(b))

# *****（18）将列表['x','y','z']和[1,2,3]转成[('x',1),('y',2),('z',3)]的形式。

# [(a,b) for a,b in zip(['x','y','z'],[1,2,3])] # 利用了zip()函数*****
# print([(a,b) for a,b in zip(['x','y','z'],[1,2,3])]) # 变成了“a，b，a，b”型

# ===================================zip()函数专栏==========================================

# python中zip()
# 函数用法举例
#
# 定义：zip([iterable, ...])
# 　　zip()
# 是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。利用 * 号操作符，可以将list
# unzip（解压），看下面的例子就明白了：
#
# a = [1, 2, 3]
# b = [2, 3, 4]
# c = [4, 5, 6, 7]
# # 返回一个对象
# zipped = zip(a, b)
#
# # list() 转换为列表
# print(list(zipped))
# 运行结果：
# [(1, 2), (2, 3), (3, 4)]
#
# # 元素个数与最短的列表一致
# zipped = zip(a, c)
# print(list(zipped))
# print(type(zipped), zipped)
# 运行结果：
# [(1, 4), (2, 5), (3, 6)]
# <
#
# class 'zip'> < zip object at 0x000001C7C9814180 >
# # 对zip对象进行解压缩
#
#
# a1, a2 = zip(*zip(a, c))
# print(a1, a2)
# 运行结果：
# (1, 2, 3)(4, 5, 6)
# # zip对象可以转化为字典
# name_list = ["bob", "jim", "james", "julie", "june"]
# number_list = ["1", "2", "3", "4", "5"]
# name_and_number = dict(zip(name_list, number_list)) # dict：字典
# print(name_and_number)
# 运行结果：
# {'bob': '1', 'jim': '2', 'james': '3', 'julie': '4', 'june': '5'}
#
# # 搭配for循环，支持并行迭代操作方法   zip()方法用在for循环中，就会支持并行迭代：
# l1 = [2, 3, 4]
# l2 = [4, 5, 6]
# for (x, y) in zip(l1, l2):
#     print(x, y, '--', x * y)
# 运行结果：
# 2
# 4 - - 8
# 3
# 5 - - 15
# 4
# 6 - - 24
#
# 其实它的工作原理就是使用了zip()
# 的结果，在for循环里解包zip结果中的元组，用元组赋值运算。
# 就好像(x, y) = (2, 6)，赋值、序列解包操作。在对文件的操作中我们也会用到遍历，
# 例如Python遍历文件夹目录与文件操作，就是很方便实用的。
#
#
# # 二维矩阵变换（矩阵的行列互换）
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # 方法一，推导式：
# print([[row[col] for row in a] for col in range(len(a[0]))]) # row：排
# 运行结果：
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#
# # 方法二，利用zip函数：
# print(list(zip(*a)))
# print(list(map(list, zip(*a))))
# 运行结果：
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#
# 这种方法速度更快但也更难以理解，将list看成tuple解压，恰好得到我们“行列互换”的效果，
# 再通过对每个元素应用list()
# 函数，将tuple转换为list

# ===================================zip()函数专栏结束=========================================

# =====================================map()函数专栏===========================================

# map函数的原型是map(function, iterable, …)，它的返回结果是一个列表。
#
# 参数function传的是一个函数名，可以是python内置的，也可以是自定义的。
# 参数iterable传的是一个可以迭代的对象，例如列表，元组，字符串这样的。
#
# 这个函数的意思就是将function应用于iterable的每一个元素，结果以列表的形式返回。注意到没有，iterable后面还有省略号，意思就是可以传很多个iterable，如果有额外的iterable参数，并行的从这些参数中取元素，并调用function。如果一个iterable参数比另外的iterable参数要短，将以None扩展该参数元素。还是看例子来理解吧！
#
# a=(1,2,3,4,5)
# b=[1,2,3,4,5]
# c="hezhan"
#
# la=map(str,a)
# lb=map(str,b)
# lc=map(str,c)
#
# print(la)
# print(lb)
# print(lc)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 输出：
# [‘1’, ‘2’, ‘3’, ‘4’, ‘5’]
# [‘1’, ‘2’, ‘3’, ‘4’, ‘5’]
# [‘h’, ‘e’, ‘z’, ‘h’, ‘a’, ‘n’]

# =====================================map()函数专栏结束=========================================

# *（19）以列表形式返回字典{'Alice':20,'Beth':18,'Cecil':21}中所有的键。

# d = {'Alice':20,'Beth':18,'Cecil':21}
# [key for key in d.keys()] # d.keys()返回的类型是<class 'dict_keys'>
# print([key for key in d.keys()])

# （20）以列表形式返回字典{'Alice':20,'Beth':18,'Cecil':21}中所有的值。

# d = {'Alice':20,'Beth':18,'Cecil':21}
# [key for key in d.values()] # d.values()返回的类型是<class 'dict_values'>
# print([key for key in d.values()])

# （21）以列表形式返回字典{'Alice':20,'Beth':18,'Cecil':21}中所有键值对组成的元组。

# d = {'Alice':20,'Beth':18,'Cecil':21}
# [key for key in d.items()] # d.items()返回的类型是<class 'dict_items'>
# print([key for key in d.items()])

# *（22）向字典{'Alice':20,'Beth':18,'Cecil':21}中追加'David':19键值对，更新'Cecil'键的值为17。

# d = {'Alice':20,'Beth':18,'Cecil':21}
# d.update({'David':19})
# d.update({'Cecil':17})
# print(d)

# （23）删除字典{'Alice':20,'Beth':18,'Cecil':21}中的Beth键后，清空该字典。

# d = {'Alice':20,'Beth':18,'Cecil':21}
# d.pop('Beth')
# print(d)
# d.clear()
# print(d)

# （24）判断'David'和'Alice'是否在字典{'Alice':20,'Beth':18,'Cecil':21}中。

# d = {'Alice':20,'Beth':18,'Cecil':21}
# 'David' in d
# print('David' in d)
# 'Alice' in d
# print('Alice' in d)

# （25）遍历字典{'Alice':20,'Beth':18,'Cecil':21}，打印键值对。

# d = {'Alice':20,'Beth':18,'Cecil':21}
# for key in d:
#     print(key, d[key])

# （26）若 a = dict(), 令 b = a，执行 b.update({'x':1}), a也被改变。为什么？如何避免？

# a = dict()
# b = a
# id(a) == id(b) # 对象a和对象b在内存中是同一个，所以会出现关联
# print(id(a) == id(b))
#
# b = a.copy() # 正确的做法是复制一个新的对象
# id(a) == id(b)
# print(id(a) == id(b))

# ***（27）以列表['A','B','C','D','E','F','G','H']中的每一个元素为键，值默认都是0，创建一个字典。

# dict.fromkeys(['A','B','C','D','E','F','G','H'], 0)
# print(dict.fromkeys(['A','B','C','D','E','F','G','H'], 0))

# ====================================fromkeys()专栏===========================================

# fromkeys()
# 方法以序列
# seq
# 中元素做字典的键，value
# 为字典所有键对应的初始值。
# 语法：
# dict.fromkeys(seq, value=None)
# 参数：
# seq - - 字典键值列表。
# value - - 可选参数, 设置键序列（seq）对应的值，默认为
# None。
# 返回值：
# 返回一个新字典。
#
# [例]
# 想要创建一个这样的字典：
#
# >> > dict_28star = {'青龙': ['角', '亢', '氐', '房', '心', '尾', '箕'], \
#                     '玄武': ['斗', '牛', '女', '虚', '危', '室', '壁'], \
#                     '白虎': ['奎', '娄', '胃', '昴', '毕', '参', '觜'], \
#                     '朱雀': ['井', '鬼', '柳', '星', '张', '翼', '轸']}
# >> >
# >> > dict_28star
# {'青龙': ['角', '亢', '氐', '房', '心', '尾', '箕'], '玄武': ['斗', '牛', '女', '虚', '危', '室', '壁'],
#  '白虎': ['奎', '娄', '胃', '昴', '毕', '参', '觜'], '朱雀': ['井', '鬼', '柳', '星', '张', '翼', '轸']}
# 使用方法fromkeys()
# 如下：
#
# 1.
# 创建时不赋值，值为None
#
# >> > dict1 = {}
# >> > seq = ('青龙', '玄武', '白虎', '朱雀')
# >> > dict1 = dict1.fromkeys(seq)
# >> > dict1
# {'青龙': None, '玄武': None, '白虎': None, '朱雀': None}
# >> >
# 然后依次赋值，
#
# >> > dict1['青龙'] = ['角', '亢', '氐', '房', '心', '尾', '箕']
# >> > dict1['玄武'] = ['斗', '牛', '女', '虚', '危', '室', '壁']
# >> > dict1['白虎'] = ['奎', '娄', '胃', '昴', '毕', '参', '觜']
# >> > dict1['朱雀'] = ['井', '鬼', '柳', '星', '张', '翼', '轸']
# >> > dict1
# {'青龙': ['角', '亢', '氐', '房', '心', '尾', '箕'], '玄武': ['斗', '牛', '女', '虚', '危', '室', '壁'],
#  '白虎': ['奎', '娄', '胃', '昴', '毕', '参', '觜'], '朱雀': ['井', '鬼', '柳', '星', '张', '翼', '轸']}
# >> >
# 可以看到得到的是想要的效果，这里顺便查以下4个值对应的内存地址（会发现是不一样的地址），方便稍后比较
#
# >> > for v in dict1.values(): print(id(v))
#
# 1533561286792
# 1533564252744
# 1533561281480
# 1533561281096
# >> >
# 2.
# 创建时赋值，4
# 个键会共用一个值，准确来说是指向同一个位置，可以用id(value)
# 看4个值指向的内存位置，发现是一样的
#
# >> > dict2 = {}
# >> > dict2 = dict2.fromkeys(seq, ['角', '亢', '氐', '房', '心', '尾', '箕'])
# >> > dict2
# {'青龙': ['角', '亢', '氐', '房', '心', '尾', '箕'], '玄武': ['角', '亢', '氐', '房', '心', '尾', '箕'],
#  '白虎': ['角', '亢', '氐', '房', '心', '尾', '箕'], '朱雀': ['角', '亢', '氐', '房', '心', '尾', '箕']}
# >> >
# >> > for v in dict2.values(): print(id(v))
#
# 1533561281288
# 1533561281288
# 1533561281288
# 1533561281288
# >> >
# 尝试更新
# '玄武'
# 键的值，更新成功，查看其内存地址，指向了别处。
#
# >> > dict2['玄武'] = ['斗', '牛', '女', '虚', '危', '室', '壁']
# >> > dict2
# {'青龙': ['角', '亢', '氐', '房', '心', '尾', '箕'], '玄武': ['斗', '牛', '女', '虚', '危', '室', '壁'],
#  '白虎': ['角', '亢', '氐', '房', '心', '尾', '箕'], '朱雀': ['角', '亢', '氐', '房', '心', '尾', '箕']}
# >> > for v in dict2.values(): print(id(v))
#
# 1533561281288
# 1533564331336
# 1533561281288
# 1533561281288
# >> >
# 用同样的方法可以更新
# '白虎'
# 键的值和
# '朱雀'
# 键的值。
#
# 3.
# 看着没什么问题，再玩一玩会发现有坑的，例如我们不想用这种直接赋值的方法改变键的值，就是想用用给append()
# 或者给二级元素一个个赋值的方法呢？下面踩踩坑
# ~
#
# 使用
# fromkeys()
# 赋值的列表里只有一个值，创建好字典后再append。这里先考虑
# '青龙'，给它的值（一个列表）append第二个元素
# '亢'，然后会发现对4个值做了一样的操作。
#
# >> > dict3 = {}
# >> > dict3 = dict3.fromkeys(seq, ['角'])
# >> > dict3
# {'青龙': ['角'], '玄武': ['角'], '白虎': ['角'], '朱雀': ['角']}
# >> > dict3['青龙'].append('亢')
# >> > dict3
# {'青龙': ['角', '亢'], '玄武': ['角', '亢'], '白虎': ['角', '亢'], '朱雀': ['角', '亢']}
# >> > for v in dict3.values(): print(id(v))
#
# 1533564587528
# 1533564587528
# 1533564587528
# 1533564587528
# >> >
# 给值（列表）中的元素赋值，4
# 个列表也一起变
#
# >> > dict3['玄武'][0] = '斗'
# >> > dict3
# {'青龙': ['斗', '亢'], '玄武': ['斗', '亢'], '白虎': ['斗', '亢'], '朱雀': ['斗', '亢']}
# >> > for v in dict3.values(): print(id(v))
#
# 1533564587528
# 1533564587528
# 1533564587528
# 1533564587528
# >> >
# 对值（列表）使用
# pop()，4
# 个列表也一起变
#
# >> > dict3['白虎'].pop()
# '亢'
# >> > dict3
# {'青龙': ['斗'], '玄武': ['斗'], '白虎': ['斗'], '朱雀': ['斗']}
# >> > for v in dict3.values(): print(id(v))
#
# 1533564587528
# 1533564587528
# 1533564587528
# 1533564587528
# >> >
# 将值（列表）清空，4
# 个列表也一起清空
#
# >> > dict3['朱雀'].clear()
# >> > dict3
# {'青龙': [], '玄武': [], '白虎': [], '朱雀': []}
# >> > for v in dict3.values(): print(id(v))
#
# 1533564587528
# 1533564587528
# 1533564587528
# 1533564587528
# >> >
# 其实道理很简单，上述过程中，4
# 个键的值（列表）所指向的一直是内存中的同一块区域，就像公用的房间，谁装修啊拆墙啊效果大家都看得见
# ~
#
# 这个有点类似浅拷贝（传送门 -> Python
# 直接赋值、浅拷贝和深度拷贝解析
# https: // www.runoob.com / w3cnote / python - understanding - dict - copy - shallow - or -deep.html）
#
# 所以这时如果直接改变某个键的值，而非给值（列表）中的元素赋值，就不会有这种副作用。如下，改变
# '玄武'
# 的值没有影响到别人，因为其值指向了别处，可以看到它的内存位置更新了，也就是它搬家啦，它在自己的新家里购置家具，曾经的室友当然看不见咯
# ~
#
# >> > dict3['玄武'] = ['斗', '牛']
# >> > dict3
# {'青龙': [], '玄武': ['斗', '牛'], '白虎': [], '朱雀': []}
# >> > for v in dict3.values(): print(id(v))
#
# 1533564587528
# 1533564586888
# 1533564587528
# 1533564587528
# >> >
# 4.
# 那有什么应对措施吗？
#
# 首先想到的就是深拷贝，但是这种方法行不通的，因为地址虽然是新的，但是还是‘玄武’一个房间，其它三人一个房间。上文提到的“类似浅拷贝”是指，这4个列表之间的关系类似浅拷贝，把整个字典深拷贝是不能解决这个问题的。
#
# >> > import copy
# >> > dict4 = copy.deepcopy(dict3)
# >> > for v in dict4.values(): print(id(v))
#
# 1533564585992
# 1533561287368
# 1533564585992
# 1533564585992
# >> >
# 害，其实这样创建字典不也挺麻烦吗？还不如像开头那样直接创建字典
# dict_28star并同时赋值，或者像1或2那样给键的值直接赋值，省事、快捷、不留坑。
#
# 或者用个循环咯，四个人一人一屋，互不影响
#
# >> > seq
# ('青龙', '玄武', '白虎', '朱雀')
# >> > dict5 = {key: [] for key in seq}
# >> > for v in dict5.values(): print(id(v))
#
# 1533564597192
# 1533564597000
# 1533564596744
# 1533564331720
# >> >
# 所以目前看来
# dict.fromkeys()
# 应该是适合那些字典中的值要保持一致的情况吧。比如吃火锅，大家点的东西都会在锅里或者即将在锅里哈哈哈
# ~

# ====================================fromkeys()专栏结束=========================================

# （28）将二维结构[['a',1],['b',2]]和(('x',3),('y',4))转成字典。

# dict([['a',1],['b',2]])
# print(dict([['a',1],['b',2]]))
#
# dict((('x',3),('y',4)))
# print(dict((('x',3),('y',4))))

# （29）将元组(1,2)和（3,4）合并成一个元组。

# (1,2) + (3,4)
# print((1,2) + (3,4))

# （30）将空间坐标元组(1,2,3)的三个元素解包（unpacking）对应到变量x,y,z。

# x,y,z = (1,2,3)
# print(x)
# print(y)
# print(z)

# ===============================解包（unpacking）专栏========================================

# 一、什么是解包（Unpacking）
# 本文所讲的是python的星号操作符和双星号操作符，
#
# *迭代器解包操作，也称之为序列拆分操作符
#
# ** 字典解包操作，也称之为映射拆分操作。作为关键字参数传递给函数。
#
# 使用 * 和 ** 的解包的好处是能节省代码量，使得代码看起来更优雅。
#
# 解包在英文里叫做
# Unpacking，就是将容器里面的元素逐个取出来Python
# 中的解包是自动完成的，例如：
#
# >> > a, b, c = [1, 2, 3]
# >> > a
# 1
# >> > b
# 2
# >> > c
# 3
# 如果列表中有3个元素，那么刚好可以分配给3个变量。除了列表对象可以解包之外，任何可迭代对象都支持解包，可迭代对象包括元组、字典、集合、字符串、生成器等实现了__next__方法的一切对象。
#
# 元组解包
#
# >> > a, b, c = (1, 2, 3)
# >> > a
# 1
# >> > b
# 2
# >> > c
# 3
# 字符串解包
#
# >> > a, b, c = "abc"
# >> > a
# 'a'
# >> > b
# 'b'
# >> > c
# 'c'
# 字典解包
#
# >> > a, b, c = {"a": 1, "b": 2, "c": 3}
# >> > a
# 'a'
# >> > b
# 'b'
# >> > c
# 'c'
# 字典解包后，只会把字典的
# key
# 取出来，value
# 则丢掉了。
#
# 二、多变量的赋值与交换
# 你可能见过多变量赋值操作，例如：
#
# >> > a, b = 1, 2
# >> > a
# 1
# >> > b
# 2
# 本质上也是自动解包过程，等号右边其实是一个元组对象(1, 2)，有时候我们代码不小心多了一个逗号,，就变成了元组对象
#
# >> > a = 1,
# >> > a
# (1,)
#
# ----------
# >> > a = 1
# >> > a
# 1
# 所以写代码的时候需要特别注意。在
# Python
# 中，交换两个变量非常方便，本质上也是自动解包过程。
#
# >> > a, b = 1, 2
# >> > a, b = b, a
# >> > a
# 2
# >> > b
# 1
# 如果在解包过程中，遇到左边变量个数小于右边可迭代对象中元素的个数时该怎么办？ 好比你们家有3口人，你老婆却买了4个苹果，怎么分配呢？
#
# 在
# Python2
# 中，如果等号左边变量的个数不等于右边可迭代对象中元素的个数，是不允许解包的。但在
# Python3
# 可以这么做了。这个特性可以在
# PEP
# 3132
# 中看到。
#
# >> > a, b, *c = [1, 2, 3, 4]
# >> > a
# 1
# >> > b
# 2
# >> > c
# [3, 4]
# >> >
# 这种语法就是在某个变量面前加一个星号，而且这个星号可以放在任意变量，每个变量都分配一个元素后，剩下的元素都分配给这个带星号的变量
#
# >> > a, *b, c = [1, 2, 3, 4]
# >> > a
# 1
# >> > b
# [2, 3]
# >> > c
# 4
# 这种语法有什么好处呢？它使得你的代码写起来更简洁，比如上面例子，在
# Python2
# 中该怎么操作呢？思考3秒钟，再看答案。
#
# >> > n = [1, 2, 3, 4]
# # 使用切片操作
# >> > a, b, c = n[0], n[1:-1], n[-1]
# >> > a
# 1
# >> > b
# [2, 3]
# >> > c
# 4
# 三、序列只包含一个元素的解包
# 我们常常看见这样的操作，
#
# line, = plt.plot()  # 这里的逗号不能丢，为什么呢
#
# 因为plot函数返回的是一个列表，而且如果只画一条线的时候，也是以列表的形式给出的
#
# a, = [1, 2, 3]  # 错误，此时列表元素不是一个，会报错
# a, = (1, 2)  # 错误，此时元组元素不是一个，会报错
# # -------------------------------------------
# a, = [11]  # 列表只包含一个元素
# print(a)
# # 等价于下面
# a = [11]
# print(a[0])
# # -------------------------------------------
# a, = (11,)  # 这里括号里面的逗号不能丢，如果是（11）指的是int 11，只有加上逗号，才表示是一个元素的             元组
# print(a)
# 四、解包在函数中的应用
# 以上是表达式解包的一些操作，接下来介绍函数调用时的解包操作。函数调用时，有时你可能会用到两个符号：星号 * 和
# 双星号 **。
#
# >> >
#
# def func(a, b, c):
#     ...
#     print(a, b, c)
#
#
# ...
# >> > func(1, 2, 3)
# 1
# 2
# 3
# func
# 函数定义了三个位置参数
# a，b，c，调用该函数必须传入三个参数，除此之外，你也可以传入包含有3个元素的可迭代对象，
#
# >> > func(*[1, 2, 3])
# 1
# 2
# 3
# >> > func(*(1, 2, 3))
# 1
# 2
# 3
# >> > func(*"abc")
# a
# b
# c
# >> > func(*{"a": 1, "b": 2, "c": 3})
# a
# b
# c
# 函数被调用的时候，使用星号 * 解包一个可迭代对象作为函数的参数。字典对象，可以使用两个星号，解包之后将作为关键字参数传递给函数
#
# >> > func(**{"a": 1, "b": 2, "c": 3})
# 1
# 2
# 3
# 看到了吗？和上面例子的区别是多了一个星号，结果完全不一样，原因是什么？ 答案是 ** 符号作用的对象是字典对象，它会自动解包成关键字参数
# key = value
# 的格式：
#
# >> > func(a=1, b=2, c=3)
# 1
# 2
# 3
# 如果字典对象中的
# key
# 不是
# a，b，c，会出现什么情况？请读者自行测试。
#
# 总结一下，一个星号可作用于所有的可迭代对象，称为迭代器解包操作，作为位置参数传递给函数，两个星号只能作用于字典对象，称之为字典解包操作，作为关键字参数传递给函数。使用 * 和 ** 的解包的好处是能节省代码量，使得代码看起来更优雅，不然你得这样写：
#
# >> > d = {"a": 1, "b": 2, "c": 3}
# >> > func(a=d['a'], b=d['b'], c=d['c'])
# 1
# 2
# 3
# >> >
# 到这里，解包还没介绍完，因为
# Python3
# .5，也就是
# PEP
# 448
# 对解包操作做了进一步扩展， 在
# 3.5
# 之前的版本，函数调用时，一个函数中解包操作只允许一个 * 和
# 一个 **。从
# 3.5
# 开始，在函数调用中，可以有任意多个解包操作，例如：
#
# # Python 3.4 中 print 函数 不允许多个 * 操作
# >> > print(*[1, 2, 3], *[3, 4])
# File
# "<stdin>", line
# 1
# print(*[1, 2, 3], *[3, 4])
# ^
# SyntaxError: invalid
# syntax
# >> >
# 再来看看
# python3
# .5
# 以上版本
#
# # 可以使用任意多个解包操作
# >> > print(*[1], *[2], 3)
# 1
# 2
# 3
# 从
# 3.5
# 开始可以接受多个解包，于此同时，解包操作除了用在函数调用，还可以作用在表达式中。
#
# >> > *range(4), 4
# (0, 1, 2, 3, 4)
# >> > [*range(4), 4]
# [0, 1, 2, 3, 4]
# >> > {*range(4), 4}
# {0, 1, 2, 3, 4}
# >> > {'x': 1, **{'y': 2}}
# {'x': 1, 'y': 2}
# 新的语法使得我们的代码更加优雅了，例如拼接两个列表可以这样：
#
# >> > list1 = [1, 2, 3]
# >> > list2 = range(3, 6)
# >> > [*list1, *list2]
# [1, 2, 3, 3, 4, 5]
# >> >
# 可不可以直接用 + 操作呢？不行，因为
# list
# 类型无法与
# range
# 对象相加，你必须先将
# list2
# 强制转换为
# list
# 对象才能做 + 操作，这个留给读者自行验证。
#
# 再来看一个例子：如何优雅的合并两个字典
#
# >> > a = {"a": 1, "b": 2}
# >> > b = {"c": 3, "d": 4}
# >> > {**a, **b}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 在3
# .5
# 之前的版本，你不得不写更多的代码：
#
# >> > import copy
# >> >
# >> > c = copy.deepcopy(a)
# >> > c.update(b)
# >> > c
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 到此，关于
# Python
# 解包给你介绍完了，如果本文对你有收获，请点赞、转发支持。
#
# 最后给你总结一下：
#
# 自动解包支持一切可迭代对象
#
# python3中，支持更高级的解包操作，用星号操作使得等号左边的变量个数可以少于右边迭代对象中元素的个数。
#
# 函数调用时，可以用 * 或者 ** 解包可迭代对象，作为参数传递
#
# python3
# .5，函数调用和表达式中可支持更多的解包操作。

# ===============================解包（unpacking）专栏结束======================================

# （31）返回元组('Alice','Beth','Cecil')中'Cecil'元素的索引号。

# ('Alice','Beth','Cecil').index('Cecil')
# print(('Alice','Beth','Cecil').index('Cecil'))

# （32）返回元组(2,5,3,2,4)中元素2的个数。

# (2,5,3,2,4).count(2)
# print((2,5,3,2,4).count(2))

# （33）判断'Cecil'是否在元组('Alice','Beth','Cecil')中。

# 'Cecil' in ('Alice','Beth','Cecil')
# print('Cecil' in ('Alice','Beth','Cecil'))

# **（34）返回在元组(2,5,3,7)中索引号为2的位置插入元素9之后的新元组。

# (*(2,5,3,7)[:2], 9, *(2,5,3,7)[2:])
# print((*(2,5,3,7)[:2], 9, *(2,5,3,7)[2:]))

# （35）创建一个空集合，增加{'x','y','z'}三个元素。

# a = set()
# a.update({'x','y','z'})
# print(a)

# （36）删除集合{'x','y','z'}中的元素'z'，增加元素'w',然后清空整个集合。

# a = {'x','y','z'}
# a.remove('z')
# a.add('w')
# print(a)
# a.clear()
# print(a)

# *（37）返回集合{'A','D','B'}中未出现在集合{'D','E','C'}中的元素（差集）。

# a = {'A','D','B'}
# b = {'D','E','C'}
# a.difference(b) # 返回a有b没有的元素集合
# print(a.difference(b))
#
# a - b # 记不住的话，这样也行
# print(a - b)

# *（38）返回两个集合{'A','D','B'}和{'D','E','C'}的并集。

# a = {'A','D','B'}
# b = {'D','E','C'}
# a.union(b) # 返回a和b的并集，虽然差集可以用a-b替代，但并集不能用a+b表示。
# print(a.union(b)) # union:并集 联合 联邦 结合

# *（39）返回两个集合{'A','D','B'}和{'D','E','C'}的交集。

# a = {'A','D','B'}
# b = {'D','E','C'}
# a.intersection(b) # 返回a和b重复元素的集合 intersection:交集 十字路口 交叉点 交点
# print(a.intersection(b))

# *（40）返回两个集合{'A','D','B'}和{'D','E','C'}未重复元素的集合。

# a = {'A','D','B'}
# b = {'D','E','C'}
# a.symmetric_difference(b) # 返回a和b未重复元素的集合 symmetric_difference:对称差分
# print(a.symmetric_difference(b))

# *（41）判断两个集合{'A','D','B'}和{'D','E','C'}中是否有重复元素。

# a = {'A','D','B'}
# b = {'D','E','C'}
# a.isdisjoint(b) # 判断a和b是否不包含相同的元素，无则返回True，有则返回False
# print(a.isdisjoint(b)) # isdisjoint:判断是否无交集 不能加入
#
# not a.isdisjoint(b) # 取反才是本题的正确答案！
# print(not a.isdisjoint(b))

# *（42）判断集合{'A','C'}是否是集合{'D','C','E','A'}的子集。

# a = {'A','C'}
# b = {'D','C','E','A'}
# a.issubset(b) # issubset:子集
# print(a.issubset(b))

# *（43）去除数组[1,2,3,2,3,4,5,'x',4,'x']中的重复元素。

# list(set([1,2,3,2,3,4,5,'x',4,'x'])) # 利用了set集合无序不可重复的特性进行元素过滤
# print(list(set([1,2,3,2,3,4,5,'x',4,'x'])))

# *（44）返回字符串'abCdEfg'的全部大写、全部小写和大小写互换形式。

# s = 'abCdEfg'
# s.upper() # 全部大写 upper：上等的、上位的、鞋面
# s.lower() # 全部小写 lower：降低 调低 走低
# s.swapcase() # 大小写互换 swapcase：大小写互换 但是它会把大写字母换成小写 大小写相互转换 将字符串大小写交换
# print(s.upper(),s.lower(),s.swapcase())

# *（45）判断字符串'abCdEfg'首字母是否大写，字母是否全部小写，字母是否全部大写。

# s = 'abCdEfg'
# s.istitle() # 首字母是大写
# s.islower() # 字母是全部小写
# s.isupper() # 字母是全部大写
# print(s.istitle(),s.islower(),s.isupper())

# *（46）返回字符串'this is python'首字母大写以及字符串内每个单词首字母大写的形式。

# s = 'this is python'
# s.capitalize() # capitalize:资本化 首字母大写 首字符大写 title:标题，首字母大写
# s.title()
# print(s.capitalize(),s.title())

# *（47）判断字符串'this is python'是否是以'this'开头，又是否以'python'结尾。

# s = 'this is python'
# s.startswith('this') # startswith：以 以…开头 开头 如果 endswith：以 以…结尾 结尾 如果
# s.endswith('python')
# print(s.startswith('this'),s.endswith('python'))

# （48）返回字符串'this is python'中'is'的出现次数。

# s = 'this is python'
# s.count('is')
# print(s.count('is'))

# *（49）返回字符串'this is python'中'is'首次出现和最后出现的位置。

# s = 'this is python'
# s.find('is') # 首次出现的索引号，未找到则返回-1 find:查找 rfind；反向查找 从后向前查找字符 从右往左按区间查找 查找某个内容最后一次出现的位置
# s.rfind('is') # 最后出现的索引号，未找到则返回-1
# print(s.find('is'),s.rfind('is'))

# （50）将字符串'this is python'切片成三个单词。

# s = 'this is python'
# s.split() # 无参数，则默认使用空格切片，且自动忽略多于空格 split：斯普利特 分割 拆分
# print(s.split())

# *（51）返回字符串'blog.csdn.net/hezhan/article/details/102946961'按路径分隔符切片的结果。

# s = 'blog.csdn.net/hezhan/article/details/102946961'
# s.split('/')
# print(s.split('/'))

# ***（52）将字符串'2.72,5,7,3.14'以半角逗号切片后，再将各个元素转成浮点型或整型。

# s = '2.72,5,7,3.14'
# [float(item) if '.' in item else int(item) for item in s.split(',')] # 三元表达式
# print([float(item) if '.' in item else int(item) for item in s.split(',')])

# *（53）判断字符串 'adS12K56' 是否完全为字母或数字，是否全为数字，是否全为字母，是否全为ASCII码。

# s = 'adS12K56'
# s.isalnum() # 完全为字母或数字
# s.isdigit() # 全为数字
# s.isalpha() # 全为字母
# s.isascii() # 全为ASCII码
# print(s.isalnum(),s.isdigit(),s.isalpha(),s.isascii)

# **（54）将字符串 'there is python' 中的 'is' 替换为 'are'。

# 'there is python'.replace('is','are') # replace:替换 取代 接替 更换
# print('there is python'.replace('is','are'))

# *（55）清除字符串 '\t python \n' 左侧、右侧，以及左右两侧的空白字符。

# s = '\t python \n'
# s.lstrip() # 清除左侧空白字符 lstrip：去除前面的空白字符 移除左边的空格 只去掉左边的
# s.rstrip() # 清除右侧空白字符 rstrip：去除后面的空白字符 移除右边的空格 只去掉右边的
# s.strip() # 清除左右两侧空白字符 strip：条子 脱衣 长片 去除
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())

# **（56）将三个全英文字符串（例如，'ok', 'hello', 'thank you'）分行打印，实现左对齐、
# 右对齐和居中对齐效果。

# a = ['ok', 'hello', 'thank you']
# len_max = max([len(item) for item in a]) # len_max为最长字符串的长度
# for item in a:
#     print('"%s"'%item.ljust(len_max)) # ljust:右边补齐 左对齐 将字符串置于最左边
#
# for item in a:
#     print('"%s"' %item.rjust(len_max)) # rjust :右对齐
#
# for item in a:
#     print('"%s"' %item.center(len_max)) # center:居中

# **（57）将三个字符串（比如，'Hello, 我是David', 'OK, 好', '很高兴认识你'）分行打印，实现左对齐、
# 右对齐和居中效果。

# a = ['Hello, 我是David', 'OK, 好', '很高兴认识你']
# a_len = [len(item) for item in a] # 各字符串长度
# a_len_gbk = [len(item.encode('gbk')) for item in a] # gbk编码的字节码长度
# c_num = [a-b for a,b in zip(a_len_gbk, a_len)] # 各字符串包含的中文符号个数
# len_max = max(a_len_gbk) # 最大字符串占位长度
# for s, c in zip(a, c_num):
#     print('"%s"'%s.ljust(len_max-c)) # 左对齐
#
# for s,c in zip(a, c_num):
#     print('"%s"'%s.rjust(len_max-c)) # 右对齐
#
# for s,c in zip(a, c_num):
#     print('"%s"'%s.center(len_max-c)) # 居中对齐

# =====================================item()专栏==========================================

# 1.
# get()
# 当我们获取字典里的值的时候，一个是通过键值对，即dict['key'], 另一个就是dict.get()
# 方法。
#
# 例如：
#
# >> > dict = {'a': 'AA', 'b': 'BB', 'c': 'CC'}
# >> > dict['a']
# 'AA'
# >> > dict.get('a')
# 'AA'
# get()
# 方法语法：
# dict.get(key, default=None)
# key - - 字典中要查找的键。
# default - - 如果指定键的值不存在时，返回该默认值。
#
# 例如：
#
# >> > dict.get('d', 'error')
# 'error'
# 2.
# items()
# 这篇文章主要介绍了Python中使用items()
# 方法遍历字典的例子,
# for ...in这种是Python中最常用的遍历字典的方法了, 需要的朋友可以参考下
#
# Python字典的遍历方法有好几种，其中一种是for... in，这个我就不说明，在Python了几乎随处都可见for... in。下面说的这种遍历方式是items()
# 方法。
#
# items()
#
# items()
# 方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回。
#
# 代码如下:
#
# # from keras.datasets import mnist
# person = {'name': 'lizhong', 'age': '26', 'city': 'BeiJing'}
#
# for key, value in person.items():
#     print('key=', key, 'value=', value)
#
# 执行结果：
# key = name value = hezhan
# key = age value = 19
# key = city value = He Nan
#
#
# 可见key接收了字典的key，value接收了字典的value值。
# 但如果只有一个参数接收呢？
#
# 代码如下:
#
# # from keras.datasets import mnist
# person = {'name': 'lizhong', 'age': '26', 'city': 'BeiJing'}
#
# for x in person.items():
#     print('x=', x)
# 执行结果:
#
# x = ('name','hezhan')
# x = ('age','19')
# x = ('city','He Nan')
#
# 只有一个变量接收值的情况下，直接返回的是每一对key, value对应的元组。
#
# 使用item()
# 就有点类似于php里的foreach类似。都能把键 = > 值的方式遍历出来，如果纯使用for..in则只能取得每一对元素的key值
#
# 如代码：
#
# 代码如下:
#
# # from keras.datasets import mnist
# person = {'name': 'lizhong', 'age': '26', 'city': 'BeiJing', 'blog': 'www.jb51.net'}
#
# for x in person:
#     print('x=', x)
# 执行结果：
#
# x = name
# x = age
# x = city
# x = blog

# =====================================item()专栏结束========================================

# **（58）将三个字符串 '15', '127', '65535' 左侧补0成同样长度。

# a = ['15', '127', '65535']
# len_max = max([len(item) for item in a])
# for item in a:
#     print(item.zfill(len_max)) # zfill:填充

# *（59）提取 url 字符串 'https://blog.csdn.net/hezhan/details/102993570' 中的协议名。

# 'https://blog.csdn.net/hezhan/details/102993570'.split('/',2)[0][:-1] # 分割两次，
# 并取序列为0的项
# a[:-1]：数组切片，用的比较多，表示不含有a最后一个元素，左闭右开的，
# 如果a是二维的，表示不含有a的最后一行，高维也类似。
# print('https://blog.csdn.net/hezhan/details/102993570'.split('/',2)[0][:-1])

# =====================================split()专栏===========================================

# 函数：split()
#
# Python中有split()
# 和os.path.split()
# 两个函数，具体作用如下：
# split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
# os.path.split()：按照路径将文件名和路径分割开
#
# 一、函数说明
#
# 1、split()
# 函数
# 语法：str.split(str="", num=string.count(str))[n]
#
# 参数说明：
# str: 表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
# num: 表示分割次数。如果存在参数num，则仅分隔成
# num + 1
# 个子字符串，并且每一个子字符串可以赋给新的变量
# [n]: 表示选取第n个分片
#
# 注意：当使用空格作为分隔符时，对于中间为空的项会自动忽略
#
# 2、os.path.split()
# 函数
# 语法：os.path.split('PATH')
#
# 参数说明：
#
# 1.
# PATH指一个文件的全路径作为参数：
#
# 2.
# 如果给出的是一个目录和文件名，则输出路径和文件名
#
# 3.
# 如果给出的是一个目录名，则输出路径和为空文件名
#
# 二、分离字符串
#
# string = "www.gziscas.com.cn"
#
# 1.
# 以
# '.'
# 为分隔符
#
# print(string.split('.'))
#
# ['www', 'gziscas', 'com', 'cn']
#
# 2.
# 分割两次
#
# print(string.split('.'，2))
#
# ['www', 'gziscas', 'com.cn']
#
# 3.
# 分割两次，并取序列为1的项
#
# print(string.split('.', 2)[1])
#
# gziscas
#
# 4.
# 分割两次，并把分割后的三个部分保存到三个文件
#
# u1, u2, u3 = string.split('.', 2)
#
# print(u1)—— www
#
# print(u2)—— gziscas
#
# print(u3) ——com.cn
#
# 三、分离文件名和路径
#
# import os
#
# print(os.path.split('/dodo/soft/python/'))
#
# ('/dodo/soft/python', '')
#
# print(os.path.split('/dodo/soft/python'))
#
# ('/dodo/soft', 'python')
#
# 四、实例
#
# str = "hello boy<[www.baidu.com]>byebye"
#
# print(str.split("[")[1].split("]")[0])

# =====================================split()专栏结束=========================================

# ===================================关于数组切片的理解========================================

# python 一维或二维数组中的 [:-1] [::-1]的理解：
# a[:-1]，数组切片，用的比较多，表示不含有a最后一个元素，左闭右开的，如果a是二维的，表示不含
# 有a的最后一行，高维类似
#
# a[::-1]
# 表示将一维数组a反转，如果a是二维的，按第一维反转（第一维为a.shape[0]）
#
# 例如：
#
# import numpy as np
#
# a = [[1.0, 2.0, 3.0, 4.0],
#      [5.0, 6.0, 7.0, 8.0]]
# a = np.array(a)
# b = a[1]
# b_1 = b[:-1]
# b_2 = b[::-1]
# a_1 = a[:-1]
# a_2 = a[::-1]
# print('a:', a)
# print('b:', b)
# print('b_1:', b_1)
# print('b_2:', b_2)
# print('a_1:', a_1)
# print('a_2:', a_2)
#
# ========================================数组切片理解结束====================================

# *（60）将列表 ['a','b','c'] 中各个元素用'|'连接成一个字符串。

# '|'.join(['a','b','c']) # join:连接 加入 参加 合并
# print('|'.join(['a','b','c']))

# =====================================join()专栏===========================================

# 函数：string.join()
#
# Python中有join()和os.path.join()两个函数，具体作用如下：
#     join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
#     os.path.join()：  将多个路径组合后返回
#
# 一、函数说明
# 1、join()函数
# 语法：  'sep'.join(seq)
# 参数说明
# sep：分隔符。可以为空
# seq：要连接的元素序列、字符串、元组、字典
# 上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
#
# 返回值：返回一个以分隔符sep连接各个元素后生成的字符串
#
#
#
#
# 2、os.path.join()函数
# 语法：  os.path.join(path1[,path2[,......]])
# 返回值：将多个路径组合后返回
#
# 注：第一个绝对路径之前的参数将被忽略
#
#
#
#
# 二、实例
# #对序列进行操作（分别使用' '与':'作为分隔符）
# >>> seq1 = ['hello','good','boy','doiido']
# >>> print ' '.join(seq1)
# hello good boy doiido
# >>> print ':'.join(seq1)
# hello:good:boy:doiido
#
# #对字符串进行操作
# >>> seq2 = "hello good boy doiido"
# >>> print ':'.join(seq2)
# h:e:l:l:o: :g:o:o:d: :b:o:y: :d:o:i:i:d:o
#
# #对元组进行操作
# >>> seq3 = ('hello','good','boy','doiido')
# >>> print ':'.join(seq3)
# hello:good:boy:doiido
#
# #对字典进行操作
# >>> seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}
# >>> print ':'.join(seq4)
# boy:good:doiido:hello
#
# #合并目录
# >>> import os
# >>> os.path.join('/hello/','good/boy/','doiido')
# '/hello/good/boy/doiido'

# =====================================join()专栏结束==========================================

# （61）将字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串。

# ','.join('abc')
# print(','.join('abc'))

# （62）从键盘输入手机号码，输出形如 'Mobile: 186 6677 7788' 的字符串。

# def print_mobile(): # 定义一个输出手机号的函数
#     num = input('请输入手机号码：') # 用num接收用户输入
#     print('Mobile: %s %s %s'%(num[:3], num[3:7], num[7:])) # 格式化输出
#     # (num[:3]:0~2三位数字切一片，num[3:7]：3~6四位数字切一片，num[7:]：数字7~末尾切一片
#
# print_mobile()

# *（63）从键盘输入六组数，分别表示年、月、日、时、分、秒，中间以空格分隔，输出形如
# '2019-05-01 12:00:00' 的字符串。

# def print_detatime(): # 定义一个时间输出函数
#     dt = input('请输入年月时分秒，中间以空格分隔：') # 用dt接收用户输入的时间
#     Y, M, D, h, m, s = dt.split() # 年月时分秒=用户输入的时间分割
#     Y, M, D, h, m, s = int(Y),int(M),int(D),int(h),int(m),int(s) # 都为int型数据
#     print('%04d-%02d-%02d %02d:%02d:%02d'%(Y, M, D, h, m, s))
#
# print_detatime()

# （64）给定两个浮点数 3.1415926 和 2.7182818，格式化输出字符串 'pi = 3.1416, e = 2.7183'。

# 'pi = %0.4f, e = %0.4f'%(3.1415926, 2.7182818)
# print('pi = %0.4f, e = %0.4f'%(3.1415926, 2.7182818))

# *（65）将 0.00774592 和 356800000 格式化输出为科学计数法表示的字符串。

# '%E, %e'%(0.00774592, 356800000)
# print('%E, %e'%(0.00774592, 356800000))

# *（66）将十进制整数 240 格式化为八进制和十六进制的字符串。

# '%o'%240 # o:octal,八进制
# print('%o'%240)
# '%x'%240 # x：hexadecimal，十六进制
# print('%x'%240)

# *（67）将十进制整数 240 转为二进制、八进制、十六进制的字符串。

# bin(240) # bin:二进制
# print(bin(240))
# oct(240) # oct：八进制
# print(oct(240))
# hex(240) # hex：十六进制
# print(hex(240))

# *（68）将字符串 '10100' 按照二进制、八进制、十进制、十六进制转为整数。

# int('10100', base=2) # base:基底；基础
# int('10100', base=8)
# int('10100', base=10)
# int('10100', base=16)
# print(int('10100', base=2,),int('10100', base=8),int('10100', base=10),int('10100', base=16))

# *（69）求二进制整数1010、八进制整数65、十进制整数52、十六进制整数b4的和。

# 0b1010 + 0o65 +52 + 0xb4 # 0b:二进制、0o：八进制、0x：十六进制，妙啊！
# print(0b1010 + 0o65 +52 + 0xb4)

# *（70）将列表 [0,1,2,3.14,'x',None,'',list(),{5}] 中的各个元素转为布尔型。

# [bool(item) for item in [0,1,2,3.14,'x',None,'',list(),{5}]]
# print([bool(item) for item in [0,1,2,3.14,'x',None,'',list(),{5}]])

# *（71）返回字符 'a' 和 'A' 的ASCII编码值

# ord('a'), ord('A')
# print(ord('a'), ord('A'))

# ====================================关于ord()函数==========================================

# chr()、unichr()和ord()
# chr()函数用一个范围在range（256）内的（就是0～255）整数作参数，返回一个对应的字符。unichr()跟它一样，只不过返回的是Unicode字符，这个从Python 2.0才加入的unichr()的参数范围依赖于你的Python是如何被编译的。如果是配置为USC2的Unicode，那么它的允许范围就是range（65536）或0x0000-0xFFFF；如果配置为UCS4，那么这个值应该是range（1114112）或0x000000-0x110000。如果提供的参数不在允许的范围内，则会报一个ValueError的异常。
#
# ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值，如果所给的Unicode字符超出了你的Python定义范围，则会引发一个TypeError的异常。
#
# >>> chr(65)
#
# 'A'
#
# >>> ord('a')
#
# 97
#
# >>> unichr(12345)
#
# u'\u3039'
#
# >>> chr(12345)
#
# Traceback (most recent call last):
#
#    File "<stdin>", line 1, in ?
#
#      chr(12345)
#
# ValueError: chr() arg not in range(256)
#
# >>> ord(u'\ufffff')
#
# Traceback (most recent call last):
#
#    File "<stdin>", line 1, in ?
#
#      ord(u'\ufffff')
#
# TypeError: ord() expected a character, but string of length 2 found
#
# >>> ord(u'\u2345')
#
# 9029

# ====================================关于ord()函数结束========================================

# *（72）返回ASCII编码值为 57 和 122 的字符。

# chr(57), chr(122)
# print(chr(57), chr(122))

# ***（73）将二维列表 [[0.468,0.975,0.446],[0.718,0.826,0.359]] 写成名为 csv_data 的 .csv
# 格式的文件，并尝试用 Excel 打开它。

# with open(r'D:\csv_data.csv','w') as fp:
#     for row in [[0.468,0.975,0.446],[0.718,0.826,0.359]]:
#         line_len = fp.write('%s\n'%(','.join([str(col) for col in row])))

# ***（74）从 csv_data.csv 文件中读出二维列表。

# data = list() # 文件是列表形式
# with open(r'D:\csv_data.csv','r') as fp:
#     for line in fp.readlines(): # 行读取
#         data.append([float(item) for item in line.strip().split(',')]) # 浮点数，逗号分隔
#    print(data)

# ***（75）向 csv_data.csv 文件追加二维列表 [[1.468,1.975,1.446],[1.718,1.826,1.359]]，然后读出所有数据。

# with open(r'D:\csv_data.csv','a') as fp: # a代表append/add
#     for row in [[1.468,1.975,1.446],[1.718,1.826,1.359]]: # row:代表xlsx文档的排
#         line_len = fp.write('%s\n'%(','.join([str(col) for col in row]))) # clo：代表xlsx文档的列
#
# data = list()
# with open(r'D:\csv_data.csv','r') as fp:
#     for line in fp.readlines(): # 行读取
#          data.append([float(item) for item in line.strip().split(',')]) # 浮点数，逗号分隔
#     print(data)

# ====================================关于Python自动化办公===========================================

# python row函数_Python 自动化办公 — 处理 Excel 文件！
#
# 橙子青提 2021-01-21 16:06:29  46  收藏
# 文章标签： python row函数

# openpyxl 介绍
# openpyxl 是一个直接可用于读写 xlsx 、xlsm、xltx、xltm 文件的 Python 内置库，借助它可以利用 Python 语法对本地 xlsx 文件进行自动化批量操作
#
# 先说一下安装部分，如果小伙伴们用 Anaconda 作为 Python 环境的话，openpyxl 无需安装可直接使用；需要安装的话方法也非常简单  pip 工具一行命令即可
#
# pip install openpyxl
# xlsx 文件属性
# 在对 Excel 表格处理之前，需要了解一下 xlsx 文件的几个名词解释及构造
#
# 1，Workbook 指的是什么？
#
# Workbook 名叫工作薄，可以代指一个 xlsx 文件；
#
# 2， sheet、cell、row 、col 分别指的是什么？
#
# 关于问题2 ，可参考下图(见注释)
#
#
# openpyxl 基本命令操作
# 1， 创建 一个空的 workbook
# from openpypl import Wrokbook
# from openpyxl.utils import get_column_letter
#
# wb = Workbook()
# ws1 = wb.active
# 一个 Workbook 默认至少含有一个 worksheet ，通过命令 Workbook.active 来获取当前第一个 sheet(也就是第一个 sheet)；
#
# 2，创建新的 worksheet
# ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
#
# ws2 = wb.create_sheet("Mysheet", 0) # insert at first position
# # or
# ws3 = wb.create_sheet("Mysheet", -1) # insert at the penultimate position
# 可通过 create_sheet() 命令创建新的 worksheet ， create_sheet 默认有两个参数 name、index;
#
# name，定义 sheet 的名字；
# index，来设置插入 sheet 的位置，默认为 None 即新创建的 sheet 插入到最后面；0 代表插入第一个 sheet 的位置；
# 3，更改 sheet 的名字
# 一行代码即可
#
# ws.title = 'New Title'
# 4，更改 sheet 上 tab 背景颜色
# ws.sheet_properties.tabColor = "1072BA"
# 通过修改 Wroksheet.sheet_properties.tabColor 参数即可，需要注意的是这里只接收 RRGGBB 颜色代码；
#
# 关于不清楚 sheet tab 背景颜色不清楚是什么的小伙伴，可参考下图；
#
#
# 5,  返回 Workbook 中所有 sheet 的名字
# 通过 Workbook.sheetname 命令即可查看
#
# >>> print(wb.sheetnames)
# ['Sheet2', 'New Title', 'Sheet1']
#
# # 或者用迭代方法
#
# >>> for sheet in wb:
# ...     print(sheet.title)
# 6，将现有的 worksheets 复制新创建的 workbook 中
# 可通过 Workbook.copy_worksheet()函数方法
#
# # 将 source 中的worksheet复制到 target 中去
#
# source = wb.active
# target = wb.copy_worksheet(source)
# 需要注意的是，当 workbook 为只读或 只写模式时不可复制；另外只有 cells(值，样式，超链接、注释) 和 特定的 worksheet 属性(维度、格式、属性)可以复制，其他的一些 workbook / worksheet 属性不可复制( Images Charts 等)
#
# 7，获取某个 cell 的数据
# 成功创建完 Workbook、Worksheet 之后，接下来就可以修改 cell(单元格中的内容，Cells 可以通过 worksheet 中特有关键词来获取
#
# >>> c = ws['A4'] # 获取第4行列名为A 单元格中的值
# 通过赋值命令对其修改
#
# ws['A4'] = 4
# openpyxl 中有一个函数 Worksheet.cell() 可修改单元格中的数据，可定位到具体行、具体列进行更改，
#
# d = ws.cell(row = 4,columns = 2,value = 10)
# row 表示指定行
# columns 表示指定列
# value 表示该单元格中需替代的数据值；当此参数不设置时表示只对该 cell 创建内存空间，不赋值
# 例如
#
# >>> for x in range(1,101):
# ...        for y in range(1,101):
# ...            ws.cell(row=x, column=y)
# 8，获取多个单元格
# 8.1 , openpyxl 也可以进行切片操作，来获取多个单元格
#
# >>> cell_range = ws['A1':'C2']
# 8.2， worksheet 中多行多列数据获取方式相似
#
# >>> colC = ws['C']
# >>> col_range = ws['C:D']
# >>> row10 = ws[10]
# >>> row_range = ws[5:10]
# 8.3，Worksheet.iter_row() 来获取 sheet 中行列范围，再利用循环迭代获取每一个单元格数据
#
# >>> for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
# ...    for cell in row:
# ...        print(cell)
# 8.4，Worksheet.iter_cols() 也可以实现同样功能
#
# >>> for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
# ...     for cell in col:
# ...         print(cell)
# 需要注意的是在 read-only 模式中，Worksheet,iter_cols() 方法不能使用
#
# 9，只查看 cell 中的 value
# 9.1，只查看 worksheet 中的 value 时，可通过 Worksheet.values 属性，该属性将迭代 worksheet 中所有行，但返回的仅仅是 cell values
#
# for row in ws.values:
#    for value in row:
#      print(value)
# 9.2，通过 Worksheet.iter_rows() 和 Worksheet.iter_cols() 也可以实现，在函数中加入一个参数 values_only = True 即可返回 cell 的值
#
# >>> for row in ws.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
# ...   print(row)
#
# (None, None, None)
# (None, None, None)
# 10，读写文件操作
# 10.1，excel 文件加载
# openpyxl.load_workbook() 函数来打开一个指定本地存储的 xlsx 文件
#
# >>> from openpyxl import load_workbook
# >>> wb2 = load_workbook('test.xlsx')
# >>> print wb2.sheetnames
# ['Sheet2', 'New Title', 'Sheet1']
# 10.2，excel 文件存储
# Workbook 修改成功后，后创建完成之后，通过Workbook.save(path) 命令即可保存至本地磁盘
#
# >>> wb = Workbook()
# >>> wb.save('balances.xlsx')
# ————————————————
# 版权声明：本文为CSDN博主「橙子青提」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_32968239/article/details/113492024

# ====================================关于Python自动化办公结束=========================================

# （76）交换变量 x 和 y 的值。

# x, y = 3, 4
# x, y = y, x
# print(x,y)

# *（77）判断给定的参数 x 是否是整型。

# x = 3.14
# isinstance(x, int)
# print(isinstance(x, int))

# *（78）判断给定的参数 x 是否为列表或元组

# x = list()
# isinstance(x, (list,tuple))
#
# x = tuple()
# isinstance(x, (list,tuple))
# print(isinstance(x, (list,tuple)),isinstance(x, (list,tuple)))

# **（79）判断 'https://blog.csdn.net' 是否以 'http://' 或 'https://' 开头。若是，则返回 'http'
# 或 'https'；否则，返回None。

# def get_url_start(url): # 定义一个获取起始url的函数
#     if url.startswith(('http://','https://')): # 条件判断
#         return url.split(':')[0] # 返回结果一
#     else:
#         return None # 返回结果二
# print(get_url_start('https://blog.csdn.net'))

# **（80）判断 'https://blog.csdn.net' 是否以 '.com' 或 '.net' 结束。若是，则返回 'com'
# 或 'net'；否则，返回None。

# def get_url_end(url): # 定义一个获取结束url的函数
#     if url.endswith(('.com','.net')): # 条件判断
#         return url.split('.')[-1] # 返回结果一
#     else:
#         return None # 返回结果二
# print(get_url_end('https://blog.csdn.net'))

# *（81）将列表 [3,'a',5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0。

# [1 if isinstance(item,(int,float)) and item>3 else 0 for item in [3,'a',5.2,4,{},9,[]]]
# print([1 if isinstance(item,(int,float)) and item>3 else 0 for item in [3,'a',5.2,4,{},9,[]]])

# *（82）a,b 是两个数字，返回其中较小者或较大者。

# a,b = 3.17, 2.72
# min(a,b)
# max(a,b)
# print(min(a,b),max(a,b))

# **（83）找到列表 [8,5,2,4,3,6,5,5,1,4,5] 中出现最频繁的数字以及其出现的次数。

# a = [8,5,2,4,3,6,5,5,1,4,5]
# v_max = max(set(a),key=a.count)
# print(v_max)
# a.count(v_max)
# print(a.count(v_max))

# （84）将二维列表 [[1], ['a','b'], [2.3, 4.5, 6.7]] 转为一维列表。不支持？

# sum([[1], ['a','b'], [2.3, 4.5, 6.7]])
# print(sum([[1], ['a','b'], [2.3, 4.5, 6.7]]))

# **（85）将等长的键列表和值列表转为字典。

# keys = ['a','b','c']
# values = [3,4,5]
# dict(zip(keys,values))
# print(dict(zip(keys,values)))

# （86）使用链状比较操作符重写逻辑表达式 a > 10 and a < 20。

# a = 0
# 10 < a < 201
# print(10 < a < 201)

# **（87）写一个函数，以0.1秒的间隔不换行打印30次由函数参数传入的字符，实现类似打字机的效果。
# import time
# def slow_print(ch, n=30, delay=0.1): # 定义一个缓慢输出打字函数 slow：缓慢的
#     for i in range(n): # 限定打印次数范围
#         print(ch, end='', flush=True) # flush参数主要是刷新， 默认flush = False，不刷新，print的内容先存到
#         # 内存中，当文件对象关闭时才把内容输出；而当flush = True时它会立即把内容刷新
#         time.sleep(delay)
# slow_print('*')

# *（88）数字列表求和。

# import random
# a = [random.random() for i in range(5)] # 这里使用random生成五个随机数
# print(a)
# sum(a)
# print(sum(a))

# （89）返回数字列表中的最大值和最小值。

# import random
# a = [random.random() for i in range(5)]
# min(a), max(a)
# print(min(a), max(a))

# （90）计算 5 的 3.5 方和 3 的立方根。

# pow(5, 3.5)
# print(pow(5, 3.5))
#
# * pow(3, 1/3)
# print(pow(3, 1/3))

# *（91）对 3.1415926 进行四舍五入，保留小数点后5位。

# round(3.1415926, 5) # round:四舍五入 圆形 圆的 回合
# print(round(3.1415926, 5))

# *（92）判断两个对象是在内存中是否是同一个。

# a = [1,2,3]
# b = a
# id(a) == id(b)
# print(id(a) == id(b))

# *（93）返回给定对象的属性和方法。

# a = ()
# for item in dir(a):
#     print(item)

# ======================================关于dir()函数================================================

# 在 Python 中，有大量的内置模块，模块中的定义（例如：变量、函数、类）众多，不可能全部都记住，这时 dir() 函数就非常有用了。

# dir() 是一个内置函数，用于列出对象的所有属性及方法。在 Python 中，一切皆对象，模块也不例外，所以模块也可以使用 dir()。除了常用定义外，其它的不需要全部记住它，交给 dir() 就好了。
# ————————————————
# 版权声明：本文为CSDN博主「一去丶二三里」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/liang19890820/article/details/75127738
# dir()
# 如果对 dir() 的用法不是很清楚，可以使用 help() 来查看帮助：
#
# >>> help(dir)
#
# Help on built-in function dir in module builtins:
#
# dir(...)
#     dir([object]) -> list of strings
#
#     If called without an argument, return the names in the current scope.
#     Else, return an alphabetized list of names comprising (some of) the attributes
#     of the given object, and of attributes reachable from it.
#     If the object supplies a method named __dir__, it will be used; otherwise
#     the default dir() logic is used and returns:
#       for a module object: the module's attributes.
#       for a class object:  its attributes, and recursively the attributes
#         of its bases.
#       for any other object: its attributes, its class's attributes, and
#         recursively the attributes of its class's base classes.
# (END)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 基本场景：
#
# 如果 dir() 没有参数，则返回当前作用域中的名称列表；否则，返回给定 object 的一个已排序的属性名称列表。
# 如果对象提供了 __dir__() 方法，则它将会被使用；否则，使用默认的 dir() 逻辑，并返回。
# 使用 dir()
# 使用 dir() 可以查看指定模块中定义的名称，它返回的是一个已排序的字符串列表：
#
# >>> import math  # 内置模块 math
# >>> dir(math)
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
# 1
# 2
# 3
# 其中，以下划线（_）开头的名称并不是自己定义的，而是与模块相关的默认属性。
#
# 例如，属性 __name__ 表示模块名称：
#
# >>> math.__name__
# 'math'
# 1
# 2
# 如果没有参数，dir() 会列出当前作用域中的名称：
#
# >>> s = 'Hello'
# >>> l = [1, 2, 3]
# >>> abs = math.fabs
# >>> dir()
# ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'l', 'math', 's']
# 1
# 2
# 3
# 4
# 5
# 通过导入 builtins 模块，可以获得内置函数、异常和其他对象的列表：
#
# >>> import builtins
# >>> dir(builtins)
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
# 1
# 2
# 3
# 自定义对象
# 根据 help 中的描述，可以看到：
#
# If the object supplies a method named __dir__, it will be used;
#
# 也就是说，如果对象有 __dir__() 方法，则将会被使用：
#
# >>> class Person:
# ...     def __dir__(self):
# ...         return ['name', 'sex', 'age']
# ...
# >>> p = Person()
# >>> dir(p)
# ['age', 'name', 'sex']
# ————————————————
# 版权声明：本文为CSDN博主「一去丶二三里」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/liang19890820/article/details/75127738

# ======================================关于dir()函数结束==============================================

# *（94）计算字符串表达式 '(2+3)*5' 的值。

# eval('(2+3)*5') # eval:串演算表达式
# print(eval('(2+3)*5'))

# =========================================关于eval()=================================================

# eval( )函数官方解释：将字符串str当作有效的表达式来求值并返回计算结果
#
# 可以理解为：与math结合的计算器
#
# （说白了，就是eval获得一个字符串输入，会计算字符串中的表达式并返回结果）
#
# a = "[[1, 2], [3, 4], [5, 6]]"
# b = eval(a)
# print(b)
# type(b)
# 1
# 2
# 3
# 4
# [[1, 2], [3, 4], [5, 6]]
# list
#
# a = "{1: 'a', 2: 'b'}"
# b = eval(a)
# print(b)
# type(b)
# 1
# 2
# 3
# 4
# {1: ‘a’, 2: ‘b’}
# dict
#
# a = "11 + 12"
# b = eval(a)
# print(b)
# 1
# 2
# 3
# 23
# ————————————————
# 版权声明：本文为CSDN博主「我是小杨我就这样」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_44478378/article/details/104789820

# =========================================关于eval()结束===============================================

# *（95）实现字符串 'x={"name":"David", "age":18}' 包含的代码功能。

# exec('x={"name":"David", "age":18}')
# print(x)

# ========================================关于exec()函数=============================================

# exec语句用来执行储存在字符串或文件中的Python语句。例如，我们可以在运行时生成一个包含Python代码的字符串，然后使用exec语句执行这些语句。下面是一个简单的例子。
#
# >>> exec 'print "Hello World"'
# Hello World
#
# 注意例子中exec语句的用法和eval_r(), execfile()是不一样的. exec是一个语句(就象print或while), 而eval_r()和execfile()则是内建函数.
#
# 理解网上的一个例子：
#
# “
#
# 实际上我是要用作域的名称…具体来说，我想实现这样一个效果…
# 有一个类叫做AFunction。
# 那么运行下述代码：
# import appuifw
# d=AFunction("Age=10")
# appuifw.note(str(d.Age).decode("utf-8"))
# 后会输出结果10。
#
# 解决方案：
# class Afunction:
#   def __init__(self,MyString):
#     exec("self."+MyString)
#
# ”
#
# exec执行了存储的字符串（self.Age=10）;所以结果为d.Age = 10
# ————————————————
# 版权声明：本文为CSDN博主「期待一片自己的蓝天」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/nyist327/article/details/47401933

# ========================================关于exec()函数结束===========================================

# *（96）使用 map 函数求列表 [2,3,4,5] 中每个元素的立方根。

# [item for item in map(lambda x:pow(x,1/3), [2,3,4,5])] # map():对每一个元素的共同操作
# print([item for item in map(lambda x:pow(x,1/3), [2,3,4,5])])

# *（97）使用 sys.stdin.readline() 写一个和 input() 函数功能完全相同的函数。

# import sys
# def my_input(prompt): # prompt:提示 迅速的 温馨提示 提示符
#     print(prompt, end='')
#     return sys.stdin.readline().strip() # stdin：标准输入，相当于input()
#
# str_input = my_input('请输入：')
#
# print(str_input)

# ===================================关于导入模块sys==========================================

# python中import用于导入模块。
#
# 具体用法：
#
# 下面程序使用导入整个模块的最简单语法来导入指定模块：# 导入sys整个模块
#
# import sys
#
# # 使用sys模块名作为前缀来访问模块中的成员
#
# print(sys.argv[0])
#
# 导入整个模块时，也可以为模块指定别名。例如如下程序：# 导入sys整个模块，并指定别名为s
#
# import sys as s
#
# # 使用s模块别名作为前缀来访问模块中的成员
#
# print(s.argv[0])
#
# 也可以一次导入多个模块，多个模块之间用逗号隔开。例如如下程序：# 导入sys、os两个模块
#
# import sys,os
#
# # 使用模块名作为前缀来访问模块中的成员
#
# print(sys.argv[0])
#
# # os模块的sep变量代表平台上的路径分隔符
#
# print(os.sep)
#
# 在导入多个模块的同时，也可以为模块指定别名，例如如下程序：# 导入sys、os两个模块，并为sys指定别名s，为os指定别名o
#
# import sys as s,os as o
#
# # 使用模块别名作为前缀来访问模块中的成员
#
# print(s.argv[0])
#
# print(o.sep)
# ————————————————
# 版权声明：本文为CSDN博主「weixin_39574246」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_39574246/article/details/111480657

# ===================================关于导入模块sys结束========================================

# ***（98）使用二维列表描述9x9围棋局面，'w'表示白色棋子，'b'表示黑色棋子，'-'表示无子，打印成下图左所示的文本棋盘。

# phase = [
# ['-','-','-','-','-','-','-','-','-',],
# ['-','-','-','-','-','-','-','-','-',],
# ['-','w','-','-','-','-','b','-','-',],
# ['-','-','-','-','-','-','-','-','-',],
# ['-','-','-','-','-','-','-','-','-',],
# ['-','-','-','-','-','-','-','-','-',],
#
# ['-','w','-','-','-','-','b','-','-',],
# ['-','-','-','-','-','-','-','-','-',],
# ['-','-','-','-','-','-','-','-','-',],
# ]
# def print_go(phase):
#     print('+-------------------+')
#     for row in phase:
#         print('| ', end='')
#         for col in row:
#             print('%s '%col, end='')
#         print('|')
#     print('+-------------------+')

# print_go(phase)
# +-------------------+
# | - - - - - - - - - |
# | - - - - - - - - - |
# | - w - - - - b - - |
# | - - - - - - - - - |
# | - - - - - - - - - |
# | - - - - - - - - - |
# | - w - - - - b - - |
# | - - - - - - - - - |
# | - - - - - - - - - |
# +-------------------+

# ***（99）对于9x9围棋盘，用a~i标识各行，用1~9标识各列，设计函数go()，输入位置和颜色，即输出文本棋盘，
# 模拟围棋对弈的过程。

# def print_go(phase):
#     print('+-------------------+')
#     for row in phase:
#         print('| ', end='')
#         for col in row:
#             print('%s ' % col, end='')
#         print('|')
#     print('+-------------------+')
#
# def go(phase, pos, color):
#     row = ord(pos[0]) - ord('a')
#     col = int(pos[1]) - 1
#     phase[row] [col] = color
#     print_go(phase)
#     return phase
# phase = [['-' for i in range(9)] for j in range(9)]
#
# phase = go(phase, 'c7', 'b')
# print('=========================观棋分割线========================')
#
# phase = go(phase, 'g3', 'w')
# print('=========================观棋分割线========================')
#
# phase = go(phase, 'g7', 'b')
# print('=========================观棋分割线========================')
#
# phase = go(phase, 'c3', 'w')
# print('=========================观棋分割线========================')

# *****（100）下图中是国际跳棋的初始局面，10x10的棋盘上只有50个深色格子可以落子，'w'表示白色棋子，'b'表示黑色棋子，
# '-'表示无子，字符串 phase = 'b'*20 + '-'*10 + 'w'*20 表示下图中的局面，请将 phase 打印成下图右所示的样子。

# phase = 'b'*20 + '-'*10 + 'w'*20
# def print_draughts(phase):
#     print('+-------------------+')
#     for i in range(10):
#         print('| ', end='')
#         for j in range(10):
#             if i%2==0 and j%2 or i%2 and j%2==0:
#                 print('%s '%phase[(10*i+j)//2], end='')
#             else:
#                 print('- ', end='')
#         print('|')
#     print('+-------------------+')
#
# print_draughts(phase)

# ===============================语感训练100题到此结束啦！要经常复习练习哦！==================================