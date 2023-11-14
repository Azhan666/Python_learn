# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 课题：request处理cookie相关的请求
# 什么是cookie？
# cookie用于存储用户信息，保持登录状态
# 案例：登录豆瓣为例

# import requests
# session = requests.session() # session:登录
#
# start_url = 'https://www.douban.com/'
# data = {
#     'ck':'',
#     'remember': 'true',
#     'name': '16607440667',
#     'password': 'aef123456'
# }
# headers = {
#     'Host': 'www.douban.com',
#     'Origin': 'https://www.douban.com',
#     'Referer': 'https://www.douban.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
#
# headers_1 = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# # 获取登陆之后的cookie，维持会话保持
# print(session.post(start_url, data=data, headers=headers).content.decode())
# # https://www.douban.com/
# next_url = 'https://www.douban.com/'
# response = session.get(next_url, headers=headers_1)
# print(response.text)
# print(response.content.decode())
# import requests
# # 2.requests.utils.dict_from_cookiejar处理cookie
# start_url = 'https://www.baidu.com'
# response = requests.get(start_url)
# print(response.cookies)
# print(requests.utils.dict_from_cookiejar(response.cookies))
# """使用cookie登录"""
# cookie_str = """douban-fav-remind=1; _vwo_uuid_v2=D4EDEB274998EF9670C11D9789C7C93BA|78d9187b2c765cfc0c80ed776\
# 7048abb; _ga=GA1.2.1416200646.1568801148; Hm_lvt_19fc7b106453f97b6a84d64302f21a04=1596096825; __utmv=30149280\
# .22281; ll="118267"; bid=qRD3Npr76rc; douban-profile-remind=1; __yadk_uid=3y414E8QNxM7v369WbTHNe5N5cM03gHZ; _\
# _gads=ID=aa84b9a3cc19bd7e-2220e3ba8cc5001d:T=1609855904:RT=1609855904:S=ALNI_MbGKQmnMAg21iJeosnlvmmOvPbTBQ; p\
# ush_doumail_num=0; push_noty_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1614859294%2C%22https%3A%2F%2Fww\
# w.baidu.com%2Flink%3Furl%3DT0KZZbcRPEpzyNd9gDqvGg5uQObSIRSEK8xZ3ZsAA1bvfCYY7jvowtI5m5bHrl9B%26wd%3D%26eqid%3D\
# e50d72b200025a7d000000066040cc1b%22%5D; _pk_id.100001.8cb4=9d88f7423196bb38.1570610339.41.1614859294.16147750\
# 58.; _pk_ses.100001.8cb4=*; __utma=30149280.1416200646.1568801148.1614775058.1614859295.51; __utmc=30149280; \
# __utmz=30149280.1614859295.51.38.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=30149280.1.10.161485929\
# 5; dbcl2="222817495:OaK5d09CZ9U"""
#
# # 将cookie转化为字典
# cookie_list = cookie_str.split('; ')
# # print(cookie_list)
# cookie_dict = {}
# for cookie in cookie_list:
#     c_data_list = cookie.split('=')
#     cookie_dict[c_data_list[0]] = c_data_list[1]
# print(cookie_dict)
#
# # 字典推导式
# cookie_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_str.split('; ')}
# # print(cookie_dict)
# import requests
# headers = {
#     'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# start_url = 'https://www.douban.com/'
# response = requests.get(start_url, cookie=cookie_dict, headers=headers)
# print(response.content.decode())
#
# dict_1 = {}
# print(dict_1)
#
# dict_1['name'] = 'hezhan'
# print(dict_1)

# requests处理ssl证书错误
# sll证书：
# s：ssl证书：购买域名，免费赠送的，购买：燃数据的传递更安全
# # ssl证书到期：ssl证书错误
# response = requests.get(start_url, verify=False)

# requests禁止页面重定向
# import requests
# headers = {
#     'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# start_url = 'https://v.douyin.com/eec2XS7/'
# response = requests.get(start_url, allow_redirects = False, headers=headers)
# # allow:允许，redirects：重定向
# print(response.content.decode())
#
# response_1 = requests.get(start_url, headers=headers)
# print(response_1.url)
# 町田一家买下近500平米的超级庭院，却无法对付疯长的杂草和各种害虫，院子完全浪费，于是改造大师出手拯救...  https://v.douyin.com/eec2XS7/ 复制此链接，打开Dou音搜索，直接觀kan視頻！

# 超时参数的使用
# import requests
# proxy = {'127.0.0.1':'9999'}
# start_url = 'https://www.baidu.com'
# try:
#     response = requests.get(start_url, timeout=5, proxies=proxy)
#     with open('代理.txt', 'a+')as f:
#         f.write(str(proxy))
# except: # except:除外
#     pass
#
# # 超时参数结合retrying模块的使用
# import requests
# from retrying import retry
#
# proxy = {
#     'https': "https://115.221.241.68:9999"
# }
# headers = {
#     'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# # # 私有方法
# @retry(stop_max_attempt_number=5)
# def _parse_url(url):
#     print('执行一次')
#     response = requests.get(url, timeout=3, proxies = proxy)
#     # 断言：非常肯定一件事，当这件事被否定的时候，会发生报错
#     assert response.status_code == 200
#     return response.content.decode()
#
# def parse_url(url):
#     try:
#         html = _parse_url(url)
#     except Exception as e:
#         print(e)
#         html = None
#     return html
#
# if __name__ == '__main__':
#     url = 'https://www.baidu.com'
#     h = parse_url(url)
#     print(h)
#
# # requests-html的使用
# # pip install requests-html
# # pip install requests-html -i https://mirrors.aliyun.com/pypi/simple
# # pip命令加-i：换源，上述为阿里云服务器
#
# from requests_html import HTMLSession
# session = HTMLSession()
#
# session.get()
#
# import requests
#
# session1 = requests.session()
#
# from requests_html import HTMLSession
#
# session2 = HTMLSession()
# # 获取源码
#
# # 获取状态码
#
# # 获取响应的url地址
#
# # 获取响应对应的请求头
#
# # 获取响应头
#
# # 获取cookie
#
# # 将响应的json数据转化为字典数据
#
# # 发送带参数的请求
#
# # 第一种
#
# # 第二种

# 案例：酷我音乐爬取vip歌曲：

# 导模块部分：
from requests_html import HTMLSession
session = HTMLSession()
from urllib.parse import quote
import os
print("欢迎使用音乐爬虫！阿展提醒您，适度娱乐，健康生活，此程序仅供学习娱乐交流！")
singer = quote(input('请输入歌手：'))
# 1.准备start_url
start_url = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={singer}&pn=1&rn=30&httpsStatus=1&reqId=55f29a40-7e53-11eb-90e7-c3453c336f36'
headers = {
    # cookie： 用户信息
    'Cookie': '_ga=GA1.2.1402840506.1614310872; _gid=GA1.2.1727781171.1615017884; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1614310872,1615017884; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1615017884; kw_token=MBL82JZS4KP',
    # csrf：相当于一把钥匙，只有拿了钥匙才能真正访问获取url地址的返回信息
    'csrf': 'MBL82JZS4KP',
    # Host：域名
    'Host': 'www.kuwo.cn',
    # referer：这个页面上一次请求的页面
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    # ua：浏览器的标识，让我们的爬虫通过模拟浏览器，达到欺骗服务器的效果
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}

# 2.发送请求，获取响应
response = session.get(start_url, headers=headers)
# 3.数据解析，数据提取，通过json()方法，会将json数据直接转化为字典数据
# 因为response返回的是json数据，所以得通过json方法转化为字典数据
data_json = response.json() # 使用data_json来接收response.json()
# json数据：字符串形式的字典数据
# 如：
# {'name':'hezhan'} # 字典数据
# "{'name':'hezhan'}" # json数据
# print(data_json) # 打印一下，看看是否获取到了response数据
# print(data_json['data']['list']) # 因为要爬取的歌曲在list的列表里面，所以要请求访问list列表
# 为了方便，下面我们用MP3_list来接收一下歌曲列表：
mp3_list = data_json['data']['list']
# 接下来我们要做第二步抓包操作，首先将已抓取的包做一个清空，
# 然后找一个可播放的歌曲，点击播放后暂停，右击谷歌浏览器任务栏界面打开新的无痕窗口，
# 重新抓包，找到稻香，找到包里后缀为MP3的url，打开新窗口访问该url
# 发现进入的是稻香的播放页面，所以要爬取歌曲，对该地址进行请求即可
# 然后回到headers，找到requests url，把它的url地址拿过来：
# http://www.kuwo.cn/url?format=mp3&rid=140064959&response=url&type=convert_url3&br=128kmp3&from=web&t=1615020522735&httpsStatus=1&reqId=c1219f00-7e58-11eb-90e7-c3453c336f36
# 可以看到url地址中有rid=140064959，这个id就是稻香这一首歌曲在数据库的编号id
# 所以，我们要爬取歌曲，就要将id替换成要爬取的歌曲的id即可
# 不仅要提取歌曲id，还要提取歌曲名字
# 下面，我们用for循环提取id和歌曲名,即大列表里所有的歌曲id和名字
for data in mp3_list: # 如果歌曲文件在大列表里
    name = data['name'] # name=rid
    rid = data['rid'] # 通过观察网页源码，可看到rid没有嵌套，直接用rid即可
    print(name, rid)
# 再次打印，我们可以发现，歌曲的名字，id都打印出来了
# 下面我们需要拼接新的url地址,直接把上面的url地址拿下来即可
    next_url = f'http://www.kuwo.cn/url?format=mp3&rid={rid}&response=url&type=convert_url3&br=128kmp3&from=web&t=1615020522735&httpsStatus=1&reqId=c1219f00-7e58-11eb-90e7-c3453c336f36'
# 将稻香的rid换成{rid}即可，（字符串拼接）
# 拼接完成之后，我们发送新的请求，获取新的response
# 我们用mp3_response来接收新的response
    mp3_response = session.get(next_url).json()
    print(mp3_response)
    print()

# 再次打印，我们发现歌曲的信息及url已经打印出来了，点击链接可播放对应歌曲
# 下面我们进入数据提取环节了
# 我们用MP3_url提取歌曲的url地址
    mp3_url = mp3_response['url']
# url地址已经提取出来了，下面只需向url地址发送请求，获取歌曲的二进制数据即可
# 下面我们用mp3data来命名
    mp3_data = session.get(mp3_url).content # content:用来获取二进制数据
# 下面我们进入数据保存环节
# 保存数据就要保存到我们自己指定的文件夹，所以就需要导入os操作系统命令模块
    os_path = './酷我爬虫MP3/' # 使用os_路径来保存到指定文件夹,文件夹后后加个/
# 因为上述文件夹还没有创建，因此，下面我们要写一个判断：
    if not os.path.exists(os_path): # 如果这个路径文件夹没有
        os.mkdir(os_path) # 就创建一个指定路径的文件夹
    with open(os_path + name + '.mp3', 'wb')as f: # 保存数据，路径+标题+数据格式
        f.write(mp3_data) # 以写入的形式保存数据
    print(f'{name}====下载完成！！！logging====') # 添加下载提示

# 到此，周杰伦的歌曲已经成功爬取下载！下面我们完善代码，用于下载任意歌手的歌曲！
# 完善步骤：在链接使端加一个f，在链接key=后面格式化字符串部分改为{singer}，接收用户输入的歌手
# 由测试发现，在部分歌曲下载时会报错，这是因为部分歌曲下载时返回的不是json数据，
# 或者请求速度太快，被服务器发现，这个问题可以用替换ua解决


# 小知识：session库比request多了一个状态保持功能