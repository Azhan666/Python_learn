# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 当前脚本就是被解释器直接解释执行的脚本。如果一个脚本是被其他脚本以模块形式导入的，该脚本
# 就不是当前脚本。判断脚本是否是当前脚本的条件是__name__=='__main__'是否为真。
# 强烈建议将脚本的执行部分置于这个条件的保护之下，而将全局变量、常量、函数和类定义置于该条
# 件的保护之外。对于一个简单的应用来说，这样做并没有特别的意义；但如果一个项目由很多脚本组成，
# 那么这样做几乎就是必然的选择了。
