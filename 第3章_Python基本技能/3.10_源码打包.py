# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""3.10 源码打包"""

"""
    Python的源码文件打包通常有两个不同的含义:一是将源码文件打包成可执行文件,以便在没有安装Python
环境的计算机上运行;二是将源码文件打包成扩展名为.whl的模块安装文件目的是便于维护、分发和使用自定义
的模块。
    3.10.1打包成可执行文件
    Py2时代,源码打包的最佳选择是py2exe模块,因为当时有一个流行的脚本,它将源码打包和安装程序制作
(使用Inno Setup, 一款免费的安装程序制作软件)整合在一起,使用非常方便。遗憾的是,从Python3.3以后, 
py2exe模块不再进行更新。
    目前将源码打包成可执行文件的工具,最常用的是pyinstaller cx_free.两个工具都支持Windows, 
Linux和Mac OS X平台,对Py3的支持也不错。比较而言, pyinstaller使用指令加参数的打包方式,更容易操作
,且支持单文件模式,可以将源码打包成单个文件,因此使用pyinstaller的用户相对多一些。其实,我更喜欢
ex_freeze,因为它支持Zipfile import, 同时可以使用打包脚本打包,拥有更强的扩展能力,如像pyzexe模块
那样增加安装程序制作功能。

    1,使用pyinstaller打包
    pyinstaller使用指令加参数的方式打包,打包过程中会自动生成buid和dist两个文件夹,可执行文件包含
在dist目录中。使用pyinstaller包时还会自动生成一个.spec文件,用户可手动修改该文件(需要打包多个文件
时,这个方法最容易操作)后,将该文件作为唯一参数重新执行打包指令。表3-11列出了pyinstaller用的打包
参数。

        参数              说明
        -h, --help      查看帮助信息
        -D,--onedir     生成一个包含可执行文件的文件夹
        -F,--onefile    生成单个可执行文件
        -w,--windowed   程序运行时不显示控制台窗口
        -c,--nowindowed 使用控制台作为标准I/O
        -d,debug        生成debug版本的可执行文件
        -i,--icon       指定可执行文件的图标（仅仅用于文件图标而非应用程序图标）
        --add-data      打包指定的文件
        
    位于D:\App\Qr路径下的源码文件QrCreator.py是一个GUI程序,运行下面的命令可将其打包成一个单文件
的可执行程序,运行时禁止显示控制台窗口,同时指定可执行程序的图标文件。
PS D: \App\Qr> pyinstaller -F orcreator.py -i Qrcreator.ico -w
运行下面的命令将D:App\SreenGIE路径下的源码文件Screenil.y打包成一个文件夹同时还将同级目录下的
res文件夹及其全部文件一并打包到目标文件夹中。
PS D: \App\Screenengif > pyinstaller -D ScreenGIF.py--add-data "res;res”

    2. 使用cx_freeze打包
    ex_freeze使用打包脚本(默认名为setup.py)完成打包。那么如何生成打包脚本呢?下面以打包
D:AppScreenGI路径下的源码文件ScreenGlE.py为例,演示cx_freeze 使用方法。

    在源码文件所在路径下运行下面的命令,根据提示输入项目名(ScreenGIF)、版本(使用默认值),描述(无)、
脚本文件名(ScreenGil.py)、生成的可执行文件名(使用默认值),选择要生成文件类型(选择C,表示控制台程序)
、打包脚本文件名(使用默认值),就可以创建打包脚本。接下来既可以选择直接运行打包脚本,也可以选择不运行
,待修改打包脚本后再单独运行。
    具体代码查看打包示例。
    
    3.10.2 打包成模块安装文件
    
    一个Python的脚本文件就是一个自定义的模块,我们可以在其他脚本文件中导入这个自定义的模块。但如何
处理当前脚本文件和作为模块的脚本文件之间的路径关系却是一个令人头疼的问题。最好的做法是,将作为模块
的脚本文件打包成扩展名为.whl的模块安装文件,然后使用pip命令安装,使之成为Python环境下的模块,这样导
入模块时就不用再担心路径问题了。
    将源码打包成模块安装文件需要用到setuptools和wheel两个模块。如果Python环境中还没有安装这两个
模块,或不确定当前安装的版本是否可以使用,需要先运行下面这个命令。
Ps: python -m pip install --user --upgrade setuptools wheel
    有了这两个模块后，接下来只需要按照下面的步骤一步一步执行，即可将源码顺利打包成模块安装文件。

    1.规划文件路径
    假定要发布的模块名称为wxgl，包含scene.py、region.py和colorbar.py等三个文件，文件目录
结构如下：

    wxgl_pkg/
    |———— wxgl/
    |   |———— __init__.py
    |   |———— colorbar.py
    |   |———— scene.py
    |   |———— region.py
    |————README.md   
    |____ setup.py
    

    2.添加init文件
    init.py文件内容可以为空。下面是一个可供参考的样例。"""

name = 'wxgl'
version = "0.3.0"
version_info = (0, 3, 0, 0)

""" 3.添加README.md文件
    README.md文件是关于安装和使用的说明，是一个支持Markdown格式的文本文件，Markdown：编辑器。
    
    4.添加setup.py文件
    setup.py是打包的脚本文件，可以参考下面的文件样例并根据实际情况修改。需要注意：License很重要，
License：许可，打包检查很严格，发布到pypy.org时，如果打包不符合规则就会被拒绝。"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wxgl",
    version="0.3.0",
    author="hezhan", # 作者
    author_eamil="835054694@qq.com",
    description="A 3d library based pyOpenGL.", # description:描述 说明 着录 产品描述
    long_description=long_description,
    url="https://github.com/Azhan666",
    packages=setuptools.find_packages(), # packages:允许一个程序安装 封装 封包
    classifiers=[ # classifiers:分类器 分类分析 指限定元 机器视觉
        "Programming Language :: Python :: 3", # 编程 程序设计,语言
        "License :: OSI Approved :: MIT License",# 许可，开放系统互连，Approved：承认，MIT：麻省理工
        "Operating System :: OS Independent", # 操作系统，独立的
    ]
)

""" 5.生成安装包文件
    在wxgl_pkg目录下运行setup.py脚本，会在同级目录下生成dist文件夹，扩展名为.whl的安装包
文件就在这里面，文件路径参考如下：
D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\3.10_源码打包.py bdist_wheel
"""


