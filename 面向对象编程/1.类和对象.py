# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 写在前面：
# 面向对象编程，英文全称为Object Oriented Programming,简称OOP。说起面向对象，就不得不提及类、
# 对象、继承、封装、静态函数、实例方法等概念。不过，作为Python语言的初学者，大可不必把精力花费
# 在令人费解的概念上，只需要掌握使用类的基本要素就可以了。随着经验的积累，OOP会自然而然的成为你
# 的思维习惯。

# 2.3.1 类和对象
# 写在前面：
# 学习面向对象编程，首先需要明白类和对象的基本概念，以及类实例化的含义。类是对要处理的客观事物
# 的抽象，用来描述具有相同属性和方法的对象的集合，它定义了该集合中每个对象共有的属性和方法。一
# 个类可以实例化为多个对象，对象是类在内存的实例。类是抽象的，不占用存储空间；而对象是具体的，
# 占用存储空间。类、对象和实例化之间的关系如下所示：

#                            /----->对象
#                   |____| 实例化
#                   | 类 |/
# 客观存在———抽象———>|____|—————————>对象
#                         \
#                           \------>对象