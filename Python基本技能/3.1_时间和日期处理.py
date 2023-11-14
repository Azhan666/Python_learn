# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" 写在前面"""

"""一名拳击手仅仅学会了直拳、摆拳、勾拳是远远不够的,接下来还要勤学苦练各种战术组合拳,直至这些
战术组合动作成为肌肉记忆,才有可能战胜对手,从而成为拳击台上的强者学习Python也是这样,掌握基本语
法仅仅是入门和起步,还要继续学习诸如时间和日期处理文件读写、数据库操作、数据处理、线程、进程等
各种基本技能。这是一个破茧成蝶的过程必然伴随着迷茫和痛苦,只有经过不懈努力,才能走出困境。"""


""" 3.1时间和日期处理
    Python提供了time和datetime两个标准模块,用于处理时间和日期,二者在功能上有重叠,在应对需求上
各有侧重。一般而言, time模块侧重于解决当前的时间日期问题,如当前日期、当前时间戳等: datetime
模块则侧重于解决时间轴上的问题,如107天又7小时28分钟之前是几月几号几时等。
"""

"""3.1.1 time模块
    time模块内部定义了一个time.struct_time类，用于表示一个时间对象，它包含了年、月、时、分、
秒、周内日、月内日、年内日等多个属性，下面列出了time.struct_time类的常用属性。

    属性名：                 说明：
    
    tm_year:    年，demo：2021
    tm_mon:     月，取值：1~12
    tm_mday:    月内日，取值：1~31
    tm_hour:    小时，取值：0~23
    tm_min:     分钟，取值：0~59
    tm_sec:     秒，取值：0~61（应对闰秒和双闰秒）
    tm_wday:    周内日，星期一至星期日分别对应0~6
    tm_yday:    年内日，取值：1~366
    tm_isdst:   夏时令，取值0、1或-1
    
    time模块提供了多个处理日期、时间的函数，可以实现时间戳和struct_time对象互转、日期
时间字符串和struct_time对象互转等功能，下面列出time模块常用的函数：

    函数：                     说明：
    time.time():    返回从1970-01-01 00：00：00至当前时刻的秒数，精度为毫秒
    time.asctime([t]):  将struct_time对象转换为日期时间字符串
    time.ctime([secs]): 将时间戳转换为日期时间字符串（返回值受时区影响）
    time.gmtime([secs]):    将时间戳转换为零时区struct_time对象
    time.localtime([secs]): 将时间戳转换为本地时区struct_time对象
    time.mktime(t): 将struct_time对象或元组代表的时间转换为时间戳
    time.perf_counter():    返回性能计数器的值（以秒为单位）
    time.process_time():    返回当前进程使用CPU的时间（以秒为单位）
    time.sleep(sces):   暂停程序（进程或线程）secs秒
    time.strftime(format[,t]):  将struct_time对象或元组格式化为日期时间字符串
    time.strptime(string[,format]):  将字符串格式的时间转换为struct_time对象
    
    1.最典型应用：获取当前时间戳和休眠
    
    获取当前时间戳时time模块最常用的功能，例如，考察一段代码的运行时长，可以在这段
代码运行开始前和结束后各获取一次时间戳，二者之差即为该段代码的运行时长。"""

# demo:

# import time
# def do_something():
#     t0 = time.time() # 记录开始时间戳
#     for i in range(5):
#         print('我正在努力工作中...')
#         time.sleep(0.3)
#     t1 = time.time() # 记录结束时间戳
#     print('工作结束，耗时%0.3f秒。'%(t1-t0)) # 显示运行时长

"""这段代码用time.sleep()休眠函数来模拟程序做某些工作需要消耗的时间，如果实际工作
耗时很少，开始和结束的两个时间戳之差就有可能为零，这种情况下，可以使用精度更高的
time.perf_count()函数代替time.time()时间戳函数。
"""

"""2.时间戳和struct_time类互转
    时间戳是一个浮点数，表示从1970年1月1日0时0分0秒至当前时刻的时间（秒），精确到毫秒
时间戳可以做加减运算，但不能直观显示日期时间，很多情况下，我们需要在时间戳和struct_time类
之间实现相互转换，具体的代码如下：
"""

import time

time.localtime() # 获取本地时区的时间，返回struct_time类
# time.struct_time(tm_year=2021, tm_mon=5, tm_mday=7, tm_hour=20, tm_min=5, tm_sec=44,
#                  tm_wday=4, tm_yday=127, tm_isdst=0)
# print(time.localtime())

time.gmtime() # 获取格林尼治时间，返回struct_time类
# print(time.gmtime())
# time.struct_time(tm_year=2021, tm_mon=5, tm_mday=7, tm_hour=12, tm_min=7, tm_sec=16, tm_wday=4,
#                  tm_yday=127, tm_isdst=0)

time.localtime(0) # 0时间戳，对应东八区时1970年1月1日8时
# print(time.localtime(0))
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

time.gmtime(0) # 时间戳，对应格林尼治零时区是1970年1月1日0时
# print(time.gmtime(0))
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

time.localtime(1620389830.0) # 时间戳转struct_time类
# print(time.localtime(1620389830.0))
# time.struct_time(tm_year=2021, tm_mon=5, tm_mday=7, tm_hour=20, tm_min=17, tm_sec=10, tm_wday=4, tm_yday=127, tm_isdst=0)

time.mktime(time.localtime()) # struct_time转时间戳
# print(time.mktime(time.localtime()))
# 1620389830.0

"""3.时间戳和日期字符串互转
    time模块使用%Y表示4位数字的年份，使用%m和%d表示两位数字的月和日，使用%H、%M、%S
分别表示两位数字的时、分、秒，使用%X表示半角冒号连接的两位数字的时、分、秒。这些约定的符号
之间可以插入任意的连接符，这也是很多Python模块通用的日期时间字符串的格式化规则。"""

time.strftime('%Y-%m-%d %H:%M:%S') # 将当前日期格式化
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

time.mktime(time.strptime('2021-05-07 20:27:30', '%Y-%m-%d %X')) # 将当前日期转为时间戳
# print(time.mktime(time.strptime('2021-05-07 20:27:30', '%Y-%m-%d %X')))
# 1620390450.0

"""datetime模块
    相比time模块，datetime模块操作日期时间的方式更加灵活、便捷。datetime模块提供了datetime
和timedelta两个内置类，前者表示日期时间，后者表示一个时间段的长度。两个datetime对象相减，
即可得到一个timedelta对象，两个timedelta对象，或datetime对象和timedelta对象，可以做加减运算
"""

"""1.datetime类
    Datetime类是一个包含来自date对象和time对象所有信息的单一对象，datetime类提供的以下方法
可以直接调用，无需实例化：
    now()  :返回当前的本地datetime对象。
    utcnow() :返回当前UTC (协调世界时)日期时间。
    fromtimestamp(timestamp, tz=None) :  将时间戳转为datetime类型的时间,tz为时区参数。
    fromisoformat(date_string):  将日期时间字符串转为datetime类型的时间。
    strptime(date_string, format):   将日期时间字符串按照format指定的格式解析生成datetime
    类型的时间
    
    以下方法只有datetime类实例化以后才可以调用:
    date(): 返回具有同样year, month和day值的date对象。
    time(): 返回具有同样hour, minute, second, microsecond值的time对象。
    timetuple(): 返回一个time.struct time类型的日期时间对象toordinal():返回日期的
    格林尼治序号。
    timestamp(): 返回时间戳。
    weekday() :返回一个代表星期几的整数,星期一为0,星期日为6
    isoweekday(): 返回一个代表星期几的整数,星期一为1,星期日为7。
    ctime(): 返回一个代表日期和时间的字符串。
    strfimeformat(): 返回一个由显式格式字符串所指明的代表日期和时间的字符串。
    
下面的代码演示了datetime类的主要用法,包括如何用时间戳、字符串、日期时间等信息生成
datetime对象，如何从datetime对象获取信息等。
"""

from datetime import datetime

# print(datetime.now()) # 获取当前时间
# 2021-05-07 21:09:20.523024

# print(datetime(2021, 1,1,0,0,0)) # 实例化datetime对象
# 2021-01-01 00:00:00

# print(datetime.fromisoformat('2021-05-07 21:09:20')) # 字符串转datetime对象
# 没有找到这个方法

# print(datetime.strptime('20211010', '%Y%m%d')) # 字符串转datetime对象
# 2021-10-10 00:00:00

# print(datetime.fromtimestamp(1620393585.0)) # 时间戳转datetime对象
# 2021-05-07 21:19:45

# dt = datetime.utcnow() # 获取当前utc时间
# dt.timetuple() # 返回time.struct_time对象
# print(dt.timetuple())

# dt.timestamp() # 返回datetime对象的时间戳
# print(dt.timestamp())
# time.struct_time(tm_year=2021, tm_mon=5, tm_mday=7, tm_hour=13, tm_min=24, tm_sec=2, tm_wday=4, tm_yday=127, tm_isdst=-1)
# 1620365042.800903

# dt.isoweekday() # 返回一个代表星期几的整数，星期一为1，星期日为7
# print(dt.isoweekday())
#
# dt.strftime('%Y-%m-%d %X') # 返回日期时间字符串
# print(dt.strftime('%Y-%m-%d %X'))
# 5
# 2021-05-07 13:28:06

""" 2.timedelta类
    timedelta类用来描述一段时间,如两个日期或时间点之间的时间间隔,timedelat对象之间以及timedelta对象
和datetime对象之间可以做加减运算,创建datetime.timedelta对象可以使用下列参数中的一个或多个指定时间
段长度,若使用了多个参数,时间段长度为多个参数之和.
    weeks:周数
    days:天数(默认)
    hours:小时数
    minutes:分钟数
    seconds:秒数
    microseconds:微秒数
"""
# from datetime import datetime, timedelta
# timedelta(3) # 生成3天的timedelta对象
# # print(timedelta(3))
#
# datetime.timedelta(days=3)
# delta = timedelta(days=3, hours=5, minutes=25, seconds=10)
# delta # delta是一个3天零19510秒的timedelta对象
# print(delta)

# datetime.timedelta(days=3, seconds=19510)
# delta.days # delta包含的天数
# print(delta.days)
# 3

# delta.total_seconds() # 返回delta的总秒数
# print(delta.total_seconds())
# # 278710.0
#
# dt = datetime.now() # 获取当前日期时间
# dt - delta # 3天又5小时25分钟10秒之前的日期时间
# print(datetime.now())
# print(dt - delta)







