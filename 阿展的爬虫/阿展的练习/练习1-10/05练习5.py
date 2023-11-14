# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 课题：数据提取之json模块于jsonpath模块

# 1.爬虫中数据的分类
# 结构化数据：
# json
# 非结构化数据：
# html

# 2.json模块方法
import json

dict_1 = {'name': '阿展', 'gender': '男'}

# 熟悉
# print(json.dumps(dict_1))
# result = json.dumps(dict_1)
# print(result, type(result))
# 可以将Python的数据类型转换成字符串（json数据）

# json.loads()
# str_1 = '{"name": "\u963f\u5c55", "gender": "\u7537"}'
# result = json.loads(str_1)
# print(result, type(result))
# 可以讲json数据（字符串形式的字典）转换成字典类型数据

# 了解
# import json
# # 写入
# dict_1 = {'name': '阿展', 'gender': '男'}
# with open('1.txt', 'w')as f:
#     json.dump(dict_1,f)

# 读取
# with open('1.txt', 'r')as f:
#     print(json.loads(f))
#
# dict_1 = {'name': '阿展', 'gender': '男'}
# with open('2.txt', 'w', encoding='utf-8')as f:
#     f.write(str(dict_1))
# with open('2.txt', 'r',encoding='utf-8')as f:
#     print(f.read())


# 3.jsonpath安装使用
# from requests_html import HTMLSession
# from  jsonpath import jsonpath
# session = HTMLSession()

# 案例，快手评论正文：

# start_url = 'https://video.kuaishou.com/graphql'
# headers = {
# 'content-type': 'application/json',
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
# # authorName 作者名
# # content    评论正文
# authorName = jsonpath(response, '$..authorName') # $:根节点
# print(authorName)
#
# content_str = jsonpath(response, '$..content')
# print(content_str)
#
# dict_1 = [{'name': 'xiaoming', 'sex': 'g'}, {'addr': 'bj'}, {'name': 'xiaohong', 'sex': '1'}]
# # print(dict_1[0]['sex1']
#
# data = jsonpath(dict_1, '$..sex1')
#
# print(data)

# 案例，抖音去水印视频：

# 抖音链接集合：
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
# 导入模块
from requests_html import HTMLSession
from  jsonpath import jsonpath
import re, os # 导入正则模块、os系统操作命令模块
session = HTMLSession()

while True: # 为实现多次请求，使用while循环
    start_url = input('请输入分享链接：') # 接收用户输入的抖音链接
    # start_url = '#英雄联盟 #狗头 生与死轮回不止，如果联盟拍成电影你去看吗？  https://v.douyin.com/JXEs3pS/ 复制此链接，打开抖音搜索，直接观'
    # 下面我们要通过正则匹配出正确的url地址
    # 首先，我们使用re.findall()方法，因为findall方法返回的是一个列表，所以我们要加上索引（下标），用来只匹配出链接部分
    # 下面第一个参数是正则规则，第二个参数是提取对象
    # 由观察可以发现，第一个要匹配的参数是http，第二个参数是起始的url地址
    # 由观察可以发现，每一个视屏链接后面都有一个空格，所以我们要在正则规则.*?后加一个空格
    # 同时，由打印的返回链接可以发现，返回的是一个列表，链接末尾有一个空格，不太严谨
    # 所以，出于严谨，我们在http后面加一个括号，此时它返回的就是括号里面的内容
    # 又由观察返回的内容可看到，返回的链接缺少http，所以我们要在re.findall前面加上一个http
    # 再次运行，我们发现链接已经变得完整了

    start_url = 'http' + re.findall('http(.*?) ', start_url)[0]
    # print(start_url)
    # 至此，我们起始的url地址已经准备完整了，下面我们进入发送请求、获取响应环节了

    # 此时，我们构造headers就需要技巧了，因为我们观察链接的preview可发现，没有任何响应信息，
    # 所以视屏是由异步加载渲染上去的，所以我们要观察异步加载的xhr小黄人，再次观察preview，
    # 发现包的信息很多，很有可能有我们要找的东西，所以，我们展开值，对比链接关键词，即可找到对应的包
    # 所以，我们直接点击右上角三点号，点击搜索，查找MP4，找到MP4的url
    # 通过搜索，我们没有找到任何mp4相关信息，其实这是谷歌抓包搜索的弊端，我们找到response里面的字符串，
    # 把内容复制，在谷歌打开json解析新窗口，解析后再次搜索，发现也没有MP4相关内容，
    # 我们也不用担心，我们返回抖音抓包，发现有视频的标志性video，在video里面查找，看看是否能找到MP4信息
    # 我们找到这个链接：
    # "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f210000bhtq8nuvld7ce16r2ou0&ratio=720p&line=0"
    # 通过访问此链接，我们发现这个链接就是视频播放链接，但是有水印，接下来我们进入除水印环节
    # 抖音的水印标志为链接里面play后面的wm，删除wm即可除水印
    # 通过删除wm，我们发现水印已经成功去除
    # 在此我们得出结论，抖音除水印机制其实很简单：
    # 我们先对起始的url地址发送请求，获取响应，它会被做一个重定向的操作，重定向之后，进行异步抓包，
    # 获取相应的json数据，找到视频链接，进行play后面的wm删除操作，获得到无水印视频
    # 然后保存无水印链接的二进制数据，即可。
    # 下面，我们进入写代码环节：
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    # 获取响应的url地址
    response_url = session.get(start_url, headers=headers).url
    # 提取id
    item_id = re.findall('video/(.*?)/', response_url)[0]
    # 提取到视屏的id
    # print(item_id)
    # url地址拼接（字符串的拼接：或者使用加号）
    next_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_id}'
    # 通过字符串拼接，将上面url地址id成功拼接，拼接完成之后，我们获取到了新的url地址，
    # 下面，我们对新的url地址发送请求，获取到的就是json数据，下面我们使用jaon_data来接收json数据，
    # 传入next_url，调用json()方法

    json_data = session.get(next_url).json()
    # print(json_data) # 打印一下json_data
    # 通过打印，我们发现已经成功获取到了json数据
    # 下面，我们从json数据中获取我们需要的信息，接下来就是数据提取环节

    # 数据提取我们就用到我们今天所学的jsonpath，我们导入jsonpath模块：from jsonpath import jsonpath
    # 首先，我们从json数据中看到了title，和desc，首先，我们使用desc，传入json_data
    # 在desc后面加入提取规则：'$..desc',打印desc，我们发现打印出的数据末尾有一个空格，
    # 所以，一个desc对应一个''空格，下面我们用share_title提取，发现打印出的是视频标题，
    # 所以，用share_title作为提取标题没有问题，所以，我们成功找到了提取标题


    # 数据提取
    # 提取标题
    share_title = jsonpath(json_data, '$..share_title')[0]
    # print(share_title)

    # 接下来，就是视屏的url地址
    # 我们通过打印的json数据发现，视频的地址多达13个，所以，需要进行过滤，
    # 过滤太麻烦，我们可以换一种提取方式
    # 我们返回抓包网页发现，url是在play_addr里面的，所以，我们可以做二级提取，
    # 首先，将这个play_addr所对应的字典提取出来：play_adder = jsonpath(json_data, '$..play_adder')
    # 提取之后它还是一个字典数据，所以我们还需要做一次play_addr提取：然后提取url_list:url = jsonpath(play_adder, '$..url_list')

    # 提取播放地址
    play_addr = jsonpath(json_data, '$..play_addr') # 提取play_addr所对应的字典
    url = jsonpath(play_addr, '$..url_list')[0][0]
    # print(url) 打印出来的就是无水印url地址
    # 观察打印结果，我们发现它有两层列表，这是因为我们的jsonpath返回的数据是一个列表，
    # 所以我们要做一个下标（索引）的操作，只提取列表部分：url = jsonpath(play_adder, '$..url_list')[0][0]
    # 此时打印的就是有效链接部分了，接下来我们就要进行wm删除操作了

    # 我们使用MP4_url来接收替换操作
    # 为了避免wm误删，我们要将playwm替换为play
    mp4_url = url.replace('playwm', 'play')

    # 无水印地址拿到之后，我们只需对无水印地址发送请求，获取它的二进制数据：
    data = session.get(mp4_url).content # .content:用来获取二进制数据

    # 接下来就是视频的保存：with open(os_path + share_title + '.mp4', 'wb')as f:  f.write(data)
    # 创建一个保存视频的文件夹：
    os_path = os.getcwd() + '/dy/' # 文件夹名后要加斜杠,getcwd:获取当前路径
    # 如果保存路径不存在，就按指定路径创建一个文件夹：
    if not os.path.exists(os_path):
        os.mkdir(os_path) # mkdir：创建目录
    # 视频的标题 + 视频的格式
    with open(os_path + share_title + '.mp4', 'wb')as f:
        f.write(data)
    # 加入保存提示：
    print(f'{share_title}----保存完成')

