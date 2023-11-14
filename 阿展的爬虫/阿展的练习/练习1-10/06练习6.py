# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 课题：数据提取之正则表达式

# 1.需要掌握的正则方法
# 正则匹配手机号码

# 15738108997

# hdgshv15738108997rewrre
import re
# str_1 = '15738108997'
# str_2 = 'hdgshv15738108997rewrre'
# 第一个参数：正则规则，第二个参数：匹配对象
# result = re.findall(r'^1[3-9]\d{9}$', str_1)
# 上述匹配代码解释：使用result接收匹配结果,re.findall:正则匹配所有
# ^:匹配除去所列首个字符外的所有字符; ^\d表示必须以数字开头。
# | 将两个规则并列起来，注意是匹配两边所有的规则
# r:要匹配 ‘I have a dog’或’I have a cat’，需要写成r’I have a (?:dog|cat)’ ，而不能写成 r’I have a dog|cat’
# 因为手机号的规则是：以数字1开头，第二位数字为3-9，共11位，还剩下9位，所以匹配代码为：
# result = re.findall(r'^1[3-9]\d{9}$', str_1)
# {9}:剩下的9位，\d：匹配数字,这是一个以’\’开头的转义字符，’\d’表示匹配一个数字，即等价于[0-9]
# $:匹配字符串的尾部字符  \d$表示必须以数字结束
# \d$符中间的数字必须用列表符{}包起来
# print(result)

# result = re.findall(r'\d+', str_2)
# 19 ‘*?’ ‘+?’ ‘??’ 最小匹配
# ‘*’ ‘+’ ‘?’通常都是尽可能多的匹配字符（贪婪匹配）。有时候我们希望它尽可能少的匹配。
# 例子 re.match(r'^(\d+)(0*)$', '102300').groups()  #('102300', '')
# re.match(r'^(\d+?)(0*)$', '102300').groups() #('1023', '00')
# print(result)

# findall: 找所有
# str_1 = '<meta http-equiv="content-type" content="text/html;charset=utf-8"/>adacc/sd/sdef/24'
#
# result = re.findall('="(.*?)"', str_1)
# print(result)

# match 从头再找一个
# result = re.match('<meta http-equiv="content-type" content="(.*?)"', str_1).groups()
# print(result)

# """group的用法
# 正则表达式中，group()用来提出分组截获的字符串，（）用来分组
# 如：
# import re
# a = "123abc456"
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,同group（）就是匹配正则表达式整体结果
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))    #123 第一个括号匹配部分
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))    #abc 第二个括号匹配部分
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))    #456 第三个括号匹配部分
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).groups())    #('123', 'abc', '456')
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).groupdict()) #{} 为空？
# m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# m.groupdict()     # {'extension': 'com', 'user': 'myname', 'website': 'hackerrank'}

# group：连带规则一起返回给我们
# groups: 返回匹配规则(.*?)括号里面的内容

# search 找到一个就返回
# result = re.search('="(.*?)"', str_1).groups()
# print(result)
# 返回的是一个元组

# 转义：
# 使用转义一般在前面加上r
# 为了便于区分，我们只在一个或两个前面加上r
# str_1 = r'123456\n789\t123'
# str_2 = '123456\n789\t123'
# str_3 = '123456\\n789\\123'
# print(str_1)

# 结论：我们可以通过字符串前面加一个r或者斜杠来进行内容的转义
# 转义常常用在路径操作中

# 案例:微博评论爬取

# 外包需求，爬取微博评论
# 微博示例链接：
# 大疆、华为云
# https://weibo.com/DJIChina?is_all=1
# https://weibo.com/hwcloud?refer_flag=1005050003_&is_hot=1#1615358404351

# 评论数据包（第一页）
# 华为云评论链接第一页：
# https://m.weibo.cn/comments/hotflow?id=4591143973292417&mid=4591143973292417&max_id_type=0
# 华为云评论链接第二页：
# https://m.weibo.cn/comments/hotflow?id=4591143973292417&mid=4591143973292417&max_id=138849035303209&max_id_type=0

# 可以发现：下一页的max_id在上一页的响应中

# 由上可发现，要爬取任意微博的评论，只需替换微博评论链接里的id即可

# 总结开发思路：
# 1.进入某个明星的微博首页
# 2.观察某一条微博动态的评论
# 3.点击查看更多，进入到微博正文详情页
# 4.进入手机模式访问
# 5.去观察异步加载评论包 ： hotflow

# 开发思路：
# 首先，我们创建一个类，以面向对象的方式开发

# 我们来导一下包：
from requests_html import HTMLSession
from jsonpath import jsonpath # 导入jsonpath帮助我们查找mid
import os, xlwt, xlrd, random
from xlutils.copy import copy
session = HTMLSession()

class WbSpider(object): # 创建一个微博爬虫的类
    # 放入ua大列表：
    USER_AGENT = ['Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Hot Lingo 2.0)',
                  'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3451.0 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:57.0) Gecko/20100101 Firefox/57.0',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2999.0 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.70 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174',
                  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.1.4322; MS-RTC LM 8; InfoPath.2; Tablet PC 2.0)',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.61',
                  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; .NET4.0C; CIBA; Maxthon 2.0)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1',
                  'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; Touch; MASMJS)',
                  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Hot Lingo 2.0)',
                  'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3451.0 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:57.0) Gecko/20100101 Firefox/57.0',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2999.0 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.70 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174',
                  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.1.4322; MS-RTC LM 8; InfoPath.2; Tablet PC 2.0)',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.61',
                  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; .NET4.0C; CIBA; Maxthon 2.0)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1',
                  'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; Touch; MASMJS)',
                  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4093.3 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Swurl) Chrome/77.0.3865.120 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                  'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Goanna/4.7 Firefox/68.0 PaleMoon/28.16.0',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:75.0) Gecko/20100101 Firefox/75.0',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/91.0.146 Chrome/85.0.4183.146 Safari/537.36',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 VivoBrowser/8.4.72.0 Chrome/62.0.3202.84',
                  'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:83.0) Gecko/20100101 Firefox/83.0',
                  'Mozilla/5.0 (X11; CrOS x86_64 13505.63.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:68.0) Gecko/20100101 Firefox/68.0',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.400',
                  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                  ]

    def __init__(self): # 定义一个初始化函数

    # 1.准备起始的url地址
        # 要爬取的微博评论的地址：
        self.start_url = 'https://m.weibo.cn/comments/hotflow?id=4613490167777746&mid=4613490167777746&max_id_type=0'
        # 构造headers：
        # 将评论地址中request headers中有用的部分复制过来：
        self.headers = {
             'cookie': 'WEIBOCN_FROM=1110005030; loginScene=102003; SUB=_2A25NQxtiDeRhGeFL61AR8SrEzTyIHXVuz6UqrDV6PUJbkdAKLUr3kW1NQrcPFCffc-yk7fH6nW110ZylyUS7C_xh; _T_WM=85509930160; XSRF-TOKEN=e9287f; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4609229132925240%26luicode%3D20000061%26lfid%3D4609229132925240%26uicode%3D20000061%26fid%3D4609229132925240',
             'Referer': 'https: //m.weibo.cn/status/JCf4pdOvv?filter = hot & root_comment_id = 0 & type = comment & jumpfrom = weibocom',
            # referer：告诉服务器上一个网页来自哪里
             'User - Agent':'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.182Safari / 537.36',
             'x-requested-with': 'XMLHttpRequest',
             'x-xsrf-token': '35c0ad'
            # token：代表浏览器认证
        }
    def parse_start_url(self): # 定义一个解析起始的url地址的函数
        # 增加条件：max_id的默认值为空，
        # 若jsonpath没有提取到max_id：他会返回False
        # 所以我们这时要在max_id = jsonpath(response_json, '$..max_id')[0]下面加一个判断：
        # if max_id： ,就执行next_url = f'https://m.weibo.cn/comments/hotflow?id=4591143973292417&mid=4591143973292417&max_id={max_id}&max_id_type=0'
        # 若为假，就退出。

    # 2.发送求，获取响应，解析起始的url地址
    # 因为我们使用的是response-html,所以下面我们使用response = response.session()方法：
    # 因为着一个异步加载包响应的是json数据，所以我们使用response_json = session.get(self.start_url, headers = self.headers).json():
        response_json = session.get(self.start_url, headers=self.headers).json()
        max_id = jsonpath(response_json, '$..max_id')[0] # 使用下标提取max_id
        self.parse_response_data(max_id)
        # 上面一行是增加的调用，然后我们可以在def parse_response_data(self, max_id):的下面执行递归操作
        # if max_id:
        #    print(max_id)
    # 爬取下一页评论需要进行字符串拼接：
         #  next_url = f'https://m.weibo.cn/comments/hotflow?id=4591143973292417&mid=4591143973292417&max_id={max_id}&max_id_type=0'
        # else:
        #     return
    # 那么，要是连续执行翻页呢？
    # 我们可以使用递归的方法来实现循环的效果，
    # 要使用递归，我们就要先搞清楚递归的出口在哪里，
    # 那么，递归加在哪里合适呢？
    # 我们可以在max_id = jsonpath(response_json, '$..max_id')[0]的下面增加调用def parse_response_data(self, max_id):的方法，
    # 翻页的url地址我们已经有了，那么，接下来我们怎样组装请求发送呢？
    # 下面我们就要重复使用parse_start_url，那么max_id就需要重复被接收，重复执行max_id = jsonpath(response_json, '$..max_id')[0]操作
        # print(response_json) # 这时候我们打印测试一下
    def parse_response_data(self, max_id):
        """
        3.解析响应，数据提取
        :return:
        """
        headers = {
            'cookie': 'WEIBOCN_FROM=1110005030; loginScene=102003; SUB=_2A25NQxtiDeRhGeFL61AR8SrEzTyIHXVuz6UqrDV6PUJbkdAKLUr3kW1NQrcPFCffc-yk7fH6nW110ZylyUS7C_xh; _T_WM=85509930160; XSRF-TOKEN=e9287f; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4609229132925240%26luicode%3D20000061%26lfid%3D4609229132925240%26uicode%3D20000061%26fid%3D4609229132925240',
            'Referer': 'https: //m.weibo.cn/status/JCf4pdOvv?filter = hot & root_comment_id = 0 & type = comment & jumpfrom = weibocom',
            # referer：告诉服务器上一个网页来自哪里
            'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.182Safari / 537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': '35c0ad'
        # token：代表浏览器认证
        }
# 递归部分：
        try:
        # 首先是url地址的拼接，判断机制同上，
           next_url = f'https://m.weibo.cn/comments/hotflow?id=4613490167777746&mid=4613490167777746&max_id=157541876424563&max_id_type=0'
        # 拼接之后继续发送请求，发送请求之后提取max_id，
        # 下面是继续发送请求：
           response_json = session.get(next_url, headers=headers).json()
        # 翻页的id
           max_id = jsonpath(response_json, '$..max_id')[0]
        # 上面一行里面包含评论的内容，接下来要获取评论：
        # 获取评论：
        # 通过观察网页源码，我们知道评论的内容就在data大列表里面，所以我们要在data里面提取数据：
        # 我们使用content_dada来接收评论：
           content_data = response_json['data']['data'] # 通过key值取value值的方法，使用两个data
           print(content_data)
        # 数据保存
           self.save_data(content_data) # 调用保存方法，保存评论
        # max_id需要继续调用def parse_response_data(self, max_id):方法：
           self.parse_response_data(max_id) # 自己调用自己
           print('开始获取下一页====logging')

# 到这里就是一个递归的机制
# 递归：函数自己调用自己本身，需要有出口，这里的出口就是max_id为false时，执行else、return，递归终止

        except Exception as e:
            print('评论爬完了，终止程序') # 增加终止提示
            return
    def save_data(self, content_data):

        """
        4.数据的保存
        :return:
        """

        for content in content_data:
            item = {}
        # 粉丝id
            fs_id = content['user']['id']
            item['粉丝id'] = fs_id

        # 评论内容text
        text = jsonpath(content, '$..text')[0]
        # 通过观察运行结果，发现打印的span标签内的内容过多，所以，我们需要加入span标签文本打印限制
        # 我们可以使用正则表达式的替换方法，把我们不需要的span标签文本替换掉
        if 'span' in text:
            text = re.sub('<span .*?</span>', ''.join(re.findall('alt=(.*?)', text)[0]), text)
        # 上述替换解释：将<span>标签内的内容替换为''(空)
        # .*?:正则表达式中最小匹配模式，匹配到一个就往下进行
        item['评论内容'] = text # 字典的键值对，没有就创建，存在就修改


        # 粉丝昵称fs_name
        fs_name = jsonpath(content, '$..screen_name')[0]
        item['粉丝昵称'] = fs_name
        # 粉丝性别
        gender = jsonpath(content, '$..gennder')[0]
        item['粉丝性别'] = gender
        list_1 = [fs_id, text, fs_name, gender]
        dict_1 = {
            '基本详情':list_1
        }
        self.save_excel(dict_1)


    def save_excel(self, data):
        # data = {
            #     '基本详情': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
            # }
        os_path_1 = os.getcwd() + '/微博评论/'
        if not os.path.exists(os_path_1):
            os.mkdir(os_path_1)
        # os_path = os_path_1 + self.os_path_name + '.xls'
        os_path = os_path_1 + '微博评论.xls'
        if not os.path.exists(os_path):
            # 创建新的workbook（其实就是创建新的excel）
            workbook = xlwt.Workbook(encoding='utf-8')
            # 创建新的sheet表
            worksheet1 = workbook.add_sheet("基本详情", cell_overwrite_ok=True)
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
            excel_data_1 = ('粉丝id', '评论内容', '粉丝昵称', '粉丝性别')
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
    Wb = WbSpider()
    Wb.parse_start_url()

# 发现运行报错，我们直接将if，else条件换成try、except Exception异常捕捉

# if __name__ == '__main__':
#     Wb = WbSpider()
#     Wb.parse_start_url()