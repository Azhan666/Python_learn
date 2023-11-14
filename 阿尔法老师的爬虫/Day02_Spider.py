"""
课题：抓包的工具说明
"""

"""1.fiddler安装"""

"""2.fiddler手机抓包"""

"""3.fiddler使用说明"""

"""4.chrome谷歌抓包说明"""
# 浏览器所展示的数据在这个url地址的源码中，没有找到相关的数据信息，就说明这一部分是异步加载渲染上去的
# 反之，就是同步加载：在源码数据中，能够找到浏览器页面，所看到的数据

# element内容：是数据渲染之后的标签结构
# requests不能够获取elements内容，selenium（自动化）

# 请求的url地址不变，参数改变(每一个请求参数不同)，
# 对应的返回的响应不一样

# filter  过滤（漏斗）

# search 搜索关键字查找更精准

#

"""案例："""

# https://video.kuaishou.com/short-video/3xgcy6ekwi2j4ea?streamSource=hotrank&trendingId=%E5%90%B4%E5%AD%9F%E8%BE%BE%E5%8E%BB%E4%B8%96&area=homexxhotlist
# http:\u002F\u002Fjs2.a.yximgs.com\u002Fupic\u002F2021\u002F02\u002F27\u002F17\u002FBMjAyMTAyMjcxNzI5MDNfODkzMDMxMDQ2XzQ1MTQyMDIxNzg3XzFfMw==_B0faaa7d665a714c75a978f66edce9c7e.jpg?tag=1-1614427163-unknown-0-x3vkdwh5gp-0d750c8c2e026975&type=hot&clientCacheKey=3xvvjui9graejmu.jpg&bp=13360",
#
# import requests
# from urllib.parse import quote, unquote
# title = input('请输入贴吧名称：')
# page = input('你想爬取多少页，请输入页码：')
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
#     'Host': 'tieba.baidu.com',
#     'Upgrade-Insecure-Requests': '1'
# }
# # 1.准备起始的url地址
# for num in range(int(page)):
#     start_url = f'https://tieba.baidu.com/f?kw={quote(title)}&pn={50 * num}&ie=utf-8'
#     # print(start_url)
#     # start_url_1 = 'https://tieba.baidu.com/f?kw=' + quote(title)
#     # start_url_2 = ''.join(['https://tieba.baidu.com/f?kw=', quote(title)])
#     # print(start_url_2)
#     # 2.发送请求，获取响应
#     response = requests.get(start_url, headers=headers)
#     # 3.解析响应，数据提取
#     data = response.content.decode()
#     # 4.保存数据
#     # print(data)
#     with open(title + '_' + str(num) + '.html', 'w', encoding='utf-8')as f:
#         f.write(data)
#     print(f'{title}----贴吧---第{num+1}页保存完成')
#
#
# import requests, os
# from urllib.parse import quote
# # os:操作系统命令模块
#
#
# class TbSpider(object):
#
#     def __init__(self):
#         self.title = input('请输入贴吧名称：')
#         self.page = input('你想爬取多少页，请输入页码：')
#         self.headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
#     'Host': 'tieba.baidu.com',
#     'Upgrade-Insecure-Requests': '1'
# }
#
#     def parse_stat_url(self):
#         """
#         1.准备起始的url地址
#         :return:
#         """
#         for num in range(int(self.page)):
#             start_url = f'https://tieba.baidu.com/f?kw={quote(self.title)}&pn={50 * num}&ie=utf-8'
#             self.parse_requests(start_url, num)
#
#     def parse_requests(self, start_url, num):
#         """
#         2.发送请求，获取响应
#         :return:
#         """
#         response = requests.get(start_url, headers=self.headers)
#         self.parse_response(response, num)
#
#     def parse_response(self, response, num):
#         """
#         3.解析响应，数据提取
#         :return:
#         """
#         data = response.content.decode()
#         self.save_data(data, num)
#
#     def save_data(self, data, num):
#         """
#         4.保存数据
#         :return:
#         """
#         # os_path = r'C:\Intel\Logs\\'
#         # os.getcwd() 获取当前文件路径
#         os_path = os.getcwd() + f'/{self.title}/'
#         # 判断这个是否存在
#         if not os.path.exists(os_path):
#             os.mkdir(os_path)
#         with open(os_path + self.title + '_' + str(num+1) + '.html', 'w', encoding='utf-8')as f:
#             f.write(data)
#         print(f'{self.title}----贴吧---第{num + 1}页保存完成')
#
#
# if __name__ == '__main__':
#     bd = TbSpider()
#     bd.parse_stat_url()
#
#
#
# os_path = os.getcwd()
# print(os_path)
# C:\Users\宋\Desktop\sx\爬虫12班_DEMO\A课_Spider
# C:\Users\宋\Desktop\sx\爬虫12班_DEMO\A课_Spider\奥迪

"""
手机抓包步骤：
1.fiddler打勾操作
2.查看IP地址192.168.3.22
3.电脑端，手机端在同一网络下
4.手机端操作
    # 1.进入wifi设置
    # 2.找到代理，配置ip和端口号port
    #  ip：填写电脑端IP地址
    #  prot：8888
    # 保存

以上操作完成，说明全部配置完成
证书：假的(模拟的)
"""

"""打开浏览器：访问百度，搜索python"""

"""
oppo手机有的实现不了
苹果手机有的实现不了

"""

# 恢复：关掉代理就可以恢复上网

