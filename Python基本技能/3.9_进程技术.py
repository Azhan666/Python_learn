# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""3.9 进程技术"""

"""    进程是一个“执行中的程序”。程序是指令、数据及其组织形式的描述，是一个没有生命的实体，
只有处理器“赋予程序生命”时（操作系统执行程序时），它才能成为一个活动的实体，我们将执行中的
程序称为进程。

    3.9.1 再论线程和进程
    上一节以经营物业管理公司为例,形象地介绍了线程和进程的概念。使用线程技术可以在一个进程中
创建多个线程,让它们在“同一时刻”分别去做不同的工作,这些线程共享同一块内存,线程之间可以共享对
象和资源,如果有冲突或需要协同,还可以随时沟通以解决冲突或保持同步。
    不过,多线程技术不是“万金油”,它有一个致命的缺点:在一个进程内,不管创建了多少线程,它们总是
被限定在一颗CPU内,或多核CPU的一个核内。这意味着多线程在宏观上是并行的,在微观上则是分时切换
串行的,多线程编程无法充分发挥多核计算资源的优势。这也是使用多线程做任务并行处理时,线程数量超
过一定数值后,线程越多速度反倒越慢的原因。
    多进程技术正好弥补了多线程技术的不足,我们可以在每一颗CPU上,或多核CPU的每一个核上启动一个
进程。如果有必要,还可以在每个进程内再创建适量的线程,最大限度地使用计算资源来解决问题。因为进
程不在同一块内存区域内,所以和线程相比,进程间的资源共享、通信、同步等都要麻烦得多,受到的限制
也更多。

    3.9.2 创建、启动和管理进程
    multiprocessing是Python内置的标准进程模块,可运行在UNIX和Windows平台上。基于该模块,程
序员得以充分利用机器上的多核资源。为便于使用, multiprocessing模块提供了和threading线程模块
相似的API.针对进程特点, multiprocessing模块还引入了在threading模块中没有的APl,如进程池
(Pool)、共享内存(Array和Value)等。
    Process类是multiprocessing模块的子进程类,用于创建、启动和管理子进程。Process类和线程
模块treading.Thread 的API几乎完全相同. Process类用来描述一个进程对象。创建子进程的时候,只
需要传入进程函数和函数的参数即可完成Process类的实例化。表3-10列出了Process类常用方法和属性。

    类成员（方法和无属性）         说明
    name                进程名，默认时Process-n
    pid                 进程id
    exitcode            运行时该值为None，进程结束后表示该进程的信号值
    daemon              默认为False，True表示后台守护进程，父进程终止，该进程也终止
    start()             启动进程，会自动调用进程对象的run()方法
    join()              若无参数，主进程等待至子进程结束，否则等待至参数指定的时间
    is_alive            判断进程是否还在运行
    terminate           强制终止一个进程，不会做任何清理工作
    run                 启动进程时自动运行的方法，调用target指向的对象
    
    在下面这段代码中，主进程启动了两个子进程，然后等待用户的键盘输入以结束程序。主进程结束后，
子进程也随之结束。
"""

# import os, time
# import multiprocessing as mp
#
# def sub_process(name, delay): # delay:延时
#     """进程函数"""
#     while True:
#         time.sleep(delay)
#         print('我是子进程%s,进程id为%s'%(name, os.getpid()))
#
# if __name__ == '__main__':
#     print('主进程(%s)开始，按任意键结束本程序'%os.getpid())
#
#     p_a = mp.Process(target=sub_process, args=('A', 1))
#     p_a.daemon
#     n = True # 设置子进程为守护进程
#     p_a.start()
#
#     p_b = mp.Process(target=sub_process, args=('B', 2))
#     p_b.daemon = True # 如果不是守护进程，主进程结束后子进程可能成为僵尸进程
#     p_b.start()
#
#     input() # 利用input()函数阻塞主进程，这是常用的调试手段

"""    
    如果将上面代码中两个子进程的daemon设置为False,则主进程结束后,两个子进程不会随之结束,从而成为
僵尸进程。图3-6所示为在任务管理器中查看当前进程,可以看到主进程以及两个子进程使用的3个Python解释器
(如果你还有其他的Python程序,如IDLE等在运行,会看到有更多的Python解释器在运行),我们既可以在任务管理
器中手动关闭僵尸进程,也可以在主进程结束前使用is_live()判断进程是否还在运行，使用terminate()强制关
闭运行中的进程。

    3.3.9 进程间通信
    
    和线程类似,多个进程同时工作的情况下也存在任务协同和资源竞争,同样需要进程之间的同步。另外,由于
各个进程分属于不同的内存区块,进程间交换数据比线程间交换数据要困难得多。这里把进程间同步和交换数据统
称为进程间通信。线程间使用的队列、互斥锁、信号量、事件和条件等5种同步方式,同样可以应用在进程间。此外
, multiprocessing模块还提供了管道和共享内存等进程间通信的手段。
    
    1.队列
    和线程类似,队列也是进程间交换数据最常用的方式之一. multiprocessing模块提供了一个和queue模块几
乎一样的Queue类。Queue类的put()方法和get()方法也默认为阻塞式,可以使用参数block指定为阻塞或非阻塞。
    我们还是沿用线程队列那个生产者一消费者模式的例子,一个负责往地上“扔钱”(写队列),另一个负责从地上
“捡钱” (读队列)。只需做一点点改动,就可以用进程实现。"""

# import os, time, random
# import multiprocessing as mp
#
# def sub_process_A(q):
#     """A进程函数：生成数据"""
#
#     while True:
#         time.sleep(5*random.random()) # 0~5秒随机延时
#         q.put(random.randint(10,100)) # 随机生成[10,100]的整数
#
# def sub_process_B(q):
#     """B进程函数：使用数据"""
#
#     while True:
#         words = ['哈哈','天哪！', 'My God!', '咦，天上掉馅饼了？']
#         while True:
#             print('%s捡到了%d块钱！'%(words[random.randint(0,3)], q.get()))
#
# if __name__ == '__main__':
#     print('主进程(%s)开始，按回车键结束本程序'%os.getpid())
#
#     q = mp.Queue(10)
#
#     p_a = mp.Process(target=sub_process_A, args=(q,))
#     p_a.daemon = True
#     p_a.start()
#
#     p_b = mp.Process(target=sub_process_B, args=(q,))
#     p_b.daemon = True
#     p_b.start()
#
#     input()

"""2. 管道
    
    管道是除队列外的另一种进程间通信的主要方式, multiprocessing模块提供了一个Pipe类用于管道通信,
默认是双工的,管道的两端都可以使用send()和recv()发送和接收消息。需要说明的是, recv()是阻塞式的,
并且没有队列那样的block参数可以设置是否阻塞。
    下面的代码演示了两个进程猜数字的游戏:进程A在心中默想了一个在(10, 127)的整数,让进程B来猜。
如果进程B猜对了,游戏结束;如果进程B猜的数字大于或小于目标数,则进程A会告诉进程B猜大了或者猜小了,
然后让进程B继续猜。"""
# send：发送，recv：接收，pipe：管道

# 关于random模块：https://www.runoob.com/python/func-number-random.html

# import time, random, multiprocessing as mp
#
# def sub_process_A(pipe):
#     """A进程函数"""
#
#     aim = random.randint(0, 128)
#     pipe.send('我想好了一个在[0,128)的数字，你猜是几？')
#     print('A:我想好了一个在[0,128)的数字，你猜是几？')
#     while True:
#         guess = pipe.recv()
#         time.sleep(0.5 + 0.5*random.random()) # 假装思考一会儿
#         if guess == aim:
#             pipe.send('恭喜你！猜中了！')
#             print('A:恭喜你！猜中了！')
#             break
#         elif guess < aim:
#             pipe.send('猜小了')
#             print('不对，猜小了')
#         else:
#             pipe.send('猜大了')
#             print('A:不对，猜大了')
#
# def sub_process_B(pipe):
#     """B进程函数"""
#
#     result = pipe.recv()
#     n_min, n_max = 0, 127
#     while True:
#         time.sleep(0.5 + 0.5*random.random()) # 假装思考一会儿
#         guess = n_min + (n_max-n_min)//2
#         pipe.send(guess)
#         print('B:我猜是%d'%guess)
#
#         result = pipe.recv()
#         if result == '恭喜你！猜中了！':
#             print('B:哈哈，被我猜中了！')
#             break
#         elif result == '猜小了':
#             n_min, n_max = guess + 1, n_max
#         else:
#             n_min, n_max = n_min, guess
#
# if __name__ == '__main__':
#     pipe_enda,pipe_endb = mp.Pipe() # 创建管道，返回管道的两个端，均可收发消息,pipe：管道
#
#     p_a = mp.Process(target=sub_process_A, args=(pipe_enda,))
#     p_a.daemon = True
#     p_a.start()
#
#     p_b = mp.Process(target=sub_process_B, args=(pipe_endb,))
#     p_b.daemon = True
#     p_b.start()
#
#     p_a.join() # 主进程等待p_a进程结束
#     p_b.join() # 主进程等待p_b进程结束

"""3. 共享内存
    通过共享内存实现状态非常简单，但在多进程中编程中，这不是首选的方法，应当尽量避免使用。
multiprocessing模块提供了Value和Array两个共享内存对象,一个用于单值共享,一个用于数组共享,实例化
Value和Array时,'d'表示双精度浮点数,'i'表示有符号整数,这些共享对象是进程和线程安全的。
    下面的代码演示了两个进程如何共享单值内存和数组内存,若共享单值为0,则进程A对共享数组的元素加2,
同时置共享单值为1；若共享单值为1,则进程B对共享数组的元素减1同时置共享单值为0,这个例子里面隐式地
涉及了ctypes模块,这是一个用于在Python和C或C++之间架设沟通桥梁的模块。"""
# ctypes:指针， Array：数组，矩阵

# import os, time, multiprocessing as mp
#
# def sub_process_A(flag, data):
#     """A进程函数"""
#
#     while True:
#         if flag.value == 0: # 若标志为0
#             time.sleep(1)
#             for i in range(len(data)): # 共享数组各元素加2
#                 data[i] += 2
#             flag.value = 1 # 置共享单值为1
#             print([item for item in data])
#
# def sub_process_B(flag, data):
#     """B进程函数"""
#
#     while True:
#         if flag.value == 1: # 若标志为0
#             time.sleep(1)
#             for i in range(len(data)):
#                 data[i] -= 1 # 共享数组各元素减1
#             flag.value = 0 # 置共享单值为0
#             print([item for item in data])
#
# if __name__ == '__main__':
#     print('主进程(%s)开始，按回车键结束本程序'%os.getpid())
#
#     flag = mp.Value('i', 0) # flag类型是ctypes.c_long, 不是普通的int
#     data = mp.Array('d', range(5))
#
#     p_a = mp.Process(target=sub_process_A,args=(flag, data))
#     p_a.daemon = True
#     p_a.start()
#
#     p_b = mp.Process(target=sub_process_B, args=(flag, data))
#     p_b.daemon = True
#     p_b.start()
#
#     input()

"""4. 互斥锁
    还记得3.8.3 小节中用线程锁模拟在微信群里统计喜欢使用PyCharm人数的例子吗?只需要将threading
模块替换为multiprocessing模块,将Thread类替换为Process ,就可以用进程的互斥锁实现这个例子,其代码
如下。"""

# import time, multiprocessing
#
# lock = multiprocessing.Lock() # 创建互斥锁
# counter = 0 # 计数器
#
# def hello():
#     """线程函数"""
#
#     global counter # global:全局的，全球的，（声明全局变量）
#     # 关键字global讲解：https://www.cnblogs.com/dflblog/p/11428631.html
#
#     if lock.acquire(): # 请求互斥锁，如果被占用，则阻塞直至获取到锁，acquire：取得
#         time.sleep(0.2) # 假装思考、按键盘，需要0.2秒
#         counter += 1
#         print('我是第%d个'%counter)
#
#     lock.release() # 千万不要忘记释放互斥锁，否则后果会非常严重,release：释放
#
# def demo():
#     Process = list()
#     for i in range(30): # 假设群里有30人都喜欢试用PyCharm
#         Process.append(multiprocessing.Process(target=hello))
#         Process[-1].start() # 下标为-1表示输出数组的最后一行数据值，
#         # 用法：当有时候弄不清数组的最后一组数据的时候，可以用这个方法。
# # 为什么取下标-1：https://blog.csdn.net/MoneyFxxker/article/details/88553379
#
#     for t in Process:
#         t.join()
#
#     print('统计完毕，共有%d人'%counter)
#
# if __name__ == '__main__':
#     demo()

"""5. 信号量
    使用同样的方式，很容易用进程的信号量模拟实现30名工人竞争使用5把电锤的例子，其代码如下："""

# import time,multiprocessing
#
# S = multiprocessing.Semaphore(5) # 有5把电锤可供使用
#
# def us_hammer(id): # hammer:锤
#     """线程函数"""
#
#     S.acquire() # P操作，阻塞式请求电锤
#     time.sleep(0.2)
#     print('%d号刚刚用完电锤'%id)
#     S.release() # V操作，释放资源（信号量+1）
#
# def demo():
#     Process = list()
#     for i in range(30): # 有30名工人要求使用电锤
#         Process.append(multiprocessing.Process(target=us_hammer, args=(i,)))
#         Process[-1].start() # 依旧取下标，输入出最后一行数据
#
#     for t in Process:
#         t.join()
#
#     print('所有线程工作结束')
#
# if __name__ == '__main__':
#     demo()

"""6.事件
    
    在上一节讲解线程同步技术时,用线程的事件对象模拟了一间办公室早上上班的场景。这个场景中,每个人
代表一个线程,工作时间到,表示事件(Event)发生。事件发生前,线程会调用wait()方法阻塞自己(对应看新闻、
聊天);一旦事件发生,会唤醒所有因调用wait()而进入阻塞状态的线程。使用进程和进程的事件(Event),同样
可以模拟这一场景。"""

# import time, multiprocessing as mp
#
# E = mp.Event() # 创建事件
#
# def work(id, E):
#     """进程函数"""
#     print('<%d号员工>上班打卡' %id)
#     if E.is_set():  # 已经到点了
#         print('<%d号员工>迟到了' %id)
#     else:  # 还不到点
#         print('<%d号员工>看新闻中...' %id)
#         E.wait()  # 等上班铃声
#
#     print('<%d号员工>开始工作了...' %id)
#     time.sleep(10)  # 工作10秒后下班
#     print('<%d号员工>下班了' %id)
#
# def demo():
#     E.clear()  # 设置为“未到上班时间”
#     threads = list()
#
#     for i in range(3):  # 3人提前来到公司打卡
#         threads.append(mp.Process(target=work, args=(i, E)))
#         threads[-1].start()
#
#     time.sleep(5)  # 5秒后上班时间到
#     E.set()
#
#     time.sleep(5)  # 5秒后，“大佬”（9号）到
#     threads.append(mp.Process(target=work, args=(9, E)))
#     threads[-1].start()
#
#     for t in threads:
#         t.join()
#
#     print('都下班了，关灯关门走人')
#
# if __name__ == '__main__':
#     demo()


"""7. 条件
    最后，我们改用进程的条件（Condition）对象来模拟实现上一节hezhan和liting两位小朋友玩的迷藏
游戏。"""

# import time, multiprocessing as mp, random
#
# cond = mp.Condition() # 创建条件对象
# draw = mp.Array('i',[0,0]) # Array:数组，[Hezhan小朋友人输，Liting小朋友认输]
#
# def hezhan(cond, draw):
#     """hezhan小朋友的进程函数"""
#
#     global draw_Hezhan, draw_Liting
#
#     time.sleep(1)  # 确保Liting小朋友已经进入消息等待状态
#     cond.acquire()  # 阻塞时请求资源
#     time.sleep(random.random())  # 假装蒙眼需要花费时间
#     print('Hezhan:我已经蒙上眼睛了')
#     cond.notify()  # 把消息通知到Liting小朋友
#     # notify(n=1):通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正
#     # 等待该condition的线程,最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调
#     # 用，否则会触发RuntimeError。notify()不会主动释放Lock。
#     cond.wait()  # 释放资源并等待Liting小朋友已经藏好的消息。
#
#     print('Hezhan:我来了')  # 收到Liting小朋友已经藏好的消息后
#     cond.notify()  # 把消息通知到Liting小朋友
#     cond.release()  # 不要再侦听消息了，彻底释放资源
#     time.sleep(random.randint(3, 10))  # Hezhan小朋友的耐心只有3~10秒
#
#     if draw[1]:
#         print('Hezhan:哈哈，我找到你了，我赢了')
#     else:
#         draw[0] = True
#         print('Hezhan:算了，你自己出来吧，我认输啦')
#
#
# def liting(cond, draw):
#     """Liting小朋友的线程参数"""
#
#     global draw_Hezhan, draw_Liting
#
#     cond.acquire()  # 阻塞时请求资源
#     cond.wait()  # 如果先于Hezhan小朋友请求到资源，则立刻释放并等待
#     time.sleep(random.random())  # 假装找地方躲藏需要花费时间
#     print('Liting：我藏好了，你来找我吧')
#     cond.notify()  # 把消息通知到Hezhan小朋友
#     cond.wait()  # 释放资源并等待Hezhan小朋友开始找人的消息
#
#     cond.release()  # 不在侦听消息了，彻底释放资源
#     time.sleep(random.randint(3, 10))  # Liting小朋友的耐心只有3~10秒
#
#     if draw[0]:
#         print('Liting:哈哈，那我出来了，我赢了')
#     else:
#         draw[1] = True
#         print('Liting:算了，这里太闷了，我还是出来吧')
#
#
# def demo():
#     p_hezhan = mp.Process(target=hezhan, args=(cond, draw))
#     p_liting = mp.Process(target=liting, args=(cond, draw))
#     p_hezhan.start()
#     p_liting.start()
#
#     p_hezhan.join()
#     p_liting.join()
#
#
# if __name__ == '__main__':
#     demo()


"""3.9.4 进程池
    使用多进程并行处理任务时，处理效率和进程数量并不是总成正比，当进程数量当过一定限度后,完成任务
所需时间反而会延长,进程池提供了一个保持合理进程数量的方案,但合理进程数量需要根据硬件状况及运行状
况来确定,通常设置为CPU的核数。
    multiprocessing.Pool() 可创建n个进程的进程池供用户调用,如果进程池任务不满,则新的进程请求会
被立即执行；如果进程池任务已满,则新的请求将等待至有可用进程时才被执行。
    向进程池提交任务有以下两种方式：
1：apply_async(func[,args[,kwds[,callback]]]):非阻塞式提交。即使进程池已满,也会接受新的任务,不会
阻塞主进程。新任务将处于等待状态。
2：apply(func[,args[,kwds]])非阻塞式提交。若进程池已满,则主进程阻塞,直至有空闲进程可以使用。

    下面的代码演示了进程池的典型用法。读者可自行尝试阻塞式提交和非阻塞式提交两种方法的差异。"""

# import time, multiprocessing as mp
#
# def power(x, a=2):
#     """进程函数：幂函数"""
#
#     time.sleep(1)
#     print('%d的%d次方等于%d'%(x, a, pow(x, a)))
#
# def demo():
#     mpp = mp.Pool(processes=4)
#
#     for item in [2,3,4,5,6,7,8,9]:
#         mpp.apply_async(power, (item, )) # 非阻塞式提交新任务
#         # mpp.apply(power, (item, )) # 阻塞式提交新任务
#
#         mpp.close() # 关闭进程池，意味着不再接受新的任务
#         print('主进程走到这里，正在等待子进程结束')
#         mpp.join() # 等待所有子进程结束
#         print('程序结束')
#
# if __name__ == '__main__':
#     demo()


"""3.9.5 MapReduce 模型
MapReduce是一种用于大规模数据集并行运算的编程模型,分为Map(映射)和Reduce(归约)两个步骤。进程池对
象Pool自带map()方法,遗憾的是没有提供reduce()方法。但是我们可以借用Python标准库functools模块中
的reduce()函数,来实现完整的MapReduce的数据处理模型。
    下面的代码以计算整数列表各元素的平方和为例,演示了Map和Reduce的用法。代码中模报一次平方计算
耗时大于0.5秒,如果使用单进程做100次平方运算至少耗时50秒,使用8个进程并行计算,实测总耗时约8秒。"""

import time
from functools import reduce
import multiprocessing as mp

def power(x, a=2):
    """进程函数：幂函数"""

    time.sleep(0.5) # 延时0.5秒，模拟耗时的复杂计算
    return power(x, a)

if __name__ == '__main__':
    mp.freeze_support()
    print('开始计算。。。')
    t0 = time.time()
    with mp.Pool(processes=8) as mpp:
        result_map = mpp.map(power, range(100))
        result = reduce(lambda  result,x:result+x, result_map, 0)

    print('结果为%d, 耗时%0.3f秒'%(result, time.time()-t0))









