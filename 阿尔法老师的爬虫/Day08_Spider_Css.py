"""
课题：数据提取之Css选择器
"""

"""1.CSS选择器的优势"""
# 稳定
# 在一个html页面，会根据css语法做一系列的demo操作
# 不改变html的css结构，可以不修改爬虫代码
# 微调，xpath标签结构就变得不一样了

"""2.CSS选择器的应用语法"""
# from fake_useragent import UserAgent
# # ua的替换
# ua = UserAgent()
# # 谷歌浏览器，火狐浏览器，ie
#
# print(ua.chrome)
#
# # Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36
# # Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36
# # Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36
# print(ua.Safari)

# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# ua = UserAgent()
# session = HTMLSession()
#
# url = 'https://www.csdn.net'
#
# response = session.get(url)
#
# data = response.html.find('#floor-nav_62 > div > div > div.index_nav_center > ul > li:nth-child(11) > a', first=True)
# # 提取标签的文本信息
# # print(data.text)
# # 将标签的属性转换为字典结构
# # print(data.attrs)
# # 获取标签中所有的连接
# # print(data.links)

# print(data)


# https://esf.fang.com/house/i32/    第2页
# https://esf.fang.com/house/i31/    第1页

# https://esf.fang.com/house/i350/

# https://esf.fang.com/chushou/3_454420843.htm?channel=2,2&psid=1_1_80
#                     /chushou/3_454420843.htm?channel=2,2&psid=1_1_80





# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# import json
# import re
# ua = UserAgent()
# session = HTMLSession()
#
# headers = {
#     'Cookie': 'city=cs; global_cookie=dfdfsj3b5yosky0jq0ywfdp5k27km7s1mfk; g_sourcepage=undefined; unique_cookie=U_dfdfsj3b5yosky0jq0ywfdp5k27km7s1mfk*1',
#     'referer': 'http://search.fang.com/',
#     'user-agent': ua.chrome
# }
#
# for page in range(1, 101):
#     # 二手房翻页url  房源列表页
#     start_url = f'https://esf.fang.com/house/i3{page}/'
#     start_url_response = session.get(start_url, headers=headers)
#     print(start_url_response.content.decode())
#     # print(start_url_response.content.decode())
#     # 提取房源详情页地址
#     href_list = start_url_response.html.xpath(
#         '//div[@class="shop_list shop_list_4"]/dl/dt/a/@href'
#     )
#     # 访问房源详情页
#     headers_1 = {
#         'Cookie': 'global_cookie=8qfc2dvuivv4psvhv84zwp08s15km7oec7w; xfAdvLunbo=; searchConN=1_1615636747_391%5B%3A%7C%40%7C%3A%5D688ee9355f37ae020aa9d254cde2d718; __utma=147393320.273984512.1615636745.1615636745.1615636745.1; __utmz=147393320.1615636745.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); city=www; __utmc=147393320; lastscanpage=0; resourceDetail=1; g_sourcepage=esf_fy%5Elb_pc; __utmb=147393320.23.10.1615636745; sfut=DED5DD3F3A5B30F19DF88B7B25BD15DF09C9A29420571BE5B2244B8D5A0F605B0A30B05DEE732E4144D06B8BEE5E970564530D1EDC4B4B792523D035EF6536C5106064869452E2513D858A276C742ADAF8BA72F15A4A7340289A69680D33478FBD9120C98DE0A30946DE172B77725388DAA13C4D03124561A48CC499DD5FCC5A88B75D4A232C7CEC; unique_cookie=U_rg7jxbz5ena5xjttikk4076tm17km7p6ezp*12; new_loginid=122382192; login_username=%E4%B8%8D%E5%B8%85%E4%BD%A0%E6%8A%A5%E8%AD%A61652359826',
#         'referer': start_url,
#         'user-agent': ua.chrome
# }
#     for url in href_list:
#         dict_1 = {}
#         next_url = 'https://esf.fang.com' + url
#         response = session.get(next_url, headers=headers_1)
#         # print(response.content.decode())
#         # print(next_url_response.content.decode())
#         # 房源配置信息
#         config_dict = re.findall('pageConfig.ubp = (.*?);', response.content.decode())[0]
#         # json.loads 将字符串形式的字典数据转化成字典
#         config_dict_result = json.loads(config_dict)
#         # print(config_dict_result, type(config_dict_result))
#         # 房源标题
#         title = response.html.xpath('//title/text()')[0]
#         dict_1['房源标题'] = title
#
#         # 价格
#         price = re.findall(r"housemoney:'(.*?)',", response.content.decode())
#         price = ''.join(price)
#         # print(price)
#         dict_1['价格'] = price
#         # 房子规格
#         house_config = response.html.xpath('//div[@class="tt"]/text()')
#         # print(house_config)
#         house_cfg = house_config[0].replace('\n', '').replace(' ', '')
#         dict_1['房子规格'] = house_cfg
#         # 平米
#         pm = house_config[1].replace('\n', '').replace(' ', '')
#         dict_1['平米'] = pm
#         # 平米价格
#         pm_price = house_config[2].replace('\n', '').replace(' ', '')
#         dict_1['平米价格'] = pm_price
#         # 房子朝向
#         cx = house_config[3].replace('\n', '').replace(' ', '')
#         dict_1['房子朝向'] = cx
#         # 楼层简介
#         jz = house_config[4].replace('\n', '').replace(' ', '')
#         dict_1['楼层简介'] = jz
#         # 装修
#         zx = house_config[5].replace('\n', '').replace(' ', '')
#         dict_1['装修'] = zx
#         # 小区
#         xq = response.html.xpath('//div[@class="title rel"]/text()')
#         xq = [i for i in xq if i != '\n']
#         xq = xq[0].replace('\n', '').replace(' ', '')
#         dict_1['小区名称'] = xq[:-2]
#         # 地址
#         addrs = response.html.xpath('//div[@id="address"]/a/text()')
#         dict_1['地址'] = '-'.join(addrs).replace('\n', '').replace(' ', '')
#         with open('1.json', 'a+', encoding='UTF-8')as f:
#             f.write(str(dict_1) + '\n')
#         print(f'{title}------提取完成')

"""
高匿名代理
# 对方并不知道你访问
6块/ 24小时

"""

"""
开发思路
1.找二手房或者新房url地址，摸清楚翻页规律
2.通过访问房源列表页，提取房源详情页url地址
3.访问房源详情页提取数据
"""

'''编码转换'''
# from urllib.parse import quote, unquote
# # %E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80 转换为汉字
# name = '王者荣耀'
# print(quote(name))
# print(unquote(quote(name)))
"""汉字转换为拼音"""
# # pip install xpinyin
# from xpinyin import Pinyin
# name = '亾兦'
# p = Pinyin()
# print(p.get_pinyin(name))
"""B站"""
# url = 'https:\u002F\u002Fupos-sz-mirrorkodo.bilivideo.com\u002Fupgcxcode\u002F20\u002F88\u002F160738820\u002F160738820-1-16.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1615044833&gen=playurl&os=kodobv&oi=2936638550&trid=9c237beb08564f7eb9fad18a0ffa5d31h&platform=html5&upsig=476ecb8f87962ddcbf3f65019e03405b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&logo=80000000'
# result = url.encode('latin-1').decode('unicode-escape')
# print(result)
""""""
# from urllib.parse import quote
# # %u795E%u5893                神墓
# # %u738B%u8005%u8363%u8000    王者荣耀
# # %5Cu738b%5Cu8005%5Cu8363%5Cu8000
# # %u738b%u8005%u8363%u8000
# name = '王者荣耀'
# result = quote(name.encode('unicode-escape')).replace('%5C', '%')
# print(result)







