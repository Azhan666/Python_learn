# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 课题：协程与爬虫
# 介绍：协程，又称为微线程，是一种用户态的轻量级线程。协程不像线程和进程那样，
# 需要进行系统内核上的上下文切换，协程的上下文切换是由程序员决定的

# 1.协程：yield 通过生成器实现协程

# 什么是生成器？
# 生成器是可以被遍历迭代的，比如说：被for循环遍历迭代

# list_1 = [i for i in range(1, 8)]
# def index(): # 我们定义一个简单的函数
#     for i in range(5): # 一个简单的for循环，我们传入一个5
#         yield i # 我们通过yield将i值返回出来

# 那么，在外部创建函数时我们该怎么操作呢？
# 比如：

# f = index()
# print(f.__next__()) # 我们通过__next__()方法来调用i值
# # 通过运行代码，我们发现只有一个输出0，我们再把print语句多来几行：
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# 由运行结果我们可得出一个结论：
# 对列表、元祖等对象可以被for循环遍历迭代的，叫做生成器
# 结论2：通过yield，对遍历的元素调用时可以断点调用（在上一次执行的地方紧接着调用执行）

# yield在爬虫当中使用得并不算多，爬虫框架（scrapy）中常用

# 什么是迭代器？

# 我们像上面一样，继续创建一个列表：

# list_2 = [1, 2, 3, 4, 5, 6, 7]
# # 首先我们创建一个可迭代对象，即将list_2转换为可迭代对象
# list_result = iter(list_2) # 此时list_2已经可迭代了
# # 我们可以结合next()函数进行调用
# print(next(list_result)) # 传入list_result可迭代对象
# # 运行可知，取出的也是1，我们和上次一样，把print语句多来几行
# print(next(list_result))
# print(next(list_result))
# print(next(list_result))
# 由运行结果可得出结论：对已有的容器，迭代遍历，断点继续执行
# 区别：迭代器是生成器的一种，而生成器能够完成迭代器的所有事

# 好了，以上就是生成器和迭代器的区别

# 下面，我们来看看yield()函数如何使用

# import time
#
# def work1():
#     while True:
#         print("----work1---")
#         yield
#         time.sleep(0.5)
#
#
# def work2():
#     while True:
#         print("----work2---")
#         yield
#         time.sleep(0.5)
#
#
# def main():
#     w1 = work1()
#     w2 = work2()
#     for i in range(5):
#         next(w1)
#         next(w2)
#
#
# if __name__ == "__main__":
#     main()

# 由运行结果可知，yield相当于伪return，下面写再多，也不会运行

# 下面我们看看协程(greenlet):

# from greenlet import greenlet
# import time
#
#
# def test1():
#     while True:
#         i = 1
#         print(f"阿姨洗得路---第{i}天")
#         # 协程之间的切换
#         g2.switch()
#         time.sleep(0.5)
#         i += 1
#
#
# def test2():
#     for i in range(5):
#         print(f"三郎还有-----第{i}天")
#         # 协程之间的切换
#         g1.switch()
#         time.sleep(0.5)

# 创建两个协程对象：参数是我们工作的函数
# g1 = greenlet(test1)
# g2 = greenlet(test2)
#
# # 切换到gr1中运行
# g1.switch()

# 我们从课件中copy过来，将字母改成表白语录，直接运行观察，再来分析代码是如何运行的
# 由运行结果可知，它们是交替执行的，
# g1.switch()、g2.switch()是协程之间的切换
# 我们可以通过打断点debug运行来观察执行步骤

# 下面我们来了解第三个协程：genvet

# import gevent
# def f(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)
#         # 获取当前
#
#
# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()

# 我们从课件中copy过来代码直接运行
# 由于这份代码的协程优势不明显，所以我们直接运行下一份代码

# 4.协程:gevent操作2

# import gevent
# import time
# from gevent import monkey
# # 只要有延迟，先执行下一步
# monkey.patch_all() # 打补丁的操作
#
#
# def kang():
#     for i in range(5):
#         print(i)
#         # time.sleep(1)
#
# def dong(url):
#     print(url)
#     time.sleep(2)
#
# if __name__ == "__main__":
#     for i in range(5):
#         # 给协程下达任务
#         g1 = gevent.spawn(kang)
#         g2 = gevent.spawn(dong, 5)
#         print("kangdong")

# 首先，我们先看一下def的两个函数都在做什么操作
# kang()就是一个for循环
# dong()直接输出了url
# g1传入了kang()函数，g2传入了dong()函数，由于dong()函数有参数，所以传入了一个参数5
# kang()函数循环输出了5次，for循环中循环5次
# dong()函数循环了5次，25+5，所以输出结果应该为30个
# 我们直接运行，发现是正确的。

# 我们发现，这一份代码也不怎么牛逼
# 协程的牛逼之处应该是它和协程池的结合使用

# 下面，我们就进入协程的牛逼的协程池：

# 5.协程池结合队列的操作
# 协程池操作

# 由于gevent的Pool没有close方法，也没有异常回调参数
# 引出需要对gevent的Pool进行一些处理，实现与线程池一样接口，实现线程和协程的无缝转换

# 同样，我们从课件copy代码：

# 我们首先观察这一份猜数字代码：

# import random
# num = random.randint(1,100)
# running = True
#
# while running: # while running其实就是while True
#     answer = int(input('guess(1-100):'))
#     if answer > num:
#         print("猜大了")
#     elif answer < num:
#          print("猜小了")
#     else:
#         print("猜对了")
#         running = False # 前两个条件都不满足的话running就为False
#         # while running就变成了while False，即这个循环就终止了



# import gevent.monkey
# gevent.monkey.patch_all()    # 打补丁，替换内置的模块
# from gevent.pool import Pool
#
#
# import requests
# from lxml import html
# etree = html.etree
# from queue import Queue
# import time
#
#
# class QiubaiSpider:
#     def __init__(self):
#         self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
#         self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X \
#         10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
#         # 创建队列容器
#         self.queue = Queue()
#         # 创建任务池(同一时间，同步并发量) 默认大小是cpu的个数
#         self.pool = Pool(5)
#         # 与break的效果相似
#         self.is_running = True
#         # 创建计数
#         self.total_requests_num = 0
#         self.total_response_num = 0
#
#     def get_url_list(self):
#         """获取url列表, 往队列中添加"""
#         for i in range(1, 14):
#             self.queue.put(self.url_temp.format(i))
#             # url计数累加
#             self.total_requests_num += 1
#
#     def parse_url(self, url):
#         """发送请求，获取响应"""
#         return requests.get(url, headers=self.headers).content.decode()
#         # 返回数据，数据解析：content.decode()
#
#     def get_content_list(self, html_str):
#         """
#         提取段子
#         :param html_str: 响应的源码
#         :return: 段子列表
#         """
#         html = etree.HTML(html_str)
#         # 获取段子内容
#         content_list = html.xpath('//div[@class="content"]/span/text()')
#         return content_list
#
#     def save_content_list(self, content_list):  # 保存数据
#         print(content_list)
#         pass
#
#     def exetute_requests_item_save(self): # 关键
#         # 从队列中获取url
#         url = self.queue.get() # 使用get方法，从队列中拿取任务（url）
#         # 拿取之后传入def parse_url(self, url)，发送请求，获取二进制数据
#         # 将url传入定义的解析函数中，获取源码
#         html_str = self.parse_url(url)
#         # 将获取的源码传入定义的数据提取函数中，获取段子内容列表
#         content_list = self.get_content_list(html_str)
#         # 将段子内容列表，传入定义的保存的函数中
#         self.save_content_list(content_list)
#         # 响应计数累加
#         self.total_response_num += 1
#
#     def _callback(self, temp):
#         # 递归退出条件
#         if self.is_running:
#             # 控制并发
#             # 合理的利用cpu性能，提高并发数。
#             self.pool.apply_async(self.exetute_requests_item_save, callback=self._callback)
#             # 执行它就是往协程池里添加任务，添加至池子的上限 # 括号内的是任务函数
#
#     def run(self):
#         """程序启动运行"""
#         self.get_url_list()
#
#         for i in range(2):
#             # 控制并发
#             # 通过apply_async的方法让函数异步执行，但是只能执行一次，为了让其能够被反复执行，通过添加回调函数的方式能够让_callback递归的
#             # 调用自己，同时需要指定退出条件  注意：先做完执行，在回调
#             self.pool.apply_async(self.exetute_requests_item_save, callback=self._callback)
#
#         while True:
#             # 防止主线程结束
#             time.sleep(0.0001)  # 避免cpu空转，浪费资源
#             # 当响应计数大于或等于url计数时，程序终止
#             if self.total_response_num >= self.total_requests_num:
#                 self.is_running = False # 当添加终止后,响应会慢慢赶上来,当响应>=添加时，执行此行代码
#                 # 此行代码执行之后执行之后if self.is_running:不成立，它所在整块代码被pass掉
#                 break
#
#
# if __name__ == '__main__':
#     """用户警告:libuv只支持毫秒定时器解决;所有时间更少将设置为1毫秒"""
#     qiubai = QiubaiSpider()
#     qiubai.run()


# 去哪儿网爬虫
# 爬虫需求：
# 美团、饿了么、去哪儿网、携程

# https://travel.qunar.com/travelbook/list.htm?page=1&order=elite_ctime # 起始的url地址
# https://travel.qunar.com/travelbook/note/7661624 # 游记详情页的url
# href="/youji/7661624" # 游记详情页的href链接
# https://travel.qunar.com/travelbook/note/7661673 # 游记详情页的url


import os, xlwt, xlrd
from xlutils.copy import copy
from requests_html import HTMLSession
from fake_useragent import UserAgent
import re # 方法2，使用正则提取
ua = UserAgent()
session = HTMLSession()

class LYSpider(object): # 创建游记爬虫类
    def __init__(self): # 定义初始化函数
        self.start_url = 'https://travel.qunar.com/travelbook/list.htm?page={}order=hot_heat' # 准备起始的url地址,page使用大括号接收翻页页码


    def parse_start_url(self): # 定义解析起始的url方法
        """
        #         构造发送请求的翻页的url
        #         :return:
        #         """

        for page in range(1, 201): # 页码for循环
            start_url = self.start_url.format(page) # 格式化起始的url页码
            # print(start_url) 打印起始URL，发现两百页的url获取成功
            # 接下来就是获取两百页攻略中的详情页
            self.parse_gl_response(start_url)
            # break # 这个break用于终止回调，只观察一个
            # 方法的回调

    def parse_gl_response(self, start_url): # 定义攻略详情响应方法，传入start_url
        """
        #         解析攻略列表页
        #         :param start_url: 翻页的url
        #         :return:
        #         """
        headers = {
            'user-agent':ua.chrome,
            'referer':start_url,
            #'Host':'travel.qunar.com',
            'upgrade-insecure-requests':'1',
            'cookie':'JSESSIONID=E74830D11AC6148C9964C8C937D7D2A5; QN1=00002b00306c306dbce0e3ea; QN300=auto_4e0d874a; QN99=1879; QunarGlobal=10.86.213.148_1147fecb_1785496456d_5f1|1616327069264; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN601=94be6a3f34da4d6a06d64306601d7a9d; _i=VInJOQqUELAqXJCxmnpu5wio1K2q; QN48=dfad3641-b25c-444c-a784-e6cfd8d84490; fid=0a378afb-9b02-4d98-97cf-111da074d1c2; viewdist=299829-1; uld=1-299829-1-1616327131; csrfToken=QPK1r59cfqV3uJhLbQKUpEKXcUygABL9; QN163=0; Hm_lvt_c56a2b5278263aa647778d304009eafc=1616327229,1616327235,1616415193,1616415203; viewbook=7662221|7661673|7661673|7661673|7661624; QN267=737174139f078eabe; _vi=GPlRe5vVCScccVX1mG-R8eiDIyUtkpLAF5dM5dQ3JKywvhOFZBPfaSRv8XJTx-JnL2aoyc71IwRZb6lohK-cU7Kfir662xZ3ZdZjUMtrU-RVlQkRDC7Ew-LTc4Mbu_vuWnQJHUKe-VJUU2oa1KaAw4a94pRodSnvs6TAKH0Mjkdc; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1616420836; QN271=9311b5ba-0115-437a-9ed8-37edba8b97eb; QN25=3476892c-b939-4bbc-b252-57c17886eb90-9f992f90'

        }
        response = session.get(start_url) # 传入响应的起始url
        if response.status_code !=200: # 如果响应状态码不为200（即被反爬）
            self.parse_gl_response(start_url) # 就回调到def parse_gl_response(self, start_url)方法中，再次对url地址发送请求
        # yj_id_list = re.findall('data-bookId="(.*?)"', response.content.decode()) # 将data-bookId=指向的id改为正则匹配规则：.*?
        # # 游记地点
        # # 通过查看网页源代码，搜索发现，游记地点可以被搜索到，那么，我们可以直接使用正则匹配提取地点
        # addr_list = re.findall('行程:(.*?)<', response.content.decode())
        # # 匹配的对象仍然是response.content.decode()
        # print(addr_list)
        # return # 返回一下，执行一次观察即可
        # 由于部分旅游攻略没有地点，所以正则无法提取，下面我们使用xpath：
        # 使用首先我们要先写一个for循环：循环10次：
        for a in range(1, 11):
            # 游记id
            yj_id = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{a}]/h2/@data-bookid')[0]
            # print(yj_id)
            # 游记地点
            yj_addr = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{a}]/p[3]/text()[1]')
            # 找到网页p标签里的“行程”，copy它的xpath
            print(yj_addr)

            # 由于那些内容标签都在li标签下面，所以我们把li标签使用大括号接收参数a
            # 然后li就变成了动态接收，此时response.html.xpath()接收的已经不是yi_id_list了，将_list删掉即可
            # 然后我们把下面的yi_id_list代码块注释掉
            #通过打印结果可发现，部分结果为空值，所以我们只能使用join()方法：
            yj_id = ''.join(yj_addr)
            # 或者使用try异常捕捉，跳过空值
            next_url = 'https://travel.qunar.com/travelbook/note/' + yj_id
            self.parse_next_url(next_url, headers, yj_addr)

    def parse_next_url(self, next_url, headers, yj_id):
        """
        #         解析游记详情页
        #         :param next_url: 游记详情页url
        #         :param headers: 游记详情页请求头
        #         :param yj_addr: 游记地点
        #         :return:
        #         """
        response = session.get(next_url, headers=headers)
        # 游记标题
        title = response.html.xpath('//title/txt()')
        # 出发时间
        start_time = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[1]/p/span[2]/text()')
        start_time = ''.join(start_time) # 使用join方法来保存出发时间数据
        # 从网页源码中找到出发日期对应的标签内容，copy它的xpath，拿过来后加上/text()
        print(title, start_time)
        # 天数
        day_data = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[2]/p/span[2]/text()')
        day_data = ''.join(day_data)

        # 方法同上
        # 人均费用
        price = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[3]/p/span[2]/text()')
        price = ''.join(price)

        # 同样同上
        # 人物
        how_people = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[4]/p/span[2]/text()')
        how_people = ''.join(how_people)
        # 方法同上
        # 游玩方式
        what_how = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[5]/p/span[2]/text()')
        what_how = '/'.join(what_how)
        # 因为游玩方式需要有一个字符在里面，所以我们需要添加一个'/'
        # 最后，我们需要创建一个list，传递要保存的数据
        list_data = [yj_addr, title, start_time, day_data, price, how_people, what_how]

        # 同上
        # 好了，下面我们进行一次数据的保存
        # 在保存数据之前，我们需要创建一个字典，字典可以直接使用大列表，因为数据最终是要保存在Excel表格里的
        list_1 = [yj_addr, title, start_time, price, how_people, day_data]





        # 使用正则提取
        # print(yj_id_list,) # 打印查看匹配结果
        # 通过正则匹配打印结果可知，成功匹配出了10个id
        # print(response.content.decode())
        # yj_id_list = response.html.xpath('//ul[@class="b_strategy_list "]/li/h2/@data-bookid') # 我们直接使用xpath提取游记id
        # 由于它返回的是一个列表，我们来打印一下
        # print(yj_id_list)
        # 打印发现，输出的是一个空列表，那么，我们可以在上面打印一下response.content.decode
        # 成功匹配出10个id后，为实现其反复爬取功能，我们需要来一个for循环：
        # for yj_id in yj_id_list:
        #     next_url = 'https://travel.qunar.com/travelbook/note' + yj_id # 字符串拼接
        #     self.parse_next_url(next_url, headers)
        #     break # 观察标题提取效果，暂时不循环
        # 需要注意的是，我们这样拼接之后，访问攻略详情页，找到headers的referer字段，这个referer字段对应的就是我们的start_url
        # 所以，这个时候referer字段也要传递下来，已经传递了start_url,无须再传递referer了
        # 这个时候我们来构造一下headers:
        # 首先是user-agent,我们直接使用ua代替,然后referer字段是我们的start_url
        # 我们把我们网页的host也添加进去
        # headers我们已经搞定了,接下来我们再来编写一个函数
    def parse_next_url(self, next_url, headers): # 定义一个解析数据的方法
        # 解析游记详情页
        # :param
        #  next_url: 游记详情页url
        # :param headers: 游记详情页请求头
        # :param yj_addr: 游记地点
        # :return:
        """这个方法需要传入：next_url, headers，
        同时在上面进行方法的回调
        """
        # 解析游记详情页搞定之后，我们来发送请求（对详情页发送请求），获取响应
        response = session.get(next_url, headers=headers)
        # 获取的是json数据
        # 我们打开详情页，右击查看网页源代码，把出发日期这个关键字在源代码里搜索，
        # 成功搜索到“出发日期”关键字，所以没有问题，说明网页内容是同步加载
        # 那么我们可以使用正则、也可以使用xpath把他提取出来
        # 我们通过检查可发现，游记详情页里面的出发日期、天数、玩法等等是通过li标签控制的
        # 所以，我们现在就根据顾客的需求把他们提取出来：标题、出发日期等等
        title = response.html.xpath('//title/text()') # xpath提取标题
        print(title) # 打印一下title，然后先关掉for循环
        # 接下来就是地点，我们在正则匹配的下面开始地点匹配








if __name__ == '__main__':
    l = LYSpider()
    l.parse_start_url()