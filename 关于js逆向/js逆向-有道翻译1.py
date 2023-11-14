# !/usr/bin/env python
# -*- coding: utf-8 -*-
from requests_html import HTMLSession
from fake_useragent import UserAgent # fake：假的
import js2py, json, re
ua = UserAgent()
session = HTMLSession()


class YDSpider(object):

    def __init__(self):
        self.title = input('请输入需要翻译的信息：')
        self.yy_url = 'https://fanyi.youdao.com/langdetect'
        self.fy_url = 'https://fanyi.youdao.com/v2transapi'
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
            'Host': 'fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=1273100589@120.219.100.128; OUTFOX_SEARCH_USER_ID_NCOO=172735692.11985913; JSESSIONID=aaaGw6e-EpzZM9tgjTFIx; ___rl__test__cookies=1617587117687',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        }
        token_url = 'https://fanyi.baidu.com/'
        res = session.get(token_url, headers=headers).content.decode()
        # print(res)
        token = re.findall("token: '(.*?)'", res)[0]
        # print(token)
        """生成sign"""
        js = js2py.EvalJs()
        with open('有道翻译-js文件.js', 'r')as f:
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
    b = YDSpider()
    b.parse_start_response()