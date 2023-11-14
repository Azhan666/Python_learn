# !/usr/bin/env python
# -*- coding: utf-8 -*-
# num1 = 1
# num2 = 2
# num3 = 3
# total = num1 + num2 + num3
# print("total is : %d"%total)

# import keyword
# print(keyword.kwlist)
# """['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
# 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']"""
# 参考链接：
# 关键字用法总结：https://www.cnblogs.com/cwp-bg/p/9830228.html

# 使用id查看内存地址：
# class Obj():
#     def __init__(self, arg):
#         self.x = arg
# if __name__ == '__main__':
#         obj = Obj(1)
#         print(id(obj))
#         obj.x = 2
#         print(id(obj))
#
# s = "abc"
# print(id(s))
#
# s = "bcd"
# print(id(s))
#
#
# x = 1
# print(id(x))
#
# x = 2
# print(id(x))
# 3114915493056
# 3114915493056
# 3114915451760
# 3114915524912
# 140736280467104
# 140736280467136

# 同时赋值多个变量：
# a = (1,2,3) # 定义一个元组
# x,y,z = a # 把序列的值分别赋给多个变量
# print("x: %d, y: %d, z: %d"%(x,y,z))
# # x: 1, y: 2, z: 3

# a = b = c = 1
# d, e, f, g = 1, 2, "jack",3
# print(d,e,f,g,)
# 1 2 jack 3

"""实现输入功能"""
# input("prompt") #prompt为可选参数，用来提供用户输入的提示信息字符串，当用户输入程序所需要的数据时，
# 就会以字符串的形式返回，也就是说，函数input不管输入的是什么，最终返回的都是字符串，如果需要输入数值，
# 则必须经过类型转换处理。

"""实现输出功能"""
# 1.value、
# 2.sep(分隔符)
# 3.end（换行符）

# print('100 + 200 =', 100 + 200)
# # 100 + 200 = 300
# 需要注意的是，对于"100 + 200"来说，python解释器自动计算出结果300，但是‘100+200=’是字符串
# 而非数学公式，python把他视为字符串，需要我们自行解释上述输出结果。

# demo_1:

# print('a','b','c')
# print('a','b','c',sep=',') # 分隔符改为“，”
# print('a','b','c',sep=';') # .........";"
# print('peace',22)
# a b c
# a,b,c
# a;b;c
# peace 22

# 实现格式化输出：

# pi = -3.141592653
# print('%10.3f'%pi) # 字段宽为10，精度为3
# -3.142
# print("pi = %.*f"%(4,pi)) # 用*从后面的元组中读取字段宽度或精度
# pi = -3.1416
# print('%010.3f'%pi) # 用0填充空白
# -00003.142
# print('%-10.3f'%pi) # 左对齐
# -3.142
# print('%+f'%pi) # 显示正负号
# -3.141593

# 实现不换行输出：

# for x in range(0,10):
#     print(x,end='')
# 0123456789

# 字符串截取：
# Var_1 = 'Hello World!'
# print(Var_1[0:1])
# # H
# # 拼接：
# num = 100
# str = '000' + str(num)
# print(str[-3:])

# print("我的名字是%s,今年%d岁"%('何展',20))

# 输入某年某月某日,判断这一天是这一年的第几天：

# import datetime
# y = int(input("请输入四位数字的年份：")) # 获取年份
# m = int(input("请输入月份：")) # 获取月份
# d = int(input("请输入是哪一天：")) # 获取“日”
#
# targetDay = datetime.date(y, m, d) # 将输入的日期转换为标准日期
# dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31) # 当前天数=当年-去年最后一天
# print('%s是%s年的第%s天'%(targetDay,y,dayCount.days))

# 输入3个整数x、y、z、请将这3个数由小到大输出
# 方法_1:
# import re

# x, y, z = re.split(',| |,| ',input('请输入3个数字，用逗号或空格隔开：'))
# x, y, z = int(x), int(y), int(z)
#
# maxNo = max(x, y, z)
# minNo = min(x, y, z)
# print(minNo, x+y+z-maxNo-minNo, maxNo)

# 方法二  用 re.split() 得到 3 个字符型数字的列表，把字符转换为数字，排下序，然后 print() 代码如下：
# import re
#
# lst = re.split(',| |，|  ', input('请输入3个数字，用逗号或空格隔开：'))
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# lst.sort()
# print(lst)