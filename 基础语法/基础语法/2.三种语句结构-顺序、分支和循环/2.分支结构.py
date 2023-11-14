# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 代码运行过程中，会根据条件选择不同的分支继续执行，这就是程序的分支就结构。
# Python语言使用if-else描述分支结构，支持嵌套，并将else-if简写为elif。

a, b, c = 3, 4, 5
if a > b: # 最简单的if-else分支结构
    print(a)
else:
    print(b)

if a > b and a > c: # 类似switch结构的分支结构
    print(a)
elif b > c:
    print(b)
else:
    print(c)

if a > b: # 嵌套的if-else分支结构
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

# 以上代码演示了三种最常见的分支结构。第一种是最简单的if-eles分支结构，即使没有else分支也是
# 合乎规则的；第二种是类似switch结构的分支结构；第三种是嵌套的if-else分支结构。