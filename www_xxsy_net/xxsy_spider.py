#coding=utf-8

'''
作者：peili
微信：yewuhaolp
时间：2018.04.23
版本：1.0
'''

import requests,time,os
from bs4 import BeautifulSoup

path = r'D:\小说下载\\'

def get_books(url):
    while True:
        try:
            webdata = requests.get(url,timeout=60)
            break
        except:
            time.sleep(3)
    soup = BeautifulSoup(webdata.text,'lxml')
    books = soup.select('div.result-list > ul > li > div > h4 > a') 
    for book in books:
        bookid = book.get('href').split('/')[-1].split('.')[0]
        bookname = book.text
        bookurl = 'http://www.xxsy.net' + book.get('href')

        if bookname+'.txt' in oldlists:
            continue
        else:
            pass

        print('=====================正在下载【' + bookname + '】=====================')
        while True:
            try:
                url = 'http://www.xxsy.net/partview/GetChapterListNoSub?bookid=%s&isvip=0' % bookid
                titles = BeautifulSoup(requests.get(url,timeout=60).text,'lxml').select('ul > li > a') 
                break
            except:
                time.sleep(3)
        for title in titles: 
            titleurl = 'http://www.xxsy.net' + title.get('href') 
            titlename = title.text
            # print(titlename,titleurl)
            try:
                f = open(path + '%s.txt' % bookname, 'a+')
                f.write('\n'*2 + titlename + '\n')
                f.close()
            except:
                pass

            while True:
                try:
                    contents = BeautifulSoup(requests.get(titleurl,timeout=60).text, 'lxml').select('div#auto-chapter > p')
                    break
                except:
                    time.sleep(3)
            for content in contents:
                content = str(content).replace('<p>', '\n').replace('</p>', '')
                try:
                    f = open(path + '%s.txt' % bookname, 'a+')
                    f.write(content)
                    f.close()
                except:
                    pass
            print(titlename + '[已下载]')


if __name__ == "__main__":
    urls = ['http://www.xxsy.net/search?vip=0&sort=2&pn={}'.format(i) for i in range(100)]
    global oldlists
    oldlists = os.listdir(path)
    for url in urls: 
        get_books(url)

        newlists = os.listdir(path)
        num = len(newlists) - len(oldlists)
        if num >= 20:
            print('今日任务下载完毕，今日下载小说%d本' % num)
            break
        else:
            pass
