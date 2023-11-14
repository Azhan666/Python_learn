# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""3.6 数据解析"""

"""
    处理数据时避免不了要解析html文档或文本文件,尤其是从互联网上抓取下来的数据,更需要进行解析,因此
解析html文档或文本文件是程序员必备的技能,本节主要讲解使用BeautifulSoup模块解析html文档,以及使用
re模块解析文本文件的基本方法。

    3.6.1 使用Beautifulsoup模块解析html/xml数据
    
    BeautifulSoup模块是一个可以从html或xml中提取数据的Python库,功能强大、使用便捷。
BeautifulSoup既支持Python标准库中的html解析器,也支持其他解析器。强烈建议使用功能强大的第三方解析
器lxml,我曾经用它处理过单个文件有几百兆字节的xml数据,反应速度非常快,毫无迟滞感。如果还没有安装lxml
模块,建议在安装BeautifulSup模块的同时,也安装lxml模块。
pip install beautifulsoup4 lxml
    我们以解析下面的html文档为例,演示BeatifulSoup模块的用法。关于html或xml,有必要说明两点;
首先,文本也是节点,称为文本型节点,例如下面文档中p标签里面的One、Two、 Three等文本内容就是p标签的
文本型子节点;其次,节点的子节点往往比表面上看到的多,因为在可见的子节点外的换行、空格、制表位等,也都
是该节点的文本型子节点。
"""
html_doc = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id ="My love">
    <p class="intro short-text" align="left">One</p>
    <p class="intro short-text" align="center">Two</p>
    <p class="intro short-text" align="right">Three</p>
</div>
    <img class="photo" src="阿婷.jpg">
    <div class="photo">
        <a href="阿婷.png"><img src="微信图片_20210207200748.jpg"></a>
        <p class="subj">阿展要提高</p>
    </div>
</body>
</html>
"""
"""1.导入模块，加载html文档
    导入Beautifulsoup模块后，创建解析器实例时，需要指定解析器，首选lxml解析器，如果没有指定解析器，
Beautifulsoup模块会自动查找并使用系统可用的解析器。"""

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc,'lxml') # 使用lxml解析器

"""2.获取节点对象的名称和属性"""
# 官方中文文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
# 使用Beautifulsoup()生成一个soup对象后，就可以使用标签名得到节点对象，继而取得节点名称、节点属性
# 字典等。

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.p.name) # p标签节点名称
# # p
# print(soup.img.attrs) # 获取img标签节点的属性字典，attrs：属性
# # {'class': ['photo'], 'src': '阿婷.jpg'}
# print(soup.img['src']) # 也可以直接使用属性名获取属性值
# # 阿婷.jpg
# print(soup.p['class']) # 获取p标签节点的样式，返回一个列表
# # ['intro', 'short-text']
# print(soup.div['id']) # 获取div标签节点的id属性
# # My love

"""从上述代码中可以很明显的看到，使用标签名得到的节点一定是html文档中第一个同类型的标签，
上面的例子还演示了如何使用节点对象的所有的属性和指定属性，当class属性有多个值时，返回的是一个列表
，而id属性不承认多值。"""

"""3.获取节点的文本内容
    获取节点的文本内容时，如果该节点只有文本型节点，则下面代码中的4种方法的效果将完全一致，
如果该节点包括元素型子节点，输出的结果可能已经不是我们需要的内容了，此时，可以使用stripped_string
得到一个迭代器，遍历即可得到我们想要的内容。"""

# print(soup.p.text) # 获取p标签节点的文本(方法1)
# # One
# print(soup.p.getText()) # 获取p标签节点的文本(方法2)
# # One
# print(soup.p.get_text()) # 获取p标签节点的文本(方法3)
# # One
# print(soup.p.string) # 获取p标签节点的文本(方法4)
# # One
# print(soup.div.text)
# # One
# # Two
# # Three
# for item in soup.div.stripped_strings:
#     print(item)
# # One
# # Two
# # Three

"""4.父节点、子节点和兄弟节点
    节点对象的parent属性指向其父节点，节点对象的children属性或contents属性指向其子节点，
descendants（后代）属性则指向其所有后代节点，另外，contents返回的是子节点的列表，children和
descendants返回的是迭代器。"""

# print(soup.p.parent.name) # 获取p标签节点的父节点的名字
# # div
# print(soup.div.contents) # 以列表形式返回div标签节点的子节点
# # ['\n', <p align="left" class="intro short-text">One</p>, '\n',
# # <p align="center" class="intro short-text">Two</p>, '\n', <p align="right"
# # class="intro short-text">Three</p>, '\n']
# print(soup.div.children) # 以迭代器的形式返回div标签节点的子节点
# # <list_iterator object at 0x000002418529BA58>
# print(list(soup.div.children)) # 迭代器转为列表
# # ['\n', <p align="left" class="intro short-text">One</p>, '\n',
# # <p align="center" class="intro short-text">Two</p>, '\n', <p align="right"
# # class="intro short-text">Three</p>, '\n']
# print(list(soup.div.descendants)) # 转为列表的后代节点
# #['\n', <p align="left" class="intro short-text">One</p>, 'One', '\n',
# # <p align="center" class="intro short-text">Two</p>, 'Two', '\n', <p align="right"
# # class="intro short-text">Three</p>, 'Three', '\n']

"""节点对象的previous_sibling和text_sibling属性分别指向该节点的上一个或下一个兄弟节点，因为
两个p标签之间有换行，相当于存在一个不可见的兄弟节点，因此下面的代码中，next_sibling和previous_
sibling属性要使用两次才能找到下一个或上一个可见的兄弟节点。
previous：以前的，上一个，sibling：兄弟姊妹"""

# p_tag = soup.p # tag：标签
# print(p_tag.text)
# # One
# p_tag = p_tag.next_sibling.next_sibling
# print(p_tag.text)
# # Two
# p_tag = p_tag.previous_sibling.previous_sibling
# print(p_tag.text)
# # One

"""5.搜索节点
    一般使用find()和find_all()搜索符合条件的第一个节点和全部节点的列表,搜索条件既可以是节点,
也可以使用正则表达式匹配节点名"""

# print(soup.find('img')) # 返回单个节点
# # <img class="photo" src="阿婷.jpg"/>
# print(soup.find_all('p')) # 返回节点列表
# # [<p align="left" class="intro short-text">One</p>, <p align="center"
# # class="intro short-text">Two</p>, <p align="right" class="intro short-text">Three</p>,
# # <p class="subj">阿展要提高</p>]
import re
# print(soup.find_all(re.compile('^d'))) # 返回节点名以d开头的节点列表
# # [<div id="My love">
# # <p align="left" class="intro short-text">One</p>
# # <p align="center" class="intro short-text">Two</p>
# # <p align="right" class="intro short-text">Three</p>
# # </div>, <div class="photo">
# # <a href="阿婷.png"><img src="微信图片_20210207200748.jpg"/></a>
# # <p class="subj">阿展要提高</p>
# # </div>]

# 除了使用节点名进行搜索外,还可以根据id或其他属性搜索节点,其代码如下:

# print(soup.find_all(id='My love')[0].name) # 查找id=My love的节点
# # div
# print(soup.find_all(id=True)[0].name) # 查找有id属性的节点
# # div
# print(soup.find_all(attrs={"id":"My love"})[0].name) # 使用attrs查找
# # div
# print(soup.find_all(attrs={"class":"intro short-text","align":"right"})[0].text)
# # 使用attrs查找
# # Three
# print(soup.find_all(attrs={"align":"right"})[0].text)
# # Three

# 使用CSS的样式名搜索节点也是常用的手段,需要注意的是,为了区分class这个关键字,样式搜索使用class_
# 作为参数名.

# 关于re.compile():https://www.cnblogs.com/xp1315458571/p/13720333.html

# print(soup.find_all("p", class_="intro"))
# # [<p align="left" class="intro short-text">One</p>, <p align="center"
# # class="intro short-text">Two</p>, <p align="right" class="intro short-text">Three</p>]
# print(soup.find_all("p", class_="intro short-text"))
# # [<p align="left" class="intro short-text">One</p>, <p align="center"
# # class="intro short-text">Two</p>, <p align="right" class="intro short-text">Three</p>]
# print(soup.find_all(string="Two"))
# # Two
# print(soup.find_all(string=re.compile("Th")))
# # Three

# BeautifulSoup模块支持使用函数搜索,该方法常用于需要大量提取数据,但判断条件又极其复杂的数据解析,
# 下面的代码搜索的是父节点有id属性且自身居中对齐的节点.

# def justdoit(tag):
#     return tag.parent.has_attr('id') and tag['align']=='center'
# print(soup.find_all(justdoit))
# [<p align="center" class="intro short-text">Two</p>]

"""3.6.2 使用正则表达式解析文本数据
    
    正则在汉语词典中被解释为“正其礼仪法则”,和正则表达式似乎毫不相干。幸好汉字可以顾名思义,将正则
理解为合乎标准的规则也很贴切。所谓正则表达式,就是用事先定义好的一些特定字符以及这些特定字符的组合,
组成一个“规则字符串”,用来表达对字符串的一种过滤逻辑。正则表达式的英文写作Regular Expression,缩写
为RE.
    正则表达式的规则之艰深酶涩,足令初学者望而却步。其实,只要理解了正则表达式的基本概念,稍微归纳一下
知识点,掌握并熟练应用正则表达式,也不是什么很难的事情,大约30分钟就可以做到。
    正则表达式的学习过程可以分成两部分:第一,如何写正则表达式;第二,怎么用正则表达式。第一个问题和
语言无关,需要了解正则表达式的字符集和特殊符号集,以及几条规则:第二个问题,就是掌握Python内置的正则
表达式标准模块re的用法。

    1.正则表达式的写法
    写正则表达式,就是用规则描述想找到的字符串的特征。例如,下面的写法描述的是由小写字母组成的、长度
为3~8位的字符串。
pstr = r'[a-z]{3,8}'
    这是一个原生字符串(字符串前标r,则不会对反斜杠进行特殊处理),方括号内约定了允许使用的字符集,
花括号约定了字符的最少位数和最多位数。
    正则表达式定义了若干符号来描述正则表达式的字符集和组合规则。表3-7列出了这些常用的符号和含义。
"""
"""表3-7:
            符号:              说明:
            .       匹配除换行\n以外的任意字符
            \       转义字符,使后一个字符改变原来的意思,例如\n,把字母n变成了换行符
            *       匹配0次或多次，等效于{0,}
            +       匹配1次或多次，等效于{1,}
            ？      匹配0次或1次，等效于{0,1}
            ^       匹配字符串开头，在多行模式中匹配每一行的开头
            $       匹配字符串末尾，在多行模式中匹配每一行的末尾
            |       匹配被|分割的表达式中的任意一个，从左到右匹配
            {}      {m}表示匹配m次，{m,n}表示至少匹配m次，至多n次，{m,}表示匹配至少m次
            []      匹配字符集，字符集内的^表示取反
            ()      子表达式，可以后接数量词
            \d      匹配数字字符集，等效于[0-9]
            \D      匹配非数字字符集，等效于[^0-9]
            \s      匹配包括空格、制表位、回车、换行等在内的空白字符集
            \S      匹配非空字符集
            \w      匹配包括下划线在内的数字和字母，等效于[A-Za-z0-9]
            \W      匹配包括下划线在内的数字和字母以外的字符集，等效于[^A-Za-z0-9]
            
    了解这些符号的含义和用法之后，就可以用他们来描述任意复杂的字符串了，下面是几个相对复杂的
正则表达式："""
# print(pstr = r'[1-9]\d{2}') # 100~999的数字
# print(pstr = r'公元([1-9]\d*)年') # 公元和年之间是不以0开头的数字，数字被指定为子表达式
# print(pstr = r'color=(red|blue)') # color=red，或者color=blue，颜色被指定为子表达式

"""2.正则表达式的用法
    尽管用原生字符串来表示一个正则表达式，在使用时没有任何问题，但是建议把原生字符串表示的正则
表达式用re.compile()编译成一个模式对象，这样就可以使用模式对象的各种方法，代码如下："""

import re
# pstr = r'公元([1-9]\d*)年'
# p = re.compile(pstr)

""" 有了正则表达式的模式对象，接下来，还要清楚需要做什么，这听起来有些莫名其妙，但的确是一个问题，
通常，使用正则表达式不外乎下面这几个目的：
    （1）验证一个字符串是否符合正则表达式约定的规则。
    （2）从一个字符串中找到符合正则表达式约定规则的子串。
    （3）从一个字符串中找到所有符合正则表达式约定规则的子串。
    （4）一个字符串若存在符合正则表达式约定规则的子串，则用这个子串分割字符串。
    （5）替换一个字符串中所有符合正则表达式约定规则的子串。
    针对这5个功能需求，模式对象提供了match()、search()、findall()、split()和sub()等5个方法，
与之一一对应，下面先来试用一下match()——模式匹配。"""

s1 = '公元2021年'
s2 = '公元2021年以后'
s3 = '自公元2021年以来'
p = re.compile(r'公元([1-9]\d*)年')
# result = p.match(s1) # 匹配s1
# print(result) # 匹配成功
# <re.Match object; span=(0, 7), match='公元2021年'>

# print(result.group()) # group()方法返回匹配到的字符串
# 公元2021年
# 正则表达式中，group()用来提出分组截获的字符串，（）用来分组,括号内为可选参数，取下标，0、1...
# 关于group():https://www.cnblogs.com/baxianhua/p/8515720.html
# example code:
# s1 = '公元2021年，阿展想阿婷了。'
# s2 = '公元2018年以来，阿展最爱阿婷。'
# s3 = '公元2018年以来，阿展要努力，以后要娶阿婷回家。'
# p = re.compile(r'公元(.*?)。')
# result = p.match(s3) # 匹配s3
# print(result.group(0)) # 匹配分组
# # 2018年以来，阿展要努力，以后要娶阿婷回家
# s4 = '2021,5月继续加油！'
# p2 = re.compile(r'([1-9]\d*)')
# result_1 = p2.match(s4)
# print(result_1)
# print(result_1.group(0))
# # 2021
# print(result.groups()) # groups()方法返回匹配到的字符串
# ('2018年以来，阿展要努力，以后要娶阿婷回家',)
# result = p.match(s3)
# print(result)
# None

# 从上述代码中可以发现，模式匹配从字符串的起始位置开始，只要起始位置字符不同，匹配就会失败，
# 而字符串如果长于模式串，则不会影响匹配结果。如果要求字符串完全匹配，则需要在正则表达式最后
# 加上$,表示期待被匹配的字符串结尾和模式串一致，其代码如下：

# p = re.compile(r'公元([1-9]\d*)年$')
# result = p.match(s3) # 模式串加上$后，末尾多了两个字得s3匹配失败
# print(result)
# None

# 模式对象的search()方法会在字符串内查找匹配的字符串，找到第一个匹配的字符串就会返回；如果字符串
# 没有匹配的子串，就返回None。

# p = re.compile(r'公元([1-9]\d*)年')
# result = p.search(s1)
# print(result)
# # <re.Match object; span=(0, 7), match='公元2021年'>
# print(result.group())
# # 公元2021年
# print(result.groups())
# # ('2021',)
# print(p.search(s2)) # s2存在匹配的子串
# # <re.Match object; span=(0, 7), match='公元2021年'>
# print(p.search(s3)) # s2存在匹配的子串
# # <re.Match object; span=(1, 8), match='公元2021年'>
#
# p = re.compile(r'公元([1-9]\d*)年$') # 若指定以模式串开头和结尾
# print(p.search(s2)) # s2不存在匹配的子串
# # None
# print(p.search(s3)) # s3不存在匹配的子串
# None
""" 模式对象的findall()方法以列表形式返回字符串中所有匹配的字符串，另外，模式对象的finditer()
和findall()方法类似，只不过finditer()方法返回的是一个迭代器，下面是一段多行文本，需要从中解析出
5行11列数值数据。"""

txt = """
WDC for Geomagnetism, Kyoto
Hourly Equatorial Dst Values (REAL-TIME)
        MARCH     2021
Day   1   2   3   4   5   6   7   8   9   10
 1    -19  -11   -10  -9  -11  -14  -15  -9
 2    -12  -14   -16  -15 -14  -11  -12  -10
 3     1   -3    -9   -9  -10  -10  -13  -9
 4    -6   -3    -2   -2  -2   -3   -6   -3
 5     1    3     3    0  -3   -2   -2   -2
"""
 
 #    经过分析可以知道，每一个数据前都至少有一个空格，除了第1列均为正数，其它列的数据有正有负，
 # 因为解析以行为单位逐行处理，所以需要指定模式编译装饰参数为re.M，且模式字符串首位要加上^和$
 # 符号，据此，可以很容易写出正则表达式，并解析出全部数据。

# p = re.compile('^\s([1-5])\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)$', flags=re.M)
# result = p.findall(txt)
# print(result)

""" 模式对象的split()方法返回的是用匹配的子串分割字符串后得到的列表，若无匹配子串，则返回空列表。
    下面的例子，演示了用标点符号分割字符串，如果不用正则表达式，很难实现这个功能。"""
# s = '无论，还是。或者？都是分隔符'
# p = re.compile(r'[,。？]')
# print(p.split(s))
# ['无论,还是', '或者', '都是分隔符']

""" 模式对象的sub()方法返回的是用指定内容替换匹配子串后的字符串，下面的代码演示了用加号(+)替换
所有的标点符号，这里的标点符号集只列出了3个元素。"""

# s = '无论,还是。或者？都是分隔符'
# p = re.compile(r'[,。？]')
# print(p.sub('+', s))
# 无论+还是+或者+都是分隔符













