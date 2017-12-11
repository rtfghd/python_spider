import requests
from bs4 import BeautifulSoup
import time
import urllib.request
import os

_auther = 'peili'
_date = '2017.01.19'

path = 'E:\\meizitu\\zipai\\'
urls = ['http://www.mzitu.com/zipai/comment-page-{}#comments'.format(str(i)) for i in range(1,300)]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Connection':'keep-alive'
}

# def get_zipai():
#     global picture_urls
#     picture_urls = []
#     for url in urls:
#         wb_data = requests.get(url,headers = headers)
#         soup = BeautifulSoup(wb_data.text,'lxml')
#         # is_exist = soup.title.text.split(' ')
#         is_exist = soup.select('div#comments > div > a')
#         if is_exist: #这个是页面下方翻页按钮的selector，没有这个结构的话证明是已经到了最后一页了，没有更多内容了
#             picture_links = soup.select('div#comments  div.comment-body > p > img')
#             for picture_link in picture_links:
#                 picture_link = picture_link.get('src')
#                 # print(picture_link)
#                 picture_urls.append(picture_link)
#                 f = open(r'E:/meizitu/links/zipai.txt', 'a')
#                 f.write(picture_link+'\n')
#                 f.close()
#         else:
#             # print('此版块已经到最后一页了')
#             break
#         j = urls.index(url)
#         print('第%d页自拍图片链接获取完毕'% (j+1))
#     print(len(picture_urls))
#     return picture_urls
#
#
# def download_picture():
#     get_zipai()
#     for picture_url in picture_urls:
#         i = picture_urls.index(picture_url)
#         download = urllib.request.urlretrieve(picture_url, path + '%d.jpg' %i)
#         print('download...%d' %(i+1),picture_url)
#     print('全部自拍下载完毕，总共'+str(len(picture_urls))+'张')


def download_picture():
    i = 1
    f = open('E:/meizitu/links/zipai.txt', 'r')
    lines = f.readlines()
    for line in lines:
        download = urllib.request.urlretrieve(line, path + '%d.jpg' % i)
        print('download...%d' % i, line)
        i += 1
    print('全部自拍下载完毕，总共' + len(lines) + '张')

download_picture()