# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""3.8 线程技术"""

""" 正确理解和使用线程编程是一个程序员从初级到中级的分水岭。线程技术让代码在宏观上实现了多任务
并行处理，为实现复杂的逻辑提供了可能。

    3.8.1 戏说线程和进程
    对于新手来说，首先要理解线程的概念，以及为什么需要线程编程。什么是线程呢?网上一般是
这样定义的：线程（thread）是操作系统能够进行运算调度的最小单位，它被包含在进程之中，是进程中的
实际运作单位。这么说，你听懂了吗？这样的定义纯粹是自说自话，新手看完了更困惑，老手看完了不以为
然。下面用”非专业“的外行话来解释一下线程和进程。
    
    假如你经营一家物业管理公司，最初，公司的业务量很小，事事都需要你亲力亲为，给老张家修完暖气
管道，立马就去老李家换电灯泡——这叫单线程，所有的工作都得顺序执行。
    后来业务拓展了，你雇佣了几个工人，这样你的物业公司就可以同时为多户人家提供服务——这叫多线程，
而你是主线程。
    工人们使用的工具是物业管理公司提供的，这些工由有大家共享，并不专属于某一个人——这叫多线程
资源共享。
    工人们在工作中都需要管钳，可是管钳只有一把——这叫冲突。解决冲突的办法有很多，如排队等候，
等同事用完后微信通知等——这叫线程同步。
    你给工人布置任务——这叫创建线程。布置任务后你还要告诉他，可以开始工作了，不然他会一直停
在那不动——这叫启动线程（start）。
    如果某个工人（线程）的工作非常重要，你（主线程）也许会亲自监工一段时间；如果不指定时间，
则表示你会一直监工到该项工作完成——这叫线程参与（join）。
    业务不忙的时候，你就在办公室喝喝茶。下班时间一到，你群发微信，通知工人该下班了，所有的
工人不管手里正在做的工作是否完成，都立刻下班。因此如果没必要，你得避免工人正忙着的时候发下
班通知——这叫线程守护属性设置和管理（daemon）。
    再后来，公司规模扩大了，同时为很多社区服务，在每个生活社区都设置了分公司，分公司由分公
司经理管理，运营机制和总公司几乎一模一样——这叫多进程，总公司叫主进程，分公司叫子进程。
    总公司和分公司，以及各个公司之间使用的工具都是独立的，不能借用、混用——这叫进程间不能共
享资源，各个公司可以通过专线电话联系——这叫管道。各个分公司之间还可以通过公司公告栏交换信息
——这叫进程间共享内存。另外，各个公司之阿还有各种协同手段，以便完成更大规模的作业——这叫进程
间同步。
    分公司可以跟着总公司一起下班，也可以把全天的工作全部做完之后再下班——这叫守护进程设置。
"""

"""3.8.2 创建、启动和管理线程
    使用threading模块的Thread类，可以快速创建并启动线程。当然，创建线程前，需要把交给线
程去做的工作写成一个函数，这个函数就叫作线程函数。
    表3-9列出了threading.Thread类的方法和属性。
    
    类成员（方法和属性）          说明
    name                线程名
    ident               线程标识符
    daemon              线程是否是守护线程
    start()             开启线程
    join()              若无参数，则等待至线程结束，否则等待至参数指定的时间
    setDaemon()         根据传入的布尔型参数设置线程是否是守护线程
    getName()           返回线程名
    isAlive()           判断线程是否还在运行
    isDaemon            判断线程是否是守护线程
    run()               定义线程功能的方法（通常在子类中被应用开发者重写）
    
    下面这段代码中，主线程创建了A和B两个子线程，线程任务都是每隔一秒”打一声招呼“，重复
5次后结束。两个子线程启动后，主线程“监工”B线程3秒后，检查了子线程A和B是否结束，然后结束程序。
"""

# import time, threading
#
# def hello(name):
#     """线程函数"""
#     for i in range(5):
#         time.sleep(1)
#         print('Hello, 我是%s'%name)
#
# def demo():
#     # threading.Thread创建并快速启动线程
#     A = threading.Thread(target=hello, args=('A',)) # args: 参数
#     B = threading.Thread(target=hello, args=('B',))
#
#     A.setDaemon(True) # 传入布尔值参数，设置为守护线程
#     B.setDaemon(True)
#
#     A.start() # 开启线程
#     B.start()
#
#     B.join(3) # “监工”B线程3秒
#
#     print('线程A%s'%('还在工作中' if A.isAlive() else '已经结束工作',))
#     print('线程B%s'%('还在工作中' if B.isAlive() else '已经结束工作',))
#     print('下班了。')
#
# if __name__ == '__main__':
#     demo()

""" 但是，运行这段代码时，你会发现，当主线程“喊下班（结束程序）时，子线程A和B并没有结束，
主线程要等到子线程任务完成才结束。那么如何令子线程在主线程结束时无条件跟随主线程一起结束呢？
很简单，在线程start()之前，使用setDaemon(True)设置该线程为守护线程就可以了，去掉上面代码中
setDaemon(True)那两行的注释，再次运行，子线程A和B就会跟随主线程一起结束。”"""

"""3.8.3 线程同步
    多个线程同时工作，既有任务协同，也有资源竞争，这就需要通过线程之间的同步来解决问题。
常用的线程同步方法有队列、线程锁、信号量、时间和条件5种。

    1.队列Queue
    队列是线程间交换数据最常用的方式之一，尤其适合生产者——消费者模式。Python的queue模块
提供了一个Queue类，它的写队列put()和读队列get()两个方法均默认为阻塞式。这意味着一旦队列
为空，则get()会被阻塞；一旦队列满了，则put()会被阻塞。如果使用参数block=False设置put()
或get()为非阻塞，则读空或写满时会抛出异常，因此读写队列前面需要使用empty()或full()进行判断
。Queue类实例化时可以指定队列长度。
    下面的代码演示了典型的生产者——消费者模式。线程A负责往地上“扔钱”（写队列），线程B负责
从地上“捡钱”（赌队列）。"""

# import os, time, random
# import queue
# import threading
#
# def sub_thread_A(q):
#     """A线程函数：生成数据"""
#     while True:
#         time.sleep(5*random.random()) # 0~5秒的随机延时
#         q.put(random.randint(10,100)) # 随机生成[10,100]的整数
#
# def sub_thread_B(q):
#     """B线程：使用数据"""
#     words = ['哈哈，','天哪！','My God!', '咦，天上掉馅饼了？']
#     while True:
#
#         print('%s捡到了%d块钱！离给阿婷买房买车又近了一步！！！'%(words[random.randint(0,3)], q.get()))
#
# if __name__ == '__main__':
#     print('线程(%s)开始，按回车键结束本程序'%os.getpid()) # os.getpid()：返回当前进程id
#
#     q = queue.Queue(10) # Queue实例化，指定队列长度为10
#
#     A = threading.Thread(target=sub_thread_A, args=(q,))
#     A.setDaemon(True) # 设置为守护线程
#     A.start() # 开启线程
#
#     B = threading.Thread(target=sub_thread_B, args=(q,))
#     B.setDaemon(True)
#     B.start()
#
#     input() # 利用input函数阻塞主线程。这是常用的调试手段

"""2. 线程锁Lock
    假设有这样一个需求，在一个几百人的微信群里统计喜欢PyCharm的人数。有人说，那就从1开始
报数吧，并发了起始数字1，立马有人发了数字2、3......但是统计很快就进行不下去了，因为大家
发现好几个人发4，有更多的人发5。
    这就是典型的资源竞争冲突：统计用的计数器就是唯一的资源，很多人（子线程）都想取得写计数
器的资格。怎么办呢？Lock（互斥锁）就是一个很好的解决方案。Lock只能有一个线程获取，且获取该锁
的线程才能执行，否则就会阻塞；获取该锁的线程执行完任务后，必须释放锁。"""

# import time, threading
#
# lock = threading.Lock() # 创建互斥锁
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
#     threads = list()
#     for i in range(30): # 假设群里有30人都喜欢试用PyCharm
#         threads.append(threading.Thread(target=hello))
#         threads[-1].start() # 下标为-1表示输出数组的最后一行数据值，
#         # 用法：当有时候弄不清数组的最后一组数据的时候，可以用这个方法。
# # 为什么取下标-1：https://blog.csdn.net/MoneyFxxker/article/details/88553379
#
#     for t in threads:
#         t.join()
#
#     print('统计完毕，共有%d人'%counter)
#
# if __name__ == '__main__':
#     demo()

""" 除了互斥锁，锁线程还有另一种形式，叫作递归锁（RLock），又称可重入锁。已经获得递归锁的线
程可以继续多次获得该锁而不会被阻塞，释放的次数必须和获取的次数相同才会真正释放该锁。"""

"""3. 信号量Semaphore
    上面的例子中，统计用的计数器是唯一的资源，因此使用只能被一个线程获取的互斥锁来解决问题。
假如共享的资源有多个，多线程竞争时一般使用信号量（Semaphore）来同步。信号量有一个初始值，
表示当前可用的资源数，多线程执行过程中会通过acquire()和release()操作动态的加减信号量。
例如，有30个工人（线程）都需要使用电锤（资源），但是电锤总共只有5把。使用信号量（Semaphore）
解决竞争的代码如下：
acquire:取得，release：释放"""
# 关于信号量：https://www.cnblogs.com/renpingsheng/p/7202818.html

# import time,threading
#
# S = threading.Semaphore(5) # 有5把电锤可供使用
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
#     threads = list()
#     for i in range(30): # 有30名工人要求使用电锤
#         threads.append(threading.Thread(target=us_hammer, args=(i,)))
#         threads[-1].start() # 依旧取下标，输入出最后一行数据
#
#     for t in threads:
#         t.join()
#
#     print('所有线程工作结束')
#
# if __name__ == '__main__':
#     demo()


"""4.事件Event，event：事件
    想象我们每天早上上班的场景：为了不迟到，总是提前几分钟（我一般都会提前30分钟）到办公室，
打卡后，一看表还不到工作时间，大家就看看新闻、聊聊天。工作时间一到，立马开始工作。如果有人
迟到了，那他自然就不能看新闻和聊天了，得立即投入工作中。
    上面这个场景中，每个人代表一个线程，工作时间到，表示事件（Event）发生。事件发生前，
线程会调用wait()方法阻塞自己（对应看新闻和聊天）；一旦事件发生，会唤醒所有调用wait()而
进入阻塞状态的线程。下面的代码模拟了办公室里的这一场景。"""

# 关于Event事件的is_set:https://blog.csdn.net/cumtv80668/article/details/107796456

# import time, threading
#
# E = threading.Event() # 创建事件
#
# def work(id):
#     """线程函数"""
#     print('<%d号员工>上班打卡'%id)
#     if E.is_set(): # 已经到点了
#         print('<%d号员工>迟到了'%id)
#     else: # 还不到点
#         print('<%d号员工>看新闻中...'%id)
#         E.wait() # 等上班铃声
#
#     print('<%d号员工>开始工作了...'%id)
#     time.sleep(10) # 工作10秒后下班
#     print('<%d号员工>下班了'%id)
#
# def demo():
#     E.clear() # 设置为“未到上班时间”
#     threads = list()
#
#     for i in range(3): # 3人提前来到公司打卡
#         threads.append(threading.Thread(target=work, args=(i,)))
#         threads[-1].start()
#
#     time.sleep(5) # 5秒后上班时间到
#     E.set()
#
#     time.sleep(5) # 5秒后，“大佬”（9号）到
#     threads.append(threading.Thread(target=work, args=(9,)))
#     threads[-1].start()
#
#     for t in threads:
#         t.join()
#
#     print('都下班了，关灯关门走人')
#
# if __name__ == '__main__':
#         demo()


"""5. 条件 Condition
    和线程锁相比，条件（Condition）更侧重于线程间的联络，有点类似于小朋友们的捉迷藏游戏，
假设两位小朋友，Hezhan和Liting，打算玩一个捉迷藏的游戏，规则是这样的：Hezhan先找个眼罩把
眼睛蒙住，喊一声“我已经蒙上眼睛了”。听到消息后，Liting就找地方藏起来，藏好以后，也喊一声
“我已经藏好了，你来找我吧”。Liting听到后，也要回应一声“我来了”，捉迷藏正式开始。各自随机
等了一段时间后，两位小朋友都忍不住跑了出来。谁先跑出来，就算谁输。下面的代码用两个线程模拟
Liting和Hezhan，玩起了捉迷藏的游戏。"""

# 关于notify：https://blog.csdn.net/yaoliuwei1426/article/details/80784877

# import time, threading, random
#
# cond = threading.Condition() # 创建条件对象
# draw_Hezhan = False # Hezhan小朋友认输
# draw_Liting = False # Liting小朋友认输
#
# def hezhan():
#     """Hezhan小朋友的线程函数"""
#
#     global draw_Hezhan, draw_Liting
#
#     time.sleep(1) # 确保Liting小朋友已经进入消息等待状态
#     cond.acquire() # 阻塞时请求资源
#     time.sleep(random.random()) # 假装蒙眼需要花费时间
#     print('Hezhan:我已经蒙上眼睛了')
#     cond.notify() # 把消息通知到Liting小朋友
#     # notify(n=1):通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正
#     # 等待该condition的线程,最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调
#     # 用，否则会触发RuntimeError。notify()不会主动释放Lock。
#     cond.wait() # 释放资源并等待Liting小朋友已经藏好的消息。
#
#     print('Hezhan:我来了') # 收到Liting小朋友已经藏好的消息后
#     cond.notify() # 把消息通知到Liting小朋友
#     cond.release() # 不要再侦听消息了，彻底释放资源
#     time.sleep(random.randint(3,10)) # Hezhan小朋友的耐心只有3~10秒
#
#     if draw_Liting:
#         print('Hezhan:哈哈，我找到你了，我赢了')
#     else:
#         draw_Hezhan = True
#         print('Hezhan:算了，你自己出来吧，我认输啦')
#
# def liting():
#     """Liting小朋友的线程参数"""
#
#     global draw_Hezhan, draw_Liting
#
#     cond.acquire() # 阻塞时请求资源
#     cond.wait() # 如果先于Hezhan小朋友请求到资源，则立刻释放并等待
#     time.sleep(random.random()) # 假装找地方躲藏需要花费时间
#     print('Liting：我藏好了，你来找我吧')
#     cond.notify() # 把消息通知到Hezhan小朋友
#     cond.wait() # 释放资源并等待Hezhan小朋友开始找人的消息
#
#     cond.release() # 不在侦听消息了，彻底释放资源
#     time.sleep(random.randint(3,10)) # Liting小朋友的耐心只有3~10秒
#
#     if draw_Liting:
#         print('Liting:哈哈，那我出来了，我赢了')
#     else:
#         draw_Hezhan = True
#         print('Liting:算了，这里太闷了，我还是出来吧')
#
# def demo():
#     th_hezhan = threading.Thread(target=hezhan)
#     th_liting = threading.Thread(target=liting)
#     th_hezhan.start()
#     th_liting.start()
#     th_hezhan.join()
#     th_liting.join()
#
# if __name__ == '__main__':
#     demo()

"""3.8.4 线程池
    尽管多线程可以并行处理多个任务，但开启线程不仅花费时间，也需要占用系统资源。因此，线程
数量不是越多越快，而是要保持在合理的水平上。线程池可以让我们用固定数量的线程完成比线程数量
多得多的任务。下面的代码演示了使用Python的标准块创建线程池，计算多个数值的平方。"""

# from concurrent.futures import ThreadPoolExecutor
#
# def pow2(x):
#     return x*x
# with ThreadPoolExecutor(max_workers=4) as pool: # 4个线程的线程池
#     result = pool.map(pow2, range(10)) # 使用4个线程分别计算0~9的平方
# print(list(result)) # result是一个生成器，转成列表才可以直观地看到计算结果
# 迭代器和生成器：https://www.runoob.com/python3/python3-iterator-generator.html





