"""
js逆向过程
# 1.数据包定位(js逆向数据的定位)
    # 寻找或定位起始的被加密(请求参数)数据所对应的包
    # 需求清晰：逆向什么数据，需要解密什么数据

# 2.定位js文件
    # 1.通过network观察包initiator下的触发的js文件
    # 2.通过search搜索关键字
    # 3.通过标签元素绑定的事件监听函数找到js
    # 注意：三种方法不保证每一种都能找到js，最好三种方式都使用

# 3.js代码分析
    # 通过js语法，理清js的数据加密过程

# 4.模拟重现
    # 第三方加载js2py，execjs，pyv8
    # python重现
"""
# # 英雄的id
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/527/527-smallskin-2.jpg
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/527/527-smallskin-2.jpg
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/505/505-smallskin-3.jpg
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/505/505-smallskin-3.jpg
#
# # ' + surl + '-smallskin-' + (i + 1) + '.jpg"
#
# # "//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + ename + '/' + ename
# # '//game.gtimg.cn/images/yxzj/img201606/heroimg/' + ename + '/' + ename,
#
# # //game.gtimg.cn/images/yxzj/img201606/skin/hero-info/505/505-smallskin-3.jpg
#
# # '//game.gtimg.cn/images/yxzj/img201606/heroimg/'+ heroid + '/'+ heroid +'-myskin-'+ skinid +'.jpg'
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/' + heroid + '/' + heroid + '.jpg
#
# hero_url = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/505/505.jpg'
#
# hero_url_1 = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/505/505-myskin-1.jpg'
#
#
# # 图像：-myskin-
# img_url = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/505/505-myskin-3.jpg'
#
# # http://game.gtimg.cn/images/yxzj/img201606/heroimg/527/527-mobileskin-1.jpg
# # //game.gtimg.cn/images/yxzj/img201606/heroimg/527/527-smallskin-2.jpg
#
# # //game.gtimg.cn/images/yxzj/img201606/skin/hero-info/505/505-bigskin-2.jpg
#
# # 大壁纸 -bigskin-
#
# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# from jsonpath import jsonpath
# ua = UserAgent()
# session = HTMLSession()
#
#
# url = 'https://pvp.qq.com/web201605/js/herolist.json'
# headers = {
#     'referer': 'https://pvp.qq.com/web201605/herolist.shtml',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
# }
# resp_json = session.get(url, headers=headers).json()
# # print(resp_json)
#
# for data_json in resp_json:
#     ename = jsonpath(data_json, '$..ename')[0]
#     i = 1
#     while True:
#         next_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i}.jpg'
#         resp = session.get(next_url)
#         if resp.status_code != 200:
#             break
#         with open(str(ename) + str(i) + '.jpg', 'wb')as f:
#             f.write(resp.content)
#
#         print(f'{ename}第{i}张下载完成')
#         i += 1
import re

"""
1.请求参数js逆向
"""
# 算法还原
# js加密代码

# 第三方库帮我们执行js代码
# 解密sign

# import js2py
# # 创建js执行环境
# js = js2py.EvalJs()
# with open('1.js', 'r')as f:
#     js.execute(f.read())
# result = js.e('我爱你')
# print(result)

# https://fanyi.baidu.com/v2transapi?from=zh&to=en
# https://fanyi.baidu.com/langdetect

from requests_html import HTMLSession
from fake_useragent import UserAgent
import js2py, json
ua = UserAgent()
session = HTMLSession()


class BDSpider(object):

    def __init__(self):
        self.title = input('请输入需要翻译的信息：')
        self.yy_url = 'https://fanyi.baidu.com/langdetect'
        self.fy_url = 'https://fanyi.baidu.com/v2transapi'
                    # https://fanyi.baidu.com/v2transapi?from=en&to=zh
        self.headers = {
            'Host': 'fanyi.baidu.com',
            'Origin': 'https://fanyi.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }

    def parse_start_response(self):
        """

        :return:
        """
        data = {
            'query': self.title
        }
        resp_json = session.post(self.yy_url, headers=self.headers, data=data).json()
        lan = resp_json['lan']
        self.parse_next_response(lan)

    def parse_next_response(self, lan):
        """
        解析翻译
        :param lan: 语言种类
        :return:
        """

        """获取token"""
        headers = {
            'Host': 'fanyi.baidu.com',
            'Cookie': 'BIDUPSID=B1B832BDC0B9036697CBAE56A3819AC0; PSTM=1616679045; BAIDUID=B1B832BDC0B90366E4545AA225C26525:FG=1; delPer=0; PSINO=7; H_PS_PSSID=33636_33261_33344_31660_33693_33675_33392_26350_33731; BA_HECTOR=0k01008hagag8h818n1g5p4470r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=8626351770282071039; BDSFRCVID=53LOJexroG3VC55eV39aIGgTgFweG7bTDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3aQ5rtKRTffjrnhPF3htA3XP6-hnjy3b7p5K5l5xL5bDoVQPJxbUKWbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMhfvJWMT-MTryKKOC0K5GefLRej5zQP-7bPjfKx-fKHnRhlRNB-3iV-OxDUvnyxAZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDMJ9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtCvDqTrP-trf5DCShUFst6JrB2Q-XPoO3KO4EIKGbqD5et_PQUJnKM5f5mkf3fbgylRM8P3y0bb2DUA1y4vpBtQmJeTxoUJ2-KDVeh5Gqfo15-0ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj_5jjO03H; BCLID_BFESS=8626351770282071039; BDSFRCVID_BFESS=53LOJexroG3VC55eV39aIGgTgFweG7bTDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR3aQ5rtKRTffjrnhPF3htA3XP6-hnjy3b7p5K5l5xL5bDoVQPJxbUKWbttf5q3RymJ42-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMhfvJWMT-MTryKKOC0K5GefLRej5zQP-7bPjfKx-fKHnRhlRNB-3iV-OxDUvnyxAZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUDMJ9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtCvDqTrP-trf5DCShUFst6JrB2Q-XPoO3KO4EIKGbqD5et_PQUJnKM5f5mkf3fbgylRM8P3y0bb2DUA1y4vpBtQmJeTxoUJ2-KDVeh5Gqfo15-0ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj_5jjO03H; __yjs_duid=1_b75ae51ad2974995196a273cb1f02d9f1616679047363; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1616679048; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BDUSS=zFvUjRqOWtEd1VyZDB6NjZuWnU1T0F6TnpSQzQxNlNZSFpRcjFwNkRoM1pJb1JnRVFBQUFBJCQAAAAAAAAAAAEAAADB7szat~y12Na0t6i52QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANmVXGDZlVxgd; BDUSS_BFESS=zFvUjRqOWtEd1VyZDB6NjZuWnU1T0F6TnpSQzQxNlNZSFpRcjFwNkRoM1pJb1JnRVFBQUFBJCQAAAAAAAAAAAEAAADB7szat~y12Na0t6i52QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANmVXGDZlVxgd; __yjsv5_shitong=1.0_7_6470de95c79259cd83793e8974ae69831657_300_1616680412079_175.9.142.188_e05e1274; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1616680422; ab_sr=1.0.0_MGFhYzliODIzODBmZTFmNWZhNWRjZDQ5ZDFhNGIyNDY1NTcwY2IxNmM3M2VlZWI1ZDM2NTEyNDMxZWRhYmM2ZDYzYzFlNjNlMjhhZDRlMDcyN2M0NGJhZDUyZjViZGI0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }
        token_url = 'https://fanyi.baidu.com/'
        res = session.get(token_url, headers=headers).content.decode()
        # print(res)
        token = re.findall("token: '(.*?)'", res)[0]
        # print(token)
        """生成sign"""
        js = js2py.EvalJs()
        with open('1(2).js', 'r')as f:
            js.execute(f.read())
        """构造请求参数"""
        to_data = 'en' if lan == 'zh' else 'zh'
        params = {
            'from': lan,
            'to': to_data
        }
        """构造请求体"""
        fy_data = {
            'from': lan,
            'to': to_data,
            'query': self.title,
            'transtype': 'realtime',
            'simple_means_flag': 3,
            'sign': js.e(self.title),
            'token': token,
            'domain': 'common'
        }
        response_json = session.post(self.fy_url, headers=headers, data=fy_data, params=params)
        print(response_json.url)
        self.parse_data(response_json.json())

    def parse_data(self, data_json):
        # "trans_result":{"data":[{"dst"
        # print(data_json)
        data = data_json['trans_result']['data'][0]['dst']
        print(data)


if __name__ == '__main__':
    b = BDSpider()
    b.parse_start_response()



"""
2.响应数据js逆向
"""











