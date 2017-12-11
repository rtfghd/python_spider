#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import urllib.request
import re


path = 'E:/huabanwang/imgs/'

pin_ids = []
gaoqing_links = []#图片的详情页列表
picture_links = []#图片的下载链接列表
huaban_urls = ['https://huaban.com/favorite/beauty/']#每一大页的链接
'''
#获取每个图片详情页链接
def get_picture_info(huaban_url='https://huaban.com/favorite/beauty/'):
    wb_data = requests.get(huaban_url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #每张图片有对应的pin_id,从源码里看到这些图片并不是一种匹配就能全部包含，因此用两个正则来匹配，最后列表相加
    pin_id_one = re.findall('"extra":null}}, \{"pin_id":(.*?), "user_id":',soup.decode('utf-8'),re.S)
    pin_id_two = re.findall('\"pin_id\":\"(.*?)\"',soup.decode('utf-8'),re.S)
    pin_id = pin_id_one + pin_id_two
    # pin_id = list(set(pin_id)) #去掉重复的图片
    pin_ids.append(pin_id)
    for i in  pin_id:
        gaoqing_url = 'http://huaban.com/pins/{}/'.format(i) #图片详情链接
        global gaoqing_links
        gaoqing_links.append(gaoqing_url)
    gaoqing_links = list(set(gaoqing_links))
    print(gaoqing_links)
    return pin_ids
    return gaoqing_links

#从图片详情页中找到图片下载的链接
def get_picture_links():
    global i
    i += 1
    for gaoqing_link in gaoqing_links:
        wb_data = requests.get(gaoqing_link)
        soup = BeautifulSoup(wb_data.text,'lxml')
        picture_key = re.findall('"hbimg", "key":"(.*?)", "type"',soup.decode('utf-8'),re.S)[0]
        #高清大图下载链接
        picture_url = 'http://img.hb.aicdn.com/' + picture_key
        print(picture_url)
        picture_links.append(picture_url)
    print('第{}页链接完成'.format(i))
    return picture_links

#下载图片
def download_picture():
    x = 0
    for picture_link in  picture_links:
        xiazaitupian = urllib.request.urlretrieve(picture_link,path + '%s.jpg' % str(x))
        x += 1
        print('download {}'.format(x))



# #异步加载页面，获取更多页面
# def get_more_page_picture():
#     get_picture_info()
#     if True:
#         for a in pin_ids[0]:
#             print(a)
#             huaban_url = 'http://huaban.com/favorite/beauty/?ixkhwcmb&max={}&limit=20&wfl=1'.format(a)
#             get_picture_info(huaban_url)
#             get_picture_links()
#             download_picture()

if __name__ == '__main__':
    i = 0
    x = 0
    get_picture_info()
    get_picture_links()
    download_picture()
    # get_more_page_picture()
'''

#下面这种方法是selenium + phantomjs + beautifulsoup，速度可能较慢
def get_picture_info(huaban_url='https://huaban.com/favorite/beauty/'):
    driver = webdriver.PhantomJS()
    driver.get(huaban_url)
    wb_data = driver.page_source
    soup = BeautifulSoup(wb_data,'lxml')
    pictures = soup.select('#waterfall > div > a > img')
    pin_ids = soup.select('#waterfall > div > a')

    #解析网页，拿到图片url
    for picture in pictures:
        picture = 'http:' + picture.get('src')[:-6]
        picture_links.append(picture)
        f = open('E:/huabanwang/links/img_urls.txt','a')
        f.write(picture + '\n')
        f.close()
        print(picture)
    print('='*30,'第' + str(len(huaban_urls)) + '页加载完毕','='*30)

    #下一页url里的pin_id就是上一页最后一张图片的pin_id
    if len(huaban_urls) < a:
        last_pin_id = pin_ids[-1].get('href').split('/')[2]  # 每一页的最后一张图片的pin_id，刚好是下一页url里的
        huaban_url = 'https://huaban.com/favorite/beauty/?izhxd6qg&max=' + last_pin_id + '&limit=20&wfl=1'
        huaban_urls.append(huaban_url)
        f = open(r'E:/huabanwang/links/page_urls.txt','a')
        f.write(huaban_url + '\n')
        f.close()
        get_picture_info(huaban_url)
    else:
        print('%d页加载完成' % a,'准备开始下载，请稍后...')

def downlosd_picture():
    i = 1
    f = open('E:/huabanwang/links/img_urls.txt', 'r')
    lines = f.readlines()
    for line in lines:
        try:
            download = urllib.request.urlretrieve(line, path + '%d.jpg' % i)
            print('download...%d' % i)
            i += 1
        except:
            print('这个图片url有问题：',line)
    print('%d页全部下载完毕，总共'%a + str(len(lines)) + '张图片')


if __name__ == '__main__':
    print('由于使用的是selenium + phantomjs + beautifulsoup，脚本前期解析速度可能较慢')
    a = int(input('输入要下载的页数，按回车确定：'))
    get_picture_info()
    # downlosd_picture()
