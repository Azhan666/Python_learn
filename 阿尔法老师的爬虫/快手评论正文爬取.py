# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 导模块部分：
from requests_html import HTMLSession
from jsonpath import jsonpath
session = HTMLSession()

# 准备起始的url地址
start_url = 'https://video.kuaishou.com/graphql'

# 构造headers
headers = {
    'content-type': 'application/json',
    'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_516b5e505a73ea248d313c3ba769882e',
    'Host': 'video.kuaishou.com',
    'Origin': 'https://video.kuaishou.com',
    'Referer': 'https://video.kuaishou.com/short-video/3xqk9kz8z59ds54?authorId=3xpbiv5ppefwdvm&streamSource=brilliant&hotChannelId=00&area=brilliantxxrecommend',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
}

# 使用data来接收payload:
data = {"operationName":"commentListQuery","variables":{"photoId":"3xqk9kz8z59ds54","pcursor":""},"query":"query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}

# 发送请求，获取响应：获取json数据
response = session.post(start_url, json=data, headers=headers).json()

# 打印json数据：
print(response)

# 导入解析模块
from requests_html import HTMLSession
session = HTMLSession()

# start_url = 'https://www.baidu.com'
# response = session.get(start_url)
# print(response.text)
# print(response.content.decode())
# # 获取源码
# print(response.html.html)