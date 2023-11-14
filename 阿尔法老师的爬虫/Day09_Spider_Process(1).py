# """
# 课题：多进程与爬虫
# """
#
# """1.应用场景"""
# # 什么是进程？
# # 资源分配和调度的基本单位
#
# """2.进程讲解"""
# # from multiprocessing import Process
# # import time
# # def index(num):
# #     start_time = time.time()
# #     for i in range(num):
# #         print('结果是：', i)
# #     end_time = time.time()
# #     print(start_time - end_time)
# #
# # def func(num):
# #     Process(target=index, args=(num,)).start()
# #     Process(target=index, kwargs={'num': num}).start()
# #
# # if __name__ == '__main__':
# #     # 进程创建
# #     # 进程之间没有任何的关联
# #     Process(target=index, args=(num,)).start()
# #     Process(target=index, kwargs={'num': num}).start()
# #     func(3)
#
# """3.进程队列"""
# # from multiprocessing import Process
# # from multiprocessing import JoinableQueue as Queue
# #
# #
# # class Love(object):
# #     def __init__(self):
# #         # 创建队列
# #         self.q = Queue()
# #
# #     def parse_data(self):
# #         """
# #         功能：给队列添加任务
# #         :return:
# #         """
# #         data = '第{}天-----阿姨洗得路'
# #         for i in range(1, 101):
# #             self.q.put(data.format(i))
# #
# #
# #     def func_1(self):
# #         """
# #         从队列中，取出任务
# #         :return:
# #         """
# #         while True:
# #         # for i in range(1, 101):
# #             result = self.q.get()
# #             print(result)
# #             # join的等待信号
# #             # 是队列计数 -1
# #             self.q.task_done()
# #
# #     def run(self):
# #         """
# #         启动函数
# #         :return:
# #         """
# #         m1 = Process(target=self.parse_data)    # m1: 发布外包单
# #         m2 = Process(target=self.func_1)        # m2： 接收外包单
# #         m1.start()
# #         # 设置守护进程：因为m2是死循环，设置守护进程的原因就在于我们需要让m1进程结束，m2跟着结束
# #         # 即只在需要的时候才会启动，完成任务后就自动接受
# #         m2.daemon = True
# #         m2.start()
# #         #
# #         m1.join()
# #
# #
# # if __name__ == '__main__':
# #     love = Love()
# #     love.run()
#
#
# """4.进程池"""
#
# # from multiprocessing import Pool
# # import time, random, os
# #
# #
# # def worker(msg):
# #     start_time = time.time()
# #     print('%s 开始执行， 进程编号位%d' % (msg, os.getpid()))
# #     time.sleep(random.random() * 2)
# #     print('==========================')
# #     print(random.random() * 2)
# #     stop_time = time.time()
# #     print(msg, '执行完毕，花费：%0.2f' % (start_time-stop_time))
# #
# #
# # if __name__ == '__main__':
# #     # 创建一个最大进程数量为3的进程池
# #     po = Pool(3)
# #     for i in range(0, 10):
# #         """
# #         apply_async: 非阻塞的形式运行我们的进程，
# #         # 进程之间没有联系 ---  进程不共享全局变量
# #         """
# #         po.apply_async(worker, args=(i,))
# #     print('开启----')
# #     po.close()  # 关闭：关闭进程池，关闭之后，不会在接受新的请求了
# #     po.join()   # 等待进程池中所有的进程执行完毕
# #     print('关闭----')
#
#
# # import random
# #
# # print(random.random())
#
# #
# # from requests_html import HTMLSession
# # from fake_useragent import UserAgent
# # ua = UserAgent()
# # session = HTMLSession()
# #
# #
# # start_url = 'https://lol.qq.com/act/a20170926preseason/data/cn/runes.json'
# #
# # response = session.get(start_url)
# #
# # with open('1.json', 'w', encoding='utf-8')as f:
# #     f.write(response.content.decode())
#
#
# # //ossweb-img.qq.com/images/lol/img/spell/SummonerBarrier.png
#
# # from requests_html import HTMLSession
# # from fake_useragent import UserAgent
# # ua = UserAgent()
# # session = HTMLSession()
# # import re, json
# #
# # url = 'https://game.gtimg.cn/images/lol/act/img/js/items/items.js'
# # resp_json = session.get(url).json()
# # print(resp_json)
#
#
#
#
#
#
#
#
#
# # url = 'https://lol.qq.com/biz/hero/summoner.js'
# #
# # response = session.get(url)
# #
# # # print(response.content.decode())
# #
# # data = re.findall('LOLsummonerjs=(.*?);', response.content.decode())[0]
# #
# # print(json.loads(data), type(json.loads(data)))
#
#
#
#
#
# from multiprocessing import Process
# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# import jsonpath, os
# session = HTMLSession()
# ua = UserAgent()
#
#
# class Lol(object):
#     def __init__(self):
#         # 获取所有英雄id的url
#         self.start_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
#         # 拼接英雄详情url地址
#         self.p_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
#
#     def parse_url(self):
#         """
#         提取c，提取英雄的名称
#         :return: item_id_list, name_list
#         """
#         response_json = session.get(url=self.start_url).json()
#         # 提取英雄的id
#         item_id_list = jsonpath.jsonpath(response_json, '$..heroId')
#         return item_id_list
#
#     def parse_item(self, item_id_list):
#         """
#         json数据的解析
#         :param item_id_list: 英雄的id列表
#         """
#         for id in item_id_list:
#             referer = 'https://lol.qq.com/data/info-defail.shtml?id={}'.format(id)
#             headers = {
#                 "user-agent": ua.chrome,
#                 "referer": referer
#             }
#             # 获取英雄详情数据
#             name_json = session.get(url=self.p_url.format(id), headers=headers).json()
#             # print(name_json)
#             # 电脑版图片
#             win_img_list = jsonpath.jsonpath(name_json, '$..mainImg')
#             # 手机版的图片
#             phone_img_list = jsonpath.jsonpath(name_json, '$..loadingImg')
#             # print(win_img_list)
#             # print(phone_img_list)
#             # 创建文件夹的名称   英雄的名称
#             name = jsonpath.jsonpath(name_json, '$..name')[0]
#             # print(name)
#             print('文件夹创建中-----logging-----')
#             os_path = os.getcwd() + '/' + name + '/'
#             if not os.path.exists(os_path):
#                 os.mkdir(os_path)
#             # 皮肤图片列表
#             # 列表下标操作，过滤第一个数据
#             name_list_data = jsonpath.jsonpath(name_json, '$..name')[1::]
#             self.process_run(phone_img_list, win_img_list, os_path, name_list_data)
#
#     def save_data(self, img_list, os_path, name_list_data, num):
#         """
#         保存
#         :param img_list: 图片列表
#         :param os_path: 保存的路径
#         :param name_list_data: 英雄皮肤的名称列表
#         :return:
#         """
#         if num == 1:
#             # 循环同下标的两个列表的元素
#             for url, title in zip(img_list, name_list_data):
#                 if url != '':
#                     data = session.get(url=url).content
#                     with open(os_path + title + '电脑版' + '.jpg', 'wb')as f:
#                         f.write(data)
#                         print('电脑版图片下载完毕------logging-------{}'.format(title))
#         if num == 2:
#             # 循环同下标的两个列表的元素
#             for url, title in zip(img_list, name_list_data):
#                 if url != '':
#                     data = session.get(url=url).content
#                     with open(os_path + title + '手机版' + '.jpg', 'wb')as f:
#                         f.write(data)
#                         print('手机版图片下载完毕------logging-------{}'.format(title))
#
#     def process_run(self, phone_img_list, win_img_list, os_path, name_list_data):
#         Process(target=self.save_data, args=(win_img_list, os_path, name_list_data, 1)).start()
#         Process(target=self.save_data, args=(phone_img_list, os_path, name_list_data, 2)).start()
#
#     def run(self):
#         item_id_list = self.parse_url()
#         self.parse_item(item_id_list)
#
#
# if __name__ == '__main__':
#     lol = Lol()
#     lol.run()


# 5百-8百

# 哪一个参数不一样，就是那个参数控制的翻页
# https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI10181324506558265&g_tk=5381&sign=zzad8ffewgr05ssr2f3fef04bda3a286eeb40136f6b80f4a&  loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singerList%22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%22%2C%22param%22%3A%7B%22area%22%3A-100%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%3A-100%2C%22sin%22%3A0%2C%22cur_page%22%3A1%7D%7D%7D
# https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI2696951322967065&g_ tk=5381&sign=zzax9lndmk1v2y2uq31a4bb609c7b78275ed2b8d0ec78fbb7& loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singerList%22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%22%2C%22param%22%3A%7B%22area%22%3A-100%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%3A-100%2C%22sin%22%3A80%2C%22cur_page%22%3A2%7D%7D%7D
# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# ua = UserAgent()
# session = HTMLSession()
#
# # 第一种
# start_url = 'https://www.baidu.com/s?wd=python'
# response = session.get(start_url)
# # 第二种
# print(response.html.xpath('//title/text()'))
#
# next_url = 'https://www.baidu.com/s'
# dict_1 = {
#     'wd': 'python'
# }
# resp = session.get(next_url, params=dict_1)
# print(resp.html.xpath('//title/text()'))


# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# ua = UserAgent()
# session = HTMLSession()
#
#
# start_url = 'https://u.y.qq.com/cgi-bin/musics.fcg'
# i = 1
# dict_1 = {
#     '-': 'getUCGI2696951322967065',
#     'g_tk': '5381',
#     # js逆向之请求参数的逆向
#     'sign': 'zzax9lndmk1v2y2uq31a4bb609c7b78275ed2b8d0ec78fbb7',
#     'loginUin': '0',
#     'hostUin': '0',
#     'format': 'json',
#     'inCharset': 'utf8',
#     'outCharset': 'utf-8',
#     'notice': '0',
#     'platform': 'yqq.json',
#     'needNewCode': '0',
#     'data': '{"comm":{"ct":24,"cv":0},"singerList":{"module":"Music.SingerListServer","method":"get_singer_list","param":{"area":-100,"sex":-100,"genre":-100,"index":-100,"sin":80,"cur_page":page_data}}}'.replace('page_data', str(i))
# }
#
# response = session.get(start_url, params=dict_1).json()
# print(response)

# 安居客房源信息爬取

# 0.将需要爬取的数据爬下来之后，进入第1步
# 1.将待爬取的数据通过文本的形式保存在本地  取名为A文件
# 2.每爬取一个，在A文件中删除相关数据
# 3.从第二次运行开始，判断有没有A文件
#
# for i in range(1, 2777):
#     url = f'https://www.adoutu.com/picture/list/{i}'
#     with open('1.txt', 'a+')as f:
#         f.write(url + '\t')
#
# with open('1.txt', 'r')as f1:
#     data = f1.read()
# list_1 = data.split('\t')
# list_1.remove('https://www.adoutu.com/picture/list/1')


# 1.成功做到手机抓包
# 2.微信访问公众号
# 3.观察判断抓包工具抓取的包，找到响应有公众号文章内容的包

# 爬取了京东80%电商商品信息
# 分布式去爬取的

# 淘宝：根据访问频率做的反爬
#













