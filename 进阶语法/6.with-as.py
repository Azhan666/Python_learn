# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 2.2.6 with-as

# 写在前面：
# with-as是和上下文管理协议相关的语法，适用于对资源进行访问的场合，确保无论使用过程是否发
# 生异常，都会事先执行必要的准备工作，事后执行必要的善后操作。例如，连接和关闭连接、打开和
# 关闭文件、获取和释放资源锁等。以文件读写为例，如果不使用with-as语法结构，代码通常如下：

fp = open('data.txt', 'r')
try:
    contents = fp.readlines()
finally:
    fp.close()

# 如果使用with-as语法结构，那就优雅多了：

with open('data.txt', 'r') as fp:
    contents = fp.readlines()

