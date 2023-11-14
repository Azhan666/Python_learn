#阶乘方法1: 使用递归：(未掌握）
# def myfact(n):
#     assert n >= 0,"Factorial not definied for negative values"
#     if n < 2:
#         return 1
#     else:
#         return n * myfact(n-1)
#
#     In [76]: myfact(6)
#     Out[76]:720





def func(n):# func:function(功能、目的），《数》函数关系
    if n == 0 or n == 1:
        return 1
    else:
        return(n * func(n -1 ))


a = func(4)

print(a)
