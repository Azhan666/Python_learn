# !/usr/bin/env python
# -*- coding: utf-8 -*-
#头文件
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import re
import time
# import threading
# import queue
from makerbean import excel_bot as ebot
import pandas as pd
import json
import csv
# 'https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key='
# 河南 req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=130&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=3f689134233b1e329424d1965050c72a&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7E-2RqF7E8jAC7HLCL4ThIWg&key={quote_plus(keyword)}')

def get_html(url):
    """请求获得网页内容"""
    print('Downloading:', url)
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url,headers = kv,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print("成功访问")
        print(r.request.headers)
        return r.text
    except:
        print("访问错误")
        return " "
def get_urls(keyword, start_page, end_page=None):
    session = requests.Session()
    liepin_urls = {}
    if keyword not in liepin_urls:
        req = session.get(
            f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=150&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=1dee8deab279865320850b4b3579a2a6&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EYd2LHk16GV6VB7sJT4heig&key={quote_plus(keyword)}')
        soup = BeautifulSoup(req.text, 'lxml')
        liepin_urls[keyword] = 'https://www.liepin.com'
        liepin_urls[keyword] += '&d_curPage={d_curPage}'.join(soup.select('.pagerbar a')[3]['href'].split('&d_curPage='))
        liepin_urls[keyword] = liepin_urls[keyword].split('&curPage=')[0] + '&curPage={curPage}'
    if end_page is None:
        end_page = start_page + 1
    data = []
    for page in range(start_page, end_page):
        time.sleep(1)
        if page > 0:
            url = liepin_urls[keyword].format(d_curPage=page - 1, curPage=page)
        else:
            url = liepin_urls[keyword].format(d_curPage=page + 1, curPage=page)
        time.sleep(2)
        html = get_html(url)
        parser_html(html,data)
    return data

def parser_html(html,data):
    soup = BeautifulSoup(html, 'lxml')

    # data = []

    for item in soup.select('.sojob-item-main'):
        job_name = item.select('h3 a')[0].text.strip()
        job_company = item.select('.company-name')[0].text.strip()
        job_field = item.select('.field-financing')[0].text.strip()
        job_salary = item.select('.condition .text-warning')[0].text.strip()
        if job_salary == '面议':
            annual_salary = -1
        else:
            if '-' in job_salary:
                min_salary = int(job_salary[:job_salary.index('-')])
                max_salary = int(job_salary[job_salary.index('-') + 1:job_salary.index('k')])
                months = int(job_salary[job_salary.index('·') + 1:-1])
                annual_salary = (min_salary + max_salary) / 2 * months * 1000
            else:
                monthly_salary = int(job_salary.split('k')[0])
                months = int(job_salary[job_salary.index('·') + 1:-1])
                annual_salary = monthly_salary * months * 1000
        job_area = item.select('.condition .area')[0].text.strip()
        job_edu = item.select('.condition .edu')[0].text.strip()
        job_experience = item.select('.condition span')[-1].text.strip()
        data.append(
            [job_name, job_company, job_field, job_salary, annual_salary, job_area, job_edu, job_experience])
    return data
def save_data(data):
    for job in data:
        ebot.add_row(job)
    ebot.save('数据分析河南前两页')

def main():
    # 新疆
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=300&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=38b5242b77be1399d00dc4da2bb2088e&d_ckId=208adb59cd43241d9f05034c74b386c0&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EdSsSNtRUg09tgzsv7oykKQ&key={quote_plus(keyword)}')
    # 宁夏
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=230&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=38b5242b77be1399d00dc4da2bb2088e&d_ckId=a5f8dc1ff931b51cb0d27141915e26f9&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7Eq9yzwZJv-mZrF_Z7-A0oVw&key={quote_plus(keyword)}')
    # 青海
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=240&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=38b5242b77be1399d00dc4da2bb2088e&d_ckId=3952d20c2df8c798bdf39fe8e0daaedf&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7Eg3uVgDK9HODPvq89PhpURA&key={quote_plus(keyword)}')
    # 澳门无
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=330&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=38b5242b77be1399d00dc4da2bb2088e&d_ckId=06feec823cf5192c82584ae884e9a2af&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EZhm13qQ83cRoTjubehmEqw&key={quote_plus(keyword)}')
    # 甘肃
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=100&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=27615313f112d8e1afc10535b0d8c4d1&d_ckId=5399b31674eb00c935873e6852927b57&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=ZFDYQyfloRvvhTxLnVV_Qg%7EIUgrFnctYtHfCwJ5QsRm_A&key={quote_plus(keyword)}')
    # 陕西
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=270&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=4ab1fda94a09a69f49788d2c28a0f2a7&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EIUgrFnctYtHfCwJ5QsRm_A&key={quote_plus(keyword)}')
    # 西藏
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=290&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=e5b5d17a2fc5752ccaa8990d21d3ff14&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EmnuVP9wLhfq0StfyW-1r8g&key={quote_plus(keyword)}')
    # 云南
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=310&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=d8f35fbe1b44d1490b4961f3e7ec3cef&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7Etc_TXaJLPCX7pJcGGMguyw&key={quote_plus(keyword)}')
    # 贵州
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=120&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=abc7f46ba4c7f1052c3aae61a34cafa2&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EsNCyEh9K8iXdc3lQri4ryw&key={quote_plus(keyword)}')
    # 四川
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=280&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=0e551b3fd83e697072fa14df8c142171&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EsmDSbXB-BhvVXveoCmlmGQ&key={quote_plus(keyword)}')
    # 海南
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=130&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=3f689134233b1e329424d1965050c72a&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7E-2RqF7E8jAC7HLCL4ThIWg&key={quote_plus(keyword)}')
    # 广西
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=110&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=8d8e3f2804f2b5221e85ec6ae1014e93&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EfFXhtCz6er9HGeShZgwDtQ&key={quote_plus(keyword)}')
    # 广东
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=050&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=1d73c89ffa2712bf8027bc9229e690b9&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EKeQOZUqNCSOR3hkAMJqC_A&key={quote_plus(keyword)}')
    # 湖南
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=180&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=eb3fba2fc68caaaff5da8c80742c9644&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7Eha394EQxjcUgWMmp6o3mbw&key={quote_plus(keyword)}')
    # 湖北
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=170&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=1ab6c317b90a86750dc5ef5a302359c4&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EfvArAsL6kEsVgriVqjWDgg&key={quote_plus(keyword)}')
    # 河南
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=150&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=1dee8deab279865320850b4b3579a2a6&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EYd2LHk16GV6VB7sJT4heig&key={quote_plus(keyword)}')
    # 山东
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=250&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=0216ca70d051c24e0c51bced71bdd3b3&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EIkEEuJuvLv2dGbdoQ234Lw&key={quote_plus(keyword)}')
    # 江西
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=200&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=8b324b86433a1c9785e2aca29e22b8c5&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EE08QNgJtmOV680BaDaEpHQ&key={quote_plus(keyword)}')
    # 福建
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=090&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=4cf0416b7818fb5fc639a6dbfb168bd7&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EJMx30n1lsc755NKLnrvnNQ&key={quote_plus(keyword)}')
    # 安徽
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=080&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=48cfff7a9fe5e32b7bd7601816515302&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EH_SzbooyWnTrJdTiOmHFOg&key={quote_plus(keyword)}')
    # 浙江
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=070&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=0c3fa54d9747e26917ded9193d93be53&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EdA5pRg4ARjK03deNFrE1ag&key={quote_plus(keyword)}')
    # 江苏
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=060&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=af0b13b2904a876d480ed0a6309f4af3&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EmvK22_75e8VLRVz0nBKwsA&key={quote_plus(keyword)}')
    # 黑龙江
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=160&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=9a54644236140cf6d3b7fcebb6a2d5c6&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7E7jg29BhZ1buipvhH1uQRpw&key={quote_plus(keyword)}')
    # 吉林
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=190&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=600bc083aa3d7ecac0e9d2082f0ef286&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EVxx8Zzcj4VofWWxzQPtnpQ&key={quote_plus(keyword)}')
    # 辽宁
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=210&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=42d04c7cb757aeb7dafe5f7cd846f69a&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7Em4FdKkgsACt9OvlfQudRNQ&key={quote_plus(keyword)}')
    # 内蒙古
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=220&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=6619c5e4febd9fc5b233b1992b5b571d&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EpB4I42HPb8cHNg8_vD66iw&key={quote_plus(keyword)}')
    # 山西
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=260&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=dac9e73bfb3c255756e5eae505881522&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7E9Zvu58iL19-7ql2G9P-uCw&key={quote_plus(keyword)}')
    # 河北
    # req = session.get(f'https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=140&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=4ab1fda94a09a69f49788d2c28a0f2a7&d_ckId=f784e49016925584bb080f53907048e0&d_sfrom=search_prime&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EBTGkT039HHupsg31gKGKVw&key={quote_plus(keyword)}')
    a = get_urls('数据分析',0,10)
    # 应该从0开始
    # 如果要40*30*10 = 12000
    print(a)
    print(len(a),type(a))
    save_data(a)

    df1 = pd.DataFrame(a)
    df =  pd.concat(df1,axis=1)
    df.columns=['岗位名称','公司全名''备注','薪资','','工作地点','学历要求','工作年限']
    df1.to_excel('河北数据分析.xlsx',sheet_name='sheet1',index=None,header=None,encoding='utf-8')
    # save_data(data)
    # print(data)

if __name__ == '__main__':
    main()

