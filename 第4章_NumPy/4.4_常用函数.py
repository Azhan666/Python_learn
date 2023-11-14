# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""4.4 常用函数"""

""" NumPy提供了大量的函数，其中和数组操作相关的函数有很大一部分是数组对象ndarray的方法在NumPy命名空间
中的映射。也就是说，NumPy的很多函数其实都是数组对象内置的方法。本节并不是对所有NumPy函数的总结，而是介绍
和函数相关的几个概念，并对部分常用函数做示例性讲解。"""

"""4.4.1 常量
    说起常量，我们首先会想到圆周率、自然常数、欧拉常数（不懂自行百度）等。的确，NumPy的常量包括np.pi(圆周
率)、np.e(自然常数)、np.euler_gamma(欧拉常数)，此还包括np.nan(非数字)和np.inf(无穷大)这两个特殊数值。
NumPy的特殊值还有正负无穷大、正负零等，但因为很少用到，这里就不进行重点介绍。

    NumPy有两个很有趣的特殊值：np.nan和np.inf。nan是Not a Number的简写，意为非数字，inf是infinity的
简写，意为无穷大。其代码如下："""

# import numpy as np
#
# a = np.array([1, 2, np.nan, np.inf])
# print(a.dtype)
# # float64
#
# a[0] = np.nan
# a[1] = np.inf
# print(a)
# # [nan inf nan inf]
# print(a[0] == a[2]) # 两个np.nan不相等
# # False
# print(a[1] == a[3]) # 两个np.inf则相等
# # True
# print(np.isnan(a[0])) # 判断一个数组元素是否是np.nan
# # True
# print(np.isinf(a[1])) # 判断一个数组元素是否是np.inf
# # True

""" 上面的代码中，两个np.nan居然不相等,但两个np.inf则是相等的。另外请注意,判断个数扎元素是否是mp.nan或
np.inf,需要使用np.isnan()和np.isinf()这两个相应的函数,而不是使用两个等号的逻辑表达式
    那么这两个特殊值有什么用途呢?原来, NumPy是用特殊值来表示缺值、空值和无效值的想想. Python语言和C语言
如何表示缺值、空值和无效值呢? Python语言因为列表元素不受类型限制,可以用None或False等表示缺值、空值和无效
值。而C语言只能在数据的值域范围之外。选一个特定值来表示,例如,假定数组存储的是学生的成绩,成绩一般都是正值,
所以C语言可以用-1表示缺考,在Numpy数组中,因为有nan和inf这两个特殊值,所以不用在意数据的值线范围,说到这里,
你可能会产生疑问,这两个特殊值,一个是非数字,一个是无穷大,数组运算的时候怎么处理呢?这就是NumPy神奇的地方,
我们根本不用担心这个问题。
    下面的代码滴示了在数组相邻的两个元素之间插入它们的算术平均值。尽管数组元素包含np.nan,但这不影响数值
计算。"""

# import numpy as np
#
# a = np.array([9, 3, np.nan, 5, 3])
# a = np.repeat(a, 2)[:-1]
# a[1::2] += (a[2::2]-a[1::2])/2
# print(a)
# # [ 9.  6.  3. nan nan nan  5.  4.  3.]

""" 4.4.2 命名空间
    
    刚开始使用NumPy函数时,对于函数的使用,你可能会有这样的困感;实现同样的功能一个函数却有两种写法:有时以为
某个函数可以有两种写法,但用起来却会出错。归纳起来这些困感有以下三种类型。

    （1）都是求和、求极值，下面这两种写法有什么区别吗？"""

# import numpy as np

# a = np.random.random(10)
# print(a.max(), np.max(a))
# # 0.8834339896247485 0.8834339896247485
# print(a.sum(), np.sum(a))
# # 4.61308845451836 4.61308845451836

""" （2）同样是复制，为什么深复制copy()两种写法都行，而浅复制view()则只有数组的方法？"""

# a = np.random.random(5)
# print(a.copy())
# # [0.22217265 0.81937982 0.38053526 0.36486704 0.4561405 ]
# print(np.copy(a))
# # [0.22217265 0.81937982 0.38053526 0.36486704 0.4561405 ]
# print(a.view())
# print(np.view(a))
# # raise AttributeError("module {!r} has no attribute "
# # AttributeError: module 'numpy' has no attribute 'view'

"""（3）为什么where()不能作为数组ndarray的函数，必须作为NumPy的函数？"""

# print(np.where(a>0.5))
# # (array([0, 2, 4], dtype=int64),)
# print(a.where(a>0.5))
# # AttributeError: 'numpy.ndarray' object has no attribute 'where'

""" 以上这些差异取决于函数在不同的命名空间是否有映射。数组的大部分函数在顶层命名空间有映射，
因此可以有两种写法。但数组的一小部分函数没有映射到顶层命名空间，所以只能有一种写法。而顶层
命名空间的大部分函数，也都只有一种写法。表4-2所示的是常用函数和命名空间的关系，仅供参考。

                表4-2 不同命名空间支持的部分函数
    顶层命名空间和数组对象均支持          仅数组对象支持         仅顶层命名空间支持
    np/ndarray.any/all()        ndarray.astype()        np.where()
    np/ndarray.max()/min()      ndarray.fill()          np.stack()
    np/ndarray.argsort()        ndarray.view()          np.rollaxis()
    np/ndarray.mean()           ndarray.tolist()        np.sin()
    ······                      ·······                 ······
    
    4.4.3 数学函数
    
    如果不熟悉NumPy,Python程序员一般都会选择使用math模块来解决数学问题，但实际上NumPy的数学函数比
math模块更加方便，而且NumPy的数学函数可以广播到数组的每一个元素上，也就是说，如果用np.sqrt()对数组
arr开方，返回的是数组arr中每个元素的平方根组成的新数组。
    下面把NumPy和math模块的数学函数罗列在一个表格中，分成了数学常数、舍入函数、快速转换函数、幂指数
对数函数和三角函数这5类，如表4-3所示。其它如求和、求差、求积的函数被归类到下一小节的统计函数中。

                    表4-3 常用数学函数
    类别                  NumPy函数             Math函数              功能
================================================================================  
                         np,e                        math.e     自然常数
数学常数                  np.pi                      math.pi      圆周率
================================================================================
舍入函数                  np.ceil()                 math.ceil()     进尾取整 
                        np.floor()                 math.floor()    去尾取整
                        np.around()                              四舍五入到指定精度
                        np.rint()                                四舍五入到最近整数
=================================================================================
快速转换函数             np.deg2rad()               math.radians()  
                        np.radians()                                度转弧度
                        ============             ================= 
                        np.rad2rad()              math.radians() 
                        np.degrees()                                 弧度转度
=================================================================================

幂指数对数函数          np.hypot()                 math.hypot()   计算直角三角形的斜边

                      np.square()                                平方
                      
                     np.sqrt()                  math.aqrt()       开平方
                     
                     np.power()                 math.pow()        幂
                     
                     np.exp()                   math.exp()        指数
                     
                     np.log()                   math.log()        对数
                     np.log10()                 math.log10()      
                     np.log2()                  math.log2()       
===================================================================================
三角函数             np.sin()/arcsin()          math.sin()/asin()   正弦/反正弦
        ·           np.cos()/arccos()          math.cos()/acos()    余弦/反余弦
                    np.tan()/arctan()          math.tan()/atan()    正切/反正切
==================================================================================="""

""" 下面的代码演示的是一些常用数学函数。"""

import numpy as np, math

print(math.e == np.e) # 两个模块的自然数相等
# True

