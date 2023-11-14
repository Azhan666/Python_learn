# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 、Edgar
# @date: 7/29
# @version: 1.0.0
# @function: search for info in the CSDN but in a more simple way

import urllib
import urllib.error
import urllib.request
import urllib.parse
import string
import re
import inspect
BIG = 1000

from bs4 import BeautifulSoup  # 该错误是因为没有从其他库中导入该模块



# 通过观察，发现csdn上的最多只有500页，而且一般都可以达到这个数目
def get_data(keyword, filename, page=500):
    # 清空原文件
    filename = filename + ".txt"
    file = open(filename, "w")
    file.close()
    # 记录内容条数
    count = 1
    # 记录错误数目
    error_count = 0

    # 第几页
    for num in range(1, page):
        print("\n这是第 {} 页 >>".format(num))
        with open(filename, "a", encoding="utf-8") as file:
            file.write("这是第 {} 页 >>\n".format(num))
        url = "https://so.csdn.net/so/search/s.do?p={}&q={}".format(num, keyword)

        # 如果keyword中含有中文，需要进行解析
        if is_chinese(keyword):
            url = urllib.parse.quote(url, safe=string.printable)

        # 构造请求头
        header = {"Users-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/75.0.3770.142 Safari/537.36"}
        request = urllib.request.Request(url, headers=header)

        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            error_count += 1
            print(e.reason)
        except urllib.error.URLError as e:
            error_count += 1
            print(e.reason)
        except Exception as e:
            error_count += 1
            print("Unknown error: %s" % e)
        else:
            bs = BeautifulSoup(response, 'lxml')
            # 避免bs是None
            try:
                content = bs.find("div", {"class": "search-list-con"})
            except Exception as e:
                error_count += 1
                print(e)
            # 网页源代码---all
            # filename_1 = "%s.html"% "content"
            # with open(filename_1, "w", encoding = 'utf-8') as file:
            #     file.write(str(content.prettify()))
            try:
                needed_content = content.find_all("dl", {"class": "search-list J_search"})[2:-1]
            except Exception as e:
                error_count += 1
                print(e)
            # 网页源代码 --局部需要的源代码
            # filename_2 = "%s.html"%"needed_content"
            # with open(filename_2, "w", encoding="utf-8") as file:
            #     file.write(str(needed_content))

            print("-"*66)

            for content in needed_content:
                # with open("data", "a", encoding="utf-8") as file:
                #     file.write(str(content.text))
                # get title
                # print(content)

                # deal with the title
                try:
                    title = "Title: {}".format(content.find("div", {"class": "limit_width"}).find("a").text)
                    if is_blog(content):
                        pass
                    else:
                        continue
                except AttributeError as e:
                    title = "Title: None"
                    pass
                else:
                    print()
                    print("第%d条：" % count)
                    count += 1
                    print(title)

                # deal with the author
                try:
                    author = "Author: {}".format(content.find("span", {"class": "author"}).find("a").text)
                except AttributeError as e:
                    author = "Author: None"
                    pass
                else:
                    print(author)

                # deal with the date
                try:
                    date = "Date: {}".format(content.find("span", {"class": "date"}).text[3:])
                except AttributeError as e:
                    date = "Date: None"
                    pass
                else:
                    print(date)

                # deal with the read times
                try:
                    read_times = "Read times: {}".format(content.find("span", {"class": "down fr"}).text.strip())
                except AttributeError as e:
                    read_times = "Read times: None"
                    pass
                else:
                    print(read_times)

                # deal with the link
                try:
                    link = "link: {}".format(content.find("dd", {"class": "author-time"}).find("span", {"class": "link"}).text.strip())
                except AttributeError as e:
                    link = "link: None"
                    pass
                else:
                    print(link)

                print()
                print("-"*66)
                try:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("-"*60)
                        file.write('\n')
                        file.write('\n')
                        file.write("第 {} 条：".format(count-1))
                        right_write(file, title)
                        file.write('\n')
                        right_write(file, author)
                        file.write('\n')
                        right_write(file, date)
                        file.write('\n')
                        right_write(file, read_times)
                        file.write('\n')
                        right_write(file, link)
                        file.write('\n')
                        file.write('\n')
                        file.write("-"*60)
                        file.write('\n')
                        file.write('\n')
                except Exception as e:
                    print(e)

    print()
    print()
    print("共检索到 {} 条内容, 有 {} 个出现意外".format(count, error_count))
    print("Done! And there will be a file with above data.")

    # 将相关的内容写入文档中
    with open(filename, "a", encoding="utf-8") as file:
        print()
        print()
        file.write("\n")
        file.write("共检索到 {} 条内容, 有 {} 个出现意外".format(count, error_count))


# 判断输入的是否是中文
def is_chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


# if the object data is None,
# replace it with None in the input
def right_write(file, data):
    if data is None:
        file.write("{}: None".format(varname(data)))
    else:
        file.write(data)


# 判断所爬取的是否是博客
def is_blog(content):
    class_name = content.dt.span
    if class_name["class"][1] == "flag_icon1":
        return True
    else:
        return False


# 网上事项将变量名转化成字符串
def varname(p):
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1)


# 找到网页上所有的内容数目,但是目前无法实现，呜呜，考虑将bs或者num_data全局化
def get_num(bs):
    bs_data = bs.find("span", {"class": "page-nav"}).find("span", {"class", "text"})
    num_data = bs_data.text
    return num_data


if __name__ == '__main__':
    print("Welcome to use this tool to search info you want in CSDN ")
    keyword = input("Please input what you want to find in CSDN: ")

    # 把搜索过的keyword保存到文件夹中
    with open("search history.txt", "a", encoding="utf-8") as file:
        file.write("--> ")
        file.write(keyword)
        file.write("\n")

    # 获取处理keyword
    while len(keyword) == 0:
        print("Please input the keyword again: ")
        keyword = input("Please input what you want to find in CSDN: ")

    get_data(keyword, keyword)

    # 防止控制台执行的时候闪退
    input("")




