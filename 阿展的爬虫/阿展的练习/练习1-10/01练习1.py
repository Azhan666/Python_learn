# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 爬虫的原理

# 1.聚焦爬虫

# 1. 导入request模块
import requests

# 2. 准备起始的url地址
start_url = 'http://www.baidu.com'

# 3. 发送请求，获取响应
response = requests.get(start_url) # 获取浏览器对应get请求的响应

# 4. 数据解析，数据提取
# 获取二进制数据
data = response.content # (content用于获取二进制数据)

#print(data) # 打印获取的数据

# 5. 保存数据
with open('2.jpg', 'wb')as f: #
    f.write(data)