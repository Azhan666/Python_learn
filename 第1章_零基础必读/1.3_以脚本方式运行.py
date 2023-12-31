# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""1.3 以脚本方式运行Python程序"""

""" 1.3以脚本方式运行Python程序
    以交互方式运行Python代码是低效的,仅适用于语法学习或代码验证。大多数情况下,程序员是在编辑器或
集成开发工具中完成以.py为扩展名的脚本文件,然后调用解释器逐行解释、执行这个脚本文件。
    1.3.1运行
    如果你习惯使用纯粹的编辑器(如Vim或Notepad++等)写代码,那就需要手工运行和调试代码。以Windows
平台为例,运行代码分成两步。
    第一步,打开一个命令行窗口,将路径切换到脚本文件所在的文件夹。我习惯在脚本文件所在窗口的空白位置
(确保没有选中任何对象),按下Shift键并单击鼠标右键,在弹出的菜单中选择“在此处打开Powershell窗口”,
如图1-4所示。
    第二步,在打开的Powershell窗口中输入python空格+脚本文件名,按回车键即可运行代码。输入脚本文件
名时,按Tab键可以自动补齐。脚本的运行信息、错误信息、运行结果等都显示在这个窗口中。这些信息都是最
原始的信息。在其他开发工具中看到的脚本的信息,都是对这些信息的再加工。
    实际上,很多编辑器都支持自定义运行命令,可以实现一键运行Python脚本。如果你习惯使用PyCharm或
VSCode等集成开发工具,运行脚本就更简单了,甚至可以在开发工具中配置多个Python运行环境。

    1.3.2调试
    通常集成开发工具会提供强大的调试工具,熟练运用该工具,很容易定位到错误的代码,可以极大地提高调试
效率。如果习惯使用编辑器做开发,或不熟悉集成开发工具的调试工具手工调试代码的手段不多,大概只能用
print()函数查看调试信息。好在Python有一个内置的调试模块pdb,它可以提供包括设置断点、单步调试,进入
函数调试,查看当前代码、查看栈片段、动态赋值等多种调试手段。
"""