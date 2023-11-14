# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 我们先直接copy检查元素的源码，使用request构造请求：
# import requests
# url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# # 有道翻译的request-url
# # 直接copy过来response-headers的内容构造headers：
# headers={
# "Accept":"application/json, text/javascript, */*; q=0.01",
# "Accept-Encoding":"gzip, deflate",
# "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
# "Connection":"keep-alive",
# "Content-Length":"251",
# "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
# "Cookie":"OUTFOX_SEARCH_USER_ID=-198948014@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1678156251.6498268; _ga=GA1.2.109926435.1582269589; UM_distinctid=170a4e98abc891-0b24cc8bee43ca-5e4f281b-144000-170a4e98abd72b; JSESSIONID=aaaPbNnhvgdpJe62qgofx; ___rl__test__cookies=1586153715407",
# "Host":"fanyi.youdao.com",
# "Origin":"http://fanyi.youdao.com",
# "Referer":"http://fanyi.youdao.com/",
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
# "X-Requested-With":"XMLHttpRequest",
# }
# # 直接copy过来form data的内容：
# data={
# "i":"你好",
# "from":"AUTO",
# "to":"AUTO",
# "smartresult":"dict",
# "client":"fanyideskweb",
# "salt":"15861537154130",
# "sign":"d0a1387da482d8d9dae92e0f24b6e4e0",
# "ts":"1586153715413",
# "bv":"5d4cb17cceb9ecd02ece3ed9923d3a7a",
# "doctype":"json",
# "version":"2.1",
# "keyfrom":"fanyi.web",
# "action":"FY_BY_REALTlME",
# }
# res=requests.post(url=url,headers=headers,data=data) # 使用res代替response来接收请求的响应
# print(res.text) # 打印响应的翻译内容
# 通过打印结果可知，i值仍为“你好”的时候返回的数据是正常的的
# 但是i值（要翻译的内容）更改之后就会返回错误码
# 所以我们需要分析到底什么地方出了问题，因为这是post方式，我们猜测是data数据种某些参数发生了变化，
# 我们再次回到浏览器输入其他语句看一下会有什么变化。

# 我们通过对比上一次翻译的请求就会发现，post的data数据中有几个参数好像每次都不一样，
# 那么这些参数是如何构造出来的呢？
#
# 打开调试台搜索如参数 sign，我们发现在某个js文件中有这个参数，猜测此文件就是构造参数的文件，
# 点击打开这个搜索到的关于sign的文件，再点击（点击左下角的花括号），即可格式化代码，看看代码。
# 发现这是一个接近一万行的js代码，但是我们只需要构造4个参数呀，在这接近一万行的代码中怎么分析呢？
# 我们继续在代码中搜索参数名称试一试。

# 鼠标点击一下代码部分，然后键盘按ctrl-f即会出现代码部分的搜索框。搜索结果大概十几个的样子，
# 我们多观察下搜索结果就会找到有用的函数。
# 继续搜索sign，查看关于sign的参数
# 怎么样，一看竟然出现了 ts、bv、salt、sign 四个参数，这不正是我们要找的构造函数吗？

# copy这段代码：
# define("newweb/common/service", ["./utils", "./md5", "./jquery-1.7"], function(e, t) {
#     var n = e("./jquery-1.7");
#     e("./utils");
#     e("./md5");
#     var r = function(e) {
#         var t = n.md5(navigator.appVersion)
#           , r = "" + (new Date).getTime()
#           , i = r + parseInt(10 * Math.random(), 10);
#         return {
#             ts: r,
#             bv: t,
#             salt: i,
#             sign: n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")
#         }
#     };
# 我们把这一段函数拿出来放进notepad++中分析一下：
# 首先变量e我们不知道是什么，变量t像是某个参数经过md5加密后的结果
# 变量r是js的gettime()函数返回的时间值的字符串，（gettime()方法可返回距1970年1月1日之间的毫秒数）
# 变量i是变量r加上1~9之间的随机整数的字符串
# 变量sign也是一个参数经过md5加密后的结果，（加密内容是"fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@"）
# 所以目前看起来我们只需要搞清楚变量 e与变量 t 中的 navigator.appVersion 是什么就可以搞定构造函数了。

# 其实现在已经成功一半了，我们已经找到了参数的构造方法，不过接下来的任务也不简单，我们需要搞清楚两个变量的内容是什么。
#
# 我们使用chrome调试台的debug功能来调试一下看看这两个变量是什么，首先在关键代码打上断点（在对应代码前点下鼠标出现蓝色标识即可）。

# 接下来我们再次点击左边页面中的翻译按钮让页面执行一次，看看变量会是什么（注意有可能需要点击debug的下一步让页面继续执行才可以看到参数）。
#
# 有两种方法查看变量如下图，一种是将鼠标移动到变量上即可，还有一种是在调试台打上变量名称即可。
# 可以看出变量e是我们需要翻译的语句，同理我们看下navigator.appVersion  ，哦吼原来是user-agent。
# *******注意：要点击翻译后才能进行debug！！！*******

# 现在我们已经搞清楚了所有的问题，那么接下来就是见证奇迹的时刻，我们将js的函数使用python构造出来，
# 看下是否可以得到我们想要的参数结果。

# import hashlib#用于md5加密
# import time
# import random
#
# def md5_b(str):
#     hash=hashlib.md5()
#     hash.update(str.encode('utf-8'))
#     return hash.hexdigest()
#
# data={}
#
# def get_data_params(t_str):
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
#     e=t_str
#     t=md5_b(user_agent)
#     r=str(int(time.time()*1000))#毫秒所以*1000
#     i=r+str(random.randint(0,10))
#     data['ts'] = r
#     data['bv'] = t
#     data['salt'] = i
#     data['sign'] = md5_b("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
#
# get_data_params('大家好')
# print(data)
# 这就是我们的复刻版构造函数了，我们看下结果是什么。
# 嗯，看起来挺像，那么我们接下来把其他不变的参数也添加进去，看看能否构造请求成功，接下来是完整代码。

import requests
import hashlib#用于md5加密
import time
import random

url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers={
"Accept":"application/json, text/javascript, */*; q=0.01",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Connection":"keep-alive",
"Content-Length":"251",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Cookie":"OUTFOX_SEARCH_USER_ID=-198948014@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1678156251.6498268; _ga=GA1.2.109926435.1582269589; UM_distinctid=170a4e98abc891-0b24cc8bee43ca-5e4f281b-144000-170a4e98abd72b; JSESSIONID=aaaPbNnhvgdpJe62qgofx; ___rl__test__cookies=1586153715407",
"Host":"fanyi.youdao.com",
"Origin":"http://fanyi.youdao.com",
"Referer":"http://fanyi.youdao.com/",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
"X-Requested-With":"XMLHttpRequest",
}

#data中的from与to参数代表着从什么语言翻译到什么语言，默认是中英互译
data={
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTlME",
}

#该函数用于字符串的md5加密
def md5_b(str):
    hash=hashlib.md5()
    hash.update(str.encode('utf-8'))
    return hash.hexdigest()

def get_data_params(t_str): # params：参数
    user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    e=t_str
    t=md5_b(user_agent)
    r=str(int(time.time()*1000))#毫秒所以*1000
    i=r+str(random.randint(0,10))
    data['i'] = e
    data['ts'] = r
    data['bv'] = t
    data['salt'] = i
    data['sign'] = md5_b("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
    return data

res=requests.post(url=url,headers=headers,data=get_data_params('你好啊，你在干什么呀?'))
print(res.text)

# 看下运行结果：
#
# {"translateResult":[[{"tgt":"Hello. What are you doing?","src":"你好啊，你在干什么呀?"}]],"errorCode":0,"type":"zh-CHS2en"}
# 好了，发现已经可以得到返回的json了，可以自己使用json库继续进行提取了，这样我们就破解了有道翻译的js加密，其他网站也类似这样操作就可以。

