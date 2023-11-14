# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""1.2以交互方式运行Python代码"""

""" 解释型语言的优势是可以写一句,执行一句,想到哪儿,写到哪儿,而不必像编译型语言那样,需要把程序全部
写完、编译成功后才能运行。在以交互方式运行Python代码的过程中,可以随时查看各个对象的类型和属性,以
便判断当前编写的代码是否在正确的方向上。

    1.2.1使用Python IDLE交互操作
    我特别喜欢使用Python的IDLE这个交互式工具,经常在IDLE中验证代码的写法是否正确,甚至在IDLE中对
项目的设计思路做原型验证。
    IDLE支持Tab键自动补齐,这个功能可以用来学习一个新的模块,查看模块里面对象的方法和属性。还有两
个技巧,有助于使用IDLE:将光标移动到执行过的语句上按回车键,可以重复这个语句;使用下划线(_)可以代替
最后一次执行结果。
    下面的代码演示了在IDLE中以交互方式连接数据库、查询数据的例子。对于初学者来说,这几行代码读起来
会比较吃力。没有关系,这里仅仅是一个演示,后面会对这些代码进行详细讲解。"""

# import pymysql,pymysql.cursors as cursors
#
# db = pymysql.connect(host='localhost', port=3306, db='photo', user='hezhan',
#                      password='liting521')
# cursor = db.cursor()
# cursor.execute('select * from album')
#
# cursor.fetchall()

""" 实际上，IDLE也是一个集成开发工具，可以用来创建或打开.py文件，并对脚本进行编辑、运行和调试。
IDLE的Run和Debug菜单包括运行和调试脚本的相关功能；另外，在Options菜单中还可以设置IDLE的配色方案、
字体字号等，如图1-3所示。"""

"""
    1.2.2 使用IPython交互操作
    IPython是一个Python的交互式Shell,比默认的Python Shell功能更强大,支持变量自动补全、自动缩进
,以及bash shell命令,内置了许多很有用的功能和函数。不过, IPython没有被包含在Python内,而是作为
Python的第三方模块,需要单独安装。在一个命令行窗口中执行下面的模块安装命令,即可安装IPython模块。
pip命令在本书的1.4节有详细讲解。
    安装完成后,在命令行窗口运行ipython.exe,即可启动IPython,和Python IDLE相比,IPython更注重
显示格式的美观,还显式地标识出了输入和输出代码。

    为代码提供美观的格式,不是IPython唯一的优点, i让IPython名扬天下的是依赖IPython运行的
Jupyter。Jupyter是一个可以编写漂亮的交互式文档的强大工具。"""





