"""
课题：爬虫理论与原理
"""

"""1.什么是爬虫？"""
# 爬虫是一个程序，按照一定的规则模拟人的操作抓取互联网的信息
# 信息的采集，短信轰炸，商品销量监测
# 5k一个平台，把学费整回来，


"""2.爬虫能够干什么"""
# 数据的整合----集成产品，hao123，
# 网吧的网管
# 本子
# 记事本.txt
# hao123

# 爬虫公司，数据
# 上海市--300万12k

"""3.爬虫的应用场景(前景)"""
# 人工智能，大数据，
# 爬虫，他有想白嫖的公司
# 预算，招聘
# 数据分析，
# 警告：灰色，拒绝
# 非法的
# 5条，违法

# 企业级用人需求案例
# 外包需求案例
# 微博评论--4次左右，安居客房源信息，
# 300-500-

"""4.爬虫的分类"""
# 聚焦爬虫
# 争对某一个平台所开发的一个爬虫

# 通用爬虫(百度)

# 爬取电商平台数据

# 大分类---小分类--商品属性--颜色，大小--品牌

"""5.爬虫的原理"""
# # 聚焦爬虫
# import requests
# # 1.准备起始的url地址
# start_url = 'http://pic.netbian.com//uploads/allimg/210216/202450-161347829080ce.jpg'
# # 2.发送请求，获取响应
# response = requests.get(start_url)
# # 3.数据解析，数据提取
# # 获取二进制数据
# data = response.content
# print(data)
# # 4.保存数据
# with open('1.jpg', 'wb')as f:
#     f.write(data)

"""6.网址的构成"""
# 什么是url地址？
# http://www.baidu.com/

# https://www.baidu.com/s?wd=python
# http://pic.netbian.com/uploads/allimg/210216/202450-161347829080ce.jpg
# 协议部分：http/https
# s：SSL证书，域名证书，
# SSL过期，

# 域名部分：www.baidu.com

# s：资源路径部分：
# C:\Users\宋\Desktop\材料\python爬虫课件\爬虫A课
# /uploads/allimg/210216/
# 202450-161347829080ce.jpg

# 参数部分：wd=python

# ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&fenlei=256&rsv_pq=a2f957310001bc8a&rsv_t=0385GMwnlCQlkfPxIYaeFtoUHGAEAfzWYlajVZLaib9LQPYkUpCZL9i7kxw&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=7&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=python&rsp=5&inputT=1108&rsv_sug4=2181&rsv_sug=2

"""
每一个url地址，都是一种资源的体现
"""
# 网址构成
'''
# 不限格式和大小
超文本传输协议：


协议部分：https
域名部分：kuwo.cn
路径资源部分：search/list
参数部分：key=%E8%83%A1%E6%A2%A6%E5%91%A8
注意点：只有get请求，才会将参数部分显示在url地址中
'''

# cookie：储存个人信息的字段，登录之后的状态保持
# dbcl2="222817495:ftNiehLN6uQ"; path=/; domain=.douban.com; expires=Sat, 27-Mar-2021 13:06:02 GMT; httponly
# douban-fav-remind=1; __yadk_uid=PyOlOp24GkPN0R5SySWoZ6fpiwZINTTh; _vwo_uuid_v2=D4EDEB274998EF9670C11D9789C7C93BA|78d9187b2c765cfc0c80ed7767048abb; _ga=GA1.2.1416200646.1568801148; Hm_lvt_19fc7b106453f97b6a84d64302f21a04=1596096825; __utmv=30149280.22281; ll="118267"; bid=qRD3Npr76rc; douban-profile-remind=1; __gads=ID=aa84b9a3cc19bd7e-2220e3ba8cc5001d:T=1609855904:RT=1609855904:S=ALNI_MbGKQmnMAg21iJeosnlvmmOvPbTBQ; __utmz=30149280.1614258200.48.35.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utma=30149280.1416200646.1568801148.1612011952.1614258200.48; __utmt=1; dbcl2="222817495:ftNiehLN6uQ"; ck=T5lF; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmb=30149280.3.10.1614258200; __utma=223695111.204901245.1568801148.1612011952.1614258493.23; __utmb=223695111.0.10.1614258493; __utmc=223695111; __utmz=223695111.1614258493.23.20.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1614258493%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=f066296b216272b8.1568725314.24.1614258493.1612011952.; _pk_ses.100001.4cf6=*


# 网页构成

"""7.页面加载方式"""
# 决定了数据的来源：
#
# 同步：数据在源码中

# 异步：数据不再源码中
# xhr：异步加载请求包的抓取
# ajax：
# 网页的数据是靠异步加载渲染上去的

"""
在爬虫开发过程中，如果页面上看到的数据不再源码中，
则这个数据是靠异步加载ajax请求，将数据渲染上去的

XHR：
"""


"""8.https与http的请求说明"""

# 一个请求由哪些构成
# get请求：
# 请求协议
# 请求头

# 空行

# post请求
# import requests
# # 1.准备起始的url地址
# start_url = 'https://www.baidu.com'
# # 2.发送请求，获取相应
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# response = requests.get(start_url, headers=headers)
#
# response_1 = requests.get(start_url)
# # 3.解析响应，提取数据
# data = response.content.decode()
# data_1 = response_1.content.decode()
# # 4.保持数据
# print(data)
# print()
# print()
# print()
# print()
# print('=========================================================================================')
# print(data_1)

# headers：没有添加headers中user-agent，代表的是程序在访问，很容易被反扒

"""9.爬虫协议"""
# 遵守：爬取不到有价值的数据
# 仅仅道德层面上的约束

"""10.状态码"""
# 200:请求成功
# 302：重定向：从一个url地址，在访问的过程中，跳转到另外一个url地址
# 403：你被限制了，限制访问：你被反扒了24小时
# 404：服务器无法找到被请求的页面
# 500：软件出bugl






