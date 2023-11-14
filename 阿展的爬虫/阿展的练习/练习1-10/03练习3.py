# !/usr/bin/env python
# -*- coding: utf-8 -*-
# request入门（urllib）

# request作用：发送网络请求

# 1. request发送get请求：

# import requests
#
# # 准备起始的url地址
# start_url = 'https://login.taobao.com/member/login.jhtml?spm=a2e0b.20350158.1997563269.1.1c74468aMpxwzX&f=top&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585%26clk1%3D406b68f2980a10f2e918316752ef2845%26upsId%3D406b68f2980a10f2e918316752ef2845&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.186.100.196_3087163_1614995091808%3Bprepvid%3A201_11.186.100.196_3087163_1614995091808&clk1=406b68f2980a10f2e918316752ef2845'
#
# # 发送请求，获取响应
# # 构造headers：
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
#
# response = requests.get(start_url, headers=headers)
#
# # 解析响应，数据提取
#
# # request常用属性
# # 获取响应源码：字符串类型
#
# print(response.content, type(response.text))
# # response.content字节类型，需要decode()编码
# # 1字节=多少位？
# # 8位
# print(response.content, type(response.content))
# # 保存数据
#
# # 获取状态码
# print(response.status_code)
# if response.status_code == 200:
#     print('数据提取')
# else:
#     print('重新发送请求')
#
# # 不常用
# # 响应对应的请求头
# print(response.request.headers)
# # 响应头
# print(response.request.headers)
# # # 请求URL地址
# print(response.request.url)
#
# # 获取响应的URL地址
# print(response.status_code)
# print(response.url)
# # 通过此方法获取到重定向之后的URL地址
# # 应用场景：
# # 302重定向
#
# # 获取cookie
#
# # cookie：存储用户登录信息，保持登录状态
# # post
# print(response.cookies)
# # CookieJar
#
# # 获取json数据
# print(response.json())
# # 这个url返回的响应必须是json数据才能够使用response.json()方法
#
# # requests发送带headers的请求
#
# import requests
#
# # 准备起始的url地址
#
# for page in range(10):
#     start_url = f'https://login.taobao.com/member/login.jhtml?spm=a2e0b.20350158.1997563269.1.1c74468aMpxwzX&f=top&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585%26clk1%3D406b68f2980a10f2e918316752ef2845%26upsId%3D406b68f2980a10f2e918316752ef2845&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.186.100.196_3087163_1614995091808%3Bprepvid%3A201_11.186.100.196_3087163_1614995091808&clk1=406b68f2980a10f2e918316752ef2845&start={page * 25}&filter='
#     print(start_url)
#     # 发送请求，获取响应
#     headers = {
#         'Referer: https://login.taobao.com/',
#         'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
#     }
#     response = requests.get(start_url, headers=headers)
#     if response.status_code == 200:
#         print(response.content.decode())
#         print()
#         print()
#         print()
# # requests发送post请求
# # 应用场景：
# # get请求：以明文状态进行传输
# # 不安全
# import requests
#
# # # 会话操作的保持，让程序记录登录状态
# session = requests.session()
#
# # # 准备起始的url地址（寻找登录的url地址）
#
# start_url = 'https://login.taobao.com/member/login_agreement.htm?style=default&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585%26clk1%3D406b68f2980a10f2e918316752ef2845%26upsId%3D406b68f2980a10f2e918316752ef2845'
# headers = {
#     'Referer: https://login.taobao.com/',
#     'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# data = {
#     'ck': '',
#     'remember': 'true',
#     'name': '15738108997',
#     'password': '15738108997zhan'
# }
# session.post(start_url, data=data, headers=headers)
# next_url = 'https://login.taobao.com/member/login_agreement.htm?style=default&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585%26clk1%3D406b68f2980a10f2e918316752ef2845%26upsId%3D406b68f2980a10f2e918316752ef2845'
# response_1 = session.get(next_url, headers=headers)
# print(response_1.content.decode())

# 人人网：

import requests

# 准备起始的url地址
start_url = 'http://www.renren.com/'

data = {
    'name': '17865695628',
    '_rtk': '15738108997zhan'
}

# 使用代理
# 防止被追踪

# import requests
# proxy = {
#     '49.86.178.113':'9999'
# }
# start_url = 'https://www.baidu.com'
# response = requests.get(start_url, proxies=proxy)
# print(response.content.decode())
