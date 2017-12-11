#!/usr/bin/python
#coding=utf-8

_auther = 'peili'

import requests
from bs4 import BeautifulSoup

start_url = 'http://sz.ganji.com/wu/'
host_url = 'http://sz.ganji.com'

def get_fenlei_url():
    web_data = requests.get(start_url)
    soup  = BeautifulSoup(web_data.text,'lxml')
    links = soup.select('dl.fenlei dt > a')
    for link in links:
            link = host_url+link.get('href')
        print(link)

# get_fenlei_url()

fenlei_url = '''
    http://sz.ganji.com/jiaju/
    http://sz.ganji.com/rirongbaihuo/
    http://sz.ganji.com/shouji/
    http://sz.ganji.com/shoujihaoma/
    http://sz.ganji.com/bangong/
    http://sz.ganji.com/nongyongpin/
    http://sz.ganji.com/jiadian/
    http://sz.ganji.com/ershoubijibendiannao/
    http://sz.ganji.com/ruanjiantushu/
    http://sz.ganji.com/yingyouyunfu/
    http://sz.ganji.com/diannao/
    http://sz.ganji.com/xianzhilipin/
    http://sz.ganji.com/fushixiaobaxuemao/
    http://sz.ganji.com/meironghuazhuang/
    http://sz.ganji.com/shuma/
    http://sz.ganji.com/laonianyongpin/
    http://sz.ganji.com/xuniwupin/
    http://sz.ganji.com/qitawupin/
    http://sz.ganji.com/ershoufree/
    http://sz.ganji.com/wupinjiaohuan/
'''