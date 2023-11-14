"""
课题：数据提取之正则
"""

"""1.需要掌握的正则方法"""
# 正则匹配手机号码
#

# 16607440667
# asdfgh16607440667afadgfaggda
import re
# str_1 = '16607440667'
# str_2 = 'asdfgh16607440667afadgfaggda'
# # 第一个参数：规则    第二个参数：匹配对象
# # result = re.findall(r'^1[3-9]\d{9}$', str_1)
# # print(result)
#
# result = re.findall(r'\d+', str_2)
# print(result)
"""findall   找所有"""
# str1 = '<meta http-equiv="content-type" content="text/html;charset=utf-8"/>adacc/sd/sdef/24'

# result = re.findall('="(.*?)"', str1)
# print(result)

"""match    从头找一个"""
# result = re.match('<meta http-equiv="content-type" content="(.*?)"', str1).groups()
# print(result)

"""search   找到一个就返回"""
# result = re.search('="(.*?)"', str1).groups()
# print(result)

"""转义"""

# str_1 = r'123456\n789\t123'
# str_2 = '123456\n789\t123'
# str_3 = '123456\\n789\\t123'
#
# print(str_3)
# 路径操作
# C:\Users\宋\Desktop\材料\python爬虫课件\爬虫A课
# str_4 = r'C:\Users\宋\Desktop\材料\python爬虫课件\爬虫A课'
# print(str_4)
# 结论：我们可以通过，字符串前面加r进行内容的转义，或者是\进行转义


"""3.案例"""

"""外包需求，爬取微博评论"""
# https://weibo.com/u/1739928273?is_hot=1#1615292640919
# https://weibo.com/xiaozhan1?is_hot=1

# 评论数据包(第一页)
# https://m.weibo.cn/comments/hotflow?id=4609229132925240&mid=4609229132925240&max_id_type=0
# https://m.weibo.cn/comments/hotflow?id=4609229132925240&mid=4609229132925240&max_id=45097742939432056&max_id_type=0

# 下一页的max_id在上一页的响应中

# 总结开发思路
# 1.进入某个明星的微博首页
# 2.观察某一条微博动态的评论
# 3.点击查看更多，进入到微博正文详情页
# 4.进入手机模式访问
# 5.去观察异步加载评论包  hotflow


from requests_html import HTMLSession
from jsonpath import jsonpath
import os, xlwt, xlrd, random
from xlutils.copy import copy
session = HTMLSession()


class WbSpider(object):
    USER_AGENT = ['Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Hot Lingo 2.0)',
                  'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3451.0 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:57.0) Gecko/20100101 Firefox/57.0',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2999.0 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.70 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174',
                  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.1.4322; MS-RTC LM 8; InfoPath.2; Tablet PC 2.0)',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.61',
                  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; .NET4.0C; CIBA; Maxthon 2.0)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1',
                  'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; Touch; MASMJS)',
                  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Hot Lingo 2.0)',
                  'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3451.0 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:57.0) Gecko/20100101 Firefox/57.0',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2999.0 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.70 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174',
                  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.1.4322; MS-RTC LM 8; InfoPath.2; Tablet PC 2.0)',
                  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.61',
                  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; .NET4.0C; CIBA; Maxthon 2.0)',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1',
                  'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
                  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; Touch; MASMJS)',
                  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4093.3 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Swurl) Chrome/77.0.3865.120 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                  'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Goanna/4.7 Firefox/68.0 PaleMoon/28.16.0',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:75.0) Gecko/20100101 Firefox/75.0',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/91.0.146 Chrome/85.0.4183.146 Safari/537.36',
                  'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 VivoBrowser/8.4.72.0 Chrome/62.0.3202.84',
                  'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:83.0) Gecko/20100101 Firefox/83.0',
                  'Mozilla/5.0 (X11; CrOS x86_64 13505.63.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:68.0) Gecko/20100101 Firefox/68.0',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.400',
                  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36',
                  ]

    def __init__(self):
        """
        1.准备起始的url地址
        """
        self.start_url = 'https://m.weibo.cn/comments/hotflow?id=4584774314492510&mid=4584774314492510&max_id_type=0'
        self.headers = {
            'cookie': 'WEIBOCN_FROM=1110005030; loginScene=102003; SUB=_2A25NQxtiDeRhGeFL61AR8SrEzTyIHXVuz6UqrDV6PUJbkdAKLUr3kW1NQrcPFCffc-yk7fH6nW110ZylyUS7C_xh; _T_WM=85509930160; XSRF-TOKEN=e9287f; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4609229132925240%26luicode%3D20000061%26lfid%3D4609229132925240%26uicode%3D20000061%26fid%3D4609229132925240',
            'referer': 'https://m.weibo.cn/status/K3S5HcgZi?filter=hot&root_comment_id=0&type=comment&jumpfrom=weibocom',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': 'e9287f'
        }

    def parse_start_url(self):
        """
        2.发送请求，获取响应，解析起始的url地址
        :return:
        """
        response_json = session.get(self.start_url, headers=self.headers).json()
        # 翻页的id
        max_id = jsonpath(response_json, '$..max_id')[0]
        self.parse_response_data(max_id)

    def parse_response_data(self, max_id):
        """
        3.解析响应，数据提取
        :return:
        """
        headers = {
            'cookie': 'WEIBOCN_FROM=1110005030; loginScene=102003; SUB=_2A25NQxtiDeRhGeFL61AR8SrEzTyIHXVuz6UqrDV6PUJbkdAKLUr3kW1NQrcPFCffc-yk7fH6nW110ZylyUS7C_xh; _T_WM=85509930160; XSRF-TOKEN=e9287f; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4609229132925240%26luicode%3D20000061%26lfid%3D4609229132925240%26uicode%3D20000061%26fid%3D4609229132925240',
            'referer': 'https://m.weibo.cn/status/K3S5HcgZi?filter=hot&root_comment_id=0&type=comment&jumpfrom=weibocom',
            'user-agent': random.choice(self.USER_AGENT),
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': 'e9287f'
        }
        try:
            next_url = f'https://m.weibo.cn/comments/hotflow?id=4584774314492510&mid=4584774314492510&max_id=637202071295295&max_id_type=0'
            response_json = session.get(next_url, headers=headers).json()
            # 翻页的id
            max_id = jsonpath(response_json, '$..max_id')[0]
            # 获取评论：
            content_data = response_json['data']['data']
            # 数据保存
            self.save_data(content_data)
            self.parse_response_data(max_id)
            print('开始获取下一页----logging----！！！')
        except Exception as e:
            print('评论爬完了，终止程序', e)
            return

    def save_data(self, content_data):
        """
        4.数据的保存
        :return:
        """
        for content in content_data:
            item = {}
            # 粉丝id
            fs_id = content['user']['id']
            item['粉丝id'] = fs_id
            # 评论内容text
            text = jsonpath(content, '$..text')[0]
            if 'span' in text:
                text = re.sub('<span .*?</span>', ''.join(re.findall('alt=(.*?) ', text)[0]), text)
            item['评论内容'] = text
            # 粉丝昵称fs_name
            fs_name = jsonpath(content, '$..screen_name')[0]
            item['粉丝昵称'] = fs_name
            # 粉丝性别
            gender = jsonpath(content, '$..gender')[0]
            item['粉丝性别'] = gender
            list_1 = [fs_id, text, fs_name, gender]
            dict_1 = {
                '基本详情': list_1
            }
            self.save_excel(dict_1)

    def save_excel(self, data):
        # data = {
        #     '基本详情': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        # }
        os_path_1 = os.getcwd() + '/微博评论/'
        if not os.path.exists(os_path_1):
            os.mkdir(os_path_1)
        # os_path = os_path_1 + self.os_path_name + '.xls'
        os_path = os_path_1 + '何炅微博评论.xls'
        if not os.path.exists(os_path):
            # 创建新的workbook（其实就是创建新的excel）
            workbook = xlwt.Workbook(encoding='utf-8')
            # 创建新的sheet表
            worksheet1 = workbook.add_sheet("基本详情", cell_overwrite_ok=True)
            borders = xlwt.Borders()  # Create Borders
            """定义边框实线"""
            borders.left = xlwt.Borders.THIN
            borders.right = xlwt.Borders.THIN
            borders.top = xlwt.Borders.THIN
            borders.bottom = xlwt.Borders.THIN
            borders.left_colour = 0x40
            borders.right_colour = 0x40
            borders.top_colour = 0x40
            borders.bottom_colour = 0x40
            style = xlwt.XFStyle()  # Create Style
            style.borders = borders  # Add Borders to Style
            """居中写入设置"""
            al = xlwt.Alignment()
            al.horz = 0x02  # 水平居中
            al.vert = 0x01  # 垂直居中
            style.alignment = al
            # 合并 第0行到第0列 的 第0列到第13列
            '''基本详情13'''
            # worksheet1.write_merge(0, 0, 0, 13, '基本详情', style)
            excel_data_1 = ('粉丝id', '评论内容', '粉丝昵称', '粉丝性别')
            for i in range(0, len(excel_data_1)):
                worksheet1.col(i).width = 2560 * 3
                #               行，列，  内容，            样式
                worksheet1.write(0, i, excel_data_1[i], style)
            workbook.save(os_path)
        # 判断工作表是否存在
        if os.path.exists(os_path):
            # 打开工作薄
            workbook = xlrd.open_workbook(os_path)
            # 获取工作薄中所有表的个数
            sheets = workbook.sheet_names()
            for i in range(len(sheets)):
                for name in data.keys():
                    worksheet = workbook.sheet_by_name(sheets[i])
                    # 获取工作薄中所有表中的表名与数据名对比
                    if worksheet.name == name:
                        # 获取表中已存在的行数
                        rows_old = worksheet.nrows
                        # 将xlrd对象拷贝转化为xlwt对象
                        new_workbook = copy(workbook)
                        # 获取转化后的工作薄中的第i张表
                        new_worksheet = new_workbook.get_sheet(i)
                        for num in range(0, len(data[name])):
                            new_worksheet.write(rows_old, num, data[name][num])
                        new_workbook.save(os_path)


if __name__ == '__main__':
    wb = WbSpider()
    wb.parse_start_url()










