"""
课题：协程与爬虫
介绍：协程, 又称为微线程,是一种用户态的轻量级线程。协程不像线程和进程那样,
     需要进行系统内核上的上下文切换,协程的上下文切换是由程序员决定的
"""

"""1.协程：yield 通过生成器实现协程"""

# 什么是生成器？
# list_1 = [i for i in range(1, 8)]
# def index():
#     for i in range(5):
#         yield i
#
# f = index()
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

# 对列表，元组等对象，可以被for循环遍历迭代的，生成器
# 通过yield 对遍历的元素，调用的时候可以进行断点调用
# scrapy


# 什么是迭代器？

# list_2 = [1, 2, 3, 4, 5, 6, 7]
# # 创建可迭代对象
# list_result = iter(list_2)
#
# print(next(list_result))
# print(next(list_result))
# print(next(list_result))
# 对已有的容器，迭代遍历，断点继续执行
# 区别：迭代器是生成器的一种，生成器能够完成迭代器的所有事


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


"""2.协程：greenlet 安装pip install greenlet"""

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
#
#
# g1 = greenlet(test1)
# g2 = greenlet(test2)
#
# # 切换到gr1中运行
# g1.switch()

"""3.协程：gevent 操作一"""
# import gevent
#
#
# def f(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)
#
#
# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# # g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()

"""4.协程：gevent  操作二"""
# import gevent
# import time
# from gevent import monkey
# # 只要有延迟，先执行下一步
# monkey.patch_all()
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

"""5.协程池结合队列的操作"""
"""协程池操作"""
'''
由于gevent的Pool的没有close方法，也没有异常回调参数
引出需要对gevent的Pool进行一些处理，实现与线程池一样接口，实现线程和协程的无缝转换
'''

# import random
# num = random.randint(1,100)
# running = True
#
# while running:
#     answer = int(input('guess(1-100):'))
#     if answer > num:
#         print("猜大了")
#     elif answer < num:
#          print("猜小了")
#     else:
#         print("猜对了")
#         running = False
#
#
# import gevent.monkey
# gevent.monkey.patch_all()    # 打补丁，替换内置的模块
# from gevent.pool import Pool
#
#
# import requests
# from lxml import etree
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
#     def exetute_requests_item_save(self):
#         # 从队列中获取url
#         url = self.queue.get()
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
#                 self.is_running = False
#                 break
#
#
# if __name__ == '__main__':
#     """用户警告:libuv只支持毫秒定时器解决;所有时间更少将设置为1毫秒"""
#     qiubai = QiubaiSpider()
#     qiubai.run()
'''
由于gevent的Pool的没有close方法，也没有异常回调参数
引出需要对gevent的Pool进行一些处理，实现与线程池一样接口，实现线程和协程的无缝转换
'''


"""去哪儿网爬虫"""
# 美团，饿了吗，去哪儿网，携程

# http://travel.qunar.com/travelbook/list.htm?page=1&order=hot_heat
# http://travel.qunar.com/travelbook/note/7595259
# http://travel.qunar.com/travelbook/note/7595185
# "/youji/7595259"
import os, xlwt, xlrd
from xlutils.copy import copy
from requests_html import HTMLSession
from fake_useragent import UserAgent
import re
ua = UserAgent()
session = HTMLSession()


class LYSpider(object):
    def __init__(self):
        self.start_url = 'http://travel.qunar.com/travelbook/list.htm?page={}&order=hot_heat'

    def parse_start_url(self):
        """
        构造发送请求的翻页的url
        :return:
        """
        for page in range(1, 201):
            start_url = self.start_url.format(page)
            self.parse_gl_response(start_url)

    def parse_gl_response(self, start_url):
        """
        解析攻略列表页
        :param start_url: 翻页的url
        :return:
        """
        headers = {
            'user-agent': ua.chrome,
            'referer': start_url,
            'Host': 'travel.qunar.com',
            'Upgrade-Insecure-Requests': '1'
        }
        response = session.get(start_url)
        if response.status_code != 200:
            self.parse_gl_response(start_url)
        # yj_id_list = re.findall('data-bookId="(.*?)"', response.content.decode())
        # print(yj_id_list, len(yj_id_list))
        # # 游记地点
        # addr_list = re.findall('行程：(.*?)<', response.content.decode())
        # print(addr_list)
        # return
        for a in range(1, 11):
            # 游记id
            yj_id = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{a}]/h2/@data-bookid')[0]
            # 游记地点
            yj_addr = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{a}]/p[3]/text()[1]')
            yj_addr = ''.join(yj_addr)[3:]
            next_url = 'http://travel.qunar.com/travelbook/note/' + yj_id
            self.parse_next_url(next_url, headers, yj_addr)

    def parse_next_url(self, next_url, headers, yj_addr):
        """
        解析游记详情页
        :param next_url: 游记详情页url
        :param headers: 游记详情页请求头
        :param yj_addr: 游记地点
        :return:
        """
        response = session.get(next_url, headers=headers)
        # 游记标题
        title = response.html.xpath('//title/text()')
        title = ''.join(title)
        # 出发时间
        start_time = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[1]/p/span[2]/text()')
        start_time = ''.join(start_time)
        # 游记天数
        day_data = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[2]/p/span[2]/text()')
        day_data = ''.join(day_data)
        # 人均费用
        price = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[3]/p/span[2]/text()')
        price = ''.join(price)
        # 人物
        how_people = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[4]/p/span[2]/text()')
        how_people = ''.join(how_people)
        # 游玩方式
        what_how = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[5]/p/span[2]/span/text()')
        what_how = '/'.join(what_how)
        list_data = [yj_addr, title, start_time, day_data, price, how_people, what_how]
        data = {
            '游记详情': list_data
        }
        self.save_excel(data)
        print('下一篇')

    def save_excel(self, data):
        # data = {
        #     '基本详情': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        # }
        os_path_1 = os.getcwd() + '/数据/'
        if not os.path.exists(os_path_1):
            os.mkdir(os_path_1)
        # os_path = os_path_1 + self.os_path_name + '.xls'
        os_path = os_path_1 + '数据.xls'
        if not os.path.exists(os_path):
            # 创建新的workbook（其实就是创建新的excel）
            workbook = xlwt.Workbook(encoding='utf-8')
            # 创建新的sheet表
            worksheet1 = workbook.add_sheet("游记详情", cell_overwrite_ok=True)
            borders = xlwt.Borders()  # Create Borders
            """定义边框实线"""
            borders.left = xlwt.Borders.THIN
            borders.right = xlwt.Borders.THIN
            borders.top = xlwt.Borders.THIN
            borders.bottom = xlwt.Borders.THIN
            borders.left_colour = 0x40
            borders.right_colour = 0x40
            borders.top_colour = 0x40
            borders.bottom_colour = 0x40
            style = xlwt.XFStyle()  # Create Style
            style.borders = borders  # Add Borders to Style
            """居中写入设置"""
            al = xlwt.Alignment()
            al.horz = 0x02  # 水平居中
            al.vert = 0x01  # 垂直居中
            style.alignment = al
            # 合并 第0行到第0列 的 第0列到第13列
            '''基本详情13'''
            # worksheet1.write_merge(0, 0, 0, 13, '基本详情', style)
            # list_data = [yj_addr, title, start_time, day_data, price, how_people, what_how]
            excel_data_1 = ('地点', '标题', '出发时间', '游玩天数', '人均价格', '出行人数', '玩法')
            for i in range(0, len(excel_data_1)):
                worksheet1.col(i).width = 2560 * 3
                #               行，列，  内容，            样式
                worksheet1.write(0, i, excel_data_1[i], style)
            workbook.save(os_path)
        # 判断工作表是否存在
        if os.path.exists(os_path):
            # 打开工作薄
            workbook = xlrd.open_workbook(os_path)
            # 获取工作薄中所有表的个数
            sheets = workbook.sheet_names()
            for i in range(len(sheets)):
                for name in data.keys():
                    worksheet = workbook.sheet_by_name(sheets[i])
                    # 获取工作薄中所有表中的表名与数据名对比
                    if worksheet.name == name:
                        # 获取表中已存在的行数
                        rows_old = worksheet.nrows
                        # 将xlrd对象拷贝转化为xlwt对象
                        new_workbook = copy(workbook)
                        # 获取转化后的工作薄中的第i张表
                        new_worksheet = new_workbook.get_sheet(i)
                        for num in range(0, len(data[name])):
                            new_worksheet.write(rows_old, num, data[name][num])
                        new_workbook.save(os_path)
if __name__ == '__main__':
    l = LYSpider()
    l.parse_start_url()


"""改造协程池爬虫"""
from multiprocessing import Process
from threading import Thread
import gevent.monkey
gevent.monkey.patch_all()    # 打补丁，替换内置的模块
from gevent.pool import Pool
from queue import Queue
import os, xlwt, xlrd, time
from xlutils.copy import copy
from requests_html import HTMLSession
from fake_useragent import UserAgent
ua = UserAgent()
session = HTMLSession()


class LYSpider(object):
    def __init__(self):
        self.start_url = 'http://travel.qunar.com/travelbook/list.htm?page={}&order=hot_heat'
        # 创建队列容器
        self.queue = Queue()
        self.q = Queue()
        # 创建任务池(同一时间，同步并发量) 默认大小是cpu的个数
        self.pool = Pool(20)
        # 与break的效果相似
        self.is_running = True
        # 创建计数
        self.total_requests_num = 0
        self.total_response_num = 0

    def parse_start_url(self, start_num, end_num, excel_name):
        """
        构造发送请求的翻页的url
        :param start_num: 起始翻页
        :param end_num: 终止翻页
        :return:
        """
        for page in range(start_num, end_num):
            start_url = self.start_url.format(page)
            result_data = {
                'start_url': start_url,
                'excel_name': excel_name
            }
            self.queue.put(result_data)
            self.total_requests_num += 1

    def parse_gl_response(self, start_url):
        """
        解析攻略列表页
        :param start_url: 翻页的url
        :return:
        """
        headers = {
            'user-agent': ua.chrome,
            'referer': start_url,
            'Host': 'travel.qunar.com',
            'Upgrade-Insecure-Requests': '1'
        }
        response = session.get(start_url)
        if response.status_code != 200:
            self.parse_gl_response(start_url)
        # yj_id_list = re.findall('data-bookId="(.*?)"', response.content.decode())
        # print(yj_id_list, len(yj_id_list))
        # # 游记地点
        # addr_list = re.findall('行程：(.*?)<', response.content.decode())
        # print(addr_list)
        # return
        for a in range(1, 11):
            # 游记id
            yj_id = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{a}]/h2/@data-bookid')[0]
            # 游记地点
            yj_addr = response.html.xpath(f'/html/body/div[2]/div/div[2]/ul/li[{a}]/p[3]/text()[1]')
            yj_addr = ''.join(yj_addr)[3:]
            next_url = 'http://travel.qunar.com/travelbook/note/' + yj_id
            data = {
                'next_url': next_url,
                'headers': headers,
                'yj_addr': yj_addr,
            }
            self.q.put(data)

    def parse_next_url(self, next_url, headers, yj_addr, excel_name):
        """
        解析游记详情页
        :param next_url: 游记详情页url
        :param headers: 游记详情页请求头
        :param yj_addr: 游记地点
        :return:
        """
        response = session.get(next_url, headers=headers)
        # 游记标题
        title = response.html.xpath('//title/text()')
        title = ''.join(title)
        # 出发时间
        start_time = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[1]/p/span[2]/text()')
        start_time = ''.join(start_time)
        # 游记天数
        day_data = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[2]/p/span[2]/text()')
        day_data = ''.join(day_data)
        # 人均费用
        price = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[3]/p/span[2]/text()')
        price = ''.join(price)
        # 人物
        how_people = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[4]/p/span[2]/text()')
        how_people = ''.join(how_people)
        # 游玩方式
        what_how = response.html.xpath('//*[@id="js_mainleft"]/div[2]/ul/li[5]/p/span[2]/span/text()')
        what_how = '/'.join(what_how)
        list_data = [yj_addr, title, start_time, day_data, price, how_people, what_how]
        data = {
            '游记详情': list_data
        }
        self.save_excel(data, excel_name)
        print('下一篇')

    def save_excel(self, data, excel_name):
        # data = {
        #     '基本详情': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        # }
        os_path_1 = os.getcwd() + '/数据/'
        if not os.path.exists(os_path_1):
            os.mkdir(os_path_1)
        # os_path = os_path_1 + self.os_path_name + '.xls'
        os_path = os_path_1 + f'数据{excel_name}.xls'
        if not os.path.exists(os_path):
            # 创建新的workbook（其实就是创建新的excel）
            workbook = xlwt.Workbook(encoding='utf-8')
            # 创建新的sheet表
            worksheet1 = workbook.add_sheet("游记详情", cell_overwrite_ok=True)
            borders = xlwt.Borders()  # Create Borders
            """定义边框实线"""
            borders.left = xlwt.Borders.THIN
            borders.right = xlwt.Borders.THIN
            borders.top = xlwt.Borders.THIN
            borders.bottom = xlwt.Borders.THIN
            borders.left_colour = 0x40
            borders.right_colour = 0x40
            borders.top_colour = 0x40
            borders.bottom_colour = 0x40
            style = xlwt.XFStyle()  # Create Style
            style.borders = borders  # Add Borders to Style
            """居中写入设置"""
            al = xlwt.Alignment()
            al.horz = 0x02  # 水平居中
            al.vert = 0x01  # 垂直居中
            style.alignment = al
            # 合并 第0行到第0列 的 第0列到第13列
            '''基本详情13'''
            # worksheet1.write_merge(0, 0, 0, 13, '基本详情', style)
            # list_data = [yj_addr, title, start_time, day_data, price, how_people, what_how]
            excel_data_1 = ('地点', '标题', '出发时间', '游玩天数', '人均价格', '出行人数', '玩法')
            for i in range(0, len(excel_data_1)):
                worksheet1.col(i).width = 2560 * 3
                #               行，列，  内容，            样式
                worksheet1.write(0, i, excel_data_1[i], style)
            workbook.save(os_path)
        # 判断工作表是否存在
        if os.path.exists(os_path):
            # 打开工作薄
            workbook = xlrd.open_workbook(os_path)
            # 获取工作薄中所有表的个数
            sheets = workbook.sheet_names()
            for i in range(len(sheets)):
                for name in data.keys():
                    worksheet = workbook.sheet_by_name(sheets[i])
                    # 获取工作薄中所有表中的表名与数据名对比
                    if worksheet.name == name:
                        # 获取表中已存在的行数
                        rows_old = worksheet.nrows
                        # 将xlrd对象拷贝转化为xlwt对象
                        new_workbook = copy(workbook)
                        # 获取转化后的工作薄中的第i张表
                        new_worksheet = new_workbook.get_sheet(i)
                        for num in range(0, len(data[name])):
                            new_worksheet.write(rows_old, num, data[name][num])
                        new_workbook.save(os_path)

    def _callback(self, temp):
        # 递归退出条件
        if self.is_running:
            # 控制并发
            # 合理的利用cpu性能，提高并发数。
            self.pool.apply_async(self.exetute_requests_item_save, callback=self._callback)

    def exetute_requests_item_save(self):
        """
        函数执行流程
        :return:
        """
        result_data = self.queue.get()
        url = result_data['start_url']
        excel_name = result_data['excel_name']
        self.parse_gl_response(url)
        data = self.q.get()
        self.parse_next_url(data['next_url'], data['headers'], data['yj_addr'], excel_name)
        self.total_response_num += 1

    def run(self, start_num, end_num, excel_name):
        self.parse_start_url(start_num, end_num, excel_name)
        for i in range(2):
            # 控制并发
            # 通过apply_async的方法让函数异步执行，但是只能执行一次，为了让其能够被反复执行，通过添加回调函数的方式能够让_callback递归的
            # 调用自己，同时需要指定退出条件  注意：先做完执行，在回调
            self.pool.apply_async(self.exetute_requests_item_save, callback=self._callback)

        while True:
            # 防止主线程结束
            time.sleep(0.0001)  # 避免cpu空转，浪费资源
            # 当响应计数大于或等于url计数时，程序终止
            if self.total_response_num >= self.total_requests_num:
                self.is_running = False
                break

    def thread_run(self):
        Thread(target=self.run, args=(1, 50, '1')).start()
        Thread(target=self.run, args=(50, 100, '2')).start()
        Thread(target=self.run, args=(100, 150, '3')).start()
        Thread(target=self.run, args=(150, 200, '4')).start()

#
if __name__ == '__main__':
    l = LYSpider()
    l.thread_run()

