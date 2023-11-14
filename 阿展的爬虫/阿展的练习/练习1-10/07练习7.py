# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 课题：数据提取之lxml与xpath

# 1.lxml的安装
# pip install lxml
# pip install lxml -i https://mirrors.aliyun.com/pypi/simple

# 作用：
# 可以将html源码，通过lxml转换为具有xpath语法熟悉的对象

# 子孙节点
# //a 找到所有的a标签
# //div 找到所有的div标签
# //p 找到所有的p标签
# .当前节点
# .. cd ..
# .. 回到上一级节点
# @ 提取标签的某一个属性，可以通过@属性名进行获取
# text() 提取标签的文本内容


# 2.使用lxml序列化html字符串数据


txt = """
<bookstore>

  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>

  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>

  <book category="web">
    <title lang="en">XQuery Kick Start</title>
    <author>James McGovern</author>
    <author>老王同学</author>
    <author>Kurt Cagle</author>
    <author>James Linn</author>
    <author>Vaidyanathan Nagarajan</author>
    <year>2003</year>
    <price>49.99</price>
  </book>

  <book category="web" cover="paperback">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>

</bookstore>"""

# 导一下包：
# from lxml import html
# etree = html.etree # etree模块引用方式
# html = etree.HTML(txt) # etree模块引用方式
# html.xpath('xpath语法') # xpath语法

# 下面我们进入实战：提取“老王同学”

# 提取老王同学我们要知道：老王同学所在的标签是author标签

# 使用data接收xpath，首先，使用双斜杠找到所有的book
# 使用单斜杠找到book标签下的author标签，之后提取文本内容
# data = html.xpath('//book/author[2]/text()')
# 做一个print文本输出：
# print(data)
# 输出之后我们发现，它提取的结果有很多，这是因为其它book标签下面也有author标签
# 所以我们需要告诉我们的程序，我们要找的author标签是在第二个author处
# 所以我们在author标签后面传入一个2（顺序），因为要提取的author是第二个author：('//book/author[2]/text()')
# 再次运行后，我们发现“老王同学”已经被单独成功提取
# 但是，上面要找的book标签最好要通过它的属性做一个定位：
# [@category="web"]/author[2]/text(),加上[@category="web"]，做一个定位
# 若不做定位的话，其它标签处若也有author，就会出现误提取

# 还有一种方法，就是我可以告诉我的程序，我要找的是第几个book，


# 下面我们要提取价格：
from lxml import html
import re
etree = html.etree
html = etree.HTML(txt)
data_1 = html.xpath('xpath语法')
result = html.xpath('//book[4]/price/text()') # 要找的book标签为第四个book标签下的price，/text()提取price其中的文本内容
# print(result)


# 案例：
# 1.起点小说爬虫
# 2.安居客房源信息网-房源数据 --外包需求
# 500-+oo

# 地址栏的url地址：
# https://www.qidian.com/search?kw=%E4%BA%BA%E5%9C%A8%E6%81%B6%E5%9C%9F%E6%97%A0%E9%99%90%E5%A4%8D%E6%B4%BB
# https://www.qidian.com/search?kw=%E4%BA%BA%E5%9C%A8%E6%81%B6%E5%9C%9F%E6%97%A0%E9%99%90%E5%A4%8D%E6%B4%BB # 拼接后生成的字符串
# %E4%BA%BA%E5%9C%A8%E6%81%B6%E5%9C%9F%E6%97%A0%E9%99%90%E5%A4%8D%E6%B4%BB：人在恶土无限复活

# 字符串拼接解析方法：
from urllib.parse import quote
from requests_html import HTMLSession # 爬取小说所需的模块
session = HTMLSession()
title = input("请输入小说名称:")

# 拼接：
start_url = 'https://m.qidian.com/book/1019189022/0' + quote(title)
# https://m.qidian.com/book/1979049/0 手机版的起始url地址
print(start_url)

# 构造headers：
headers = {
    # 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding':'gzip, deflate, br',
    # 'accept-language':'zh-CN,zh;q=0.9',
    # 'cache-control':'max-age=0',
    # 'cookie':'_csrfToken=dyg90wcvUCYnKpuUZ806OQT2e2Vt4vYc0Fwwo3AK; newstatisticUUID=1615209092_795958365; qdrs=0%7C3%7C0%7C0%7C1; qdgd=1; showSectionCommentGuide=1; rcr=1115277; lrbc=1115277%7C22087045%7C0; mrecUUID=94cde428cfbd0dc91ba4c189b97b246d; _yep_uuid=477a9916-abee-83a2-115f-dcf43ce18582; hiijack=0; e1=%7B%22pid%22%3A%22qd_P_Searchresult%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_Searchresult%22%2C%22eid%22%3A%22qd_S04%22%2C%22l1%22%3A3%7D',
    # 'referer':'https://www.qidian.com/',
    # 'sec-ch-ua':'Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    # 'sec-ch-ua-mobile':'?0',
    # 'sec-fetch-dest':'document',
    # 'sec-fetch-mode':'navigate',
    # 'sec-fetch-site':'same-origin',
    # 'sec-fetch-user':'?1',
    # 'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Mobile Safari/537.36'
}
response = session.get(start_url, headers=headers)
print(response.content.decode())
# 经过响应数据的格式化，我们发现返回的数据是对应小说的数据，但是太过杂乱，我们下面使用xpath提取操作，只提取需要的内容：
# 现在我们要提取a标签，但是只按照a标签还不行，a标签太多，提取不够精准，因此我们再使用a标签的父一级标签：li标签，
#
href_list = response.html.xpath('//a')

# 由返回的数据可知，电脑版无法爬取全部内容，需要电脑浏览器也进入手机版
# 并不只是headers是手机版就行，起始的url地址也要是手机版

# https://m.qidian.com/book/1979049
# https://m.qidian.com/book/1025325411
# 末尾的数组是该书在服务器里的id

href_list = response.html.xpath('//ol[@id="book-"]/li/a')
title_list = response.html.xpath('//ol[@id="book-"]/li/a')
# 提取所有小说名称
title_list = response.html.xpath('//ol[@id="books-"]/li/a/div/div/h4/text()')
print(one + title_list)
print(len(href_list), len(one + title_list))
print(response.content.decode())
print(href_list)
# 直接使用href_list接收xpath操作

# # 提取第一部小说
one = response.html.xpath('//ol[@id="books-"]/li/a/div/div/h4/mark/text()')
one.remove(one[0])

# 同时循环两个列表
for href, name in zip(href_list, one + title_list):
    # print(name, href)
    bookid = href[6:]
    next_url = 'https://m.qidian.com' + href + '/0'
    response = session.get(next_url, headers=headers)
    # print(response.content.decode())
    next_id = re.findall('data-chapter-id="(.*?)"', response.content.decode())[0]
    next_id = ''.join(next_id)
    # print(next_id)
    page_url = f'https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=ke1OMTYda0hLVKxjJxBmqGtargy5OcCFtsuK54n1&bookId={bookid}&chapterId={next_id}'
    response = session.get(page_url, headers=headers)
    # print(html.html.html)
    # 翻页的id提取
    next_id = re.findall('"next":(.*?),', response.content.decode())[0]
    # print(page_id)
    page_url = f'https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=ke1OMTYda0hLVKxjJxBmqGtargy5OcCFtsuK54n1&bookId={bookid}&chapterId={next_id}'
    response = session.get(page_url, headers=headers)
    print(response.content.decode())
    # 递归处理

    break

    # 提取翻页id

"""起点小说"""
# 1.进入手机模式
# 2.通过用户搜索小说文本名称进入搜索结果页(提取小说id，名称)
# 3.url地址的拼接
# https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=ke1OMTYda0hLVKxjJxBmqGtargy5OcCFtsuK54n1&bookId=1025649259&chapterId=629790265
