"""
课题：Requests与Requests-Html深入学习
"""

"""1.Requests处理cookie相关的请求"""
# 什么是cookie
# cookie存储用户信息
"""案例：登录豆瓣为例"""
# import requests
# session = requests.session()
#
# start_url = 'https://accounts.douban.com/j/mobile/login/basic'
# data = {
#     'ck': '',
#     'remember': 'true',
#     'name': '16607440667',
#     'password': 'aef1234562'
# }
# headers = {
#     'Host': 'accounts.douban.com',
#     'Origin': 'https://accounts.douban.com',
#     'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
# }
#
# headers_1 = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
# }
# # 获取登录之后的cookie，维持会话保持
# print(session.post(start_url, data=data, headers=headers).content.decode())
# # https://www.douban.com/
# next_url = 'https://www.douban.com/'
# response = session.get(next_url, headers=headers_1)
# print(response.text)
#
# print(response.content.decode())
# import requests
# """2.requests.utils.dict_from_cookiejar处理cookie"""
# start_url = 'https://www.baidu.com'
# response = requests.get(start_url)
# print(response.cookies)
# print(requests.utils.dict_from_cookiejar(response.cookies))

"""使用cookie登录"""
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
# 1.将cookie字符串转换成字典
# cookie_list = cookie_str.split('; ')
# # print(cookie_list)
# cookie_dict = {}
# for cookie in cookie_list:
#     c_data_list = cookie.split('=')
#     cookie_dict[c_data_list[0]] = c_data_list[1]
# print(cookie_dict)

# 字典推导式
#
# cookie_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_str.split('; ')}
# # print(cookie_dict)
# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
# }
# start_url = 'https://www.douban.com/'
# response = requests.get(start_url, cookies=cookie_dict, headers=headers)
# print(response.content.decode())

# dict_1 = {}
# print(dict_1)
#
# dict_1['name'] = 'xiaoming'
# print(dict_1)

"""3.Requests处理ssl证书错误"""
# ssl证书:
# s:ssl证书：购买域名，免费送的，购买：让数据的传递更安全
# # ssl证书到期：ssl证书错误
# response = requests.get(start_url, verify=False)

"""4.Requests禁止页面重定向"""
# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
# }
# start_url = 'https://v.douyin.com/eec2XS7/'
# response = requests.get(start_url, allow_redirects=False, headers=headers)
# print(response.content.decode())
#
# response_1 = requests.get(start_url,  headers=headers)
# print(response_1.url)
# 町田一家买下近500平米的超级庭院，却无法对付疯长的杂草和各种害虫，院子完全浪费，于是改造大师出手拯救...  https://v.douyin.com/eec2XS7/ 复制此链接，打开Dou音搜索，直接觀kan視頻！
"""5.超时参数的使用"""
# import requests
# proxy = {'127.0.0.1':'9999'}
# start_url = 'https://www.baidu.com'
# try:
#     response = requests.get(start_url, timeout=5, proxies=proxy)
#     with open('代理.txt', 'a+')as f:
#         f.write(str(proxy))
# except:
#     pass

"""6.超时参数结合retrying模块的使用"""
# import requests
# from retrying import retry
#
# proxy = {
#     'https': "https://115.221.241.68:9999"
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
# }
# # 私有方法
# @retry(stop_max_attempt_number=5)
# def _parse_url(url):
#     print('执行一次')
#     response = requests.get(url, timeout=3, proxies=proxy)
#     # 断言:非常肯定某一件事，当这件事被否定的时候，会发生报错
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

"""7.Requests-html的使用"""
# pip install requests-html
# pip install requests-html -i https://mirrors.aliyun.com/pypi/simple

# from requests_html import HTMLSession
# session = HTMLSession()
#
# session.get()

""""""

# import requests
#
# session1 = requests.session()
#
# from requests_html import HTMLSession
#
# session2 = HTMLSession()
"""获取源码"""

"""获取状态码"""

"""获取响应的url地址"""

"""获取响应对应的请求头"""

"""获取响应头"""

"""获取cookie"""

"""将响应的json数据转化成字典数据"""

"""发送带参数的请求"""

"""第一种"""

"""第二种"""

"""案例：酷我音乐破解VIP付费下载"""

# from requests_html import HTMLSession
# session = HTMLSession()
# from urllib.parse import quote
# import os
#
# singer = quote(input('请输入歌手：'))
# # 1.准备start_url
# start_url = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={singer}&pn=1&rn=30&httpsStatus=1&reqId=caa89750-7cea-11eb-ac48-0565e0f277eb'
# headers = {
#     # 用户信息
#     'Cookie': '_ga=GA1.2.876172058.1604060182; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1613741090,1614258676,1614426612,1614863276; _gid=GA1.2.289411456.1614863276; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1614863328; kw_token=K6606TBNGCF',
#     # 一把钥匙
#     'csrf': 'K6606TBNGCF',
#     # 域名
#     'Host': 'www.kuwo.cn',
#     # 这个页面上一次请求的页面
#     'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
#     # 浏览器的标识，让我们的爬虫程序模拟浏览器，达到欺骗服务器的效果
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
# }
# # 2.发送请求，获取响应
# response = session.get(start_url, headers=headers)
# # 3.数据解析，数据提取,通过.json方法，会将json数据直接转化成字典数据
# data_json = response.json()
# # 字符串形式的字典数据,
# # "{'name':'xiaoming'}"
# mp3_list = data_json['data']['list']
#
# # http://www.kuwo.cn/url?format=mp3&rid=140064959&response=url&type=convert_url3&br=128kmp3&from=web&t=1614864179973&httpsStatus=1&reqId=bd955a61-7cec-11eb-9153-eb3ada92d759
# # 是稻香这一首歌曲存放在数据库的编号id
# for data in mp3_list:
#     # 获取歌曲名称
#     name = data['name']
#     # 获取歌曲数据库的rid
#     rid = data['rid']
#     # 获取单首歌曲的播放json信息的url地址
#     next_url = f'http://www.kuwo.cn/url?format=mp3&rid={rid}&response=url&type=convert_url3&br=128kmp3&from=web&t=1614864179973&httpsStatus=1&reqId=bd955a61-7cec-11eb-9153-eb3ada92d759'
#     # 发送请求
#     mp3_response = session.get(next_url).json()
#     # 提取单首歌曲的播放的url地址-----他只是一个字符串
#     mp3_url = mp3_response['url']
#     # 对歌曲播放的url地址发送请求，获取二进制数据
#     mp3_data = session.get(mp3_url).content
#     """4.数据的保存"""
#     os_path = './酷我MP3/'
#     if not os.path.exists(os_path):
#         os.mkdir(os_path)
#     with open(os_path + name + '.mp3', 'wb')as f:
#         f.write(mp3_data)
#     print(f'{name}=====下载完成！！！logging=====')

"""快手评论正文下载"""
from requests_html import HTMLSession
session = HTMLSession()


start_url = 'https://video.kuaishou.com/graphql'
headers = {
    'content-type': 'application/json',
    'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_516b5e505a73ea248d313c3ba769882e',
    'Host': 'video.kuaishou.com',
    'Origin': 'https://video.kuaishou.com',
    'Referer': 'https://video.kuaishou.com/short-video/3xqk9kz8z59ds54?authorId=3xpbiv5ppefwdvm&streamSource=brilliant&hotChannelId=00&area=brilliantxxrecommend',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
}
data = {"operationName":"commentListQuery","variables":{"photoId":"3xqk9kz8z59ds54","pcursor":""},"query":"query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}

response = session.post(start_url, json=data, headers=headers).json()
print(response)

from requests_html import HTMLSession
session = HTMLSession()

start_url = 'https://www.baidu.com'
response = session.get(start_url)
print(response.text)
print(response.content.decode())
# 获取源码
print(response.html.html)
