#!/usr/bin/env python
#coding=utf-8

import requests
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.0.0',
    'Cookie':'thw=cn; UM_distinctid=15b13671485223-0fbed515b559e8-6d28626c-1fa400-15b13671486689; CNZZDATA30057895=cnzz_eid%3D2068677963-1490674135-null%26ntime%3D1490933406; CNZZDATA30058279=cnzz_eid%3D753590560-1490678406-https%253A%252F%252Fs.2.taobao.com%252F%26ntime%3D1490934640; CNZZDATA1252911424=1526003520-1490676799-null%7C1490934809; v=0; _tb_token_=33ee56887e6be; swfstore=136160; uc1=cookie14=UoW%2BufunPTqo8w%3D%3D&lng=zh_CN&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&existShop=false&cookie21=VT5L2FSpczFp&tag=7&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; uc3=sg2=Vv6YOWneGigexaEX3wJ8n%2FnKXAdKb1m66CjeyxVm3HE%3D&nk2=o%2FMuqFij&id2=UUGrdCl1SXYM3Q%3D%3D&vt3=F8dARVQ0alATkYPMcXc%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; hng=CN%7Czh-CN%7CCNY; existShop=MTQ5MTM4NjM2Mw%3D%3D; uss=VTx%2FqAd1faC8LzodZV3odXscFAMJqiebyinm5rUGaSp4K%2Fguv7qd2FF65g%3D%3D; lgc=%5Cu674E%5Cu6C9B69; tracknick=%5Cu674E%5Cu6C9B69; cookie2=1c474790ec319dd8008f140609d817c4; sg=919; mt=np=&ci=6_1&cyk=0_0; cookie1=BxoGLibvCyrC5acB7QMZukC%2BNrrcKhrUYfteXw%2BHtgo%3D; unb=2992847871; skt=9fa208e6a1f9dedc; t=9e02dd43591dd90123d6210ffb2ed37a; _cc_=VT5L2FSpdA%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=%5Cu674E%5Cu6C9B69; cookie17=UUGrdCl1SXYM3Q%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261491387249799; cna=bjVWEU3mE3MCAdoRxaz1J6gs; l=AnFxLStK4iMNoFzmAjsFjACdAfcLXuXQ; isg=Au_vsjs464IKr--LJl0FejTkfgP090O2-BqGpwF8i95lUA9SCWTTBu0CpPcV'
}

host_url = 'https://2.taobao.com/'


#获取所有板块一级标题的链接
def get_first_level_url():
    global first_level_urls
    first_level_urls = []  # 这个列表是所有一级标题的链接

    web_data = requests.get(host_url,headers = headers)
    soup = BeautifulSoup(web_data.text,'lxml')
    first_level = soup.select('div.category-wrapper > dl > dt > a')
    for first_level_url in first_level:
        first_level_url = first_level_url.get('href')
        first_level_urls.append(first_level_url)
    print(first_level_urls)
    return first_level_urls


#获取所有板块二级标题的链接
def get_second_level_url():

    for first_level_url in first_level_urls:
        print(first_level_url)
        web_data = requests.get(first_level_url,headers = headers)
        soup = BeautifulSoup(web_data.text,'lxml')
        second_level_urls = soup.select('div#J_CategoryFilters > div > ul > li > a')
        for second_level_url in second_level_urls:
            second_level_url = second_level_url.get('href')
            print(second_level_url)

get_second_level_url()