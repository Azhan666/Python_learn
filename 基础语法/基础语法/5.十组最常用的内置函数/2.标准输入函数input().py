# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# input()函数用于程序执行过程中接收键盘输入。按回车键，input()函数即返回从键盘输入的字符串
# ，但不包括回车符。因为input()函数本身具备IO阻塞的功能，所以也可以在程序中作为调试断点来使
# 用。input()函数没有默认参数，接受一个字符串作为输入提示信息。

# 以下代码演示了input()函数的用法。

# nums = input('请输入三个整数，中间以空格分隔，按回车键结束输入：')
# print(nums) # 请注意，nums是一个字符串，不是整数
# [int(item) for item in nums.split()] # 这样才可以把输入的字符串变成三个整数

"""实现输入功能"""
# input("prompt") #prompt为可选参数，用来提供用户输入的提示信息字符串，当用户输入程序所需要的数据时，
# 就会以字符串的形式返回，也就是说，函数input不管输入的是什么，最终返回的都是字符串，如果需要输入数值，
# 则必须经过类型转换处理。

# example：猜数游戏
# import random
# num = random.randint(0,10) # 猜数区间
# print('------欢迎挑战猜数字游戏！------')
# def strToint(temp): # strToint：将字符串转换为整型
#     try:
#         g = int(temp)
#         return g
#     except:
#         print('出错啦！请输入一个非零数字哦')
# temp=input('输入一个非零数字吧：')
# guess = strToint(temp)
# n = 0
# while(guess!=num and n<2):
#     if(guess>num):
#         print('嘿嘿，猜大了，你还有'+(str)(2-n)+'次机会哦')
#         n = n+1
#     else:
#         print('嘿嘿，猜大了，你还有'+(str)(2-n)+'次机会哦')
#         n = n+1
#     temp=input('再猜一个数字吧：')
#     guess=int(temp)
# if(n==3):
#     print('太遗憾了，你已经没有机会了')
# else:
#     print('你太厉害了，猜对了！')
# print("游戏结束")

