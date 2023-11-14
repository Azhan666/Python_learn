# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 2.4 编码规范
# 写在前面：

# 说起编码规范，大多数人都会提到PEP8。PEP是Python Enhancement Proposal（Python增强建议书）的
# 简写。PEP8整个文档引入了很多其他的标准，很难在实践中付诸行动。好在龟叔说过，“A Foolish
# Consistency is the Hobgoblin of Little Minds（尽信书，不如无书）”，文档只要保持一致性、
# 可读性，就是一个好的规范。

# 在Linux平台上，一个规范的Python源码文件应该包含以下部分：解释器声明、编码格式声明、模块注释
# （文档字符串）、模块导入、常量和全局变量定义、函数或类定义、当前脚本代码执行等7项。
# 在Windows平台上，可以省略第一项。下面这个Python源码文件清晰地展示了这7项，各项之间使用一个
# 或两个空行进行分割。

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""通常这里是关于本文档的说明（docstring），需要以半角的句号、问号或叹号结尾！

# 本行之前应当空一行，继续完成关于本文档的说明
# 如果文档说明可以在一行内结束，结尾的三个双引号不需要换行；否则，就要像下面这样
"""

import os, time
import datetime

# BASE_PATH = r》d:\Youthgit》
# LOG_FILE = u》运行日志.txt"

class GameRoom(object):
    """对局室"""
    def __init__(self, name, limit=100, **kwds):
        """构造函数！

        name          对局室名字
        limit         人数上限
        kwds          参数字典
        """
        pass

def craete_and_start():
    """创建并启动对局室"""

    pass

if __name__ == '__main__':
    # 开启游戏服务
    craete_and_start()

