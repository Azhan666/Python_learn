"""
课题：反爬虫处理
"""

"""反爬IP代理池"""
# ip1, ip2, ip3...
# 限制

# ip  pv 次数
# 暴增
# 异常
# 用户，爬虫
# 误差
# 得不偿失
# 宁可错杀，不放过
# 反爬策略不足
# 正常的
from pytesseract import pytesseract

"""IP代理"""
# 软件：baacloud
# https://www.baacloud34.com/modules/register.php
# 小舒代理：http://www.xsdaili.cn/
# 快代理：https://www.kuaidaili.com/

# 识别中文
"""2.图片识别OCR与打码平台的使用"""
"""OCR识别引擎安装"""
"""
步骤：1.库的安装pip install pillow -i http://mirrors.aliyun.com/pypi/simple
        pip install PIL 安装报错切换  c 这是解释器版本的问题
        pip install pytesseract
     2.识别引擎tesseract-ocr下载
        版本选择：https://digi.bib.uni-mannheim.de/tesseract/
        配置环境变量
            1.系统变量path 添加ocr安装路径 (例：D:\tesseract\Tesseract-OCR)
            2.系统变量创建新变量
                变量名：TESSDATA_PREFIX
                变量值：引擎路径 (例：D:\tesseract\Tesseract-OCR\tessdata)
     3.修改pytesseract源码的文件路径
        from pytesseract import pytesseract
        ctrl + 鼠标左键点击后面的(第二个)进入源码
        在第37行位置,将安装的tesseract关联
     4.重启pycharm,若失效,重启电脑，让电脑重新加载系统变量
"""


# import pytesseract
# from PIL import Image
# text = pytesseract.image_to_string(Image.open('2.jpg'), lang='chi_sim')
# print(text)

# 讲效率的
"""
图片识别引擎的使用扩展
其他OCR平台
微软Azure图像识别：
        https://azure.microsoft.com/zh-cn/services/cognitive-services/computer-vi
有道智云文字识别：
        http://aidemo.youdao.com/ocrdemo
阿里云图文识别：
        https://www.aliyun.com/product/cdi/
腾讯OCR文字识别：
        https://cloud.tencent.com/product/ocr
"""


"""打码平台的使用"""
"""
网上可以搜索到很多打码平台，课程以超级鹰打码平台主线教学
超级鹰打码平台
http://www.jianjiaoshuju.com/
流程：注册登录 --> 滑动到最下面，点击图片验证码识别 --> 找到对应的接口地址,将url地址复制
     点击下方的请求示例，代码复制，只需做代码参数的修改即可
"""
"""掌握打码平台的对接"""
# 学会掌握，看开发文档写代码

"""
AppCode：	20B9054575C6917DE9BC05175DDAD2D2
AppKey：	AKIDa0fac224bccad10c4ea86d9b73bd4f62
AppSecret：	a5a51b5a2cff7dcd5fdc9cd82d11e7bd
"""

# import urllib, urllib2, sys

# host = 'http://apigateway.jianjiaoshuju.com'
# path = '/api/v_1/yzm.html'
# method = 'POST'
# appcode = '你自己的AppCode'
# appKey = '你自己的AppKey'
# appSecret = '你自己的AppSecret'
# querys = ''
# bodys = {}
# url = host + path
#
# bodys['v_pic'] = '''v_pic'''
# bodys['v_type'] = '''v_type'''
# post_data = urllib.urlencode(bodys)
# request = urllib2.Request(url, post_data)
# request.add_header('appcode', appcode)
# request.add_header('appKey', appKey)
# request.add_header('appSecret', appSecret)
# # //根据API的要求，定义相对应的Content-Type
# request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
# response = urllib2.urlopen(request)
# content = response.read()
# if (content):
#     print(content)




# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# import base64
# ua = UserAgent()
# session = HTMLSession()
# with open('7.jpg', 'rb')as f:
#     img_data = f.read()
#     base64_data = base64.b64encode(img_data).decode()
#     # print(base64_data)
#
# data = {
#     'v_pic': base64_data,
#     'v_type': 'js'
# }
# headers = {
#     'AppCode': '20B9054575C6917DE9BC05175DDAD2D2',
#     'AppKey': 'AKIDa0fac224bccad10c4ea86d9b73bd4f62',
#     'AppSecret': 'a5a51b5a2cff7dcd5fdc9cd82d11e7bd',
#     'user-agent': ua.chrome
# }
# start_url = 'http://apigateway.jianjiaoshuju.com/api/v_1/fzyzm.html'
#
# response = session.post(start_url, headers=headers, data=data)
# print(response.json())

# 在凌晨3点，执行这个爬虫
# 商品秒杀
# 9：25
# 9：24：
from urllib.parse import quote
import requests, os


class TBSpider(object):
    """os.getcwd() 获取文件当前路径"""
    os_path = os.getcwd() + '/贴吧/'
    if not os.path.exists(os_path):
        """判断此路径是否存在，不存在就创建"""
        os.mkdir(os_path)

    def __init__(self):
        """
        初始化数据
        """
        self.title = '奥迪'
        self.page = 5

    def parse_start_url(self):
        """
        1.准备起始的url地址
        :return:
        """
        title = quote(self.title)
        for page in range(int(self.page)):
            start_url = f'https://tieba.baidu.com/f?kw={title}&ie=utf-8&pn={page*50}'
            self.parse_start_response(start_url, page)

    def parse_start_response(self, start_url, page):
        """
        2.发送请求，获取响应
        :param start_url: 爬虫起始翻页的url地址
        :param page: 页码
        :return:
        """
        response = requests.get(start_url)
        self.parse_data(response, page)

    def parse_data(self, response, page):
        """
        3.解析响应，数据提取
        :param response: url地址的响应
        :param page: 页码
        :return:
        """
        data = response.content.decode()
        self.save_data(data, page)

    def save_data(self, data, page):
        """
        4.保存数据
        :return:
        """
        with open(self.os_path + self.title + str(page) + '.html', 'w', encoding='utf-8')as f:
            f.write(data)
        print(f'{self.title}贴吧====第{page + 1}页保存完成====logging！！！')



# 1.APScheduler-BackgroundScheduler的基本用法
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.executors.pool import ThreadPoolExecutor
# import time
#
# # 1.定义执行器
# executors = {
#     # 线程池
#     'default': ThreadPoolExecutor(max_workers=10)
# }
#
# # 2.创建调度器
# scheduler = BackgroundScheduler(executors=executors)
#
#
# # 3.定义定时任务函数
# # 爬虫任务函数
# def print_test():
#     t = TBSpider()
#     t.parse_start_url()
#
# # 4.添加定时任务
# scheduler.add_job(print_test, 'interval', seconds=3)
# # 5.启动调度器，不阻塞
# scheduler.start()
#
# # 6.手动添加代码，防止程序退出，相当于阻塞的角色
# # 执行5遍，3s执行一次，for循环速度快，不添加睡眠，定时程序不执行
# for i in range(5):
#     time.sleep(3)


# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.executors.pool import ProcessPoolExecutor
# # 1.定义执行器
# executors = {
#     # default表示执行定时任务时，使用进程的方式
#     # 3表示在同一时刻，最多只有3个进程同时执行
#     'default': ProcessPoolExecutor(3)
# }
# # 2.使用上面的执行器，创建调度管理对象，使用单独运行的方式
# scheduler = BlockingScheduler(executors=executors)
#
#
# # 3.定义定时任务函数
# def print_test():
#     print('定时任务执行开始')
#     # t = TBSpider()
#     # t.parse_start_url()
#     print('定时任务执行成功')
#     # main1()
#
#
# # 4.添加任务,使用date指定在某个时间执行
# # 使用run_date指定运行的时间
# # scheduler.add_job(print_test, 'date', run_date='2021-3-23 21:37:00')
#
# # 指定每天15：36运行
# scheduler.add_job(print_test, 'cron', hour=21, minute=42)
#
# # 使用interval 指定在开始时间到结束时间
# # 从start_date开始，到end_date结束，每隔3秒中执行一次
# # scheduler.add_job(print_test,
# #                   'interval',
# #                   seconds=3,
# #                   start_date='2021-3-23 21:39:40',
# #                   end_date='2021-3-23 21:40:00')
#
# if __name__ == '__main__':
#     scheduler.start()


"""
OCR:识别精准度不高，打码平台
"""

"""IP代理"""

# -*- coding: utf-8 -*-

"""
使用requests请求代理服务器
请求http和https网页均适用
"""

# import requests
#
# # 提取代理API接口，获取1个代理IP
# api_url = 'http://kps.kdlapi.com/api/getkps/?orderid=951650719969677&num=1&pt=1&sep=1'
# # 获取API接口返回的代理IP
# proxy_ip = requests.get(api_url).text
# print(proxy_ip)
# # 用户名密码认证(私密代理/独享代理)
# username = "s403411124"
# password = "80i9bdkq"
# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
# }
#
# # pro = {
# #     'http': 'http://42.193.123.159:16819',
# #     'https': 'https://42.193.123.159:16819'
# # }
#
# for i in range(1,3):
#     # 要访问的目标网页
#     target_url = f"http://www.dianping.com/changsha/ch45/g147p{i}"
#
#     headers = {
#         'Cookie': 'fspop=test; cy=344; cye=changsha; _lxsdk_cuid=1785da10d3eb5-0679debca6eca-5771031-144000-1785da10d3fc8; _lxsdk=1785da10d3eb5-0679debca6eca-5771031-144000-1785da10d3fc8; _hc.v=5aa1c48a-20bf-669a-d7a2-df00700db5b9.1616478539; s_ViewType=10; _dp.ac.v=30444106-7128-4d3b-aa24-0aec6ca8d51c; ctu=19741bb7ed2c3a472cfa3d5e93ef043d165e463bf905eec69cae5430096f4208; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1616478540,1616481656,1616508102; dper=082cc9f53967eb143f8a3e8c030df773a148d295f2403502b2e37c5f3b71b7de6ceb223f6b53d4dd84d5d0aad693c26acc7b1a900c597103e6da7fde051fecfe18ff3c7b0f7a8811de27c34fbed5df872a624ebee0bc8baa91a97a6d9ea94060; ll=7fd06e815b796be3df069dec7836c3df; ua=%E9%98%BF%E5%B0%94%E6%B3%95; uamo=16607440667; dplet=52eace30f6a15e06f3035850e86b7570; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1616508182; _lxsdk_s=1785f6422fd-362-d1-634%7C%7C85',
#         'Host': 'www.dianping.com',
#         'Referer': 'http://www.dianping.com/changsha/ch45/g147p2',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
#     }
#     # 使用代理IP发送请求
#     response = requests.get(target_url, proxies=proxies, headers=headers)
#
#     # 获取页面内容
#     if response.status_code == 200:
#         print(response.text)



















