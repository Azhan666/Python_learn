# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 百度贴吧爬取

import requests # 导入request模块

from urllib.parse import quote, unquote # quote unquote: urllib里面的函数，用于屏蔽特殊字符，因为url不允许出现特殊字符

title = input('请您输入贴吧名称：') # 获取用户要爬取的贴吧标题
page = input('请您输入要爬取的页数：') # 获取用户要爬取的页码数，page：页码
headers = {
    # 构造一个headers，模拟浏览器访问服务器，获取响应，避免被反爬
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'Host': 'tieba.baidu.com',
    'Upgrade-Insecure-Requests': '1' # html Upgrade-Insecure-Requests:1 请求头
# HTTP Upgrade-Insecure-Requests 请求头向服务器发送一个客户端对HTTPS加密和认证响应良好，并且可以成功处理的信号，可以请求所属网站所有的HTTPS资源。
# 在https页面中，如果调用了http资源，那么浏览器就会抛出一些错误。为了改变成这一状况，chrome(谷歌浏览器)会在http请求中加入 ‘Upgrade-Insecure-Requests: 1’ ，服务器收到请求后会返回 “Content-Security-Policy: upgrade-insecure-requests” 头，告诉浏览器，可以把所属本站的所有 http 连接升级为 https 连接。
}

# 准备起始的url地址
for num in range(int(page)): # 如果用户输入的爬取页码在可爬范围内
    start_url = f'https://tieba.baidu.com/f?kw={quote(title)}&pn={50*num}' # quote：屏蔽特殊字符，url中不允许出现特殊字符
    print(start_url) # 请求成功则打印起始的URL地址
    start_url_1 = 'https://tieba.baidu.com/f?kw=' + quote(title) #
    start_url_2 = ''.join(['https://tieba.baidu.com/f?kw=',quote(title)]) # join()方法连接字符串
    print(start_url_2)
    # 2.发送请求，获取响应
    response = requests.get(start_url, headers=headers)
    # 3.解析响应，数据提取
    data = response.content
    # 4.保存数据
    #print(data)
    with open(title + '_' + str(num) + '.html', 'wb')as f:
        f.write(data)
    print(f'{title}----贴吧----第{num+1}页保存完成')