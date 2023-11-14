# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""本章主要涉及的知识点：

1.urllib网络请求库的基本认识和使用
2.requests库的基本使用
3.熟练使用urllib和requests编写一个简单的爬虫
4.re正则提取数据
5.XPath提取数据

"""

"""3.1 urllib:"""

"""本节主要讲解Python3中的urllib库的用法，urllib是Python标准库中用于网络请求的库。该库有4高模块，
分别是：urllib.request、urllib.error、urllib.robotparser.其中urllib.request和urllib.error两
个库在爬虫程序中应用比较频繁。"""

"""3.1.1 urlopen()"""

# 模拟浏览器发起一个http请求，需要用到urllib.request模块。urllib.request的作用不仅是发起请求，
# 还能获取请求返回结果。下面先看一下urlopen()的API。

# API（Application Programming Interface，应用程序接口）是一些预先定义的接口（如函数、HTTP接口），
# 或指软件系统不同组成部分衔接的约定。 [1]  用来提供应用程序与开发人员基于某软件或硬件得以访问的一组例程，
# 而又无需访问源码，或理解内部工作机制的细节。参考链接：https://baike.baidu.com/item/API/10154

# urlopen()的API：(已被阿展注释）

# urllib.request.urlopen(
#   url,
#   data=None,
#   [timeout,]*,
#   cafile=None,
#   capath=None,
#   cadefault=False,
#   context=None
# )

"""
（1）url参数是string类型的地址，也就是要访问的URL，如：http://www.baidu.com。
（2）data参数是bytes类型的内容，可通过bytes()函数转换为字节流，它也是可选参数。使用data参数，
请求方式变成以post方式提交表单。使用标准格式是application/x-www-form-urlencoded。
（3）timeout参数用于设置请求超时时间，单位是秒。
（4）cafile和capath参数代表CA证书和CA证书的路径，如果使用HTTPS则需要用到。
（5）context参数必须是ssl.SSLContext类型，用来指定SSL设置。
（6）cadefault参数已经被弃用，可以忽略。
（7）该方法也可以单独传入urllib.request.Request对象。
（8）该函数返回的结果是一个http.client.HTTPResponse对象。

PS：其实在实际使用过程中，用的最多的参数就是url和data。
"""

"""3.1.2 简单抓取网页"""

# 下面来看一个简单的示例，使用urllib.request.urlopen()去请求百度贴吧，并获取到它页面的源代码。

# import urllib.request # 导入要使用的urllib.request包
# url = "http://tieba.baidu.com" # 传入起始的url地址，直接请求访问
# response = urllib.request.urlopen(url) # 使用response接收请求网页的响应，传入参数：url
# html = response.read() # 使用html来接收响应，并使用read()方法读取它 即：获取到页面的源代码
# print(html) # 打印获取到的html响应，也可以使用.decode()方法进行编码转换

# 通过我们实际操作实例可以看到，使用urllib.request.urlopen()方法，传入http://tieba.baidu.com(百度贴吧）
# 这个网址，就可以成功得到它的网页源代码。

"""3.1.3设置请求超时"""

# 有时候，在访问网页时常常会遇到这样的情况：因为某些原因，如自己的计算机网络慢或者服务器压力过大而崩溃，
# 导致在请求时迟迟无法得到响应，同样的，在程序中去请求也会遇到这种情况，因此可以手动设置超时时间，当请求
# 超时时可以采取进一步措施，如直接丢弃该请求或再请求一次，为了应对这个问题，在urllib.open()中可以通过
# timeout参数设置超时时间。
# 下面看一下该如何设置，从下面的代码中可以看到，只需要在url参数的后面再加上一个参数就可以了--设置timeout
# 参数，如果时间超过了一秒就会舍弃它或重新访问。
# import urllib.request
#
# url = 'http://www.baidu.com'
# response = urllib.request.urlopen(url, timeout=1)
# print(response)

"""3.1.4使用data参数提交数据"""

# 前面介绍的API中已提到除了可以传递url和timeout超时参数外，还可以传递其他内容，如data，
# data参数是可选的，如果要添加data，需要它是字节流编码格式的内容，即bytes类型，通过bytes()
# 函数可以进行转换，另外，如果传递了data参数，那么它的请求方式就不再是get方式，而是post方式
# 下面看一下如何传递这个参数。
# 通过下面的示例代码可以看到，data需要被转码成字节流，而data是一个字典，需要使用
# urllib.parse.urlencode()将字典转化成字符串，再使用bytes()函数转换为字节流，最后使用urlopen()
# 发起请求，请求是模拟用post方式提交表单数据
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())
#
# # 运行后控制台会输出：
# b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    ' \
# b'"word": "hello"\n  }, \n  "headers": {\n    "Accept-Encoding": "identity", \n    ' \
# b'"Content-Length": "10", \n    "Content-Type": "application/x-www-form-urlencoded", \n    ' \
# b'"Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.7", \n    ' \
# b'"X-Amzn-Trace-Id": "Root=1-606a7960-022244ab3108c5760591954d"\n  }, \n  ' \
# b'"json": null, \n  "origin": "112.6.111.54", \n  ' \
# b'"url": "http://httpbin.org/post"\n}\n'

"""3.1.5 Request"""
# 通过3.1.1小节介绍的urlopen()方法可以发起简单的请求，但它的几个简单的参数并不足以构建一个完整
# 的请求，如果请求中需要加入headers（请求头）、指定请求方式等信息，那么就可以利用更强大的request
# 类来构建一个请求，下面看一个request的构造方法
# urllib.request.Request(
#     url,
#     data=None,
#     headers={}
#     orgin_req_host=None,
#     unverifiable=False,
#     method=None
# )
#
# （1）url参数是请求链接，它是必选参数，其他都是可选参数
# （2）data参数与urlopen()中的data参数用法相同
# （3）headers参数是指定发起的http请求的头部信息，headers是一个字典，他除了在request中添加外，
# 还可以通过调用request实例的add_header()方法来添加请求头
# （4）orgin_req_host参数指的是请求方的host名称或IP地址
# （5）unverifiable参数表示这个请求是否是无法验证的，默认值是False，意思是说用户没有足够的权限
# 来选择接收这个请求的结果，例如，我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，
# 我们就要将unverifaable设置为True
# （6）method参数指的是发起http请求的方式，有get、post、gelete和put等。

"""3.1.6简单使用Request"""
# 了解了Request参数后，下面就来简单地使用它请求一下http://tieba.baidu.com（百度贴吧）这个网址
# 需要注意的是，适用Reauest伪装成浏览器发起http请求，如果不设置headers中的User-Agent，默认的
# ua是Python-urllib/3.5,因为可能一些网站会将该请求拦截，所以需要伪装成浏览器发起请求，例如，
# 使用的ua为Chrome浏览器，随便打开一个网站直接将Chrome的ua copy过来就行了

# import urllib.request
# url = 'http://tieba.baidu.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# print(response)

"""3.1.7 Request高级用法"""

# 如果需要在请求中添加代理、处理请求的Cookie，那么就要用到Handler和OpenerDirector两个知识点

'1. Handler'
# Handler即处理者、处理器，能处理请求（HTTP、HTTPS、FTP等）中的各种事情，Handler的具体实现是
# urllib.request.BaseHandler类，urllib.request.BaseHandler类是所有其它Handler的基类，其提
# 供了最基本的Handler的方法，如default_open()、protocol_request()等，继承BaseHandler类的Handler
# 子类有很多，这里列举几个比较常见的类。
# （1）ProxyHandler:为请求设置代理 # proxy：代理模式
# （2）HTTPCookieProcessor：处理HTTP请求中的Cookie
# （3）HTTPDefaultErrorHandler：处理HTTP响应错误
# （4）HTTPRedirectHandler：处理HTTP重定向
# （5）HTTPPasswordMgr：用于管理密码，它维护了用户名密码的表
# （6）HTTPBasicAuthHandler：用于登录认证，一般和HTTPPasswordMgr结合使用

'2. OpenerDirector'
# OpenerDirector，也可以称为Opener，之前用过的urlopen()方法，实际上就是urllib提供的一个Opener
# 那么Opener和Handler又有什么关系呢？Opener对象是由build_opener(handler)方法创建出来的，创建
# 自定义的Opener，就需要使用install_opener(opener)方法，值得注意的是，install_opener实例化会
# 得到一个全局的OpenerDirector对象。

'3.1.8 使用代理'
# 了解了Opener和Handler后，接下来就通过示例来深入学习——为HTTP请求设置代理，有些网站做了浏览器
# 频率限制，如果请求频率过高，该网站会封IP，禁止我们的访问，所以就需要使用代理来突破这个“枷锁”
# 下面来看一个示例：

# import urllib.request
# url = 'http://tieba.baidu.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# proxy_handler = urllib.request.ProxyHandler({ # 调用ProxyHandler()方法,{}内传入代理ip即可使用代理
#     'http':'172.12.24.45:8080',
#     'https':'120.34.5.46:8080'
# })
# opener = urllib.request.build_opener(proxy_handler) # Opener对象是由build_opener(handler)方法创建出来的
# urllib.request.install_opener(opener) # 创建自定义的Opener，就需要使用install_opener(opener)方法
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# print(response)

# 通过以上示例代码可以看到，调用ProxyHandler方法就可以设置代理，模拟成多个不同的客户端，
# 成功“欺骗”网站，获取了数据

"""温馨提示："""
# 在实际项目中，如需要大量使用代理IP，可到专门做代理IP的提供商处购买，虽然网上有大量免费的，
# 但是大都不稳定，故这里推荐两个代理IP提供商地址：http.zhiliandaili.com; http://www.etdaili.com

"""3.1.9 认证登录"""

# 有些网站需要携带账号和密码进行登陆之后才能继续浏览网页，遇到这样的网站，就需要用到认证登录。
# 首先需要使用HTTPPasswordMgrWithDefaultRealm()实例化一个账号密码管理对象，然后使用add_password()
# 函数添加账号和密码，接着使用HTTPBasicAuthHandler()得到Handler，再使用build_opener()获取Opener
# 对象，最后使用Opener()的open()函数发起请求。下面以携带账号和密码请求登录百度贴吧为例，代码如下：

# import urllib.request
# url = 'http://tieba.baidu.com'
# user = '15738108997' # 用户名
# password = '15738108997he' # 密码
# pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm() # 实例化账号密码管理对象
# pwdmgr.add_password(None,url,user,password) # 添加账号密码
# auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr) # 得到handler
# opener = urllib.request.build_opener(auth_handler) # 获取Opener对象
# response = opener.open(url) # 传入响应的url
# print(response)

"""3.1.10 Cookie设置"""
# 如果请求页面每次都需要身份验证，那么就可以使用Cookie来自动登录，免去重复登录验证的操作。
# 获取cookie需要使用http.cookiejar.CookieJar()实例化一个Cookie对象，
# 再用urllib.request.HTTPCookieProcessor构建出Handler对象，最后使用Opener的open()函数即可。
# 下面以获取请求百度贴吧的Cookie并保存到文件中为例，代码如下：

# import http.cookiejar
# import urllib.request
#
# url = 'http://tieba.baidu.com'
# fileName = 'cookie.txt'
#
# cookie = http.cookiejar.CookieJar() # 使用http.cookiejar.CookieJar()实例化一个Cookie对象
# handler = urllib.request.HTTPCookieProcessor(cookie) # 用urllib.request.HTTPCookieProcessor构建出Handler对象
# opener = urllib.request.build_opener(handler) # 使用build_opener()获取Opener对象
# response = opener.open(url) # 用Opener的open()函数
#
# # 保存文件
# f = open(fileName,'a')
# for item in cookie:
#     f.write(item.name + item.value+'\n')
# f.close() # 关闭文件

"""3.1.11 HTTPResponse"""
# 从前面的例子可知，使用urllib.request.urlopen()或opener.open()返回结果是一个
# http.client.HTTPResponse对象，http.client.HTTPResponse对象包含msg、version、status、reason、
# debuglevel、closed等属性及read()、readinto()、getheaders()、fileno()等函数。

"""3.1.12 错误解析"""
# 发起请求难免会出现各种异常，因此就需要对异常进行处理，异常处理主要用到两个类：
# uellib.error.URLError和urllib.error.HTTPError

'''1.URLError'''
# URLError是urllib.error异常类的基类，可以捕获由urllib.request产生的异常，它具有一个属性：reason，
# 即返回错误的原因，捕获URL异常的示例代码如下：

# import urllib.request
# import urllib.error
#
# url = 'http://www.google.com'
# try:
#     response = request.urlopen(url)
# except error.URLError as e:
#     print(e.reason)

'''2.HTTPError'''
# HTTPError是UEKError的子类，专门处理HTTP和HTTPS请求的错误，它具有以下3个属性：
# （1）code：HTTP请求返回的状态码
# （2）renson：与基类（reason）用法一样，表示返回错误的原因
# （3）headers：HTTP请求返回的响应头信息
# 获取HTTP异常的示例代码（输出了错误状态码、错误原因、服务器响应头）如下：

# import urllib.request
# import urllib.error
#
# url = 'http://www.google.com'
# try:
#     response = request.urlopen(url)
# except error.HTTPErrpr as e:
#     print('code' + e.code + '\n')
#     print('reason' + e.reason + '\n')
#     print('headers' + e.headers + '\n')

"""3.2 requests"""

'''3.2.2 requests模块的使用方法介绍'''
# 在使用requests库之前，先来看一下它有哪些方法，requests库的7个主要方法如下：
# （1）requests.request() 构造一个请求，支持以下各种方法
# （2）requests.get()     获取HTML的主要方法
# （3）requests.head()    获取HTML头部信息的主要方法
# （4）requests.post()    向HTML网页提交POST请求的方法
# （5）requests.put()     向HTML网页提交put请求的方法
# （6）requests.path()    向HTML网页提交局部修改的请求
# （7）requests.delete()  向HTML网页提交删除请求的方法

"""3.2.3 requests.get()"""

# requests.get()方法是常用的方法之一，通过该方法可以了解到其他方法，使用方法如下面的示例代码：
# res = requests.get(url, params, **kwargs)
# （1）url：需要爬取的网站地址
# （2）params：url中的额外参数，字典或字节流形式，为可选参数
# （3）**kwargs：12个控制访问的参数

# 下面先来介绍**kwargs，其参数如下所示：
'''参数名称'''   '''描述'''
# params：字典或字节序列，作为参数增加到url中，使用这个参数可以把一些键值对
# 以？key1=value1&key2=value2的模式增加到url中

# data：字典、列表或元组的字节的文件，作用是向服务器提交资源，作为request的内容，与params不
# 同的是，data提交的数据并不放在链接中，而是放在url链接对应位置的地方作为数据来存储，它也可以
# 接受一个字符串对象

# json：JSON格式的数据，json是HTTP中经常使用的数据格式，作为内容部分可以向服务器提交，例如：
# kv = {'key1':'value1'}
# r = requests.request('POST','http://python123.io/ws',json=kv)

# headers：字典是HTTP的相关语，对应了向某个url访问时所发起的HTTP的头字段，可以用
# 这个字段来定义HTTP的访问的HTTP头，可以模拟任何想模拟的浏览器来对url发起访问，例如：
# hd = {'user-agent':'Chrome/10'}
# r = requests.request('POST','http://python123.io/ws',headers=hd)

# cookie: 字典或CookieJar,指的是从HTTP中解析Cookie

# auth： 元组，用来支持HTTP的认证功能

# files： 字典，是用来向服务器传输文件时使用的字段，例如：
# fs = {'files':open('data.txt','rb')}

# timeout: 用来设定超时时间，单位为秒，当发起一个get请求时，可以设置一个timeout时间，
# 如果在timeout时间内请求内容没有返回，将产生一个timeout的异常

# proxies：字典，是用来设置访问代理服务器

# allow_readirects： 开关，表示是否允许对url进行重定向，默认为True

# stream： 开关，表示是否允许获取内容进行立即下载，默认为True

# verify： 开关，用于认证SSL证书，默认为True

# cert： 用于设置保存本地SLL证书路径|

# 前面示例代码中的代码是构造一个服务器请求requests，返回一个包含服务器资源的Response对象。
# 其中Response对象有以下属性：

'''属性'''      '''说明'''
# status_code     HTTP请求的返回状态，若为则200表示请求成功
# text            HTTP响应内容的字符串形式，即返回的页面内容
# encoding        从HTTPheader中猜测的相应内容编码方式
# apparent_encoding 从内容中分析出的响应内容编码方式（备选编码方式）
# content         HTTP响应内容的二进制形式

'''举例说明，示例代码如下：'''
# import requests
#
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# print(r.encoding)
# print(r.apparent_encoding)
# print(r.text)

"""3.2.4 requests库的异常"""
# requests库有时会产生异常，如网络连接错误、HTTP错误异常、重定向异常、请求url超时异常等。
# 这里可以利用r.rause_for_status()语句来捕捉异常，该语句在方法内部判断r.status_code是
# 否等于200，如果不等于，则抛出异常，示例代码如下：

# import requests
#
# try:
#     r = requests.get("//www.baidu.com", timeout=30) # 请求超时时间为30秒
#     r.raise_for_status() # 如果状态码不是200，则引发异常
#     r.encoding = r.apparent_encoding # 配置编码
#     print(r.text)
# except:
#     print("产生异常")

"""3.2.6 requests.post()"""
# requests.post()方法一般用于表单提交，向指定url提交数据，可提交字符串、字典、
# 文件等数据，示例代码如下：
# import requests
#
# # 向url post一个字典：
# payload = {"key1":"balue1","key2":"value2"}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)
# # 向url post一个字符串，自动编码为data
# r = requests.post("http://httpbin.org/post", data='helloworld')
# print(r.text)

"""requests.put()和requests.patch()"""
# requests.path()与requests.put()类似，两者不同的是：当用patch时，仅需提交需要修改的字段，
# 当用put()时，必须将20个字段一起提交到url，未提交字段将会被删除，patch的优点是节省网络带宽，
# 示例代码如下：
# import requests
#
# payload = {"key1":"value1","key2":"value2"}
# r = requests.put("http://httpbin.org/put",data=payload)
# # requests.patch()
# payload = {"key1":"value1","key2":"value2"}
# r = requests.patch("http://httpbin.org/post",data=payload)


# 关于python爬虫中常用的两个网络请求库本节暂讲到此，至于如何在实际应用中使用它们编写爬虫
# 爬取数据，将会在后面的内容中讲到。

"""3.3 re正则使用"""

# 正则表达式是一个特殊的字符序列，它帮助用户便捷地检查一个字符串是否与某种模式匹配，在爬虫中，
# 我们经常会使用它从抓取到的网页源码或接口返回内容中匹配提取我们想要的数据，python自1.5版本
# 增加了re模块，它提供Perl风格的正则表达式模式，re模块使python语言拥有全部的正则表达式功能
# compile函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象，该对象拥有一系列方法
# 用于正则表达式匹配和替换

# re模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串作为他们的第一个参数，
# 本节主要介绍python中常用的正则表达式处理函数

"""3.3.1 re.match函数"""

# re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功，那么match()就返回None，
# re.match的语法格式如下：

'''参数'''      '''描述'''
# pattern        匹配的正则表达式
# string         要匹配的字符串
# flags          标志位，用于控制正则表达式的匹配方式，如是否区分大小写、是否多行匹配等

# 匹配成功re.match返回一个匹配的对象，否则返回None，还可以使用group(num)或groups()匹配
# 对象函数来获取匹配表达式，如下所示：

"""匹配对象方法及描述"""

'''匹配对象方法'''      '''描述'''
# group(num=0)           匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下，
# 它将返回一个包含那些组所对应值的元组

# groups()               返回一个包含所有小组字符串的元组，从1到所含的小组号

# 了解了以上内容，我们来看一个示例，代码如下：
# import re
#
# print(re.match('www', 'www.baidu.com').span()) # 在起始位置配
# print(re.match('com', 'www.baidu.com'))        # 不在起始位置匹配

# 运行后控制台会输出：
# (0,3]
# None

# 获取匹配表达式的示例代码如下：
# import re
# line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*)are(.*?).*', line)
#
# if matchObj:
#     print("matchObj.group():",matchObj.group())
#     print("matchObj.group(1):",matchObj.group(1))
#     print("matchObj.group(2):",matchObj.group(2))
# else:
#     print("No match!!")

# 运行后控制台会输出:
# matchObj.group(): Cats are smarter than dogs
# matchObj.group(1): Cats
# matchObj.group(2): smarter（我的.号不正常，所以smarter没显示）

"""3.3.2 re.search()函数"""
# re.search用于扫描整个字符串并返回第一个成功的匹配，re.search的语法格式如下：
# re.search(pattern, string, flags=0)

# re.search也有3个参数，这三个参数的作用与上面re.match参数的作用是一样的，需要注意的是
# flags参数可写可不写，不写也能正常返回结果，原因是它的底层给了默认值。
# 示例代码如下：
# import re
#
# print(re.search('www','www.runoob.com').span()) # 在起始位置匹配
# print(re.search('com','www.runoob.com').span()) # 不在起始位置匹配
# 运行后控制台会输出:
# (0,3)
# (11,14)
# 可以看到，匹配成功了，它会返回一个元组，该元组包含匹配内容的开始位置和结束位置

"""3.3.3 re.match与re.search的区别"""

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None，
# 而re.searchh匹配整个字符串，直到找到一个匹配

# 示例代码如下：
# import re
#
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'dogs', line)
# if matchObj:
#     print("match -->matchOBj.group():",matchObj.group())
# else:
#     print("No match!!")
#
# matchObj = re.search(r'dogs', line)
# if matchObj:
#     print("search -->matchObj.group():",matchObj.group())
# else:
#     print("None match!!")

# 运行后控制台会输出：
# "None match!!"
# search -->matchObj.group():dogs

# 从运行结果中可以看到，使用re.match时，它会从"Cats are smarter than dogs"这个字符串的开始
# 位置开始匹配，这里开始位置"Cats"并不满足他的要求，他从这里停止了匹配，所以返回了未匹配到，
# 反之，re.search从开始没匹配到，会继续往后匹配，直到把"Cats are smarter than dogs"这个字
# 符串匹配完，这里在字符串的最后结尾位置找到了他要匹配的内容，所以返回了匹配到的数据。

"""3.3.4 检索和替换"""

# 当需要替换某段文字中的某些内容时，例如有一句话：“等忙完这一阵，就可以接着忙下一阵了。”
# 想要把“忙”字替换成“过”，这时该如何去实现替换呢？python的re模块提供了re.sub,可用于替换
# 字符串中的匹配项，通过re.sub就可以将字符串中满足匹配条件的内容全部替换，
# re.sub的语法格式如下：

# re.sub(pattern, repl, string, count=0, flags=0)
# 可以看出，re.sub有以下几个比较重要的参数：
# （1）pattern:正则中的模式字符串
# （2）repl：替换的字符串，也可为一个函数
# （3）string：要被查找替换的原始字符串
# （4）count：模式匹配后替换的最大次数，默认为0，表示替换所有的匹配
# 示例代码如下：

# import re
# st = "忙完这一阵，就可以接着忙下一阵了。"
#
# # 替换其中的忙字
# new_st = re.sub(r'忙', "过",st)
# print("替换后的句子：",new_st)

# 运行后控制台会输出：
# 替换后的句子：过完这一阵，就可以接着过下一阵了。
# 从运行结果可以看到，已经成功地把“忙”字替换成“过”了。

"""3.3.5 re.compile函数"""

# re.compile用于编译正则表达式，生成一个正则表达式（Pattern）对象，供match()和search()函数使用
# re.compile()的语法格式如下：
# import re
# re.compile(pattern[,flags])

# 参数说明如下：
# （1）pattern:一个字符串形式的正则表达式
# （2）flags：可选参数，表示匹配模式，如忽略大小写、多行模式等，具体参数如下：
# 1.re.I:忽略大小写
# 2.re.L:表示特殊字符集\w、\W、\b、\B、\s、\S依赖于当前环境
# 3.re.M:多行模式
# 4.re.S:即为.并且包含换行符在内的任意字符（.不包含换行符）。
# 5.re.U:表示特殊字符集w、\W、\b、\B、\d、\D、\s、\S依赖于Unicode字符数型数据库
# 6.re.X:为了增加可读性，忽略空格和#后面的注释。

# 下面来看一个示例：
# import re
#
# pattern = re.compile(r'\d+') # 用于匹配至少一个数字
# m1 = pattern.match('one12twothree34four') # 查找头部，没有匹配
# m2 = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
# m3 = pattern.match('one12twothree34four',3,10) # 从'1'的位置开始匹配，正好匹配
#
# print(m1)
# print(m1)
# print(m1)
# print(m3.group(0))
# print(m3.start(0))
# print(m3.end(0))
# print(m3.span(0))

# 运行结果：
# None
# None
# None
# 12
# 3
# 5
# (3, 5)

# 在上面的例子中，当匹配成功时返回一个match对象，其中group([group1,...])方法用于获得
# 一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用group()或group(0),
# start([group])方法用于获取分组匹配的子串在整个字符串中的起始位置（字串第一个字符的索引）
# 参数默认值为0，end([group])方法用于获取分组匹配的子串在整个字符串中的结束位置（字串最后
# 一个字符的索引+1），参数默认值为0，span([group])方法返回(start(group),end(group))
# 再来看一个示例：

# import re
#
# pattern = re.compile(r'([a-z]+) ([a-z])', re.I) # re.I表示忽略大小写
# m = pattern.match('Hello World Wide Web')
# print(m)
# print(m.group(0)) # 返回匹配成功的整个子串
# print(m.span(0)) # 返回匹配成功的整个子串的索引
# print(m.group(1)) # 返回第一个分组匹配成功的子串
# print(m.span(1)) # 返回第一个分组匹配成功的子串的索引
# print(m.group(2)) # 返回第二个分组匹配成功的子串的
# print(m.group(2)) # 返回第二个分组匹配成功的子串的
# print(m.groups()) # 等价于(m.group(1),m.group(2),...)
# print(m.group(3)) # 不存在第三个分组

"""3.3.6 findall函数"""

# findall用于在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，
# 就返回空表，findall的语法格式如下：
# findall(string[,pos[endpos]])
# 参数说明如下：
#（1）string：待匹配的字符串
#（2）pos：可选参数，指定字符串的起始位置，默认为0
#（3）可选参数，指定字符串的结束位置，默认为字符串的长度

# 下面来看一个示例：查找字符串中的所有数字

# import re
#
# pattern = re.compile(r'\d+') # 查找数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run880oob123google456', 0,10)
# print(result1)
# print(result2)

"""XPath"""
# XPath是一门在xml文档中查找信息的语言，Xpath可用来在xml文档中对元素和属性进行遍历
# XPath是W3C XSLT标准的主要元素，并且XQuery和XPointer都构建于XPath表达之上
# XPath在python的爬虫学习中，起着举足轻重的作用，对比正则表达式re，两者可以完成同样的工作
# 实现的功能也类似，但xpath明显比re具有优势，在网页分析上使re退居二线
# xpath的全名称为xml path language，是一种小型的查询语言，具有如下优点：
# （1）可在xml中查找信息
# （2）支持HTML的查找
# （3）可通过元素和属性进行导航

# python开发使用下path条件：由于xoath属于lxml库模块，因此需要先安装lxml库，
# 具体的安装步骤如下：
# 1：这里使用下载lxml的whl文件进行安装，下载地址为：https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
# 下载对应的版本，例如，这里下载的是lxml-4.2.5-cp36-cp36m-win_amd64.whl
# 2.下载完成之后，放在一个文件夹中，然后按住shift键的同时单击鼠标右键，在弹出的快
# 捷菜单中选择在此处打开命令窗口，打开cmd命令行窗口
# 3。使用如下pip命令进行安装
# pip install lxml-4.2.5m-win_amd64.whl

"""3.4.1 XPath的使用方法"""

# 下面介绍一下Xpath的基本语法知识，常见的使用方法主要有以下几种：
# （1）//（双斜杠）：定位根节点，会对全文进行扫描，在文档中选取所有符合条件的内容，以列表
# 的形式返回
# （2）/（单斜杠）：寻找当前标签路径的下一层路径标签或对当前路径标签内容进行操作
# （3）/text()：获取当前路径下的文本内容
# （4）/@xxxx：提取当前路径下标签的属性值
# （5）|（可选符）：使用"|"选取若干个路径，如//p | //div，即在当前路径下选取所有符合条件的p标签
# 和div标签。
# （6）.（点）：用来选取当前节点
# （7）..（双点）：选取当前节点的父节点

"""3.4.2 利用实例讲解XPath的使用"""
# 以下是一段HTML
# <div>
#   <url>
#     <li class="item-0"><a href="www.baidu,com">baidu</a>
#     <li class="item-1"><a href="blog.csdn.net/qq_835054694">myblog</a>
#     <li class="item-2"><a href="www.csdn.net">csdn</a>
#     <li class="item-3"><a href="hao123.360.cn/?a1004">hao123</a>

# 显然，这段HTML中的节点没有闭合，因此可以使用lxml中的etree模块进行补全，示例代码如下：

# from lxml import html
# etree = html.etree
# text = '''
# <div>
#   <url>
#     <li class="item-0"><a href="www.baidu,com">baidu</a>
#     <li class="item-1"><a href="blog.csdn.net/qq_835054694">myblog</a>
#     <li class="item-2"><a href="www.csdn.net">csdn</a>
#     <li class="item-3"><a href="hao123.360.cn/?a1004">hao123</a>
#     '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result)

# 运行后控制台会输出：

# <html><body><div>\n  <url>\n
# <li class="item-0"><a href="www.baidu,com">baidu</a>\n
# </li><li class="item-1"><a href="blog.csdn.net/qq_835054694">myblog</a>\n
# </li><li class="item-2"><a href="www.csdn.net">csdn</a>\n
# </li><li class="item-3"><a href="hao123.360.cn/?a1004">hao123</a>\n
# </li></url></div></body></html>'

# 可以看到etree不仅闭合了节点，还添加了其他需要的标签，除了直接读取文本进行解析外，etree也
# 可以读取文件进行解析，示例代码如下：
# from lxml import html
# etree = html.etree
#
# html = etree.parse('./test.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result)

"""3.4.3 """
# 获取所有节点
# 根据xpath规则可知，通过"//"可以查找当前节点下的子孙节点，以上面的HTML为例获取所有子孙节点，
# 示例代码如下
# from lxml import html
# etree = html.etree
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//*') # //获取当前节点下的子孙节点，*表示所有节点
# for item in result:
#     print(item)

# 如果不是获取所有节点而是指定获取某个节点，只需将"*"号改为指定哪个节点的名称即可，
# 如获取所有的li节点，这个HTML代码可以直接放在代码的变量中，也可以放在文件中，效果都一样。

"""3.4.4 获取子节点"""

# 根据xpath常用规则可知，通过"/"或“//”可以获取子节点或子孙节点，如果要获取li节点下的
# a节点，可以使用//ul//a,首先选择所有的ul节点，然后再获取ul节点下的a节点，最后结果是一样的，
# 但是用//ul/a就不行了，首先选择所有的ul节点，然后再获取ul节点下的直接子节点a，然而ul节点下
# 没有直接子节点a，当然获取不到，需要深刻理解“//”和“/”的不同之处
# “/”用于获取直接子节点，“//”用于获取子孙节点，示例代码如下：
# from lxml import html
# etree = html.etree
#
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li/a') # //li表示选择所有的li节点，/a表示选择li节点下的直接子节点a
# for item in result:
#     print(item)

"""3.4.5 获取文本信息"""

# 很多时候找到指定的节点都是要获取节点内的文本信息，这里使用text()方法获取节点内的文本信息，
# 例如，获取所有a标签的文本信息，示例代码如下：

# from lxml import html
# etree = html.etree
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//ul//a/text()')
# print(result)

"""3.5 新书实训"""

"""1.requests库爬取阳光电影网"""
# 本实例主要希望是读者通过练习requests库的使用，试着用它请求阳光电影网的首页获取源码并打印出来
# 请求地址为：https://www.ygdy8.com,需要实现的目标如下：
# （1）构造一个访问阳光电影网的请求
# （2） 输出请求的状态码
# （3）输出请求的网页源码
# （4）将源码打印到控制台

# 为了实现目标，这里给大家一个参考步骤：读者可以参考此步骤，实现对阳光电影网的请求，达到举一反三的目的
# 相关的步骤如下：

# 步骤1：输入网址https://www.ygdy8.com,进入阳光电影网首页
# 步骤2：寻找headers信息，按F12，或右击检查元素，进入network选项卡，选择一个请求查找headers相关信息
# 步骤3：分析页面源码结构，获取编码方式，在网页中右击，在弹出的快捷菜单中选择查看网页源代码，
# 通过查看顶部的meta......可以发现charset是gb123的
# 步骤4：编写代码实现请求获取源码并打印，示例代码如下：

# import requests
#
# url = 'https://www.ygdy8.com'
# headers = {
#   'Accept-Ranges': 'bytes',
#   'Content-Encoding': 'gzip',
#   'Content-Length': '11521',
#   'Connection': 'keep-alive',
#   'If-None-Match': '809ff881032d71:0',
#   'Referer':'https://www.ygdy8.com/',
#   'Upgrade-Insecure-Requests': '1',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# # 定义一个req为一个request请求的对象
# req = requests.get(url, headers=headers)
# # 获取请求的状态码
# status_code = req.status_code
# print(status_code)
# # 知道网页的编码方式
# req.encoding='gb2312'
# # 获取网页源码，将req.content返回的文本内容赋值给html变量，然后打印到控制台
# html = req.content
# print(html)

"""2.百度搜索关键字提交"""

# 通过requests库携带参数取请求百度搜索，然后获取返回的HTML源码，百度搜索地址为：https://www.baidu.com/s?=keyword,
# 参考步骤如下：
# 步骤1：打开百度首页，再搜索框中输入“python”，输入之后会自动跳转到搜索结果页面，
# 步骤2：观察url地址栏，发现有一个wd参数，这个就是表示输入的要搜索的内容
# 步骤3：知道了wd参数，就可以使用python编写代码模拟这个过程了，示例代码如下：

# import requests
#
# keyword = 'python'
#
# try:
#     # 变量接收待传参数：
#     kv = {'wd':keyword} # key，value键值对
#     # 变量接收请求的对象，同时传入请求的关键字参数（使用params=传入）
#     r = requests.get('https://www.baidu.com/s',params=kv) # params:参数
#     # 返回状态码
#     r.raise_for_status()
#     # 当网页出现乱码时可以把apparent_encoding的编码格式赋值给encoding
#     r.encoding = r.apparent_encoding
#     # 函数：len()
#     # 1：作用：返回字符串、列表、字典、元组等长度
#     # 2：语法：len(str)
#     # 打印长度
#     print(len(r.text))
#     # 异常处理
# except:
#     print("失败")

"""小Python的温馨提示：学习爬虫是一件快乐有趣的事情，读者一定要多动手写代码，善于观察发现，
带着问题去学习，这样才能达到事半功倍的效果。"""

"""新手问答：
学完本章之后，读者可能会有以下疑问：
1.异常处理中except的用法和作用是什么？
答：执行try下的语句，如果引发异常，则执行过程会跳到except语句，对每个except分支顺序尝试执行，
如果引发的异常与except中的异常组匹配，则执行相应的语句，如果所有的except都不匹配，则异常会传
递到下一个调用本代码的最高层try代码中

try下的语句如果正常执行，则执行else块代码，如果发生异常，就不会执行，如果存在finally语句，
最后总是会执行。

2.如何解决urllib.request找不到的问题？
答：python3.x中urllib库和urllib2库合并成了urllib库，其中：
urllib2.urlopen()变成了urllib.request.urlopen()
urllib.request()变成了urllib.request.Request()
因此，python3.x版本中可以使用urllib.request库，但是在python2.7版本的库中还是
使用urllib2.urlopen。"""

"""本章小结"""

# 本章主要介绍了urllib和requests库的基本使用方法，以及如何用它们编写简单的爬虫，本章的内容还需要
# 读者积极配合练习进行巩固加深，一步一个脚印，才能真正学会使用urllib和requests进行网络请求抓取数据。

