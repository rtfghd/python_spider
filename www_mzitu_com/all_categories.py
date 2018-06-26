#coding=utf-8
import requests
from bs4 import BeautifulSoup

categories_list = []

def get_all_categories():
    global categories_list
    url = 'http://www.meizitu.com/'
    web_data = requests.get(url)
    web_data.encoding = 'gb2312'  #网页编码为gb2312，不设置此条中文乱码
    soup = BeautifulSoup(web_data.text,'lxml')
    categories = soup.select('div.tags > span > a')
    for category in categories:
        category_name = category.get_text()
        category_url = category.get('href')
        categories_list.append(category_name + category_url)


def get_all_categories222():
    global categories_list
    url = 'http://www.meizitu.com/a/yundong.html'
    web_data = requests.get(url)
    web_data.encoding = 'gb2312'  #网页编码为gb2312，不设置此条中文乱码
    soup = BeautifulSoup(web_data.text, 'lxml')
    categories = soup.select('div.tags > span > a')
    for category in categories:
        category_name = category.get_text()
        category_url = category.get('href')
        categories_list.append(category_name + category_url)
    categories_list = list(set(categories_list))


if __name__ == '__main__':
    get_all_categories()
    get_all_categories222()
    print(len(categories_list))
    print(categories_list)



categories_dict = {
    '清纯':'http://www.meizitu.com/a/qingchun.html',
    '福利':'http://www.meizitu.com/a/fuli.html',
    '运动':'girlhttp://www.meizitu.com/a/yundong.html',
    '成熟':'http://www.meizitu.com/tag/chengshu_487_1.html',
    '模特':'http://www.meizitu.com/tag/mote_6_1.html',
    '欧美美女':'http://www.meizitu.com/a/oumei.html',
    '足球宝贝':'http://www.meizitu.com/a/baobei.html',
    '颜值控':'http://www.meizitu.com/a/pure.html',
    '可爱':'http://www.meizitu.com/tag/keai_64_1.html',
    '长腿美臀':'http://www.meizitu.com/a/legs.html',
    '浴室':'http://www.meizitu.com/a/xinggan.html',
    '半裸':'http://www.meizitu.com/tag/banluo_5_1.html',
    '气质':'http://www.meizitu.com/tag/qizhi_53_1.html',
    '日系妹纸':'http://www.meizitu.com/a/rixi.html',
    '美臀':'http://www.meizitu.com/tag/meitun_42_1.html',
    '全裸':'http://www.meizitu.com/tag/quanluo_4_1.html',
    '性感1':'http://www.meizitu.com/a/sexy.html',
    '萌妹':'http://www.meizitu.com/a/cute.html',
    '性感2':'http://www.meizitu.com/a/xinggan.html',
    '女神':'http://www.meizitu.com/tag/nvshen_460_1.html',
}



