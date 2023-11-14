# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# Python语言的文本处理功能非常强大，仅仅依赖字符串类的方法，就可以实现几乎所有的字符串操作。
# 字符串对象还可以像列表那样索引和切片，但无法改变字符串对象的内容，这有点类似元组不可以增
# 加、删除和修改元素。

str(3.14) # 数字转字符串
'3.14'

str(['a',1]) # 列表转字符串
"['a',1]"

str({'a':1,'b':2}) # 字典转字符串
"{'a':1,'b':2}"

s = 'python真好用，very good.'
s[1:-1] # 掐头去尾
print(s[1:-1])

s[::2] # 隔一个取一个元素
print(s[::2])

s[::-1] # 反转字符串
print(s[::-1])

s.upper() # 全部大写 upper:adj. 上面的，上部的；较高的
print(s.upper())

s.lower() # 全部小写 lower:adj. 下方的；在底部的；（数字或数量）较小
print(s.lower())

s.capitalize() # 字符串首字母大写 capitalize:资本化 首字母大写 首字符大写
print(s.capitalize())

s.title() # 单词首字母大写 title：标题 题目 头衔
print(s.title())

s.startswith('python') # 判断是否以指定的子串开头,返回True或False
print(s.startswith('python')) # startswith：以 以…开头 开头

s.endswith('good.') # 判断是否以指定的子串结尾 end:结尾，末尾
print(s.endswith('good.'))

s.find('very') # 查找字符串首次出现的索引，未找到则返回-1
print(s.find('very'))

s.split() # 分割字符串，还可以指定分隔符,默认分隔符为逗号
print(s.split()) # split：斯普利特 分割 分裂

s.replace('very','veryvery') # 替换子串 replace:替换 取代 接替
print(s.replace('very','veryvery'))

'2345.6'.isdigit() # 判断是否是数字
print('2345.6'.isdigit())

'ads12k56'.isalpha() # 判断是否是字母
print('ads12k56'.isalpha())

'ads12k56'.isalnum() # 判断是否是字母和数字
print('ads12k56'.isalnum())

'\t ads12k56 \n'.strip() # 去除首尾空格（包括制表位和换行符）
print('\t ads12k56 \n'.strip())