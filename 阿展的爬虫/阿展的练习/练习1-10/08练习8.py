# !/usr/bin/env python
# -*- coding: utf-8 -*-

# python之urlencode()，quote()及unquote()：

# URL编码、解码原因：

# 通常如果一样东西需要编码，说明其并不适合直接传输。原因多种多样，如Size过大，包含隐私数据。对于Url来说，之所以要进行编码，是因为Url中有些字符会引起歧义。
#
# 例如，Url参数字符串中使用key = value键值对这样的形式来传参，键值对之间以 & 符号分隔，如 / s?q = abc & ie = utf - 8。如果你的value字符串中包含了 = 或者 &，那么势必会造成接收Url的服务器解析错误，因此必须将引起歧义的 & 和 = 符号进行转义，也就是对其进行编码。
#
# 字符串被当作url提交时会被自动进行url编码处理，在python里也有个urllib.urlencode的方法，可以很方便的把字典形式的参数进行url编码。当url地址含有中文或者“ / ”的时候，这是就需要用做urlencode一下编码转换。
#
# urlencode和quote：
# urlencode的参数是词典，它可以将key - value这样的键值对转换成我们想要的格式，将URL中的键值对以连接符 & 划分。如果你用的是python2. *，urlencode在urllib.urlencode。如果使用的是python3，urlencode在urllib.parse.urlencode。
#
# 1 import urllib.parse
#
# 2 data = {"name": "王尼玛", "age": "/", "addr": "abcdef"}
# 3 print(urllib.parse.urlencode(data))

# 结果：
#
# name = % E7 % 8E % 8B % E5 % B0 % BC % E7 % 8E % 9B & addr = abcdef & age = % 2F
# 1
# 如果只想对一个字符串进行urlencode转换，使用urllib提供的另外一个函数：quote()
#
# print(urllib.parse.quote("hahaha你好啊！"))
# 1
# 结果：
#
# hahaha % E4 % BD % A0 % E5 % A5 % BD % E5 % 95 % 8A % EF % BC % 81
# 1
# unquote：
# 对url进行解码，把类似"%xx"
# 的字符替换成单个字符，当urlencode之后的字符串传递过来之后，接收完毕解码使用urllib提供的unquote()
# 函数，注意没有urldecode()！若unquote方法接收到的参数类型是unicode，则返回的值类型也是unicode，只不过是把
# "%"
# 替换成了’\x’，明智的做法是使用str（）转换一下再用
#
# import urllib.parse
#
# data = {"name": "王尼玛", "age": "/", "addr": "abcdef"}
# print(urllib.parse.urlencode(data))
# print(urllib.parse.unquote("name=%E7%8E%8B%E5%B0%BC%E7%8E%9B&addr=abcdef&age=%2F"))
# print(urllib.parse.quote("hahaha你好啊！"))
# print(urllib.parse.unquote("hahaha%E4%BD%A0%E5%A5%BD%E5%95%8A%EF%BC%81"))

# 结果：
#
# name = % E7 % 8E % 8
# B % E5 % B0 % BC % E7 % 8E % 9
# B & addr = abcdef & age = % 2F
# name = 王尼玛 & addr = abcdef & age = /
# hahaha % E4 % BD % A0 % E5 % A5 % BD % E5 % 95 % 8
# A % EF % BC % 81
# hahaha你好啊！

# 在做解码的时候，看unquote()
# 这个函数的输出，是对应中文在gbk下的编码，在对比一下quote()
# 的结果不难发现，所谓的解码就是把字符串转成gbk编码，然后把\x替换成 %。如果你的终端是utf8编码的，那么要把结果再转成utf8输出，否则就乱码。
# 可以根据实际情况，自定义或者重写urlencode()、urldecode()
# 等函数。
#
# 注意：
# 如果是已经获得了Unicode类型的字符串，字符串内容是，quote过的，带百分号 % 的，比如：
# % E8 % BD % AC % E5 % 8F % 91 % E5 % BE % AE % E5 % 8D % 9A
# 而此处，想要获得对应的中文内容，则需要：
# 先去把当前的unicode字符串转换为普通的str
#
# quotedStringStrType = str(quotedStringUnicodeType)
#
# 再去通过urllib.unquote去解码，得到真正的中文内容
#
# urlunquotedOriginalStr = urllib.unquote(quotedStringStrType);
#
# 此处的最终解码得到的字符串是UTF - 8编码的。

# unicode - escape编码集，他是将unicode内存编码值直接存储
#
# # python3
#
# >> > s = '中国'
#
# >> > b = s.encode('unicode-escape')
#
# >> > b
#
# b'\\u4e2d\\u56fd'
#
# >> > c = b.decode('unicode-escape')
#
# >> > c
#
# '中国'
#
# logData.encode('GBK', 'ignore')
#
# showLog(logData.decode('utf8').encode('GBK'))

# decode('utf-8') 把 UTF-8 转化为 Unicode 编码

# encode('utf-8') 把 Unicode 转化为 UTF-8 编码

# 课题：数据提取之css选择器

# 1.CSS选择器的优势
# 稳定
# 在一个html页面，会根据css语法做一系列的demo操作
# 不改变html的css结构，可以不修改爬虫代码
# 微调，xpath标签结构就变得不一样了


"""2.CSS选择器的应用语法"""
# from fake_useragent import UserAgent
# # ua的替换
# ua = UserAgent()
# # 谷歌浏览器，火狐浏览器，ie
#
# print(ua.chrome)
#
# # Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36
# # Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
# # Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36
# print(ua.Safari)

# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# ua = UserAgent()
# session = HTMLSession()
#
# url = 'https://www.csdn.net'
#
# response = session.get(url)
#

# data = response.html.find('#floor-nav_62 > div > div > div.index_nav_center > ul > li:nth-child(11) > a', first=True)
# # 提取标签的文本信息
# # print(data.text)
# # 将标签的属性转换为字典结构
# # print(data.attrs)
# # 获取标签中所有的连接
# # print(data.links)


# print(data)


# https://wf.esf.fang.com/house/i32/    第2页
# https://wf.esf.fang.com/house/i31/    第1页

# https://wf.esf.fang.com/house/i350/?rfss=1-b0278f1794ba2c8870-06  第50页

# https://esf.fang.com/chushou/3_454420843.htm?channel=2,2&psid=1_1_80
#                     /chushou/3_454420843.htm?channel=2,2&psid=1_1_80

# 导包部分:
from requests_html import HTMLSession
from fake_useragent import UserAgent
import json
import re
ua = UserAgent()
session = HTMLSession()

# 构造headers：

headers = {
    'Cookie': 'city=wf; global_cookie=6l1ggx8pv0kiddj8c6thk174k17km92g9ws; __utma=147393320.596975187.1615720852.1615720852.1615720852.1; __utmc=147393320; __utmz=147393320.1615720852.1.1.utmcsr=wf.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; new_search_uid=ca76f7e6ff53feef31fe00c3d5059658; searchConN=1_1615721839_1114%5B%3A%7C%40%7C%3A%5Dd70e704ca42701a00354b66b7489620b; csrfToken=bexqfjtJ759cggksYMR2R7zg; g_sourcepage=esf_fy%5Elb_pc; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; unique_cookie=U_6l1ggx8pv0kiddj8c6thk174k17km92g9ws*18; __utmb=147393320.63.10.1615720852',
    'referer': 'http://search.fang.com/',
    'user-agent': ua.chrome
}

for page in range(1, 101):
    # 二手房翻页url  房源列表页
    start_url = f'https://esf.fang.com/house/i3{page}/' # 传入翻页数
    start_url_response = session.get(start_url, headers=headers)
    print(start_url_response.content.decode())
    # print(start_url_response.content.decode())
    # 提取房源详情页地址
    href_list = start_url_response.html.xpath(
        '//div[@class="shop_list shop_list_4"]/dl/dt/a/@href'
    )


    for url in href_list:
        dict_1 = {}
        next_url = 'https://esf.fang.com' + url
        response = session.get(next_url, headers=headers_1)
        # print(response.content.decode())
        # print(next_url_response.content.decode())
        # 房源配置信息
        config_dict = re.findall('pageConfig.ubp = (.*?);', response.content.decode())[0]
        # json.loads 将字符串形式的字典数据转化成字典
        config_dict_result = json.loads(config_dict)
        # print(config_dict_result, type(config_dict_result))
        # 房源标题
        title = response.html.xpath('//title/text()')[0]
        dict_1['房源标题'] = title
        #
        # 价格
        price = re.findall(r"housemoney:'(.*?)',", response.content.decode())
        price = ''.join(price)
        # print(price)
        dict_1['价格'] = price
        # 房子规格
        house_config = response.html.xpath('//div[@class="tt"]/text()')
        # print(house_config)
        house_cfg = house_config[0].replace('\n', '').replace(' ', '')
        dict_1['房子规格'] = house_cfg
        # 平米
        pm = house_config[1].replace('\n', '').replace(' ', '')
        dict_1['平米'] = pm
        # 平米价格
        pm_price = house_config[2].replace('\n', '').replace(' ', '')
        dict_1['平米价格'] = pm_price
        # 房子朝向
        cx = house_config[3].replace('\n', '').replace(' ', '')
        dict_1['房子朝向'] = cx
        # 楼层简介
        jz = house_config[4].replace('\n', '').replace(' ', '')
        dict_1['楼层简介'] = jz
        # 装修
        zx = house_config[5].replace('\n', '').replace(' ', '')
        #         dict_1['装修'] = zx
        # 小区
        xq = response.html.xpath('//div[@class="title rel"]/text()')
        xq = [i for i in xq if i != '\n']
        xq = xq[0].replace('\n', '').replace(' ', '')
        dict_1['小区名称'] = xq[:-2]
        # 地址
        addrs = response.html.xpath('//div[@id="address"]/a/text()')
        dict_1['地址'] = '-'.join(addrs).replace('\n', '').replace(' ', '')
        with open('1.json', 'a+', encoding='UTF-8')as f:
         f.write(str(dict_1) + '\n')
        print(f'{title}------提取完成')

"""
    高匿名代理
    # 对方并不知道你访问
    6块/ 24小时

    """

"""
    开发思路
    1.找二手房或者新房url地址，摸清楚翻页规律
    2.通过访问房源列表页，提取房源详情页url地址
    3.访问房源详情页提取数据
    """

'''编码转换'''
# from urllib.parse import quote, unquote
# # %E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80 转换为汉字
# name = '王者荣耀'
# print(quote(name))
# print(unquote(quote(name)))
"""汉字转换为拼音"""
# # pip install xpinyin
# from xpinyin import Pinyin
# name = '亾兦'
# p = Pinyin()
# print(p.get_pinyin(name))
"""B站"""
# url = 'https:\u002F\u002Fupos-sz-mirrorkodo.bilivideo.com\u002Fupgcxcode\u002F20\u002F88\u002F160738820\u002F160738820-1-16.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1615044833&gen=playurl&os=kodobv&oi=2936638550&trid=9c237beb08564f7eb9fad18a0ffa5d31h&platform=html5&upsig=476ecb8f87962ddcbf3f65019e03405b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&logo=80000000'
# result = url.encode('latin-1').decode('unicode-escape')
# print(result)
""""""
# from urllib.parse import quote
# # %u795E%u5893                神墓
# # %u738B%u8005%u8363%u8000    王者荣耀
# # %5Cu738b%5Cu8005%5Cu8363%5Cu8000
# # %u738b%u8005%u8363%u8000
# name = '王者荣耀'
# result = quote(name.encode('unicode-escape')).replace('%5C', '%')
# print(result)


