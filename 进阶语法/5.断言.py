# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 2.2.5 断言

# 写在前面：
# 断言就是声明表达式的布尔值必须为真的判定，否则将触发AssertionError异常。严格来讲，assert是
# 调试手段，不宜使用在生产环境中，但这不影响用断言来实现一些特定功能，如输入参数的格式、类型验
# 证等。 AssertionError：断言错误 声明错误 潩䕮牲

import time
def i_want_to_sleep(delay):
    assert(isinstance(delay, (int,float))), '函数参数必须为整数或浮点数'
    print('开始睡觉')
    time.sleep(delay)
    print('睡醒了')

i_want_to_sleep(1.1)
print(i_want_to_sleep(1.1))

i_want_to_sleep(2)
print(i_want_to_sleep(2))

i_want_to_sleep('2')
print(i_want_to_sleep('2'))  # 会触发AssertionError异常啦！

# 以上代码使用断言对函数的输入参数delay做类型检查，如果delay既不是整数，又不是浮点数，就会
# 抛出异常，其异常类型是断言错误。