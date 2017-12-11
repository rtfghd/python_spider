#/usr/bin/python
#coding=utf-8
_auther = 'peili'

from bs4 import BeautifulSoup
import requests
import time

miui_article = [] #关于nexus的miui版本的帖子存放在这个列表
path = 'H:/linshi/' #将最后的结果存放在此目录

def get_article(num):
    '''爬取一个页面上的文章标题及url'''
    wbdata = requests.get('http://bbs.gfan.com/forum-1566-{}.html'.format(str(num))) #页码参数化
    soup = BeautifulSoup(wbdata.text,'lxml')
    articles = soup.select('table > tbody > tr > th > a')

    for article in articles:
        article_title = article.get_text()
        article_url = article.get('href')

        #判断帖子标题有没有包含‘miui’或者‘MIUI’
        if 'miui' in article_title or 'MIUI' in article_title:
            miui_article.append(article_url)
            f = open(path+'article.txt','a+')
            f.write(article_title + '： ' + article_url + '\n')
            f.close()
            # print(article_title)
        else:
            pass

def get_all_article():
    '''爬取相应版块所有页面的文章'''
    for num in range(1,164):
        get_article(num)
        print('第%d页加载完毕' %num)

if __name__ == '__main__':
    get_all_article()
    print(miui_article)