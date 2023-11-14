# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 简单的图片文字识别：

# from PIL import Image
# from pytesseract import pytesseract
# text=pytesseract.image_to_string(Image.open('shitu1.png'),lang='chi_sim') # lang='chi_sim':识别为中文
# print(text)
#
# # CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
# # tesseract_cmd = 'tesseract'
# tesseract_cmd = 'D:\python_learn\Tesseract-OCR\tesseract.exe'

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

# 尖叫数据可用用户信息：
# AppCode：	2414B1DBA6CFC171867486CE13EA1080
# AppKey：	AKIDdc5aaadbb10d6d2cec9b53b7d9f17b83
# AppSecret：	9988da07b8b84f855c4d733a7cc88e3e


# 尖叫数据python请求代码示例：

# import urllib, urllib2, sys
#
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

# 他们使用的是urllib，非常麻烦，我们直接使用request-html:

# 导包：

# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# import base64
# ua = UserAgent()
# session = HTMLSession()
# with open('6624.jpg', 'rb')as f: # 保存图片，二进制写入
#     img_data = f.read() # 读取这张图片
#     base64_data = base64.b64encode(img_data).decode() # 使用base_64来接收加密之后的内容
#     # 传入img_data,使用decode()方法
#     # print(base64_data) # 打印观察一下加密的数据长什么样子，把下面的代码先注释一下
#     # 通过打印的加密数据可知，加密数据这个步骤已经处理好了
#     # 我们现在可以直接把base64_data放到v_pic那
#     # 那么现在base、data、headers、url都已经有了，现在就是发送请求获取响应了
#
# # 构造请求头(headers)：
# data = {
#     'v_pic': base64_data,
#     'v_type': 'n4' # 因为我们现在要识别图片验证码5374，根据请求提示，四位纯数字对应验证码类型为n4
#                 # 所以，v_type为n4
# }
# headers = {
#     'AppCode': '2414B1DBA6CFC171867486CE13EA1080',
#     'AppKey': 'AKIDdc5aaadbb10d6d2cec9b53b7d9f17b83',
#     'AppSecret': '9988da07b8b84f855c4d733a7cc88e3e',
#     'user-agent': 'ua.chrome'
# }
# # 向上面一样，我们把用户信息都添加在headers里面
# # 起始的url地址：
# start_url = 'http://apigateway.jianjiaoshuju.com/api/v_1/yzm.html'
#
# # 发送请求，获取响应：（请求类型与上述代码示例保持一致）
# # 因为我们要传递过去一张图片，所以应该是post请求，还需要一个data={}
# # 下面我们在headers上面构造一下data（根据尖叫数据的请求参数构造）
# # 同时根据尖叫数据请求头提示，我们导入自带包base64（图片加密验证码）
# response = session.post(start_url, headers=headers, data=data) # 传入所需参数
# print(response.json())
# # 通过打印响应结果可发现，返回的有404，所以可能我们的url有问题
# # 这时候，我们更换一下请求的url地址，对尖叫数据提供的接口url发送请求
# # 因为接口地址下面说明了返回的是json数据，所以我们把response方法里面的content.decode()换为
# # .json()
# # 再次打印,识别成功！
#
# 爬虫定时任务：
# 商品秒杀
# 定时秒杀

from urllib.parse import quote
import requests, os

class TBSpider(object): # 创建贴吧爬虫类
    """os.getcwd() 获取文件当前路径"""
    os_path = os.getcwd() + '/贴吧/' # 保存路径
    if not os.path.exists(os_path):
        """判断此路径是否存在，不存在就创建"""
        os.mkdir(os_path)

    def __init__(self):
        """
        初始化数据
        """
        self.title = input('请输入要爬取的贴吧标题：') # 要爬取的贴吧标题
        self.page = input('请输入要爬取的页数：') # 要爬取的页数
    def parse_start_url(self):
        """
        1.准备起始的url地址
        :return:
        """
        title = quote(self.title)
        for page in range(int(self.page)):
            start_url = f'https://tieba.baidu.com/f?kw={title}&ie=utf-8&pn={page*50}'
            # 循环url地址，花括号拼接title、page
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
        print(f'{self.title}贴吧===第{page + 1}页保存完成===logging！！！')


# 1.APScheduler-BackgroundScheduler的基本用法
# 导包：（包不用记，用到直接搬）

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
import time

#
 # 1.定义执行器
executors = {
    # 线程池
    'default': ThreadPoolExecutor(max_workers=10) # 同一时间最多可以有十个线程
}

# # 2.创建调度器
scheduler = BackgroundScheduler(executors=executors)
# 创建调度器（scheduler）会有一个函数（executors）来指定执行器（executors）执行函数
#
#
# # 3.定义定时任务函数（爬虫任务函数）
# # 爬虫任务函数
def print_test():
# 放入贴吧爬虫
    t = TBSpider()
    t.parse_start_url()
#
# # 4.添加定时任务
scheduler.add_job(print_test, 'interval', seconds=3) # seconds=3：每隔三秒执行一次（必须结合for循环才能运行）
# interval 在某个时间范围内间隔多长时间执行一次
# # 5.启动调度器，不阻塞
scheduler.start()
#
# # 6.手动添加代码（for循环），防止程序退出，相当于阻塞的角色
# # 执行5遍，3s执行一次，for循环速度快，不添加睡眠，定时程序不执行
for i in range(5):
    time.sleep(3)


# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.executors.pool import ProcessPoolExecutor
# # # 1.定义执行器
# executors = {
#     # default表示执行定时任务时，使用进程的方式
#     # 3表示在同一时刻，最多只有3个进程同时执行
#     'default': ProcessPoolExecutor(3)
# }
# # 2.使用上面的执行器，创建调度管理对象，使用单独运行的方式
# scheduler = BlockingScheduler(executors=executors)
#
# #
# # # 3.定义定时任务函数
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
# scheduler.add_job(print_test,
#                   'interval',
#                   seconds=3,
#                   start_date='2021-3-23 21:39:40',
#                   end_date='2021-3-23 21:40:00')
#
# if __name__ == '__main__':
#     scheduler.start()
#
# """
# OCR:识别精准度不高，打码平台
# """
#
# """IP代理"""
#
# # -*- coding: utf-8 -*-
#
# """
# 使用requests请求代理服务器
# 请求http和https网页均适用
# """
#
# import requests
# #
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


