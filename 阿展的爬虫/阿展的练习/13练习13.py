# !/usr/bin/env python
# -*- coding: utf-8 -*-
# js逆向过程
# 1.数据包定位（js逆向数据的定位）
    # 寻找或定位起始的被加密（请求参数）数据所对应的包
    # 需求清晰：逆向什么数据，需要解密什么数据

# 2.定位js文件
    # 1.通过network观察包initiator下的触发的js文件
    # 2.通过search搜索关键字
    # 3.通过标签元素绑定的事件监听函数找到js
    # 注意：三种方法不保证每一种都能找到js

# 3.js代码分析
    # 通过js语法，理清js的数据加密过程

# 4.模拟重现
    # 第三方加载js2py，execjs，pyv8
    # python重现

# # 英雄的id
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/533/533-smallskin-2.jpg
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/533/533-smallskin-1.jpg
# # //game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + ename + '/' + ename,
# copy的burl
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/' + ename + '/' + ename,
# copy的surl

# //game.gtimg.cn/images/yxzj/img201606/heroimg/'+ heroid + '/'+ heroid +'-myskin-'+ skinid +'.jpg
# //game.gtimg.cn/images/yxzj/img201606/heroimg/' + heroid + '/' + heroid + '.jpg
# 搜索heroimg找到

# 我们发现这些url的前面一大部分都相同,所以我们把前面相同的部分直接使用一个变量hero_url存储起来:
from twisted.words import im

# hero_url = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/'
# # 我们再把不同的id部分拼接起来访问一下能否成功：
# hero_url = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/533/533-smallskin-1.jpg'
# # 我们发现是可以成功访问的
#
# # 我们再把东西多的那一行一起拼接起来：
# hero_url_1 = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/533/533-myskin-1.jpg'
# # 使用一个变量hero_url
# # 访问成功，我们发现他又变大了一点，我门通过改变myskin-后面的值可以改变图片
# # 所以，-myskin-代表的是图像
#
# # 下面我们去找壁纸的关键字
#
# # 我们通过查找标签里的图片url，发现了大图的url，并且可以直接访问，下面是他们的的url之一：
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/533/533-mobileskin-1.jpg
#
# # 我们发现他有一个前面都没有的-mobileskin-，那么我们可以尝试用它进行替换
# # 我们把前面的链接拿过来对比一下，然后将带-mobileskin-的链接的数字id换成其它id进行访问:
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/533/533-mobileskin-1.jpg
# # 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/527/527-myskin-1.jpg'
#
# # //game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-6.jpg
# # 大壁纸-bigskin-，且-bigskin-后面的id可替换
# # 下面我们来搜索一下-bigskin-在js的哪一个位置
# # 通过搜索，我们发现-bigskin-在page.js的js文件里
#
# # 下面我们通过代码来实现：
#
# from requests_html import HTMLSession
# from  fake_useragent import UserAgent
# from jsonpath import jsonpath
# ua = UserAgent()
# session = HTMLSession()
#
# # 首先获取所有英雄的id
# # https://pvp.qq.com/web201605/js/herolist.json
# # 这个herolist.js链接里面的response都是关于英雄id的内容
# # 所以我们对他发送请求:
#
# # 起始的url地址
# url = 'https://pvp.qq.com/web201605/js/herolist.json'
# # 构造headers
# headers = {
#     'referer': 'https://pvp.qq.com/web201605/herolist.shtml',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
# }
# response_json = session.get(url, headers=headers).json()
# # 使用response来接收一下返回的json数据
# # print(response_json)
# # 成功获取json数据
# # 下面我们使用json_path把英雄皮肤名称提取出来，这个先放一边，我们先把英雄的id提取出来
#
# # 提取英雄的id我们就要做一个测试：第一个英雄的id是多少
# # 通过点击第一个英雄（司空震）的详情并点击检查查看源码，找到了537.html,并且在返回的json数据中查找的到所以，第一个英雄的id应该就是537
# # 司空震：ename：'537',这个ename我们也是见过的
# # 由于返回的数据都是由很多个字典数据所组成的，所以，我们首先对字典数据进行一个遍历:
#
# for data_json in response_json: # 导入from jsonpath import jsonpath
#     """使用ename接收一下：传入我们的提取对象：data_json、提取规则：$..ename
#     """
#     ename = jsonpath(data_json, '$..ename')[0]
#     # print(ename) # 别忘注释掉上一个print()
#     # 成功取得所有英雄的id（无序）
#
# # 下一步就是url地址的拼接，拼接也很简单，看需要大壁纸还是小壁纸
# # 现在我们获取大壁纸，在ename下面进行拼接：（使用f，格式化字符串）
#     i = 1
#     while True:
#         next_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i}.jpg'
#         response = session.get(next_url)
#         if response.status_code != 200:
#             break
#         with open(str(ename) + str(i) + '.jpg', 'wb')as f:
#             f.write(response.content)
#         print(f'{ename}第{i}张图片下载完成')
#         i += 1
#     # 在id处分别使用两个大括号来接收ename，在提取规则后面使用下标[0]来固定提取每次的id
#     # 但是我们发现在next_url中又出现了需要循环的数据-6（id也需要不断循环），那么我们直接在next_url上面使用while True,
#     # 然后给next_url增加一下缩进，使while True语法生效
#     # 为什么使用while True？因为我们不知道它具体有多少张壁纸。
#     # 使用while True还需要在while True上面声明我们的动态加载变量（循环变量）i值，在next_url下面声明i += 1（i循环自增）
#     # 然后在把-bigskin-后的id换成{i}
#     # 接下来就要使用状态码来结合我们的请求来做判断了，然后终止循环
#     # 示例：response = session.get(next_url)，传入我们的next_url
#     # 然后做一个判断：if resp.status_code != 200:,就退出循环（终止while True死循环）：break
#     # 否则就直接with open保存壁纸图片：with open(str(ename) + str(i) + '.jpg', 'wb')as f:
#     # str：字符串，（因为打印的是字符串）ename是图片名称 ，str（i）：第i张图片
#     # 接下来我们观察一下效果：print(f'{ename}第{i}张下载完成')


# 接下来我们学习请求参数逆向：

# 需要我们做两件事情：
  # 1.算法还原（js加密代码）
  # 2.使用第三方库帮我们执行js代码，我们只需要传参数进去就行
  # 解密sign

# 下面我们进入第二个案例：百度翻译

# 首先把那一段js文件copy下来,把js文件保存在pycharm中（创建一个js文件）

# 把js文件保存下后，还有两个内容我们没有搞定，就是js中的'r'我没还没确定他代表什么
# 我们搜索function r，发现它return了一个v，说明调用r，他返回的就是v，再次搜索function v，
# 发现它传入了一个t，这样搜索太麻烦，我们使用一个简单的方法来做观察
# 其实这里的r和我们之前看到的r是一样的，只是它以数组的形式显示了
# 我们之前copy了一段js'文件，现在我们看一下js文件里缺少哪些东西
# 具体来说是少了哪些变量，因为在js中，有些变量是没有定义的
# 我们发现，js文件中第24行凭空出现了一个i，通过查找，发现这个i没有定义
# 又可以看到，i=windows[l],那么，我们就可以通过window去找到i和l（源码搜索）
# 通过源码搜索，我们成功找到了window所指向的window.bdstoken = 'bfb24840d5ffdabc4faafdb0573af3ee';window.gtk = '320305.131321201';
# 下面我们来写一段简单的js代码：var i = 320305.131321201 // 变量i的值为window.gtk
# // 定义一下变量i（下面的i没有定义）

import js2py
# # 创建js执行环境
js = js2py.EvalJs()
with open('13练习13js文件', 'r')as f:
    js.execute(f.read())
result = js.e('我爱你')
print(result)


from requests_html import HTMLSession
from fake_useragent import UserAgent
import js2py, json
ua = UserAgent()
session = HTMLSession()

class BDSpider(object): # 创建百度翻译爬虫类
    def __init__(self): # 类的初始化
        self.title = input('请输入需要翻译的信息：')
        self.yy_url = 'https://fanyi.baidu.com/langdetect'
        self.fy_url = 'https://fanyi.baidu.com/v2transapi'
                    # https://fanyi.baidu.com/v2transapi?from=en&to=zh
        # https://fanyi.baidu.com/v2transapi?from=zh&to=en 翻译的url地址
        # 还有一个要请求的url地址，即百度翻译的首页，请求首页获取token值


        # 构造headers
        self.headers = {
            'Host': 'fanyi.baidu.com',
            'Origin': 'https://fanyi.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }

    def parse_start_response(self): # 解析响应
        """
         :return:
        """







