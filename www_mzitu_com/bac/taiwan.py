import requests
from bs4 import BeautifulSoup
import time
import urllib.request
import os
from multiprocessing import Pool

_auther = 'peili'
_date = '2017.01.19'

path = 'E:/meizitu/taiwan/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Connection':'keep-alive'
}


'''
五个总分类的链接(性感妹子，日本妹子，台湾妹子，清纯妹子，妹子自拍),其中自拍板块结构不一样
这段函数其实只是为了拿到五个板块的主链接，浪费时间，还不如手动自己去网页上复制下来
'''
def get_zong_fenlei():
    url = 'http://www.mzitu.com/'
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title_ones = soup.select('div.header > div.mainnav > ul.menu > li > a')[1:-1]
    fenlei_ones = soup.select('div.header > div.mainnav > ul.menu > li > a')[1:-1]
    for title_one,fenlei_one in zip(title_ones,fenlei_ones):
        data = {
            'title':title_one.get_text(),
            'fenlei':fenlei_one.get('href')
        }
        print(data)

urls = ['http://www.mzitu.com/xinggan/page/',
        'http://www.mzitu.com/japan/page/',
        'http://www.mzitu.com/taiwan/page/',
        'http://www.mzitu.com/mm/page']

#获取台湾美女这个板块所有的套图链接
def get_taotu_links(taotu_url):
    global taotu_links
    taotu_links = []
    i = 1
    for q in range(1,100):
        wb_data = requests.get(taotu_url+str(q))
        soup = BeautifulSoup(wb_data.text,'lxml')
        is_exist = soup.title.text.split(' ')
        if '404' in is_exist:
            # print('此版块已经到最后一页了')
            break
        else:
            titles = soup.select('ul#pins > li > span > a')
            links = soup.select('ul#pins > li > a')
            print('正在爬取台湾美女板块套图链接，第%s页' % i, end='...')
            for title, link in zip(titles,links):
                data = {
                    'title':title.get_text(),
                    'link':link.get('href')
                }
                # print(data)
                taotu_links.append(data['link']) #dict['keys'],这个方法是从字典里面取出某个key的值
                f = open(r'E:/meizitu/links/taiwan_taotu.txt', 'a')
                f.write(data['link'] + '\n')
                f.close()
            print('完成')
            i += 1
    print('台湾美女板块共有'+str(len(taotu_links))+'套图','\n')
    return taotu_links


#获取套图中每一张图片的链接并下载
def get_pictures(taotu_link):
    global pictures_links
    pictures_links = []
    global j
    for j in range(1,100):
        picture_url = taotu_link+'/'+str(j)
        wb_data = requests.get(picture_url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        link = soup.select('div.main-image > p > a > img')[0].get('src')
        if len(pictures_links) == 0: #判断图片链接列表里是不是为空
            pictures_links.append(link)
            f = open(r'E:/meizitu/links/taiwan_single.txt','a')
            f.write(link+'\n')
            f.close()
        else:
            if link in pictures_links:
                print('第%d套图所有图片链接获取完毕' %k,'开始下载')
                break
            else:
                pictures_links.append(link)
                f = open(r'E:/meizitu/links/taiwan_single.txt','a')
                f.write(link+'\n')
                f.close()


#根据上一个函数获得的图片链接下载图片
def download_pictures(taotu_link):
    # global x
    get_pictures(taotu_link)
    x = 1
    # print(pictures_links)
    for pictures_link in pictures_links:
        download = urllib.request.urlretrieve(pictures_link,path + '%d_%d.jpg'%(k,x))
        print('download...%d_%d'%(k,x),pictures_link)
        x += 1
    print('第%d套图所有图片下载完毕' %k,'\n')


if __name__ == '__main__':
    taotu_url = 'http://www.mzitu.com/taiwan/page/'
    get_taotu_links(taotu_url)
    for taotu_link in taotu_links:
        global k
        k = (taotu_links.index(taotu_link)+1) # 通过index方法获取元素在列表中的位置
        print('正在爬取第%d套图' %k,end=' ')
        print(taotu_link)
        download_pictures(taotu_link)
    print('台湾美女板块所有图片下载完毕')



'''
taotu_url --> 这个模块的主链接
taotu_links --> 所有的套图链接
taotu_link --> 某一个套图链接
pictures_links --> 所有的图片链接
pictures_link --> 某一张图片链接
'''
