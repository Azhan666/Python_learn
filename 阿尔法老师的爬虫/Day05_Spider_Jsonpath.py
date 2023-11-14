"""
课题：数据提取之json模块与jsonpath模块
"""

"""1.爬虫中的数据分类"""
# 结构化数据
#     json
# 非结构化数据
# html

"""2.json模块方法"""
# import json

# dict_1 = {'name': '彭于晏', 'gender': '女'}

# 熟悉
# print(json.dumps(dict_1))
# result = json.dumps(dict_1)
# print(result, type(result))
# 可以将python的类型数据转换成字符串(json数据)

# json.loads()
# str_1 = '{"name": "\u5f6d\u4e8e\u664f", "gender": "\u5973"}'
# result = json.loads(str_1)
# print(result, type(result))
# 可以将json数据(字符串形式的字典)转换成字典类型数据

# 了解
# import json
# """写入"""
# dict_1 = {'name': '彭于晏', 'gender': '女'}
# with open('1.txt', 'w')as f:
#     json.dump(dict_1, f)
#
# """读取"""
# with open('1.txt', 'r')as f:
#     print(json.load(f))

# dict_1 = {'name': '彭于晏', 'gender': '女'}
# # with open('2.txt', 'w', encoding='utf-8')as f:
# #     f.write(str(dict_1))
# with open('2.txt', 'r', encoding='utf-8')as f:
#     print(f.read())


"""3.jsonpath安装与使用"""
# from requests_html import HTMLSession
from jsonpath import jsonpath
# session = HTMLSession()
#
#
# start_url = 'https://video.kuaishou.com/graphql'
# headers = {
#     'content-type': 'application/json',
#     'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_516b5e505a73ea248d313c3ba769882e',
#     'Host': 'video.kuaishou.com',
#     'Origin': 'https://video.kuaishou.com',
#     'Referer': 'https://video.kuaishou.com/short-video/3xqk9kz8z59ds54?authorId=3xpbiv5ppefwdvm&streamSource=brilliant&hotChannelId=00&area=brilliantxxrecommend',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
# }
# data = {"operationName":"commentListQuery","variables":{"photoId":"3xqk9kz8z59ds54","pcursor":""},"query":"query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
#
# response = session.post(start_url, json=data, headers=headers).json()
# print(response)
# authorName  作者名
# content     评论正文
# authorName = jsonpath(response, '$..authorName')
# print(authorName)
#
# content_str = jsonpath(response, '$..content')
# print(content_str)

# dict_1 = [{'name': 'xiaoming', 'sex': 'g'}, {'addr': 'bj'}, {'name': 'xiaohong', 'sex': '1'}]
# # print(dict_1[0]['sex1'])
#
# data = jsonpath(dict_1, '$..sex1')
#
# print(data)



"""
安徽的天好冷，就像我想复习的心一样  https://v.douyin.com/JGACH6s/ ;复制此链接，打开抖音搜索，直接观看视频！
帅！回顾“九三阅兵”震撼场面，每个动作都像是复制粘贴！一起期待，国庆70年大阅兵！  https://v.douyin.com/JXETnfd/ 复制此链接，打开抖音搜索，直接观看视频！
#轻vlog #埃罗芒阿老师 纱雾的雷神斩灭剑  https://v.douyin.com/JXEvGxT/ 复制此链接，打开抖音搜索，直接观看视频！
#英雄联盟 #狗头 生与死轮回不止，如果联盟拍成电影你去看吗？  https://v.douyin.com/JXEs3pS/ 复制此链接，打开抖音搜索，直接观看视频！
#国漫 #天使彦 #凉冰  https://v.douyin.com/JXKGLng/ 复制此链接，打开抖音搜索，直接观看视频！
#斗破苍穹 你们要的美杜莎女王，要回老家陪奶奶过年，昨晚一个通宵熬出来的感觉很多地方没画好将就着看吧！  https://v.douyin.com/JXKx2pn/ 复制此链接，打开抖音搜索，直接观看视频！
欣赏来自WLOP大佬的第五波作品  #wlop  #鬼刀  #动态壁纸  #高清60帧  @DOU+小助手  https://v.douyin.com/J4PR5UP/ 复制此链接，打开抖音搜索，直接观看视频！
神医套路多 %搞笑  %套路  %大兵  %沙雕  %影视 全0帧  @DOU+小助手  https://v.douyin.com/J4PR5UP/ 复制此打开抖音搜索，直接观看视频！
曾经真的以为人生就这样了%鬼迷心窍 %车载音乐 %热门音乐  https://v.douyin.com/JguscCJ/ 复制此链接，打开抖音搜索，直接观看视频！
这个音乐太上头了 %圣诞节🎄 %秀身材秀腿 %辣妹@抖音小助手  https://v.douyin.com/JgunGsT/ 复制此链接，打开抖音搜索，直接观看视频！
既然那么多人送你圣诞礼物，那少我一个也没关系了吧 %小丑竟是我自己  https://v.douyin.com/JgHRCUG/ 复制此链接，打开抖音搜索，直接观看视频！
出车吗，马上到  %高清  %雅马哈mt09  https://v.douyin.com/edAUSE4/ 复制此链接，咑鐦Dou吟搜索，直接觀看視频！
"""

# from requests_html import HTMLSession
# from jsonpath import jsonpath
# import re, os
# session = HTMLSession()
#
# while True:
#     start_url = input('请输入分享链接：')
#     # start_url = '#英雄联盟 #狗头 生与死轮回不止，如果联盟拍成电影你去看吗？  https://v.douyin.com/JXEs3pS/ 复制此链接，打开抖音搜索，直接观'
#     start_url = 'http' + re.findall('http(.*?) ', start_url)[0]
#     # print(start_url)
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
#     }
#     # 获取响应的url地址
#     response_url = session.get(start_url, headers=headers).url
#     # 提取id
#     item_id = re.findall('video/(.*?)/', response_url)[0]
#     # print(item_id)
#     # url地址拼接
#     next_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_id}'
#
#     json_data = session.get(next_url).json()
#     # print(json_data)
#
#     """数据提取"""
#     # 提取标题
#     share_title = jsonpath(json_data, '$..share_title')[0]
#     # print(share_title)
#
#     # 提取播放地址
#     play_addr = jsonpath(json_data, '$..play_addr')
#     url = jsonpath(play_addr, '$..url_list')[0][0]
#     # print(url)
#     mp3_url = url.replace('playwm', 'play')
#     data = session.get(mp3_url).content
#
#     os_path = os.getcwd() + '/dy/'
#     if not os.path.exists(os_path):
#         os.mkdir(os_path)
#     with open(os_path + share_title + '.mp4', 'wb')as f:
#         f.write(data)
#
#     print(f'{share_title}----保存完成')



# https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=6753916611243101443
# https://www.iesdouyin.com/share/video/6753916611243101443/?region=CN&mid=6753906665231305479&u_code=17fdgi3i1&titleType=title&did=61021263948&iid=2902353627851342&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme


# from requests_html import HTMLSession
# from jsonpath import jsonpath
# session = HTMLSession()
#
# start_url = 'https://video.kuaishou.com/graphql'
#
# headers = {
#     'content-type': 'application/json',
#     'Cookie': 'clientid=3; did=web_d8ccc186d82b7f7b61768498067e7f64; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1600780303; didv=1610018300000; kpf=PC_WEB; kpn=KUAISHOU_VISION',
#     'Host': 'video.kuaishou.com',
#     'Origin': 'https://video.kuaishou.com',
#     'Referer': 'https://video.kuaishou.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
# }
#
# data = {"operationName":"brilliantDataQuery","variables":{"semKeyword":"","semCrowd":"","utmSource":"","utmMedium":"","page":"home","photoId":""},"query":"fragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    id\n    duration\n    caption\n    likeCount\n    realLikeCount\n    coverUrl\n    photoUrl\n    coverUrls {\n      url\n      __typename\n    }\n    timestamp\n    expTag\n    animatedCoverUrl\n    distance\n    videoRatio\n    liked\n    stereoType\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  __typename\n}\n\nfragment photoResult on PhotoResult {\n  result\n  llsid\n  expTag\n  serverExpTag\n  pcursor\n  feeds {\n    ...feedContent\n    __typename\n  }\n  webPageArea\n  __typename\n}\n\nquery brilliantDataQuery($pcursor: String, $semKeyword: String, $semCrowd: String, $utmSource: String, $utmMedium: String, $page: String, $photoId: String, $utmCampaign: String, $webPageArea: String) {\n  brilliantData(pcursor: $pcursor, semKeyword: $semKeyword, semCrowd: $semCrowd, utmSource: $utmSource, utmMedium: $utmMedium, page: $page, photoId: $photoId, utmCampaign: $utmCampaign, webPageArea: $webPageArea) {\n    ...photoResult\n    __typename\n  }\n}\n"}
# response = session.post(start_url, headers=headers, json=data).json()
# url_list = jsonpath(response, '$..photoUrl')
# print(url_list)



# url = 'https:\u002F\u002Fupos-sz-mirrorkodo.bilivideo.com\u002Fupgcxcode\u002F20\u002F88\u002F160738820\u002F160738820-1-16.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1615044833&gen=playurl&os=kodobv&oi=2936638550&trid=9c237beb08564f7eb9fad18a0ffa5d31h&platform=html5&upsig=476ecb8f87962ddcbf3f65019e03405b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&logo=80000000'
# result = url.encode('latin-1').decode('unicode-escape')
# print(result)


# https://video.pearvideo.com/mp4/short/20210305/cont-1722306-15623520-hd.mp4




# https://video.pearvideo.com/mp4/short/20210305/cont-1722375-15623959-hd.mp4
# https://video.pearvideo.com/mp4/short/20210305/cont-1722376-15623982-hd.mp4












