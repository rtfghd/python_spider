#!/usr/bin/python
#coding=utf-8
_auther = 'peili'

from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random


client = pymongo.MongoClient('localhost',27017)
wu8_com = client['wu8_com']
url_list = wu8_com['url_list'] #这张表存储所有商品的链接
item_info = wu8_com['item_info'] #这张表存储商品的详细信息

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Connection':'keep-alive',
    'Cookie':'id58=Cra8GlhKdVvN68QDC/T6cQ==; mcity=sz; 58home=sz; ipcity=sz%7C%u6DF1%u5733%7C0; als=0; commonTopbar_myfeet_tooltip=end; myfeet_tooltip=end; bj58_new_session=1; bj58_init_refer="http://sz.58.com/sale.shtml?utm_source=market&spm=b-31580022738699-me-f-824.bdpz_biaoti"; bj58_new_uv=1; bj58_id58s="dnJHVlJ3dm89Mkx5NDI5NA=="; sessionid=d3cb238c-d09b-443b-92bf-2e37e2813688; 58cooper="userid=43395089459990&username=ncq3er&cooperkey=b0977b30030bb2e90272d2c301a36c83"; www58com="AutoLogin=true&UserID=43395089459990&UserName=ncq3er&CityID=0&Email=&AllMsgTotal=0&CommentReadTotal=0&CommentUnReadTotal=0&MsgReadTotal=0&MsgUnReadTotal=0&RequireFriendReadTotal=0&RequireFriendUnReadTotal=0&SystemReadTotal=0&SystemUnReadTotal=0&UserCredit=0&UserScore=0&PurviewID=&IsAgency=false&Agencys=null&SiteKey=2A31A22D9706340594BD65372F0241395129CD05CC06B4F5B&Phone=&WltUrl=&UserLoginVer=887EB60F8846773DBF927A4ED1B3481D1&LT=1481275340901"; city=sz; PPU="UID=43395089459990&PPK=db3d278d&PPT=3d5f9362&SK=4E2D7FDC8FC54575808AFF5F38597ED37D21E87AFC7D471B8&LT=1481275341413&UN=ncq3er&LV=e5d60885&PBODY=ieUhXn9kvsXLTUbepJvCKyHOjdJd4G9K5vf57tfbV5YKwEP0A7t7lwteHB_dcVo_q8u0n3saYeoYUQsSSBA3Sm4qYzicIbtLHecPsqJ91gaXNnj5dciKD6zMcRUwhYoP04Y2YEKllYlu8n7CGn66TgsgpEfJfR3K-uLIcRK_4TU&VER=1"; 58tj_uuid=7cd6d5dc-2e43-430a-afca-1e1be4573a18; new_session=0; new_uv=1; utm_source=market; spm=b-31580022738699-me-f-824.bdpz_biaoti; init_refer=; 43395089459990_opened_menu_id=-56-'
}


# # http://cn-proxy.com/
# proxy_list = [
#     'http://101.200.144.37:3128',
#     'http://222.186.161.215:3128',
#     'http://60.11.41.124:3128',
#     ]
# proxy_ip = random.choice(proxy_list)
# proxies = {'http':proxy_ip}


#爬取商品链接
def get_links_from(category,pages,who_shell=0):
    #http://sz.58.com/bangongshebei/0/pn2/
    list_view = '{}{}/pn{}/'.format(category,str(who_shell),str(pages))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        for link in soup.select('td.t > a.t'):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url':item_link})
            print(item_link)
    else:
        pass


#从DB里读取所爬取的商品链接
def urls_():
    urls = []
    for i in url_list.find():
        item = i['url']
        urls.append(item)
    return urls


#获取商祥页信息--原网页
def get_item_info(url):
    # urls = urls_()
    # for url in urls:

        wb_data = requests.get(url,headers=headers)
        soup = BeautifulSoup(wb_data.text,'lxml')
        no_longer_exit = '400' in soup.title.text.strip()
        lianjie_guoqi = '此信息已过期' in soup.find_all()
        if no_longer_exit:
            pass
        elif lianjie_guoqi:
            pass
        else:
            try:
                title = soup.title.text.strip()
                price = soup.select('span.price.c_f50')[0].text.strip() if soup.find('span','price') else None
                date  = soup.select('li.time')[0].text if soup.find('li','time') else None
                area = list(soup.select('div.su_con a')[0].stripped_strings) if soup.find('div','su_con') else None
                username = soup.select('ul.userinfo li > a.tx')[0].text if soup.find('ul','userinfo') else None
                item_info.insert_one({'title':title,'price':price,'date':date,'area':area,'username':username,'url':url})
                print({'title':title,'price':price,'date':date,'area':area,'username':username})
            except UnicodeEncodeError:
                pass


#获取商祥页信息--转转
def get_zhuan_info(url):
    # urls = urls_()
    # for url in urls:

        wb_data = requests.get(url,headers=headers)
        soup = BeautifulSoup(wb_data.text,'lxml')
        no_longer_exit = '400' in soup.title.text.strip()
        url_guoqi = '商品已下架' in soup.find_all()
        if no_longer_exit:
            pass
        elif url_guoqi:
            pass
        else:
            try:
                title = soup.title.text.strip()
                price = soup.select('span.price_now > i')[0].text
                date  = soup.select('li.time')[0].text if soup.find('li','time') else None
                area = soup.select('div.palce_li i')[0].text if soup.find('div','palce_li') else None
                username = str(soup.select('p.personal_name')[0].get_text())
                item_info.insert_one({'title': title, 'price': price, 'date': date, 'area': area, 'username': username,'url':url})
                print({'title': title, 'price': price, 'date': date, 'area': area, 'username': username})
            except UnicodeEncodeError:
                pass

