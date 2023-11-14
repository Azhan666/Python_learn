# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 下面介绍一下XPath的基本语法知识，常见的使用方法主要有以下几种：
# （1）// （双斜杠）：定位根节点，会对全文进行扫描，在文档中选取所有符合条件的内容，以列表的形式返回。
# （2）/  （单斜杠）：寻找当前标签路径的下一层路径标签或对当前路径标签内容进行操作。
# （3）/text()：获取当前路径下的文本内容
# （4）/@xxx：提取当前路径下标签的属性值
# （5）|（可选符）：使用“|”可选取若干个路径，如//p|//div,即在当前路径下选取所有符合条件的p标签和div标签。
# （6）.（点）：用来选取当前节点。
# （7）..（双点）：选取当前节点的父节点。


# 3.4.3 获取所有节点

# 根据XPath常用规则可知，通过“//”可以查找当前节点下的子孙节点，以上面的HTML为例获取所有节点，实例代码如下：

from lxml import html
etree = html.etree
html = html.etree.parse('./test.html',etree.HTMLParse())
result = html.xpath('//*') # //表示获取当前节点下的子孙节点，*表示所有节点
                           # //*表示获取当前节点下的所有节点
for item in result:
    print(item)

# 如果不是获取所有节点而是指定获取某个节点，只需将*改成节点名称即可，如获取所有的li节点。
# 这个HTML代码可以直接放在代码的变量中，也可以放在文件中，效果都一样。


# 3.4.4 获取所有节点

# 根据XPath常用规则可知，通过“/”或“//”可以获取子孙节点或子节点，如果要获取li节点下的a节点，也可以使用//ul/a，
# 首先选择所有的ul节点，然后再获取ul节点下的所有a节点，最后结果是一样的。但是使用//ul/a就不行了，首先选择所
# 有的ul节点，然后再获取ul节点下的直接子节点a，当然获取不到。需要深刻理解“//”和“/”的不同之处。
# “/”用于直接获取子节点，“//”用于获取子孙节点，示例代码如下：

from lxml import html
etree = html.etree
html = html.xpath('//li/a') # //li表示选择所有的li节点，/a表示选择li节点下的直接子节点a
for item in result:
    print(item)


# 3.4.5 获取文本信息

# 很多时候找到指定的节点都是要获取节点内的文本信息，这里使用text()方法获取节点中的文本，例如，获取所有
# a标签的文本信息，示例代码如下：

from lxml import html
etree = html.etree
html = etree.parse('./test.html',etree.HTMLParse())
result = html.xpath('//ul//a/text()')
print(result)

# XPath在爬虫中使用得最频繁的方法基本就是这些，当然，除了以上讲解的这些外，它还有很多使用方法，有兴趣可以去
# W3School官网查看XPath教程
