# !/usr/bin/env python
# -*- coding: utf-8 -*-


# 课题：多进程与爬虫

# 1.应用场景
# 什么是进程？
# 资源分配和调度的基本单位

# 2.进程讲解
# 导入模块：
# from multiprocessing import Process
# import time
# def index(num):
#     start_time = time.time()
#     for i in range(num):
#         print('结果是：', i)
#     end_time = time.time()
#     print(start_time - end_time)
#
# def func(num):
#     Process(target=index, args=(num,)).start()
#     Process(target=index, kwargs={'num': num}).start()
#
# if __name__ == '__main__':
#     # 进程创建
#     # 进程之间没有任何关联
#     Process(target=index, args=(num,)).start()
#     Process(target=index, kwargs={'num': num}).start()
#     func(3)
#
# # 3.进程队列
#
# from multiprocessing import Process
# from multiprocessing import JoinableQueue as Queue
#
# class Love(object):
#     def __init__(self):
#         # 创建队列
#         self.q = Queue()
#
#     def parse_data(self):
#         # 功能：给队列添加任务
#         #:return:
#
#         data = '第{}天-----阿姨洗的路'
#         for i in range(1, 101):
#             self.q.put(data.format(i))
#
#     def func_1(self):
#         # 从队列中，取出任务
#         #:return:
#         while True:
#             for i in range(1, 101):
#                 result = self.q.get()
#                 print(result)
#                 # join的等待信号
#                 #是队列数-1
#                 self.q.task_done()
#     def run(self):
#         # 启动函数
#         # :return:
#         m1 = Process(target=self.parse_data()) # m1:发布外包单
#         m2 = Process(target=self.func_1()) # m2:接收外包单
#         m1.start()
#         # 设置守护进程：因为m2是死循环，设置守护进程的原因就在于我们需要让m1结束，m2跟着结束
#         # 即只在需要的时候才会启动，完成任务后就自动接收
#         m2.daemon = True
#         m2.start()
#         #
#         m1.join()
#
#     if __name__ == '__main__':
#         love = Love()
#         love.run()
#
#
# # 4.进程池
#
# from multiprocessing import Pool
# import time, random, os
#
# def worker(msg):
#     start_time = time.time()
#     print('%s开始执行，进程编号为%d' % (msg, os.getpid()))
#     time.sleep(random.random() * 2)
#     print('================')
#     print(random.random() * 2)
#     stop_time = time.time()
#     print(msg, '执行完毕，花费时间：%0.2f' % (start_time-stop_time))
#
#
# if __name__ == '__main__':
#     # 创建一个最大进程数量为3的进程池
#     po = Pool(3)
#     for i in range(0, 10):
#         # apply_async:非阻塞的形式运行我们的进程，
#         # 进程之间没有联系 --- 进程不共享全局变量
#         po.apply_async(worker, args=(i,))
#     print('开启---')
#     po.close() # 关闭：关闭进程池，关闭之后，不会再接受新的请求了
#     po.join() # 等待进程池中所有进程执行完毕
#     print('关闭---')


# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# import re, json
# session = HTMLSession()
#
# start_url = 'https://lol.qq.com/act/a20170926preseason/data/cn/runes.json'
# response = session.get(start_url)
#
# with open('1.json', 'w', encoding='utf-8')as f:
#     f.write(response.content.decode())

# 技能屏障的url：//ossweb-img.qq.com/images/lol/img/spell/SummonerBarrier.png

# url = 'https://lol.qq.com/biz/hero/summoner.js'
# 通过搜索查找到的关于hero的summoner.js链接

# response = session.get(url) # 传入url

# print(response.content.decode())

# data = re.findall('LOLsummonerjs=(.*?);', response.content.decode())[0] # 使用正则匹配,data接收

# print(data)
# 通过打印结果可知，大字典已经成功匹配出来，然后我们使用下标

# print(json.loads(data), type(json.loads(data))) # 使用json.loads(data)将json转换为python数据，同时使用type查看数据类型

# 英雄url https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js

# url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
#
# response = session.get(url) # 传入url
#
# response_json = response.json()
#
# print(response_json)

# 完整代码：(使用面向对象）

# 导入模块
# from multiprocessing import Process # 多进程模块
# from requests_html import HTMLSession # requests_html模块
# from fake_useragent import UserAgent # fake：假的
# import jsonpath, os
# session = HTMLSession()
# ua = UserAgent() # ua就一个UserAgent()就行
#
# class LOL(object): # 创建类
#     def __init__(self): # 定义类初始化
#         self.start_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
#         # 获取所有英雄id的url,使用heroList和hero_list.js来接收所有英雄的id
#         self.p_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
#         # 拼接英雄详情url地址，使用{}来接收拼接的英雄详情url地址
#
#     def parse_url(self): # 定义解析url
#         """
#         #         提取c，提取英雄的名称
#         #         :return: item_id_list, name_list
#         #         """
#         response_json = session.get(url=self.start_url).json()
#         # 接收请求起始url的响应，获取json数据
#         item_id_list = jsonpath.jsonpath(response_json, '$..heroId')
#         # 也可以这样传入：
#         # self.parse_item(item_id_list)
#         # 通过jsonPath提取英雄的id
#         return item_id_list
#         # return id后需要有东西接收item_id_list，因此，我们在后面写了：item_id_list = self.parse_url()来做调用，
#         # 然后传递到self.parse_item(item_id_list)中
#         # 返回英雄id
#
#     def parse_item(self, item_id_list):
# #         """
# #         json数据的解析
# #         :param item_id_list: 英雄的id列表
# #         """
#           for id in item_id_list: # for循环遍历id列表
#              referer = 'https://lol.qq.com/data/info-defail.shtml?id={}'.format(id)
#              # url地址拼接
#              headers = {
#                  "user-agent": ua.chrome,
#                  "referer": referer
#              }
#              # 为防止反扒，增加一个headers，ua，referer
#              # 然后获取referer的url地址所对应的json数据，即英雄详情数据
#              # 获取英雄详情数据：
#              name_json = session.get(url=self.p_url.format(id), headers=headers).json()
#              # print(name_json)
#              # 电脑版图片
#              # 通过jsonPath提取电脑版图片
#              win_img_list = jsonpath.jsonpath(name_json, '$..mainImg')
#              # 手机版图片
#              # 通过jsonPath提取手机版图片
#              phone_img_list = jsonpath.jsonpath(name_json, '$..loadingImg')
#              # print(win_img_list)
#              # print(phone_img_list)
#              # 因为返回的是图片列表，很可能有多个，所以不用下标处理
#              # 创建文件夹的名称   英雄的名称
#              name = jsonpath.jsonpath(name_json, '$..name')[0]
#              # 提取皮肤的名称
#              print(name)
#              print('文件夹创建中-----logging-----')
#              os_path = os.getcwd() + '/' + name + '/' # 文件路径，文件夹创建
#              if not os.path.exists(os_path): # 没有就创建：
#                  os.mkdir(os_path)
#              # 皮肤图片列表
#              # 列表下标操作，过滤第一个数据
#              name_list_data = jsonpath.jsonpath(name_json, '$..name')[1::]
#              # 根据英雄皮肤名称分类存储
#              self.process_run(phone_img_list, win_img_list, os_path, name_list_data)
#              # 将上面几个图片列表、路径、文件名称传递到process_run方法中，下面在process_run方法中会进行进程的分类
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
#         # 两个线程同时运行：
#         Process(target=self.save_data, args=(win_img_list, os_path, name_list_data, 1)).start()
#         Process(target=self.save_data, args=(phone_img_list, os_path, name_list_data, 2)).start()
#
#     def run(self):
#         # 传参：
#         item_id_list = self.parse_url()
#         self.parse_item(item_id_list)
#
# if __name__ == '__main__':
#     lol = LOL()
#     lol.run()

# 断点续爬讲解：(爱斗图)

# 0.将需要爬取的数据爬下来之后，进入第1步
# 1.将待爬取的数据通过文本的形式保存在本地  取名为A文件
# 2.每爬取一个，在A文件中删除相关数据
# 3.从第二次运行开始，判断有没有A文件

for i in range(1, 2777): # 循环爱斗图所有图片页数
    url = f'http://www.adoutu.com/article/list/{i}' # 爱斗图url，{i}接收页码，实现所有的翻页爬取
    # f'http://www.adoutu.com/article/list/{i}':f:格式化字符串
    with open('1.txt', 'a+')as f: # 文件追加写入（不覆盖）保存：a+
    # 通过with open保存url地址
        f.write(url + '\t')
        # 传入我们的url，还要加上一个\t


with open('1.txt', 'r')as f1: # 文件读取，更新页码用于断点续爬，判断有没有A文件
    data = f1.read()
list_1 = data.split('\t') # 以换行分割各链接
list_1.remove('https://www.adoutu.com/picture/list/1') # 删除已经爬取的第一页
# 在A文件中删除相关数据

# 微信公众号爬取开发思路：
# 1.成功做到手机抓包
# 2.微信访问公众号
# 3.观察判断抓包工具抓取的包，找到响应有公众号文章内容的包

# 爬虫B课：
# 京东爬取：
# 爬取了京东80%电商商品信息
# 分布式去爬取的

# 淘宝爬取：
# 淘宝：根据访问频率做的反爬
#











