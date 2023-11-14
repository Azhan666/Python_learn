# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
# python之正则表达式大全
#
# Clark_Xu
# 2019 - 06 - 12
# 15: 04:23
# 9863
# 已收藏
# 342
# 分类专栏： python
# 文章标签： 正则表达式
# NLP
# python
# 版权
#   nlp任务中，正则表达式是一个很好的工具。
#
#  推荐资源：
#
#  https: // github.com / ziishaned / learn - regex /
#   https: // regex101.com /    在线练习
#
#   结合网上的教程，我的整理如下：
#
#   先来举个例子：
#
# # 解析网页  HTML  <html><body><h1>hello world<h1></body></html>
# import re
#
# key = r"<html><body><h1>hello world<h1></body></html>"
# p1 = r"(?<=<h1>).+?(?=<h1>)"
# pattern1 = re.compile(p1)
# matcher1 = re.search(pattern1, key)
# print(matcher1.group(0))  # hello world
# 然后下面是常用的正则字符和规则：
#   
#
# """
# ### 常用元字符 ###
# 1 .:匹配任何一个字符;
# 2 ^:匹配除去所列首个字符外的所有字符; ^\d表示必须以数字开头。
# 3 $:匹配字符串的尾部字符  \d$表示必须以数字结束
# 4 []:由一对方括号括起来的字符，表明一个字符集合，能够匹配包含在其中的任意一个字符。’-‘ 减号来指定一个字符集合的范围。例子：[a-zA-Z][^a-zA-Z]
# 5 | 将两个规则并列起来，注意是匹配两边所有的规则
#     要匹配 ‘I have a dog’或’I have a cat’，需要写成r’I have a (?:dog|cat)’ ，而不能写成 r’I have a dog|cat’
# 5 (?: )  如果想限定它的有效范围，必需使用一个无捕获组 ‘(?: )’包起来
# 6 \d  匹配数字,这是一个以’\’开头的转义字符，’\d’表示匹配一个数字，即等价于[0-9]
# 7 \D 匹配非数字 这个是上面的反集，即匹配一个非数字的字符，等价于[^0-9]。注意它们的大小写
#    下面我们还将看到Python的正则规则中很多转义字符的大小写形式，代表互补的关系。
# 8 \w 匹配字母和数字 匹配所有的英文字母和数字，即等价于[a-zA-Z0-9]。 \W  等价 [^a-zA-Z0-9]
# 9 \s 匹配间隔符  即匹配空格符、制表符、回车符等表示分隔意义的字符，它等价于[ \t\r\n\f\v]。（注意最前面有个空格)  补集：  \S
# 10 \A 匹配字符串开头  匹配字符串的开头。它和’^’的区别是，’\A’只匹配整个字符串的开头，即使在’M’模式下，它也不会匹配其它行的行首。
# 11 \Z 匹配字符串结尾  匹配字符串的结尾。它和’$’的区别是，’\Z’只匹配整个字符串的结尾，即使在’M’模式下，它也不会匹配其它各行的行尾。
# 12 \b’ 匹配单词边界  它匹配一个单词的边界，比如空格等，不过它是一个‘0’长度字符，它匹配完的字符串不会包括那个分界的字符。
#        而如果用’\s’来匹配的话，则匹配出的字符串中会包含那个分界符
# 13 \B 匹配非边界 它同样是个0长度字符。re.findall( r’\Bbc\w+’ , s )     #匹配包含’bc’但不以’bc’为开头的单词
#     ['bcde']  #成功匹配了’abcde’中的’bcde’，而没有匹配’bcd’
# 14 (?# ) 注释 Python允许你在正则表达式中写入注释
# ### 重复 规则 ###
# 15 *   0或多次匹配
# 16 +  1次或多次匹配  表示匹配前面的规则至少1次，可以多次匹配
# 17 ?  0或1次匹配 只匹配前面的规则0次或1次
# ### 精确匹配和最小匹配  ###
# 18 {m}    精确匹配m次
#    {m,n}  匹配最少m次，最多n次。(n>m)  指定最少3次：{3,}  最大为5次：{,5}
#     例子： re.findall( r’\b\d{3}\b’ , s )            # 寻找3位数
# 19 ‘*?’ ‘+?’ ‘??’ 最小匹配
#    ‘*’ ‘+’ ‘?’通常都是尽可能多的匹配字符（贪婪匹配）。有时候我们希望它尽可能少的匹配。
#    #例子 re.match(r'^(\d+)(0*)$', '102300').groups()  #('102300', '')
#    #     re.match(r'^(\d+?)(0*)$', '102300').groups() #('1023', '00')
#
# ### 前向界定与后向界定 ###
# 20 (?<=…) 前向界定  括号中’…’代表你希望匹配的字符串的前面应该出现的字符串。
#     前向界定括号中的表达式必须是常值，也即你不可以在前向界定的括号里写正则式
#     re.findall( r’(?<=[a-z]+)\d+(?=[a-z]+)' , s )          # 错误的用法
# 21 (?=…)  后向界定
#    不过如果你只要找出后面接着有字母的数字，你可以在后向界定写正则式：
#    re.findall( r’\d+(?=[a-z]+)’, s )
# 22 (?<!...) 前向非界定
# 只有当你希望的字符串前面不是’…’的内容时才匹配
# 23 (?!...) 后向非界定
# 只有当你希望的字符串后面不跟着’…’内容时才匹配。
# ### 使用组 ###
# 24  ()    包含在’()’中的内容，而虽然前面和后面的内容都匹配成功了，却并不包含在结果中,
#     用group()或group(0)返回匹配的所有结果，用 group(1)，(2)...返回第1，2...个()里面的内容
# 25  (?(id/name)yes-pattern|no-pattern) 判断指定组是否已匹配，执行相应的规则
#     这个规则的含义是，如果id/name指定的组在前面匹配成功了，则执行yes-pattern的正则式，否则执行no-pattern的正则式。
#
# ### 注意 ###
# 碰到字符串里面有以上的符号的或者像是 _ - 等字符  要加转义符 \
# """
# import re
#
# p1 = '.+'
# p2 = '[^bc]'
# p3 = '[ab$]'
# p4 = '[a-z]'
# string = 'abc'
# m = re.match(p1, string)
# n = re.match(p2, string)
# l = re.match(p3, string)  # ?
# o = re.match(p4, string)
# # m.group() #abc
# # n.group() # a
# # l.group() # a
# o.group()  # a
#
# s = '12 34\n56 78\n90'
# print(re.findall(r'^\d+', s, re.M))  # 匹配位于行首的数字
# print(re.findall(r'\A\d+', s, re.M))  # 匹配位于字符串开头的数字
# print(re.findall(r'\d+$', s, re.M))  # 匹配位于行尾的数字
# print(re.findall(r'\d+\Z', s, re.M))  # 匹配位于字符串尾的数字
#
# s1 = 'abc abcde bc bcd'
# print(re.findall(r'\bbc\b', s1))  # 匹配一个单独的单词 ‘bc’ ，而当它是其它单词的一部分的时候不匹配
#
# ### 综合例子  ###
#
# s2 = 'aaa bbb111 cc22cc 33dd'
# re.findall(r'\b[a-z]+\d*\b', s2)  # ['aaa', 'bbb111']       #必须至少1个字母开头，以连续数字结尾或没有数字，并且首尾为边界符
#
# s3 = '123 10e3 20e4e4 30ee5'
# re.findall(r'\b\d+[eE]?\d*\b', s)  # ['123', '10e3']   这样就可以把科学计数法记录的数字也拿出来了
#
# s4 = '/* part 1 */ code /* part 2 */'  # 找出 C++注释
# re.findall(r'/\*.*?\*/', s4)  # ['/* part 1 */', '/* part 2 */']   #  .*?  表示匹配任意一个字符0次或多次，加？表示尽可能少匹配,要加转义符 \
#
# re.findall(r'(?<=/\*).+?(?=\*/)', s4)  # 不希望匹配的结果把’/*’和’*/’也包括进来
#
# s5 = 'aaa111aaa , bbb222 , 333ccc'
# # re.findall( r'(?<=[a-z]+)\d+(?=[a-z]+)' , s5 )   # 前向错误 ，后向可以  # 要匹配包夹在字母中间的数字
#
# re.findall(r'[a-z]+(\d+)[a-z]+', s5)  # 使用group
#
# # 下面使用组！#
# s6 = 'aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg'
# re.findall(r'([a-z]+)\d+([a-z]+)', s6)  # [('aaa', 'aaa'), ('fff', 'ggg')]  # 找出中间夹有数字的字母
#
# # (?P<name>…)’ 命名组  ,‘(?P=name)’ 调用已匹配的命名组
# re.findall(r'(?P<g1>[a-z]+)\d+(?P=g1)', s6)  # ['aaa']   # 找出被中间夹有数字的前后同样的字母 fff777ggg不满足
#
# # \number       通过序号调用已匹配的组  ，上面的也可以写为
# re.findall(r'([a-z]+)\d+\1', s6)  # ['aaa']
#
# s7 = '111aaa222aaa111 , 333bbb444bb33'
# re.findall(r'(\d+)([a-z]+)(\d+)(\2)(\1)', s7)  # [('111', 'aaa', '222', 'aaa', '111')] #找出完全对称的 数字－字母－数字－字母－数字 中的数字和字母
#
# # (?(id/name)yes-pattern|no-pattern)’ 判断指定组是否已匹配，执行相应的规则
# s8 = '<usr1@mail1>  usr2@maill2'  # 要匹配一些形如 usr@mail 的邮箱地址，有的写成< usr@mail >有的没有，要匹配这两种情况
# re.findall(r'(<)?\s*(\w+@\w+)\s*(?(1)>)', s8)  # [('<', 'usr1@mail1'), ('', 'usr2@maill2')]
# findall
# 在很多复杂情况下不能很好地解决，下面我们用到  group ：
#
# """group的用法
# 正则表达式中，group()用来提出分组截获的字符串，（）用来分组
# """
#
# import re
#
# a = "123abc456"
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0))  # 123abc456,同group（）就是匹配正则表达式整体结果
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1))  # 123 第一个括号匹配部分
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))  # abc 第二个括号匹配部分
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3))  # 456 第三个括号匹配部分
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).groups())  # ('123', 'abc', '456')
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).groupdict())  # {} 为空？
# m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)', 'myname@hackerrank.com')
# m.groupdict()  # {'extension': 'com', 'user': 'myname', 'website': 'hackerrank'}
#    接下来介绍几个常用的函数：
#
# """
# re.sub用于替换字符串中的匹配项
# re.sub(pattern, repl, string, count=0, flags=0)
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# """
# import re
#
# phone = "2004-959-559 # 这是一个国外电话号码"
#
# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码是: ", num)  # 电话号码是:  2004-959-559
#
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print("电话号码是 : ", num)  # 电话号码是 :  2004959559
#
#
# # repl 参数是一个函数
# # 将匹配的数字乘以 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))  # A46G8HFD1134
#
# # 如果我们只想替换前面两个，则
# s = 'I have a dog , you have a dog , he have a dog'
# print(re.sub(r'dog', 'cat', s, 2))  # ' I have a cat , you have a cat , he have a dog '
#
# # 或者我们想知道发生了多少次替换，则可以使用subn
# print(re.subn(r'dog', 'cat', s))  # ('I have a cat , you have a cat , he have a cat', 3)
# """findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。
# findall(string[, pos[, endpos]])
# 参数：
# string : 待匹配的字符串。
# pos : 可选参数，指定字符串的起始位置，默认为 0。
# endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。"""
# import re
#
# pattern = re.compile(r'\d+')  # 查找数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)
#
# """re.finditer
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
# re.finditer(pattern, string, flags=0)"""
# it = re.finditer(r"\d+", "12a32bc43jf3")
# for match in it:
#     print(match.group())
# """
# re.match(pattern, string, flags=0)
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
# pattern	匹配的正则表达式
# string	要匹配的字符串
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
# """
# """flags:
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和 # 后面的注释
# """
# """
# re.search 扫描整个字符串并返回第一个成功的匹配。
# re.search(pattern, string, flags=0)
# """
# """re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。"""
#
# import re
#
# line = "Cats are smarter than dogs";
#
# matchObj = re.match(r'dogs', line, re.M | re.I)  # No match!!
# if matchObj:
#     print("match --> matchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")
#
# matchObj = re.search(r'dogs', line, re.M | re.I)  # search --> matchObj.group() :  dogs
# if matchObj:
#     print("search --> matchObj.group() : ", matchObj.group())
# else:
#     print("No match!!")
# """re.split
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
# re.split(pattern, string[, maxsplit=0, flags=0])
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。"""
# import re
#
# re.split('\W+', 'runoob, runoob, runoob.')
# re.split('(\W+)', ' runoob, runoob, runoob.')
# # ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
# re.split('\W+', ' runoob, runoob, runoob.', 1)
# # ['', 'runoob, runoob, runoob.']
# re.split('a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
# # ['hello world']
#  
#
# 在编写正则表达式，我们正规写法通常是
# 用re.complie, 可以加快规则的编译。
#
# """
# re.compile 函数
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# 直接使用findall,split,sub等 的方式来匹配字符串，如果是多次使用的话，由于正则引擎每次都要把规则解释一遍，而规则的解释又是相当费时间的，
# 所以这样的效率就很低了。如果要多次使用同一规则来进行匹配的话，可以使用re.compile函数来将规则预编译
# re.compile(pattern[, flags])
# """
# import re
#
# pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
# m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
# print(m)
# m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
# print(m)
# m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
# print(m)  # 返回一个 Match 对象
# m.group()
# """group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
# start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置
# end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置
# span([group]) 方法返回 (start(group), end(group))"""
#
# # compile过的规则使用和未编译的使用很相似。compile函数还可以指定一些规则标志，来指定一些特殊选项。多个选项之间用 ’|’（位或）连接起来。
#
# ————————————————
# 版权声明：本文为CSDN博主「Clark_Xu」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / Findingxu / article / details / 91526471