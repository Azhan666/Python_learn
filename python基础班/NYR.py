#年月日表示;

#
year = int(input('请输入年份:'))

month = int(input('请输入月份:'))

day = int(input('请输入天份:'))

sum = 0

months = [0,31,59,90,120,151,181,212,243,273,304]       # months累加记录1-11月

if 0 < month <= 12:         # 假设为非闰年时，当前日期的天数

    sum = months[month - 1] + day
leap = 0    # 或者将leap换成flag
if (year % 4 == 0) and ((year % 100 == 0) or (year % 400 != 0)):  #判断是否为闰年，如果为闰年，则 leap = 1
    leap = 1
if (leap == 1) and (month > 2):   #年份为闰年且月份大于2
    sum += 1
print("%d.%d.%d 是 %d 年的第 %d 天" % (year,month,day,year,sum))




#今年还剩多少天
# year = int(input("请输入年份"))
# month = int(input("请输入月份"))
# day = int(input("请输入日期"))
#
# days = 365 #定义今年的总天数
# months = [0,31,59,90,120,151,1881,212,243,273,304]
#
# if 0 <month <12:
#     sum = months[month - 1] + day
#
# falg = 0
# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#    flag = 1
#    days += 1
#
# if flag == 1 and month > 2:
#     sum += 1
#
# surplus_day = days - sum
#
# print("今天是: %d年.%d月.%d日, 今年还剩 %d 天" % (year,month,day,surplus_day))
#


