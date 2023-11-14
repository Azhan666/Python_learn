# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 如何使用css选择器：

# 导入选择器包:
from bs4 import BeautifulSoup
import html
soup = BeautifulSoup(html, 'html.parser')
soup.select()

# BeautifulSoup对象的.select()方法中传入字符串参数，选择的结果以列表形式返回.

# css基本语法:
# 元素选择器：
# 直接选择文档元素
# 比如head，p
# 类选择器：
# 元素的class属性，比如 < h1class ="important" >
#
#
# 类名就是important
# .important选择所有有这个类属性的元素
# 可以结合元素选择器，比如p.important
# ID选择器：
# 元素的id属性，比如 < h1
# id = "intro" >
# id就是intro
# # intro用于选择id=intro的元素
# 可以结合元素选择器，比如p  # intro
# 属性选择器：
# 选择有某个属性的元素，而不论值是什么。
# *[title]
# 选择所有包含title属性的元素
# a[href]
# 选择所有带有href属性的锚元素
# 还可以选择多个属性，比如：a[href][title]，注意这里是要同时满足。
# 限定值：a[href = "www.so.com"]
# 后代（包含）选择器：
# 选择某元素后代的元素（层级不受限制）
# 选择h1元素的em元素：h1
# em
# 子元素选择器：
# 范围限制在子元素
# 选择h1元素的子元素strong：h1 > strong

# 具体参考如下：
# *：选择所有节点
# #container：选择所有is、为container的节点
# .container：选择所有class包含container的节点
# li a：选取所有li下所有a节点
# ul + p：选取ul后面的第一个p元素
# div#container>ul:选取id为container的div的第一个ul子元素
# ul~p：选取与ul相邻的所有p元素
# a[title]：选取所有有title属性的a元素
# a[href*="http:jobbole.com"]：选取所有href属性为http:jobbole.com的a元素
# a[href*="jobbole"]：选取所有href属性中包含jobbole的a元素
# a[href^="http"]：选取所有href属性以http开头的a元素
# a[href$="jpg"]：选取所有href属性以.jpg结尾的a元素
# input[type=radio]:checked：选择选中的radio的元素
# div:not(#container)：选取所有id、为非container的div属性
# li:nth-child(3)：选取第三个li元素
# li:nth-child(2n)：选取第偶数个li元素


