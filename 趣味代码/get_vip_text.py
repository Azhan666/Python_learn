# !/usr/bin/env python
# -*- coding: utf-8 -*-
# coding =utf-8
import tkinter as tk
import re  # 正则表达式
import urllib

import requests


window = tk.Tk()
url = "https://wenku.baidu.com/view/0b6e1af8777f5acfa1c7aa00b52acfc788eb9f7f.html?fr=search-1-wk_es_paddle-income4&fixfr=iavk7DwNwLKuMHW3uIYE%2Bg%3D%3D"

window.title('百度文库爬虫')
window.geometry('500x300')
baseNum = tk.Label(window, text='请输入网址：')
baseNum.pack()
base_text = tk.StringVar()
base = tk.Entry(window, textvariable=base_text)
base.pack()
def xxxx():

    print("wo you shuchu")
    url = base_text.get()

    content_list = kaishi(url)
    f = open(r'D:\python_learn\Python基础阶段\趣味代码\123.txt', 'a+')




    for i in range(0, len(content_list)):
        f.write(str(content_list[i]))



    print("xxxxx")

    print(str(content_list))



def main():

    tk.Button(window, text="生成桌面文件", command=xxxx).pack()

    tk.Button(window, text="退出1", command=window.quit).pack()




    window.mainloop()




findgupiao = re.compile('">(.*?)</p>')





def kaishi(url):
    headers = {

    }

    request = urllib.request.Request(url, headers=headers)

    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('unicode_escape')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    content_list=[]
    content_list = re.findall('"c":"(.*?)","p"', html)







    return content_list

    # with open("rsp.html", "w+", encoding="utf-8")as f:
    #     f.write(session.get(url1).text)


if __name__ == "__main__":
    main()

