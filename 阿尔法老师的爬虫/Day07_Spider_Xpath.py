"""
课题：数据提取之lxml与xpath
"""

"""1.lxml的安装"""
# pip install lxml
# pip install lxml -i https://mirrors.aliyun.com/pypi/simple
# 非常的便捷


# 作用：
# 可以将html源码，通过lxml转换为具有xpath语法熟悉的对象

# 子孙节点
# //a 找到所有的a标签
# //div 找到所有的div标签
# //p   找到所有的p标签
# .  当前节点
# ..  cd ..
# ..  回到上一级节点
# @   提取标签的某一个属性 ，可以通过@属性名进行获取
# text()  提取标签的文本内容

# 直接右击标签，copy_xpath语法




"""2.使用lxml序列化html字符串数据"""
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
    <author>Kurt Cagle</author> 
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

</bookstore>
"""
# from lxml import etree
# # 通过lxml转换为具有xpath语法熟悉的对象
# html = etree.HTML(txt)
# data_1 = html.xpath('xpath语法')
# # result = html.xpath('//book[4]/price/text()')
# result = html.xpath('//book[@cover="paperback"]/price/text()')
# print(result)


# data = html.xpath('//book[3]/author[2]/text()')
# print(data)

# 1.起点小说爬虫
# 2.安居客房源信息网-房源数据    --  外包需求
# 500-oo   数据量

# https://www.qidian.com/search?kw=%E4%B8%BB%E7%A5%9E%E6%8C%82%E4%BA%86
# https://www.qidian.com/search?kw=%E4%B8%BB%E7%A5%9E%E6%8C%82%E4%BA%86
# %E4%B8%BB%E7%A5%9E%E6%8C%82%E4%BA%86 主神挂了

from urllib.parse import quote
from requests_html import HTMLSession
session = HTMLSession()
import re
title = input("请输入小说名称")
title = '从零开始的富豪人生'
# 拼接
# 手机版
start_url = 'https://m.qidian.com/search?kw=' + quote(title)
# https://www.qidian.com/search?kw=%E4%B8%BB%E7%A5%9E%E6%8C%82%E4%BA%86
# https://m.qidian.com/
print(start_url)

# 手机版
headers = {
    'cookie': '_qda_uuid=bfecb5d9-a0b7-d076-dfbe-3dc08498459f; newstatisticUUID=1578364957_1604014157; qdrs=0%7C3%7C0%7C0%7C1; qdgd=1; showSectionCommentGuide=1; mrecUUID=e6886710154aceaa2b42b71669adf97b; _csrfToken=ke1OMTYda0hLVKxjJxBmqGtargy5OcCFtsuK54n1; lrbc=1115277%7C22058859%7C0%2C1009817672%7C375339314%7C0%2C63856%7C340494470%7C1; rcr=1115277%2C1009817672%2C63856; _yep_uuid=d5ffa660-ea39-9eae-4fd5-7029f4fb9850; hiijack=0; tf=1; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_H_Search%22%2C%22l1%22%3A2%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%7D',
    'referer': 'https://www.qidian.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
# https://m.qidian.com/book/1019189022 梦回大明春
# https://m.qidian.com/book/1025548403 从零开始的富豪人生

response = session.get(start_url)
# 提取第一页所有小说的href链接属性
href_list = response.html.xpath('//ol[@id="books-"]/li/a/@href')
# print(href_list)
# 提取第一部小说
one = response.html.xpath('//ol[@id="books-"]/li/a/div/div/h4/mark/text()')
one.remove(one[0])

# 提取所有小说名称
title_list = response.html.xpath('//ol[@id="books-"]/li/a/div/div/h4/text()')
# print(one + title_list)

# print(len(href_list), len(one + title_list))
# print(response.content.decode())
# 1025649259 主神挂了在对方服务器数据库中的 id

# https://m.qidian.com/book/1025649259
# https://m.qidian.com/book/1017559907

# https://m.qidian.com/book/1025649259/629790265


# https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=ke1OMTYda0hLVKxjJxBmqGtargy5OcCFtsuK54n1&bookId=1025649259&chapterId=629790265

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



































