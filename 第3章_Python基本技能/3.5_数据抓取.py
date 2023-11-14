# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""3.5 数据抓取"""

"""    数据抓取大概是很多Python初学者接触最早、使用最多的技术之一,看似简单,却涉及网络通信、应用协议、
HTML、 CSS. JavaScript、数据解析、服务框架等多个技术领域的知识,初学者往往不容易掌握。这里面, HTTP 
(Hyper Text Transfer Protocol,超文本传输协议)无疑是最基础、最重要的。初学者一定要拿出一些时间,
弄清楚HTTP请求和应答的格式组成,GET和POST两种请求方式各自的含义,以及cookie和session的基本原理。
在理解基本概念原理的前提下,再去学习数据抓取技术,才能事半功倍,否则就会欲速则不达。
    通常情况下,我们使用标准模块urllb或第三方模块requests, pycurl等抓取数据;特殊情况下,使用自动化
测试工具selenium模块也是一种选择。当然,也有很多封装好的框架可以使用,如pyspider, scrapy 等。"""

"""3.5.1 urlib模块

    urllib是Python内置的标准模块,用于发送HTTP请求,以及接收并处理来自服务器的应答。
urllib模块包含4个子模块: request子模块提供最基本的构造HTTP请求的方法,利用它可以模拟浏览器的一个
请求发起过程，同时它还带有处理authenticaton (授权验证)、 redirections (重定向), cookie(浏览器
Cookies)等功能: parse子模块是一个工具模块,提供许多URL处理方法,如拆分、解析、合并等: error子模块用于
异常处理:robotparser子模块主要用来判断网站是否可以爬取,这个子模块极少用到。

    很多人认为urlib模块太过烦琐复杂,初学者不容易掌握。其实,只要理解了下面这三个要点, urlib模块很容
易成为我们手中驾轻就熟的有力工具。"""

"""1.使用urlib.request.Request(url, data=None, headers={}, method=None)构造请求"""
    # 这里url参数是必需的。data参数仅接受bytes类型的字符串。如果data参数存在,则method默认为POST,
    # headers参数是一个字典,用于定制请求报头。除了在构造函数中定制请求报头,还可以调用Request实例的
    # add_header()方法来定制请求报头。

"""2.使用urllib.request.urlopen(url, data=None)发送请求"""
    # 如果url参数是一个字符串,则发送GET请求;如果url参数是一个urllib.request.Request对象,则请求方式
    # 由该对象指定。data参数仅接受bytes类型的字符串。如果数据类型为字典,可使用
    # urllib.parse.urlencode()转换为bytes类型。
    # 例如:data = bytes(urllib.parse.urlencode({'name':'Alice', 'age':18}),encoding='utf8')

"""3.每一个请求都会返回一个response应答对象"""
    # 应答对象的status或code属性都是应答状态码(HTTP协议)。使用getheaders()可以获取字典类型应
    # 答报头,且字典的键对大小写不敏感。使用getheader(key)可以获取报头中指定键的值。使用read( )方法
    # 返回应答内容(body)。

"""下面的代码演示了使用urllib模块发送GET请求,处理应答对象,以及从应答对象中获取数据的基本方法。"""

# import urllib.request
#
# resp = urllib.request.urlopen('https://cn.bing.com') # 发送get请求
# print(resp.status) # HTTP协议状态码
# print(resp.getheader('Content-Type')) # 取得应答报头中的Content-Type
# html = html = resp.read()
# print(html) # 取得应答内容（body的内容）
# print(len(html)) # 打印字长
# print(type(html)) # html类型
# html = html.decode('utf-8')
# print(len(html))
# print(type(html))

"""下面代码中演示了使用urllib模块构造请求对象，对需要提交的数据编码，以及定制请求报头的基本方法"""

# import urllib.request, urllib.parse
#
# url = 'http://httpbin.org/post'
# from_data = {'name':'liting', 'age':20}
# data = bytes(urllib.parse.urlencode(from_data), encoding='utf8')
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
#     }
# req = urllib.request.Request(url=url, data=data, headers=headers)
# resp = urllib.request.urlopen(req) # 发送请求
# print(resp.code)
# print(resp.read()) # 响应内容
# print(resp.getheader('Content-Length'))


"""3.5.2 requests模块
    urllib模块功能虽然强大，但不够精炼，对于初学者来说，想要完全掌握它不是一件容易的事情，因此
越来越多的程序员转向了requests模块，requests模块基于urllib模块开发，但用起来要比urllib模块
更加方便、简洁、requests模块不是python的标准库，需要使用pip命令安装
pip install requests"""

"""1.发送请求
    requests模块之所以容易掌握，是因为它的设计理念符合人类的思维习惯，例如，发送一个GET请求，
只要给出URL即可，除了发送GET和POST请求，还可以使用requests模块发送HTTP协议中的PUT、DELETE、
HEAD及OPTIONS请求，使用时注意方法名都是小写字母。"""
# import requests
# resp = requests.get('http://httpbin.org/post')

""" 1.如果需要在URL中传递参数, requests模块允许使用params关键字参数,以一个字符串字典的形式来提供
这些参数。
    2.如果想为请求添加请求报头信息,只需要传递一个字典给关键字参数headers即可。虽然cookie信息属于请求
报头的一部分,但如果要发送cookie,需要将cookie字典传递给cookies个关键字参数。

    3.如果需要在POST请求中提交表单(form)或类似的数据,可以使用关键字参数data来接受字典类型的数据;
如果使用关键字参数json来接受字典类型的数据,该数据会被自动编码,相当于调用了json.dumps()函数。

    4.如果需要上传文件,可以通过关键字参数files接受一个描述上传文件信息的字典。如果一次上传多个文件,
则需要用键名区分不同的文件,键值为open()函数返回的对象。"""

"""2.处理应答

    发送请求后,服务端会返回一个response对象,包含服务器响应的全部内容。我们可以通过response对象的
各种属性和方法,获取需要的信息。

    1.response.ok :应答成功的标志(针对HTTP协议级的,而非业务逻辑层次的)。
    2.response.status code :应答状态码(HTTP协议)。
    3.response.encoding :编码方式。可以通过赋值修改编码方式并自动影响应答内容。
      例如: response.encoding = 'utf-8'或response.encoding = 'gbk'
    4.response headers :字典类型的应答报头。该字典的键对大小写不敏感
    5.response.request :针对本应答的请求对象。处理应答时,可以通过该对象了解请求报头等信息。
    6.response.raw:原生的应答对象,即urllib的response对象(urllib3.response.HTTPResponse object)。
    7.response.content :字节码形式的应答体(body)response.text:字符串形式的应答体(body).
    8.response.json():如果应答类型是json格式,该方法返回应答体(body)的json解码结果
    9.response.raise for status():如果应答失败,调用该方法将抛出异常。
    10.response.cookies: RequestsCookieJar类型的cookie对象。该对象的get_dict()返回cookie字典。
"""

"""3.应用实例

    MODIS是搭载在TERRA和AQUA遥感卫星上的一个重要的传感器,其实时观测到的数通过X波段向全球直接广播,
任何用户都可以免费接收并无偿使用这些数据。为便于读者深入理解数据下载过程,下面的代码使用了一个模拟的
MODIS数据下载服务站点。MODIS数据下载流程如图3-5所示。

    下面的代码以交互方式展示了从模拟的MODIS数据源下载数据的全过程。本例并没有直接使用requests的
get()和post()方法,而是使用Session类的get()和post()方法. Session在发送请求、接收应答时会自动
处理cookie,我们无须做任何干预。
"""

# import requests
# sess = requests.session() # session类自动处理cookie
# url_login = 'http://sdysit.com/modis' # 登陆地址
# form_login = { # form:表单，login：登录
#     "account":"guest", # account:账户，guest：客人
#     "password":"hello"
# }
# resp = sess.post(url_login, data=form_login)
# print(resp.ok) # 查看应答是否成功
# # True
#
# url_list = 'http://sdysit.com/modis/list' # 文件列表地址
# resp = sess.get(url_list)
# print(resp.ok) # 查看应答是否成功
#
# result = resp.json() # 解析json格式的响应
# print(result['code']) # 响应代码为10，表示数据可用
#
# print(result['data']) # 文件名和下载地址的列表
#
# for item in result['data']:
#     print('开始下载文件...%s'%item['name'])
#     resp = sess.get(item['url'])
#     if resp.ok:
#         with open(r'D:\python_learn\Python基础阶段\Python高手修炼之道\Python基本技能\%s'%item['name'], 'wb')as fp:
#             fp.write(resp.content)
#         print('文件%s下载完毕\n'%item['name'])
#     else:
#         print('下载文件%s失败'%item['name'])




