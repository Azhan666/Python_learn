# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 单实例模式（Singleton Pattern）是一种常见的软件设计模式，其主要目的是确保某一个类只有一
# 个实例存在。当需要在整个系统中确保某个类只能出现一个实例时，单实例模式就能派上用场。
# 例如，一般应用程序中的配置类，Python日志模块中的日志对象，异步通信框架twisted里面的
# 反应堆（reactor），都是典型的单实例模式。
# 单实例模式有很多种实现方式，其中使用装饰器的方法是最容易理解的。

def Singleton(cls): # 定义单实例模式装饰器
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@Singleton
class Config(object): # 定义单实例类
    pass

cfg1 = Config() # 实例化
cfg2 = Config() # 实例化
print(cfg1 is cfg2) # 两次实例化得到的实例是同一个对象

# 以上代码定义了一个单实例模式装饰器，用来管理所有开启单实例保护的类的实例化。当一个类实
# 例化时，装饰器函数首先检查该类是否已有实例存在。若有，则直接返回已存在实例；若没有，则
# 创建实例并做好记录后返回新的实例。
