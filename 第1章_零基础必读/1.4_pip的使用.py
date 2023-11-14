# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""1.4 使用pip安装和管理模块"""

"""1.4 使用pip安装和管理模块
    pip是Python目前最流行、最方便的包管理工具。早期的Python使用setup.py安装模块,比较麻烦。很多
程序员都曾经用过把模块文件直接放进Python安装路径下的Lib\site-packages文件夹的“暴力”安装法。后来
稍微进步了一点,使用esy installI具,模块文件的扩展名是egg.再后来,终于进化到了pip时代,对应的模块文
件变成whl文件,甚至GitHub上的zip文件也可以直接安装。
    1.4.1使用pip的两种方式
    使用pip工具有两种方式:一种是运行pip.exe可执行程序;另一种是调用Python解释器把pip模块当成脚本
来运行。以安装NumPy模块为例,两种使用方式的命令如下。
    pip安装numpy
    pip install numpy
    第一种方式的命令里, pip指的是pip.exe程序。如果尝试在计算机上安装多个版本的Python,安装程序一
般会自动(也可以手动)将pip.exe程序复制并在文件名中加入版本信息。
    图1-5是我的计算机上Python3.7默认安装路径下的pip.exe程序和两个副本的名字。无论使用pp还是pip3
,又或者是pip3.7,都能正确安装模块。
    和第一种方式相比,第二种方式的安装命令前面多了python-m,这里的python指的是python.exe程序,也
就是Python解释器: -m是Python解释器的参数,用来说明解释器运行的不是脚本文件,而是把pip模块当作脚本
来运行。 pip模块位于Python的安装路径下, Python 解释器会找到它。
    在安装了多个Python版本的系统中,以第二种方式使用pip工具,只要能正确调用解释器就不容易出错。如
果用第一种方式安装模块失败,不妨试试第二种方式。

    1.4.2 安装模块
    安装模块使用install命令。这个子命令支持很多的选项,其中最常用的参数是-U,它表示将指定的模块升
级到最新的可用版本。
pip install numpy -U
    
    安装子命令默认从http://pypi.org/simple下载模块文件,使用-参数可以指定下载的镜像源。下面的安装
命令分别使用了清华大学资源站、阿里云资源站、中科大资源站、华中科技大学作为下载的镜像源地址。
清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
阿里云：http://mirrors.aliyun.com/pypi/simple/
中科大：http://pypi.mirrors.ustc.edu.cn/simple/
华中科技大学：http://pypi.hustunique.com/

    安装模块时，还可以使用两个等号（==）指定模块的版本。
    pip install numpy==1.15.0
    
    使用install 命令还可以安装本地whl文件,甚至是GitHub上的zip文件。下面两个命令分别安装了
basemap模块和pyinstaller模块的开发版。

pip install basemap-1.2.0-cp37-cp37m-win_amd64.whl
pip install https://github.com/pyinstaller/pyinstaller/archile/develop.zip

    1.4.3 卸载模块
    卸载模块使用uninstall 命令。这个子命令比较简单,只有-r和-y两个选项,前者指定卸载依赖包，
后者跳过卸载确认。请谨慎使用这两个选项。

    1.4.4 查看模块列表和模块信息
    查看模块列表使用list命令，这个命令支持的选项较多，如使用-o参数可以列出过时的模块，使用-u参数
可以列出最新的模块。下面是使用-o参数显示的结果。

Package        Version Latest Type
-------------- ------- ------ -----
watchdog       2.0.2   2.1.2  wheel
xdis           5.0.8   5.0.9  wheel
zipp           3.4.0   3.4.1  wheel
zope.interface 5.2.0   5.4.0  wheel

    使用show命令可以查看指定模块的信息，下面是以NumPy模块为例显示的信息。
    
D:\python_learn\Python基础阶段>pip show numpy
Name: numpy
Version: 1.19.5
Summary: NumPy is the fundamental package for array computing with Python.
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email: None
License: BSD
Location: c:\users\阿展要提高\appdata\local\programs\python\python37\lib\site-packages
Requires:
Required-by: pandas, opencv-python, netCDF4, matplotlib, h5py, cftime, blind-watermark

"""



