# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""3.7 系统相关操作"""

""" 在python的内置模块中，os和sys这两个模块都和操作系统有关，因此这里把这两个模块放在一起讲解，
实际上二者在功能上几乎没有重叠，os模块主要用于获取程序运行所在操作系统的相关信息，sys模块是一个
和python解释器关系密切的标准库，它可以帮助我们访问和python解释器紧密关联的变量和函数。"""

"""3.7.1 os模块
    os模块常用于文件和路径操作，它也可以用于运行外部命令、打开关联了工具的文件等。此外，os模块
还提供查看系统环境信息、进程信息等辅助功能。

    1.文件操作
    使用os模块还可以创建或删除文件夹、删除文件，还可以读取文件的大小、创建时间、最后更新时间、
最后访问时间等信息。"""

import os
# print(os.getcwd()) # 返回程序当前路径
# D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能
# print(os.listdir(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能'))
# 返回指定路径下的文件夹和文件列表，listdir：列出指定目录下的所有文件名

# ['3.1_时间和日期处理.py', '3.2_图像处理.py', '3.3数据文件读写.py', '3.4数据库操作.py',
# '3.5_数据抓取.py', '3.6_数据解析.py', '3.7_系统相关操作.py', 'demo.html', 'hezhan.db',
# 'liting.db', 'test.db', 'test_demo_files', 'water.db', '图3-5 MODIS数据下载流程.jpg',
# '微信图片_20210207200748.jpg', '滤镜效果', '阿婷.jpg', '阿婷.png']

# print(os.mkdir(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_folder'))
# 新建单级文件夹（新文件夹的父级已存在），folder：文件夹
# None,由于我的语法垃圾原因，输出了None,但是新文件夹创建成功

# print(os.makedirs(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\A\B'))
# 新建多级文件夹
# print(os.rmdir(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\A\B'))
# 删除空文件夹（非空则抛出异常）
# print(os.rmdir(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\A'))
# # 删除空文件夹（非空则抛出异常）

# print(os.remove(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\water.db'))
# 删除文件

# print(os.path.isfile(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\readme.md'))
# 判断是否是文件
# True

# print(os.path.exists(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\滤镜效果'))
# 判断文件或文件夹是否存在
# True

# finfo = os.stat(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\滤镜效果')
# 返回文件的大小、创建时间等信息
# print(finfo.st_size) # 文件大小（以字节为单位）
# 4096

# print(finfo.st_ctime) # 文件创建时间（时间戳）
# 1620475532.1006734
# print(finfo.st_mtime) # 文件最后更新时间（时间戳）
# # 1620475548.2023363
# print(finfo.st_atime) # 文件最后访问时间（时间戳）
# # 1621249449.4157457

# 下面，我们结合所学知识，对时间戳进行时间的转换
""" 使用3.1节介绍的日期和时间处理知识，可以直观地1显示这几个时间暗处哦对应的日期时间。"""

# import time # 导入time模块，显示时间戳对应的日期时间
# print(time.strftime("%Y-%m-%d %X",time.localtime(finfo.st_ctime)))
# # strftime:根据区域设置格式化本地时间 格式 时间格式, localtime:取得本地时间,# 文件创建时间:
# # 2021-05-08 20:05:32
#
# print(time.strftime("%Y-%m-%d %X",time.localtime(finfo.st_mtime))) # 文件最后更新时间
# # 2021-05-08 20:05:48
#
# print(time.strftime("%Y-%m-%d %X",time.localtime(finfo.st_atime))) # 文件最后访问时间
# # 2021-05-17 19:04:09

"""2.路径操作
    不同的操作系统使用的路径分隔符也不同，例如，UNIX使用(/),w\Windows使用反斜杠(\)。
os模块的路径操作功能为代码跨平台运行提供了有力保障。"""

# print(os.sep) # 当前路径分隔符
# \
# print(os.path.join('youth', 'github', 'README.md')) # 路径拼接
# youth\github\README.md
# print(os.path.split('youth\github\README.md')) # 返回路径名和文件名的元组
# ('youth\\github', 'README.md') # split()返回的是元组
# print(os.path.basename('youth\\github\README.md')) # 返回文件名
# README.md
# print(os.path.splitext('youth\\github\README.md')) # 返回路径名和文件扩展名的元组
# ('youth\\github\\README', '.md')

# Ps: join和split：https://blog.csdn.net/weixin_39795284/article/details/110554424

"""3.运行外部命令
    os模块提供了两种执行外部命令的方法：os.system()和os.popen()。前者相当于在当前进程中
打开一个shell（子进程）来执行系统命令；后者则会打开一个管道，返回一个连接管道的文件对象，从
该文件对象中读取返回结果。"""

# (os.system('cmd')) # 运行cmd命令（打开一个命令行窗口）

# os.system('notepad') # 打开记事本，notepad：记事本

# f = os.popen('ping cn.bing.com', mode='r', buffering=-1) # 运行ping命令窗口
# f.readlines() # 从该文件中读取返回结果
# 'ping' �����ڲ����ⲿ���Ҳ���ǿ����еĳ���
# ���������ļ���

# 关于ping命令：ping (Packet Internet Groper)，因特网包探索器，用于测试网络连接量的程序。
# Ping发送一个ICMP；回声请求消息给目的地并报告是否收到所希望的ICMP echo （ICMP回声应答）。
# 它是用来检查网络是否通畅或者网络连接速度的命令
# https://blog.csdn.net/hebbely/article/details/54965989

"""4.打开关联了工具的文件
    关联了打开工具的文件，如：Office文件、PDF文件、各种格式的图像文件等，可以使用os.startfile
()直接打开。"""

# os.startfile(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\副本腾讯招聘1.xls')
# os.startfile(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\test_demo_files\Effective Python (1).pdf')
# os.startfile(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\阿婷.jpg')

"""5.其他辅助功能
    os模块可以获取与当前操作系统、当前用户、当前进程相关的各种信息。"""

# print(os.name) # 操作系统名
# nt
# nt：windows nt  n. Windows New Technology（微软公司发行的操作系统）

# print(os.getenv('OS')) # 返回操作系统名
# Windows_NT

# print(os.getlogin()) # 返回当前用户名，login：登录
# # 阿展要提高
# print(os.cpu_count()) # 返回cpu数量
# # 16
# print(os.getpid()) # 返回当前进程id
# 1320

# import signal # signal：信号
# os.kill(1320, signal.SIGILL) # 终止进程，kill：杀死
# 报错：PermissionError: [WinError 5] 拒绝访问。

# 关于signal：https://www.cnblogs.com/madsnotes/articles/5688681.html
# 进程模块（os.skill）了解：https://www.cnblogs.com/now-fighting/p/3534185.html

"""3.7.2 sys模块
    sys模块是一个和Python解释器关系密切的标准库，可以用来查看Python解释器的版本号、版权信息、
存储路径、最大递归深度、最大整数、导入模块的路径等信息。此外，sys模块还提供了标准输入函数
sys.stdin(),和标准输出函数sys.stdout()，以及命令行参数列表sys.argv,借助命令行参数列表，
我们还可以再运行代码的命令中传递运行参数，表3-8列出了sys模块的常用变量和函数。

    sys成员（变量和函数）        功能描述
    sys.version     返回Python解释器的版本信息
    sys.winver      返回Python解释器的主版本号
    sys.copyright   返回与Python解释器有关的的版权信息
    sys.executable   返回Python解释器在磁盘上的存储路径
    sys.path        返回路径列表。导入模块时，解释器从这些路径中查找指定的模块
    sys.modules     返回模块名和载入模块对应关系的字典
    sys.byteorder   显示本地字节序的指示符。如果本地字节序是大端模式，则该属性返回big，
                    否则返回little
    sys.maxsize     返回Python支持的最大值，在32位平台上，该属性值为2的31次方-1，
                    在64位平台上，该属性值为2的63次方-1.
    sys.getswitchinterval() 返回Python解释器中线程切换的时间间隔。该属性可通过
                            sys.setswitchinterval()函数改变
    sys.getrecursionlimit() 返回Python解释器当前支持的最大递归深度，该属性可通过
                            sys.setrecursionlimit()方法重新设置
    sys.getrefcount(object) 返回指定对象的引用计数，当object对象的引用计数为0时，
                            系统会回收该对象
    sys.stdin               标准输入的类文件流对象，默认从控制台读入
    sys.stdout              表顺输出的类文件流对象，默认输出到控制台
    sys.stderr              标准错误信息的类文件流对象，默认输出到控制台
    sys.exit()              通过引发SystemExit异常来退出程序
    sys.argv                运行Python程序的命令行参数列表，列表的首元素通常是Python程序，
                            其后的元素均为程序的运行参数。
                            
    了解了sys模块后，我们就再也不用担心找不到Python的安装路径、版本等问题了。"""

# import sys
# print(sys.version)
# # 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# print(sys.winver)
# # 3.7
# print(sys.executable)
# # C:\Users\阿展要提高\AppData\Local\Programs\Python\Python37\python.exe

""" 第2章中讲过的Python内置函数print()和input(),实际上就是对标准输入对象sys.stdin和
标准输出对象sys.stdout的封装，代码如下："""

# print('Hello,World.') # 使用print()函数输出
# Hello,World.
# count = sys.stdout.write('Hello,World.\n') # 使用sys.stdout输出
# Hello,World.
# txt = input() # 使用input()函数从键盘读入
#
# txt = sys.stdin.readline() # 使用sys.stdin函数从键盘读入
# print(txt)

""" 下面的代码演示了sys模块最简单的两种应用：从命令行读取参数和终止脚本执行。"""

import sys

def summation(x, y): # summation:求和
    try:
        x, y = float(x), float(x)
    except:
        print('非法参数')
        sys.exit(1)
    finally:
        print('即使异常终止，这一句仍会被执行')
    print('%f + %f = %f'%(x, y, x+y))

if __name__ == '__main__':
    if len(sys.argv) !=3:
        print('请在程序名后输入两个数值型参数，每个参数前都以空格分隔')
        sys.exit(1)
    print(sys.argv)
    summation(sys.argv[1], sys.argv[2])

""" 将上面这段代码命名为sys_sum.py,在命令行窗口运行，可以直观地看到参数列表，下面的代码
分别使用合法的、非法的输入参数验证，体会sys.exit()的使用方法。

    在代码的任何地方调用sys.exit(),都会引发SystemExit异常，进而退出程序，需要注意的是，
如果sys.exit()放在try语句块中，SystemExit异常被捕获后，无论退出还是不退出程序，都无法阻止
finally语句块的执行，另外，提供一个整数作为sys.exit()的参数（默认为0，标识成功）来标识
程序是否成功运行，这时Unix平台的一个惯例。"""






































