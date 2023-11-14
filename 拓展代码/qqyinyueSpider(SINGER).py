# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------

import requests, os, jsonpath, time
from lxml import html
etree = html.etree
from pprint import pprint


def main():
    # 1、url + headers
    # start_url = input('请输入要下载音乐链接: ')
    singer_name = input('请输入要下载歌手名字: ')
    start_url = r'https://music.taihe.com/search?word={}'.format(singer_name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36'
    }

    # 2、发请求，响应
    response = requests.get(start_url, headers=headers).text
    # pprint(response)

    # 3、解析数据，获取song_names, song_hrefs
    html_str = etree.HTML(response)
    song_names = html_str.xpath(r'//li[@class="pr t clearfix"]/div[@class="song ellipsis clearfix"]/div/a/text()')
    # pprint(song_names)
    song_hrefs = html_str.xpath(r'//li[@class="pr t clearfix"]/div[@class="song ellipsis clearfix"]/div/a/@href')
    # pprint(song_hrefs)

    # 4、遍历得到song_name, song_id
    for song_name, song_href in zip(song_names, song_hrefs):
        song_id = song_href.replace(r'/song/', '')
        # pprint(song_id)

        # 5、获取当前时间戳 time_stamp
        time_stamp = int(time.time())
        # pprint(time_stamp)

        # 6、拼接song_url,发请求，得到song_info
        song_url = r'https://music.taihe.com/v1/song/tracklink?sign=3df91096f695aac4eb88eacd723e25e4&appid=16073360' \
                   r'&TSID={}&timestamp={}'.format(song_id, time_stamp)
        song_info = requests.get(song_url, headers=headers).json()
        # pprint(song_info)

        # 7、解析数据，得到song_url, song_content
        song_url = jsonpath.jsonpath(song_info, '$..path')[0]
        song_content = requests.get(song_url, headers=headers).content

        # 8、创建文件夹
        if not os.path.exists(r'./{}'.format(singer_name)):
            os.mkdir(r'./{}'.format(singer_name))

        # 9、保存文件
        try:
            with open(r'./{}/{}.mp3'.format(singer_name, song_name), 'wb') as f:
                f.write(song_content)
                print(r'***歌曲下载完成：{}.mp3'.format(song_name))
        except Exception as e:
            continue


if __name__ == '__main__':
    main()