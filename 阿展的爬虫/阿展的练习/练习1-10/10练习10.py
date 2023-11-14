# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 课题：线程与爬虫

# 1.线程讲解
# 什么是线程？
# 程序运行的最小单位

# 我们来一个的线程简单实现：

# from threading import Thread # 多线程模块
# import time # 时间模块
#
# def index(x, y): # 创建一个index函数，接收两个参数：x、y
#     print(f'我是{x}, 你是{y}') # 直接格式化输出
#
# def run(): # 我们再来创建一个run函数，run函数里面没有任何参数
# 我们直接线程创建：
# # Thread(target=index, args=('暴', '揍')).start()
# # Thread(target=index, args=('美', '国佬')).start()
# # args参数传递：元祖或者字典
#     # url列表
#     list_1 = ['暴', '揍', '美', '国佬', 1, 2, 3, 4]
# # 因为list_1中共有八个数据，而index函数中只有两个参数，所以要将list_1拆分为4份：

#     num = len(list_1)//2  # 拆成四份，一个/拆两份，
#     list_2 = list_1[:num] # 第三份
#     list_3 = list_1[num:] # 第四份
#     print(list_1)
#     print(list_3)
# # 参数1：暴、参数2：揍
#     Thread(target=index, args=('暴', '揍')).start()
#     Thread(target=index, args=('美', '国佬')).start()
#
# run()

# 2.线程间共享全局变量

# 3.GIL锁的应用

from threading import Thread
import threading
import time

#
# 主要问题：数据的保存
# # 十个线程保存十张壁纸
# # 保存的图片与名称不对应（线程间的资源竞争）
#
# # 保存到excel表格数据
# # 表格间的数据顺序会错乱
#
# # 进程非常的类似了，线程队列，线程池

# GIL锁：

# x = ['a', 'b', 'c']
#
#
# def func(num):
#     # mutex.acquire()  # 上锁
#     time.sleep(2)
#     for i in range(num):
#         x.append(i)
#     print('我是func', x)
#     # mutex.release()  # 解锁
#
# def function(num):
#     # mutex.acquire()  # 上锁
#     time.sleep(2)
#     for i in range(num):
#         x.append(i)
#     print('我是function', x)
#     # mutex.release()  # 解锁
#

# if __name__ == '__main__':
#     mutex = threading.Lock()
#     Thread(target=func, args=(3,)).start()
#     Thread(target=function, args=(5,)).start()

# 结合gil锁运用线程

# 4.多线程实现

# 5.线程池
# 有资源竞争的问题

from concurrent.futures import ThreadPoolExecutor
import threading
import time

# # 定义一个准备作为线程任务的函数
# def index(num, name):
#     my_sum = 0
#     for i in range(num):
#         # 了解
#         threading.current_thread().name = 'aef'
#         print(threading.current_thread().name + '  ' + str(i) + name)
#         # threading.current_thread() 进行中的进程 代码表示获取进行中的进程名称
#         # print(threading.current_thread().getName() + '  ' + str(i))
#         my_sum += i
#     return my_sum
#
#
# # 创建一个包含3条线程的线程池
# pool = ThreadPoolExecutor(max_workers=3)
#
# # 向线程池提交一个task(任务), 1000会作为action()函数的参数
# f1 = pool.submit(index, 10, 'name')
#
# # 向线程池再提交一个task(任务), 100会作为action()函数的参数
# # f2 = pool.submit(index, 6)
#
# # # 判断f1代表的任务是否结束
# # 有没有僵尸线程 -- 根据f1.done()的返回值，来终止我们的线程
# # print(f1.done())
# # time.sleep(3)
# #
# # # 判断f2代表的任务是否结束
# # print(f2.done())
# #
# # # 查看future1代表的任务返回的结果
# # print('运行结果', action(50), '\t\n')
# # print('运行结果', f1.result(), '\t\n')
# # print('运行结果', f2.result(), '\t\n')
# #
# # # 查看future2代表的任务返回的结果
# # print(f2.result())
#
# # 关闭线程池
# pool.shutdown()







"""6.线程队列"""
# from threading import Thread
#
# from queue import Queue
# import time
#
#
# class Love(object):
#     def __init__(self):
#         self.q = Queue()
#
#     def parse_data(self):
#         for i in range(101):
#             data = f'第{i}天，我爱你，三郎还有，阿姨洗得路'
#             # 往队列中添加任务
#             time.sleep(1)
#             self.q.put(data)
#         self.q.join()
#
#     def parse_queue(self):
#         while True:
#         # for i in range(101):
#             # 往队列中拿取任务
#             data = self.q.get()
#             print(data)
#             self.q.task_done()
#
#     def run(self):
#         t1 = Thread(target=self.parse_data)
#         t2 = Thread(target=self.parse_queue)
#         t1.start()
#         # 设置守护线程
#         t2.daemon = True
#         t2.start()
#
#
# if __name__ == '__main__':
#     d = Love()
#     d.run()

"""注意点(面试)"""

# 案例实战：


