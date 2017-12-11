#!/usr/bin/python
#coding=utf-8

_auther = 'peili'

import requests
from bs4 import BeautifulSoup
import time
import pymongo
import random

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.0.0',
    'Cookie':'citydomain=sz; ganji_uuid=7867229953480587552964; ganji_xuuid=1cce8c58-d342-4227-c41b-571abf3f10dd.1481891149000; STA_DS=2; als=0; 58uuid=587e612a-e9a7-4f4b-9544-61376a5a58fd; new_uv=1; __utmt=1; xxzl_tracker=vw+SdIcohaCLWAkKZ4F4cJab47MTVdtiqH74Q+GTyZCQnnZuOuM9LsmfidoGNyUi2+L53foad+jKREYNkscX5g==; supercookie=AGDjAmD2Awx1WTL2LJIxMJMwZQN4ZGt5ZzV4MQZ1AQtlA2Z1ZmDjZGV2LGVjZwHlATD%3D; lg=1; crawler_uuid=148189757625619764419065; GANJISESSID=3a3188a94c043cfb9613ec2ad5de8f20; __utmganji_v20110909=a6079116-c14d-4a7b-9636-2898ad5815ad; _gj_txz=MTQ4MTg5ODE4ODpE+WbZuLIk2GBvch9kguAxM+6NnA==; sscode=iAgfVgKGQGPfagGyiATiEjip; GanjiUserName=guyjhfgh; GanjiUserInfo=%7B%22user_id%22%3A540746695%2C%22email%22%3A%22%22%2C%22username%22%3A%22guyjhfgh%22%2C%22user_name%22%3A%22guyjhfgh%22%2C%22nickname%22%3A%22PEI%22%7D; bizs=%5B%5D; last_name=guyjhfgh; ganji_login_act=1481897589231; _gl_tracker=%7B%22ca_source%22%3A%22cn.bing.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_bing%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A73522897121%7D; __utma=32156897.310999990.1481891123.1481891123.1481897545.2; __utmb=32156897.5.10.1481897545; __utmc=32156897; __utmz=32156897.1481897545.2.2.utmcsr=sz.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/wu/; nTalk_CACHE_DATA={uid:kf_10111_ISME9754_540746695}; NTKF_T2D_CLIENTID=guestC8C68A2C-2CDB-7A73-A6CC-07FA506D36B8'
}

# http://cn-proxy.com/
proxy_list = [
    'http://125.33.58.108:8888',
    'http://113.109.63.19:81',
    'http://120.199.224.78:80',
    'http://219.139.240.145:8090',
    'http://60.191.47.54:81'
    ]
proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}

client = pymongo.MongoClient('localhost',27017)
ganji_com = client['ganji_com']
goods_url  = ganji_com['goods_url']
goods_info = ganji_com['goods_info']

def get_one_links(fenlei_url,pages):
    #http://sz.ganji.com/jiaju/o2/
    list_view ='{}o{}/'.format(fenlei_url,str(pages))
    web_data = requests.get(list_view,headers=headers,proxies=proxies)
    soup = BeautifulSoup(web_data.text,'lxml')
    time.sleep(1)

    if soup.find('tr','zzinfo'):  #这个find用法下次查一下，不是很会用，和find_all的区别是什么
        links = soup.select('tr.zzinfo > td.t > a.t')
        for link in links:
            goods_link = link.get('href').split('?')[0]
            goods_url.insert_one({'url':goods_link})
            print(goods_link)
    elif soup.find('li','js-item'):
        links = soup.select('li.js-item > a')
        for link in links:
            goods_link = link.get('href').split('?')[0]
            goods_url.insert_one({'url': goods_link})
            print(goods_link)
    else:
        pass


# get_one_links('http://sz.ganji.com/jiaju/',3)








