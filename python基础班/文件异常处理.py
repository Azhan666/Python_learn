# 文件操作：异常处理
# 用 try 来捕获异常
# 由于错误不同，所以需要捕获错误类型

# try:
#     num = int(input('请输入一个数字：'))
#     a = 8 / num
# except ValueError:
#     print('值错误')
#
# #无论出现什么错误，都会捕获:
# except ValueError as result:
#     print('未知错误%s' % result)
#
# #print(8/2)
# else:
#     print('在没有异常的时候才会执行')
#
# finally:
#     print('不管有没有异常都会执行')


#异常具有传递性，当函数在执行遇到异常时会传递给函数的调用者，如果传递到主程序还没有处理异常，程序终止

#如何解决：可以在主函数中增加异常捕捉

def func_1():
    return int(input('请输入数字：'))

def func_3():
    pwd = input('请输入')
    print('aaa')
    #开发人员可以自己定义错误，并且主动抛出错误:
    if len(pwd) <= 8:
        return pwd
    ex = Exception('我是在打印的时候字符类型没有加双引号')
    raise ex   #主动抛出异常


def func_2():

    func_1()   #此时func_2是主函数，因为func_1、func_3都依赖于func_2的调用，所以可在func_2中增加异常捕捉：
    func_3()

try:
    a = func_3()
    print(a)
except ValueError:
    print('名字错误')
except ValueError:

    print('值错误')

except ValueError as result:

    print(result)




