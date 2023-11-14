"""
课题：线程与爬虫
"""


"""1.线程讲解"""
# 什么是线程？
# 程序运行的最小单位

# from threading import Thread
# import time
#
# def index(x, y):
#     print(f'我是{x}, 你是{y}')
#
# def run():
#     # url地址列表
#     list_1 = ['电', '光', '风儿', '莎儿', 1, 2, 3, 4]
#     num = len(list_1)//2
#     list_2 = list_1[:num]
#     list_3 = list_1[num:]
#     print(list_2)
#     print(list_3)
#     Thread(target=index, args=('电', '光')).start()
#     Thread(target=index, args=('风儿', '莎儿')).start()
#
# run()


"""2.线程间共享全局变量"""

"""3.GIL锁的应用"""
# from threading import Thread
# import threading
# import time
#
# # 主要问题：数据的保存
# # 十个线程保存十张壁纸
# # 保存的图片与名称不对应
#
# # 保存到excel表格数据
# # 表格间的数据顺序会错乱
#
# # 进程非常的类似了，线程队列，线程池
#
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
#
# if __name__ == '__main__':
#     mutex = threading.Lock()
#     Thread(target=func, args=(3,)).start()
#     Thread(target=function, args=(5,)).start()

"""结合gil锁运用线程"""

"""4.多线程实现"""
"""5.线程池"""
# 有资源竞争的问题
# from concurrent.futures import ThreadPoolExecutor
# import threading
# import time
#
#
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



"""案例实战"""
# 壁纸的特征
# https://konachan.net/sample/f6e113c3724311767522ed8770c7bf13/Konachan.com%20-%20324472%20sample.jpg
# https://konachan.net/sample/7b8e5120452a4513943a58b106be6e98/Konachan.com%20-%20324463%20sample.jpg
#
# 1.访问列表页
# 2.匹配出图片的特征
# 3.url地址的拼接(大图)

# 读写分离
# 请求与保存分离

# from concurrent.futures import ThreadPoolExecutor
# import threading
# from queue import Queue
# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# from threading import Thread
# import re, os
# ua = UserAgent()
# session = HTMLSession()
#
#
# class Bz(object):
#
#     def __init__(self):
#         self.start_url = 'https://konachan.net/post?page={}&tags='
#         self.q = Queue()
#         # # 创建一个包含5条线程的线程池
#         self.pool = ThreadPoolExecutor(max_workers=5)
#
#     def thread_start_url(self):
#         self.pool.submit(self.parse_start_url, 1, 2000, 't1')
#         self.pool.submit(self.parse_start_url, 2000, 4000, 't2')
#         self.pool.submit(self.parse_start_url, 4000, 6000, 't3')
#         self.pool.submit(self.parse_start_url, 6000, 8000, 't4')
#         self.pool.submit(self.parse_start_url, 8000, 12280, 't5')
#
#         # Thread(target=self.parse_start_url, args=(1, 5001, 't1')).start()
#         # Thread(target=self.parse_start_url, args=(5001, 12280, 't2')).start()
#
#     def parse_start_url(self, page_start_number, page_end_number, name_thread):
#         """
#         解析起始的url类地址
#         :return:
#         """
#         # 创建循环记数，统计下载图片张数
#         num = 1
#         # 使用循环模拟发送翻页请求
#         for page in range(page_start_number, page_end_number):
#             # 发送请求，获取响应
#             response = session.get(self.start_url.format(page))
#             # 解析源码内容
#             html_str = response.content.decode()
#             # 正则提取小型图片url地址,返回一个列表
#             url_list = re.findall("preload\('(.*?)'\);", html_str)
#             # 方法回调解析
#             self.parse_url_list(url_list, num, name_thread)
#             # 计数累加
#             num += 1
#
#     def parse_url_list(self, url_list, num, name_thread):
#         """
#         解析拼接大型图片url地址
#         :param url_list: 小型图片url地址列表
#         :param num: 循环计数，统计下载图片张数
#         :param name_thread: 线程名称
#         :return:
#         """
#         # 遍历图片列表
#         for url in url_list:
#             # 正则匹配出壁纸属性id
#             img_id = url[40:-4]
#             # url地址拼接，获取大壁纸url
#             next_url = f'https://konachan.net/sample/{img_id}/Konachan.com%20-%20324421%20sample.jpg'
#             print(next_url)
#             # 发送请求，获取二进制响应
#             data = session.get(next_url).content
#             dict_1 = {
#                 'data': data,
#                 'num': num,
#                 'img_id': img_id,
#                 'name_thread': name_thread
#             }
#             self.q.put(dict_1)
#             self.q.join()
#
#     def save_data(self):
#         """
#         保存
#         :param data: 图片二进制数据
#         :param num: 循环计数，统计下载图片张数
#         :param img_id: 保存图片的名称
#         :param name_thread: 线程名称
#         :return:
#         """
#         while True:
#             dict_1 = self.q.get()
#             name_thread = dict_1['name_thread']
#             img_id = dict_1['img_id']
#             data = dict_1['data']
#             num = dict_1['num']
#             # 创建保存壁纸文件夹
#             os_path = os.getcwd() + '/图片/'
#             # 判断改文件夹路径是否存在，不存在就创建
#             if not os.path.exists(os_path):
#                 os.mkdir(os_path)
#             # 壁纸保存
#             with open(os_path + name_thread + '_' + img_id + '.jpg', 'wb')as f:
#                 f.write(data)
#             print(f'第{num}张壁纸下载完成====logging====！！！')
#             self.q.task_done()
#
#     def run(self):
#         t1 = Thread(target=self.thread_start_url)
#         t2 = Thread(target=self.save_data)
#         t1.start()
#         t2.daemon = True
#         t2.start()
#
#
# if __name__ == '__main__':
#     b = Bz()
#     b.run()


"""线程队列"""
# from threading import Thread
# from queue import Queue
# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# import re, os
# ua = UserAgent()
# session = HTMLSession()
#
#
# class Bz(object):
#
#     def __init__(self):
#         self.start_url = 'https://konachan.net/post?page={}&tags='
#         self.q = Queue()
#
#     def parse_start_url(self):
#         """
#         解析起始的url类地址
#         :return:
#         """
#         # 创建循环记数，统计下载图片张数
#         num = 1
#         # 使用循环模拟发送翻页请求
#         for page in range(1, 12280):
#             # 发送请求，获取响应
#             response = session.get(self.start_url.format(page))
#             # 解析源码内容
#             html_str = response.content.decode()
#             # 正则提取小型图片url地址,返回一个列表
#             url_list = re.findall("preload\('(.*?)'\);", html_str)
#             # 方法回调解析
#             self.parse_url_list(url_list, num)
#             # 计数累加
#             num += 1
#
#     def parse_url_list(self, url_list, num):
#         """
#         解析拼接大型图片url地址
#         :param url_list: 小型图片url地址列表
#         :param num: 循环计数，统计下载图片张数
#         :return:
#         """
#         # 遍历图片列表
#         for url in url_list:
#             # 正则匹配出壁纸属性id
#             img_id = url[40:-4]
#             # url地址拼接，获取大壁纸url
#             next_url = f'https://konachan.net/sample/{img_id}/Konachan.com%20-%20324421%20sample.jpg'
#             print(next_url)
#             # 发送请求，获取二进制响应
#             data = session.get(next_url).content
#             # 方法回调解析，保存
#             self.save_data(data, num, img_id)
#             # 计数累加
#             num += 1
#
#     def save_data(self, data, num, img_id):
#         """
#         保存
#         :param data: 图片二进制数据
#         :param num: 循环计数，统计下载图片张数
#         :param img_id: 保存图片的名称
#         :return:
#         """
#         # 创建保存壁纸文件夹
#         os_path = os.getcwd() + '/图片/'
#         # 判断改文件夹路径是否存在，不存在就创建
#         if not os.path.exists(os_path):
#             os.mkdir(os_path)
#         # 壁纸保存
#         with open(os_path + img_id + '.jpg', 'wb')as f:
#             f.write(data)
#         print(f'第{num}张壁纸下载完成====logging====！！！')
#
#
# if __name__ == '__main__':
#     b = Bz()
#     b.parse_start_url()
#
#
# # https://konachan.net/post/show/324421/black_hair-blush-chitanda_eru-crying-hyouka-long_h
# # https://konachan.net/sample/9dd006f482163934535db8ae45f8cf7d/Konachan.com%20-%20324421%20sample.jpg
# # https://konachan.net/data/preview/9d/d0/9dd006f482163934535db8ae45f8cf7d.jpg  小
# # https://konachan.net/sample/8a5091c117d80a8c33af7701e2a5d8bb/Konachan.com%20-%20324415%20sample.jpg
# # https://konachan.net/sample/079defeaf37fcec6c53b038bcf04677a/Konachan.com%20-%20324421%20sample.jpg
# # https://konachan.net/data/preview/07/9d/079defeaf37fcec6c53b038bcf04677a.jpg



# 页码
# img_id


"""断点续爬"""

# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# import re, os, json
# ua = UserAgent()
# session = HTMLSession()
#
#
# class Bz(object):
#
#     def __init__(self):
#         self.start_url = 'https://konachan.net/post?page={}&tags='
#
#     def if_file(self):
#         if not os.path.exists('./壁纸.log'):
#             print('没有发现日志====logging====')
#             self.parse_start_url(1)
#         else:
#             print('发现日志，开始读取====logging====')
#             with open('壁纸.log', 'r', encoding='utf-8')as f:
#                 data = json.load(f)
#             dict_1 = dict(data)
#             page = dict_1['page']
#             print('日志读取完成，====logging====')
#             self.parse_start_url(page)
#
#     def parse_start_url(self, page_num):
#         """
#         解析起始的url类地址
#         :return:
#         """
#         # 创建循环记数，统计下载图片张数
#         num = 1
#         # 使用循环模拟发送翻页请求
#         for page in range(page_num, 12280):
#             # 发送请求，获取响应
#             response = session.get(self.start_url.format(page))
#             # 解析源码内容
#             html_str = response.content.decode()
#             # 正则提取小型图片url地址,返回一个列表
#             url_list = re.findall("preload\('(.*?)'\);", html_str)
#             # 方法回调解析
#             self.parse_url_list(url_list, num, page)
#             # 计数累加
#             num += 1
#
#     def parse_url_list(self, url_list, num, page):
#         """
#         解析拼接大型图片url地址
#         :param url_list: 小型图片url地址列表
#         :param num: 循环计数，统计下载图片张数
#         :param page: 页码
#         :return:
#         """
#         # 遍历图片列表
#         for url in url_list:
#             # 正则匹配出壁纸属性id
#             img_id = url[40:-4]
#             if not os.path.exists('./壁纸.log'):
#                 print('由于没有发现日志，开始记录日志信息====logging====')
#                 file = {
#                     'page': page,
#                     'img_id': [img_id]
#                 }
#                 with open('./壁纸.log', 'w', encoding='utf-8')as f:
#                     json.dump(file, f)
#                 print('日志记录完成，====logging====')
#             else:
#                 print('开始更新日志数据，====logging====')
#                 with open('./壁纸.log', 'r', encoding='utf-8')as f:
#                     f_data = f.read()
#                 """更新数据的操作"""
#                 dict_1 = json.loads(f_data)
#                 if img_id in dict_1['img_id']:
#                     continue
#                 dict_1['img_id'].append(img_id)
#                 dict_1['page'] = page
#                 with open('./壁纸.log', 'w', encoding='utf-8')as f:
#                     json.dump(dict_1, f)
#                 print('日志记录完成，====logging====')
#             # url地址拼接，获取大壁纸url
#             next_url = f'https://konachan.net/sample/{img_id}/Konachan.com%20-%20324421%20sample.jpg'
#             # 发送请求，获取二进制响应
#             data = session.get(next_url).content
#             # 方法回调解析，保存
#             self.save_data(data, num, img_id)
#             # 计数累加
#             num += 1
#
#     def save_data(self, data, num, img_id):
#         """
#         保存
#         :param data: 图片二进制数据
#         :param num: 循环计数，统计下载图片张数
#         :param img_id: 保存图片的名称
#         :return:
#         """
#         # 创建保存壁纸文件夹
#         os_path = os.getcwd() + '/图片/'
#         # 判断改文件夹路径是否存在，不存在就创建
#         if not os.path.exists(os_path):
#             os.mkdir(os_path)
#         # 壁纸保存
#         with open(os_path + img_id + '.jpg', 'wb')as f:
#             f.write(data)
#         print(f'第{num}张壁纸下载完成, {img_id}====logging====！！！')
#
#
# if __name__ == '__main__':
#     b = Bz()
#     b.if_file()

