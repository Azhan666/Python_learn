# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# Python语言的循环结构有两种：for循环和while循环。for循环一般用于循环次数确定的场
# 合，如遍历列表、字典等。while循环一般用于循环次数不确定的场合，每次循环之前，都要对循环条件做
# 判断。为了避免“死循环”，在while循环体内通常都会存在影响循环条件的代码，除非希望while循环永不
# 停止。
#     循环体内有两个特殊语句会影响到for循环和while循环，这就是continue和break语句。
# continue语句可以立即结束本次循环，开始下一个循环；break语句则是立即跳出循环，继续执行for或者
# while循环后面的语句。

for i in range(3): # 这是for循环最经典的用法 range:范围
    print(i)

for i in [3,4,5,6,7,8,9,10]: # 遍历数组是for循环应用最频繁的形式
    if i%2 == 0:
        continue
    if i > 8:
        break
    print(i*'*')

d = {'a':1, 'b':2}
for key in d: # 遍历字典的标准写法
    print(key, d[key])

# 以上代码是for循环的几种应用形式。for循环常被用来遍历列表、字典，如果用来计数循环，一般使用
# range()函数返回一个计数范围。关于range()函数，2.1.6节有详细讲解。

a = 3
while a > 0: # 判断循环条件
    print(a*'*')
    a -= 1 # 影响循环条件

a = 0
while True: # 死循环
    a += 1 # 影响循环出口条件
    if a > 3: # 设置循环出口条件
        break
    print(a*'*')

# 以上代码是while循环的两种应用形式，第一种方式设置了循环条件，如果条件不满足则退出循环；
# 第二种方式的循环条件永远为真，只能通过break语句终止循环。