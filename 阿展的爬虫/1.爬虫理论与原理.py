# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.什么是爬虫？

# 爬虫是一个程序，按照一定的规则模拟人的操作抓取互联网的信息。
# 信息采集、商品销量监测、短信轰炸等。
# 5k一个平台，把学费挣回来。

# 2.爬虫能够干什么？

# 数据整合--->集成产品:hao123
# 爬虫公司，数据
# 爬取上海市全市的公司资料：300万家公司，12k

# 3.爬虫的应用市场（前景）。

# 人工智能、大数据时代。
# 公司需要巨大的数据支撑--->预算吃紧
# 有许多公司想要白嫖数据--->招聘爬虫工程师
# 数据分析
# 警告：远离灰色爬取，拒绝非法。
# 企业级用人需求
# 外包需求案例--->微博评论、安居客房源信息

# 4.爬虫的分类

# 聚焦爬虫：针对某一个平台开发的爬虫

# 通用爬虫（如百度）

# 爬取电商平台数据：大分类-->小分类-->细化：品牌、种类、尺码、款式等。

# 5.爬虫的原理
import requests # 导包模块
# 聚焦爬虫：
# # 1.准备起始的url地址
# start_url = 'http://pic.netbian.com//uploads/allimg/210226/000842-1614269322985f.jpg'
# # 2.发送请求，获取响应
# response = requests.get(start_url) # response：响应
#
# # 3.数据解析，数据提取
# data = response.content # 获取二进制数据
# print(data) # 做一个验证，查看是否获取到二进制数据
# # 4.保存数据
# with open('1.爬取的第一张图片.jpg', 'wb')as f: # 传入文件参数，‘wb’表示二进制数据，as f：给前面保存文件的操作取一个别名
#     f.write(data) # 写入二进制数据

# 6.网址的构成

# 超文本传输协议:
# 不限格式和大小

# 1.什么是url地址？
# http://www.baidu.com/

# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=python&oq=%25E5%25BD%25BC%25E5%25B2%25B8%25E5%259B%25BE%25E7%25BD%2591&rsv_pq=dfee0b23000000e1&rsv_t=5100e%2FApcUHY7VxE4skVhBHOQpJ4Q0iaUJ6U0WdlHAZFM8A%2BHNtCACcol0Q&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&rsv_btype=t&inputT=2468&rsv_sug4=4280
# 协议部分：http/https
# s:SSL证书：域名证书
# 爬取网页时会遇到SSL证书过期：如何跳过SSL证书过期的爬取？
# 域名部分：www.baidu.com
# s:资源路径部分：/uploads/allimg/210226/
# 资源部分：000842-1614269322985f.jpg # 类似于文件路径

# 每一个url地址都是一种资源的体现。

# 参数部分：wd=python
# 注意点：只有get请求，才会将参数部分显示在url地址中。

# cookie：储存个人信息的字段，常用于登陆之后的状态保持

# 页面加载方式

# 决定了数据的来源:

# 同步:数据在源码中

# 异步：数据不在源码中
# xhr（小黄人）：异步加载请求包的抓取
# ajax（阿贾克斯）：
# 网页的数据是靠异步加载渲染上去的

# 在爬虫开发过程中，如果页面上看到的数据不在源码中，
# 则这些数据是靠异步加载ajax请求，将数据渲染上去的。

# 8.http和https的请求说明：
# 一个请求由哪些构成？
# get请求：
# 请求协议
# 请求头
# 请求体
# 空行

# post请求：
#

import requests
# 1.准备起始的url地址
start_url = 'https://www.baidu.com/'
# 2.发送请求，获取响应 user-agent:浏览器相关信息
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
response = requests.get(start_url, headers=headers) # 第一个请求，有请求头
response_1 = requests.get(start_url) # 第二个请求，没有请求头
# 3.解析响应，提取数据
data = response.content.decode() # 获取源码数据
data_1 = response_1.content.decode()
# 4.保存数据
print(data)
print()
print()
print()
print('============================用于区分两个请求=============================')
print(data_1)

# 由运行结果可知，没有请求头的请求打印的结果非常少

# headers：没有添加headers中的user-agent，代表的是程序在访问，很容易被反爬。

# 9.爬虫协议

# 若遵守，则爬取不到任何有价值的信息
# 仅仅是道德层面上的约束

# 10.状态码

# 记住常见的即可
# 200：请求成功
# 302：重定向（跳转到其它url地址）
# 404（服务器无法找到被请求的页面）
# 403（服务器拒绝访问，权限不够）。403：你被反爬了。
# 服务器端出现错误，常用500（请求未完成。服务器遇到不可预知的情况，出了bug）。


