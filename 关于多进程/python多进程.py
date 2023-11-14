# # !/usr/bin/env python
# # -*- coding: utf-8 -*-

# multiprocessing
# 在multiprocessing模块中有一个Process类，Python用它来创建进程。
#
# 1.Process类的参数：
# Process(self,group=None,target=None,name=None,args=(),kwargs={})
# 1
# group ：group参数并不使用；
# target：表示调用对象，即该进程要执行的任务，或者说是传入一个方法；
# name ： 进程的别名；
# args ： srgs是一个元组，它里面是调用target方法需要传入的参数；
# kwargs：kwargs是一个字典，它里面是调用target方法需要传入的关键字参数；
# 2.Process类的方法：
# start() ： 启动进程，并调用方法run()；
# run() ： 进程启动后运行target调用函数的方法；
# join(timeout) ：让主线程等待子进程结束后再继续进行，通常用于进程间的同步。timeout是可选的超时时间，即超过该时间主线程将不再继续等待。
# terminate() ：强制终止进程，但不会进行任何清理操作；
# is_alive() ：判断进程是否"存活"，存活返回True，否则返回False；
# 3.实例化Process类创建一个进程
# 示例1：
#
# from multiprocessing import Process
# import os
# def text(id):
#     print('Child Process %s is running.' % id)
# if __name__ == '__main__':
#     print('Main process %s is running.' % (os.getpid()))
#     p = Process(target=text,args=('727',))
#     p.start()
#     p.join()
#     print('Main Process end.')
# ##
# Main process 13324 is running.
# Child Process 727 is running.
# Main Process end.

# <分析>
#
# 在上面的程序中一共启动了两个进程，一个主进程和一个子进程，主进程就是主程序，也就是第五行代码之后的程序，然后在主进程中用Process类实例化了一个子进程，子进程调用到了一开始创建的text函数，之后用start()方法启动子进程，用join()方法使主进程等待子进程，直到子进程结束主进程继续向下执行。
# os模块下的getpid()方法用于获得进程识别码。 另外，用Process类创建并启动进程时必须先判断 if __ name __ ==
# ‘__ main__’ ，否则可能发生异常。
#
# 示例2：
#
# from multiprocessing import Process
# from time import ctime,sleep
# import os
# def text(pause):
#     for i in range(3):
#         print('Child Process %s is running,at %s.' % (os.getpid(),ctime()))
#         sleep(pause)
# if __name__ == '__main__':
#     print('Main Process %s is running,at %s.' % (os.getpid(),ctime()))
#     p = Process(target=text,args=(2,))
#     p.start()
#     if not p.is_alive():
#         print('Main Process %s end,at %s.' % (os.getpid(),ctime()))
# ##
# Main Process 5540 is running,at Sat Aug 17 13:22:51 2019.
# Child Process 1236 is running,at Sat Aug 17 13:22:52 2019.
# Child Process 1236 is running,at Sat Aug 17 13:22:54 2019.
# Child Process 1236 is running,at Sat Aug 17 13:22:56 2019.

# <分析>
#
# 我们用time模块下的sleep()函数让子进程休眠，用ctime()函数获取当前当地时间的字符串，可以看到，子进程不会结束，主进程也不会结束，主进程会默认等待子进程结束后其本身才会结束，这在一定程度上避免了僵尸进程的产生。
# 什么是僵尸进程呢，当子进程结束运行后会产生一个僵尸进程，它的作用是使进程退出，僵尸进程保存着进程的退出状态等信息，除此之外，僵尸进程不再占有任何内存空间。它需要父进程来回收这些信息，虽然父进程会默认等待子进程结束并回收资源后本身才会结束，但是如果父进程出现了其它异常情况，这就有可能造成僵尸进程继续残留，大量的僵尸进程积累会使内存空间被挤占。
# 这时有必要使用join()函数，join()函数会使主进程等待子进程，并且join()函数内部也有一个清除僵尸进程的函数可以用来回收资源；另外，如果有多条子进程被创建，那么start()函数也能够回收之前的僵尸进程。
#
# 示例3：
#
# from multiprocessing import Process
# a = 777
# def text():
#     global a
#     a = 666
#     print('Child Process,a = %d.' % (a))
# if __name__ == '__main__':
#     p = Process(target=text)
#     p.start()
#     p.join()
#     print('Main Process,a = %d.' % (a))
# ##
# Child Process,a = 666.
# Main Process,a = 777.
#
# <分析>
#
# 在text()函数中，我们设置了一个全局变量a，但是可以看到即便如此父进程和子进程的a仍然是不同的，这说明进程之间的内存空间是隔离的，进程与进程之间相互独立。
#
# 4.继承Process类创建子进程
# 除了直接实例化Process类创建进程外，我们也可以定义继承Process类的子类，重写其run()方法，通过实例化Process子类创建进程。
#
# 示例：
#
# from multiprocessing import Process
# import os
# class ChildProcess(Process):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         print('Child Process %s is running.' % (os.getpid()))
# if __name__ == '__main__':
#     print('Main Process %s is running.' % (os.getpid()))
#     p = ChildProcess()
#     p.start()
#     p.join()
#     print('Child Process end.')
#     print('Main Process end.')
# ##
# Main Process 14956 is running.
# Child Process 1724 is running.
# Child Process end.
# Main Process end.
#
# 5.进程池
# 进程池函数Pool()可以用来批量创建子进程，也可以用来管理进程。
# 进程池实际上是multiprocessing模块下的Pool类。
#
# 进程池常用方法：
#
# 1.apply(func,args=(),kwargs={})：将func函数提交给进程池处理。
#
# 2.apply_async(func,args=(),kwargs={},callback=None,error_callback=None)：apply()方法的异步版本，该方法不会被阻塞。其中callback指定func函数完成后的回调函数，error_callback指定func函数出错后的回调函数。这两个参数可以省略。
#
# 3.map(func,iterable) ：类似于Python内置的map函数。
#
# 4.map_async(func,iterable,callback=None,error_callback=None)：map()的异步版本，该方法不会被阻塞。
#
# 5.close() ：关闭进程池。不允许进程池继续接受新的任务，执行close()方法后，进程池会在当前进程池中所有任务执行完后关闭自己。
#
# 6.terminate() ：立即终止进程池。
#
# 7.join() ：等待进程池中所有任务完成。此方法只能在close()或terminate()之后调用。
#
# 说明：
#
# 1.回调函数：只有异步函数才会有回调函数，即每当进程池的的某个进程的任务处理完成了，它就将处理结果交给回调函数，由回调函数作进一步处理后告知主进程，再由主进程调用其它函数处理回调函数返回的结果。
# 如果是在主进程等到进程池中的所有任务都执行完毕了再统一处理结果，则不需要回调函数。
#
# 2.当创建一个进程池时，可以设定它的最大进程容纳数。之后每当有新的请求提交到Pool中时，如果池还没满，那就创建一个进程来执行该请求，如果进程池已满，那么该请求将会等待，直到池中有进程结束。如果没有设置Pool的大小，那么默认是CPU的核数。
#
# 示例1：
#
# from multiprocessing import Pool
# from time import sleep
# import os
# def text(id):
#     print('Process %s is running as id(%d).' % (os.getpid(),id))
#     sleep(5)
# if __name__ == '__main__':
#     pool = Pool(4)
#     pool.apply_async(text,args=(111,))
#     pool.apply_async(text,args=(222,))
#     pool.apply_async(text,args=(333,))
#     pool.close()
#     pool.join()
# ##
# Process 13340 is running as id(111).
# Process 852 is running as id(222).
# Process 5192 is running as id(333).
#
# <分析>
#
# 第8行代码创建了一个进程池，该进程池最多能容纳四个进程。同时我们用apply_async方法在进程池中创建了三个进程，这里需要特别注意的一点就是进程池中的这三个进程是立刻执行的，是异步，不是同步，而如果采用的是apply方法的话，那么进程池将会顺序执行，即执行完第一个进程后，再去执行第二个，以此类推。
#
# 示例2：
#
# from multiprocessing import Pool
# from time import sleep
# import os
# def text(id):
#     print('Process %s is running as id(%d).' % (os.getpid(),id))
#     sleep(5)
# if __name__ = '__main__':
#     with Pool(4) as pool:
#         pool.map(text,(111,222,333))
#  ##
#  Process 12612 is running as id(111).
#  Process 8436 is running as id(222).
#  Process 816 is running as id(333).
#
# <分析>
#
# 示例2展示了用Pool对象的map()方法创建一个包含多个进程的进程池，map()方法自带close()和join()方法，因此不需要额外再使用。
#
# 示例3：
#
# from multiprocessing import Pool
# from time import sleep
# import os
# def text(con):
#     sleep(2)
#     con = con**2
#     return con
# if __name__ == '__main__':
#     pool = Pool(2)
#     for i in range(1,5):
#         result = pool.apply_async(text,args=(i,))
#         print(result.get())
#     pool.close()
#     pool.join()
# ##

# <分析>
#
# 在示例3中text()函数多了个返回值，并且执行结果是一个接着一个的输出，中间有停顿，但是apply_async()方法不是立即输出所有进程么？这里其实它和示例1的不同就在于示例3是循环传入进程，而且有返回值。返回值的存在导致apply_async()方法必须执行一个返回一个后才能去执行下一个。如果去掉返回值，那么进程池将会立即几乎同时执行前两个进程，之后再同时执行后两个进程，因为Pool的容量为2。
# 另外应该注意到，对于apply_async()方法具有返回值的情况，要想输出返回值需要借用get()方法。
#
# 示例4：
#
# from multiprocessing import Pool
# from time import sleep
# import os
# def text(con):
#     sleep(2)
#     con = con**2
#     return con
# if __name__ == '__main__':
#     pool = Pool(2)
#     results = pool.map(text,(1,2,3,4))
#     print(results)
#     pool.close()
#     pool.join()
# ##
# [1, 4, 9, 16]

# <分析>
#
# map()有返回值时与apply_async不一样，map()会等到所有进程都执行完毕后，再把结果以列表的形式返回。如本例，在启动进程池后，程序休眠了四秒，之后直接返回一个包含所有进程结果的序列。
# ————————————————
