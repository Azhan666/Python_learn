from requests_html import HTMLSession
from fake_useragent import UserAgent
import re, os
ua = UserAgent()
session = HTMLSession()


class Bz(object):

    def __init__(self):
        self.start_url = 'https://konachan.net/post?page={}&tags='

    def parse_start_url(self):
        """
        解析起始的url类地址
        :return:
        """
        # 创建循环记数，统计下载图片张数
        num = 1
        # 使用循环模拟发送翻页请求
        for page in range(1, 12280):
            # 发送请求，获取响应
            response = session.get(self.start_url.format(page))
            # 解析源码内容
            html_str = response.content.decode()
            # 正则提取小型图片url地址,返回一个列表
            url_list = re.findall("preload\('(.*?)'\);", html_str)
            # 方法回调解析
            self.parse_url_list(url_list, num)
            # 计数累加
            num += 1

    def parse_url_list(self, url_list, num):
        """
        解析拼接大型图片url地址
        :param url_list: 小型图片url地址列表
        :param num: 循环计数，统计下载图片张数
        :return:
        """
        # 遍历图片列表
        for url in url_list:
            # 正则匹配出壁纸属性id
            img_id = url[40:-4]
            # url地址拼接，获取大壁纸url
            next_url = f'https://konachan.net/sample/{img_id}/Konachan.com%20-%20324421%20sample.jpg'
            print(next_url)
            # 发送请求，获取二进制响应
            data = session.get(next_url).content
            # 方法回调解析，保存
            self.save_data(data, num, img_id)
            # 计数累加
            num += 1

    def save_data(self, data, num, img_id):
        """
        保存
        :param data: 图片二进制数据
        :param num: 循环计数，统计下载图片张数
        :param img_id: 保存图片的名称
        :return:
        """
        # 创建保存壁纸文件夹
        os_path = os.getcwd() + '/图片/'
        # 判断改文件夹路径是否存在，不存在就创建
        if not os.path.exists(os_path):
            os.mkdir(os_path)
        # 壁纸保存
        with open(os_path + img_id + '.jpg', 'wb')as f:
            f.write(data)
        print(f'第{num}张壁纸下载完成====logging====！！！')


if __name__ == '__main__':
    b = Bz()
    b.parse_start_url()


# https://konachan.net/post/show/324421/black_hair-blush-chitanda_eru-crying-hyouka-long_h
# https://konachan.net/sample/9dd006f482163934535db8ae45f8cf7d/Konachan.com%20-%20324421%20sample.jpg
# https://konachan.net/data/preview/9d/d0/9dd006f482163934535db8ae45f8cf7d.jpg  小
# https://konachan.net/sample/8a5091c117d80a8c33af7701e2a5d8bb/Konachan.com%20-%20324415%20sample.jpg
# https://konachan.net/sample/079defeaf37fcec6c53b038bcf04677a/Konachan.com%20-%20324421%20sample.jpg
# https://konachan.net/data/preview/07/9d/079defeaf37fcec6c53b038bcf04677a.jpg
















