# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# python是一种代表简单思想的语言，其语法相对简单，很容易上手。不过，如果就此小视Python语法的精
# 妙和深邃，那就大错特错了。事实上，Python几乎具备高级语言的所有特性，还有很多独特精妙的语法结
# 构。深入了解Python语言的高级特性，熟练应用那些独特精妙的语法结构，是每一位Python程序员的必修
# 课。

# 2.2.1 函数的参数

# 在学习函数的参数前，我们先来设计一个计算体重指数（BMI）的函数。体重指数就是体重与身高的平方之
# 比，其中体重以千克为单位，身高以米为单位。

def bmi(height, weight, name):
    i = weight/height**2
    print('%s的体重指数为%0.1f'%(name, i))

bmi(1.75, 70, 'Hezhan')

# 自定义函数bmi()有三个参数，每个参数都有明确的含义。调用这个函数时，必须按照定义的顺序传入这三
# 个参数，缺一不可。这也是Python函数最基本的参数传递规则。

# 接下来把bmi()函数稍微改造一下，给name参数指定一个默认值。

def bmi(height, weight, name='您'):
    i = weight/height**2
    print('%s的体重指数为%0.1f'%(name, i))

bmi(1.75, 70) # 可以不传递name参数，使用默认值

bmi(1.75, 70, 'Hezhan') # 也可以传递name参数

# 现在bmi()函数有了两种类型的参数：weight和height，他们是函数调用时不可少的参数，且顺序必须与函
# 数定义的保持一致，这样的参数称为位置参数；name是函数调用时可有可无的参数，如果没有则使用默认值
# ，这样的参数称为默认参数。默认参数可以有多个。

# 为了使结果准确，还可以考虑使用体重均值来计算体重指数。这样函数除了接受一个weight参数外，还需要
# 接受不确定个数的体重参数。

def bmi(height, weight, *args, name='您'):
    weight = (weight+sum(args))/(1+len(args))
    i = weight/height**2
    print('%s的体重指数为%0.1f'%(name, i))

bmi(1.75, 70, name='Hezhan')

# 这下就有点复杂了，bmi()函数有了三种类型的参数。除了位置参数和默认参数，又多了一种可变参数，
# 即bmi()函数可以接受不限数量的参数。在函数定义时，可变参数名前面冠以“*”号；在函数体内，可
# 变参数相当于一个元组。

# 如此一来，就产生了一个新的问题：三种类型的参数应该以怎样的顺序被定义呢？位置参数排在首位，
# 这一点没有异议。默认参数可以放在最后，但被调用时必须加上参数名（如上面的例子），否则函数
# 无法区分究竟是可变参数的继续输入值，还是默认参数。同时，默认参数也可以放在可变参数之前，
# 但被调用时不能使用参数名，即便使用默认值也不能省略参数，否则函数会使用后面的可变参数（如
# 果有）强制为其赋值。

# 下面说一说更复杂的情况。除了上面介绍的三种类型的参数外，Python函数还支持第四种类型的参数：
# 关键字参数。关键字参数由不限数量的键值对组成。在函数定义时，关键字参数名前面冠以“**”号；
# 在函数体内，关键字参数相当于一个字典。

def bmi(height, weight, *args, name='您', **kwds):
    weight = (weight+sum(args))/(1+len(args))
    i = weight/height**2
    print('%s的体重指数为%0.1f'%(name, i))
    for key in kwds:
        print('%s的%s是%s'%(name, key, str(kwds[key])))

bmi(1.75, 70, 71, 72, 76, name='Hezhan')
print('++++++++++++++++++阿婷我好爱你++++++++++++++++++++')
bmi(1.75, 70, 71, name='Hezhan', 性别='男', 爱好='爱阿婷')

# 如果一个函数同时具备了上述四种类型的参数，参数正确的顺序应该是位置参数排在首位，关键字参数
# 排在末尾，可变参数和默认参数没有严格限定。不过，如果默认参数排在可变参数之前，则默认参数不
# 能使用参数名传参。
