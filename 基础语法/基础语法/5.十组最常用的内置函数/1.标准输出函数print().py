# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# Python语言的内置函数超过70个（习惯上把内置类也统称为内置函数），覆盖面广，功能强大。
# 不过，对于初学者而言，有些函数晦涩难懂，在初级阶段完全可以忽略；有些函数则必须深刻理
# 解、熟练应用。以下十组、共计21个函数是最常用的，也是无可替代的，自然也是初学者“应知应会”
# 的函数。

# ********************************我是分割线***************************************
# 1.标准输出函数print()
# 写在前面：
# print()函数应该是每一位Python语言初学者首先接触到的函数，也应该是使用的非常熟练的一个函
# 数。众所周知，print()函数一次可以打印多个对象，打印对象也可以是任意类型。此外，print()函
# 数还有四个默认参数，学会灵活运用这些参数，方能在使用print()函数时得心应手。

# sep:间隔多个对象，默认值是一个空格。

# end：设定结尾，默认值是换行符(\n)。

# file：要写入的文件对象，默认是标准输出控制台（sys.stdout）。

# flush：是否立即输出缓存，默认内容不会立即被输出（False）。

print(3,[1,2,3],{'name':'David'}) # 一次可以打印多个对象，打印对象可以是任意类型

print(1,2,'x','y',sep='*') # 多个打印对象之间使用星号分隔

for item in [1,2,'x','y']:  # item：项目 道具 项
    print(item,end=',') # 不换行打印

with open(r'd:\print_out.txt','w') as fp: # 打印到文件d:\print_out.txt
    print(1,2,'x','y',sep='*',file=fp)

# 以上代码以交互式方式演示了print()函数的几个使用技巧。鉴于在Python的IDEA上无法体验
# flush参数的效果，下面以源码的形式给出三个例子。这三个例子巧妙利用print()函数的多个
# 参数，实现打字机效果、旋转式进度提示、覆盖式打印效果等特殊效果。

import time

def printer(text,delay=0.2):   # delay:延迟 延时 耽搁 # 定义一个打印机函数
    """打字机效果"""
    for ch in text:
        print(ch,end='',flush=True)  # flush:同花 冲洗 刷新
        time.sleep(delay)   # 调用函数sleep(delay)
    print()

def waiting(cycle=20,delay=0.1):  # waiting:等待 等待 恭候 cycle:周期 循环 套曲
    """旋转式进度提示"""
    # 定义一个进度提示函数

    for i in range(cycle):
        for ch in ['年','青人','不讲','武德']:
            print('\b%s'%ch,end='',flush=True)
            time.sleep(delay)
    print()

def cover(cycle=100,delay=0.2):  # cover:覆盖 封面 涵盖
    """覆盖式打印效果"""
    # 定义一个覆盖式打印效果函数

    for i in range(cycle):
        s = '\r%d'%i
        print(s.ljust(3),end='',flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print('敢问来者何人？吾乃形意门马保国！孰能与我一决高下！')
    waiting(cycle=10)
    cover(cycle=10)

