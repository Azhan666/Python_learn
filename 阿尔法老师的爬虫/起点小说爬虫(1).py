from requests_html import HTMLSession
from urllib.parse import quote
import re, os
session = HTMLSession()


class QdBookSpider(object):

    def __init__(self):
        """
        1.准备起始数据
        """
        self.txt_book_name = input('请输入小说名称：')
        self.headers = {
    'cookie': '_qda_uuid=bfecb5d9-a0b7-d076-dfbe-3dc08498459f; newstatisticUUID=1578364957_1604014157; qdrs=0%7C3%7C0%7C0%7C1; qdgd=1; showSectionCommentGuide=1; mrecUUID=e6886710154aceaa2b42b71669adf97b; _csrfToken=ke1OMTYda0hLVKxjJxBmqGtargy5OcCFtsuK54n1; lrbc=1115277%7C22058859%7C0%2C1009817672%7C375339314%7C0%2C63856%7C340494470%7C1; rcr=1115277%2C1009817672%2C63856; _yep_uuid=d5ffa660-ea39-9eae-4fd5-7029f4fb9850; hiijack=0; tf=1; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_H_Search%22%2C%22l1%22%3A2%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%7D',
    'referer': 'https://www.qidian.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

    def parse_start_url(self):
        """数据的转化(编码)"""
        title = quote(self.txt_book_name)
        start_url = 'https://m.qidian.com/search?kw=' + title
        """
        2.发送请求，获取响应
        :return: 
        """
        response = session.get(start_url)
        """提取小说列表页第一部小说名称"""
        one = response.html.xpath('//ol[@id="books-"]/li/a/div/div/h4/mark/text()')
        one.remove(one[0])
        """提取小说列表页第一页其他小说名称"""
        title_list = response.html.xpath('//ol[@id="books-"]/li/a/div/div/h4/text()')
        """提取小说的链接"""
        href_list = response.html.xpath('//ol[@id="books-"]/li/a/@href')
        """循环遍历两张列表：小说名称列表，小说链接列表"""
        for href, name in zip(href_list, one+title_list):
            # href：小说链接
            # name: 小说名称
            """提取bookid"""
            book_id = href[6:]
            """拼接小说正为第一章第一页页伪url链接
            为什么称为伪url链接？
            因为其他的章节小说正文与这个url地址毫无关联
            """
            next_url = 'https://m.qidian.com' + href + '/0'
            resp = session.get(next_url, headers=self.headers)
            """提取第一页的翻页id"""
            next_id = re.findall('data-chapter-id="(.*?)"', resp.content.decode())[0]
            next_id = ''.join(next_id)
            self.callback_func(next_id, book_id)
            break

    def callback_func(self, next_id, book_id, num=0):
        """
        递归函数，构造翻页，获取小说正文
        :param next_id: 翻页id
        :param book_id: 小说id
        :param num: 翻页计数，记录章节
        :return:
        """
        try:
            """翻页url地址拼接"""
            page_url = f'https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=ke1OMTYda0hLVKxjJxBmqGtargy5OcCFtsuK54n1&bookId={book_id}&chapterId={next_id}'
            response = session.get(page_url, headers=self.headers)
            """提取翻页id"""
            next_id = re.findall('"next":(.*?),', response.content.decode())[0]
            """提取小说正文"""
            content = re.findall('"content":"(.*?)"', response.content.decode())[0]
            """替换<p>标签"""
            content = content.replace('<p>', '\n\t')
            """保存"""
            self.save_data(content, num)
            num += 1
            """回调递归翻页"""
            self.callback_func(next_id, book_id, num)
        except Exception as e:
            print(e)
            print('小说爬完了====55555！！！！')

    def save_data(self, content, num):
        """
        保存-
        :param content: 小说正文
        :param num: 翻页计数，记录章节
        :return:
        """
        os_path = os.getcwd() + '/起点小说/'
        if not os.path.exists(os_path):
            os.mkdir(os_path)
        with open(os_path + self.txt_book_name + '.txt', 'a+', encoding='UTF-8')as f:
            f.write(content)
        print(f'小说===={self.txt_book_name}====第{num+1}章下载完成')


if __name__ == '__main__':
    q = QdBookSpider()
    q.parse_start_url()






