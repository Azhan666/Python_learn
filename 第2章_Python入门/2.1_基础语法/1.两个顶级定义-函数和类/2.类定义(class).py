# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""类定义"""

"""
    写在前面：说到类，自然离不开面向对象，类是面向对象编程思想的载体。关于面向对象编程，
Python高手修炼之道2.3节有详细讲解。Python的面向对象编程提供了丰富的封装手段，类定义的
规则非常灵活，既有强制性的，也有建议性的。如果不想深入研究那些让人头疼的概念，只需要了解
以下几个点就可以从容应对类的各种需求。

    1.使用关键字class定义类。
    2.如果没有基类，类名之后不需要圆括号。
    3.构造函数__init__()在类实例化时自动运行，类的属性要在这里定义或声明。
    4.self不是关键字，虽然可以换成其他的写法，但不建议这样做。
    5.类是属性和方法的混合体。
    6.同一个类，可以生成很多实例（单实例模式除外），这就叫类的实例化。
    7.类的各个实例之间是相互隔离的。"""

# class GameServer: # 游戏服务器，server：服务器
#     def __init__(self, port): # 构造函数 port:港口，即端口，先定义参数
#         self.port = port # 类属性：服务使用的端口           再self.调用参数
#         self.running = False # 类属性：服务运行标志
#     def start(self): # 定义类方法：启动服务
#         self.running = True
#     def stop(self): # 定义类方法：停止服务
#         self.running = False
#     def status(self): # 定义类方法：查看服务状态 status:状态
#         if self.running:
#             print('服务运行于%d端口上。'%self.port)
#         else:
#             print('服务已停止。')
#
# gs = GameServer(3721) # 类实例化，生成一个服务器对象，变量名见名知意
#
# gs.port # 对象属性：服务端口
#
# gs.status() # 对象方法：查看服务状态
#
# gs.start() # 对象方法：启动服务
#
# gs.status() # 对象方法：查看服务状态
#
# gs.stop() # 对象方法：停止服务
#
# gs.status() # 对象方法：查看服务状态

# 以上代码定义了一个游戏服务类，包括两个属性和三个方法。生成实例时，需要传入游戏端口作为参数。

"""有了上面的example，我们再来写一个表白阿婷的服务器"""

# class ExpressingServer(): # 定义表白服务器类
#     def __init__(self, port, win): # 类初始化，传入参数，构造函数，新传入参数win代表成功
#         self.port = port # 类属性，服务器使用的端口
#         self.win = win # 新增表白成功的类属性
#         self.running = False # 类属性服务器运行标志
#     def start(self): # 定义类方法：启动表白服务
#         self.running = True # 调用类running,表白服务启动
#     def stop(self): # 定义类方法，停止表白服务
#         self.running = False # 调用running=False，表白失败,但我不会放弃！
#     def again(self): # 定义重新表白的方法，继续努力，准备表白，直至成功。
#         self.win = True # 表白成功！
#     def status(self): # 定义类方法，查看服务状态，表白失败，等待下次表白，下次一定成功！
#         if self.running:
#             print('表白服务运行于%d端口上。'%self.port)
#         else:
#             print('表白失败，但我不会放弃！下次一定成功！')
#             if self.win:
#                 print('表白成功！')
#
#
# # 要对类进行实例化：(别忘记新增属性类也要实例化)
# es = ExpressingServer(3721, win=1) # 类实例化，生成一个服务器对象
# print(es.port, es.win) # 对象属性：服务端口,新增对象属性：win表白成功，
#
# es.status() # 对象方法，查看表白服务状态
#
# es.start() # 对象方法：启动表白服务
# es.status() # 对象方法，查看表白服务状态
#
# es.stop() # 对象方法：停止服务
# es.status() # 对象方法，查看表白服务状态
#
# es.again() # 对象方法，再次表白
# es.status() # 对象方法，查看表白服务状态



