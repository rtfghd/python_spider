#!/usr/bin/env python
#coding=utf-8

'''
煎蛋网妹子图板块的图片
'''

from bs4 import BeautifulSoup
import time
import requests
import urllib.request
import os


imgs = []
path = './images/'

def path_is_exists():
    if os.path.exists(path):
        print('图片文件夹已经存在')
    else:
        os.mkdir(path)
        print('图片文件夹不存在，现在已经自动创建好')
    return path

def get_image_url():
    #首先查看煎蛋网妹子图板块一共有多少页内容
    start_url = 'http://jandan.net/ooxx'
    totle_images_page = BeautifulSoup(requests.get(start_url).text,'lxml').select('span.current-comment-page')[0].text[1:-1]
    print('煎蛋网妹子图板块一共%s页' %totle_images_page)
    for k in range(int(totle_images_page)):
        base_url = 'http://jandan.net/ooxx/page-%s#comments' %k
        print('正在解析第%s页' %k)
        try:
            wb_data = requests.get(base_url)
            soup = BeautifulSoup(wb_data.text,'lxml')
            images = soup.select('p > img')

            for image in images:
                image = image.get('src').replace('//','http://') #完整的图片链接前面要加上http:
                if 'mw600' in image:
                    image = image.replace('mw600','large')
                    imgs.append(image)
                else:
                    image = image.replace('mw600', 'large')
                    imgs.append(image)
            # print(imgs)
        except:
            pass
    return imgs

def download_image():
    i = 1
    for img in imgs:
        try:
            urllib.request.urlretrieve(img, path+'%s' %(img[-12:]))
            print('已经下载%s张' %i)
            i += 1
        except:
            print(img)
            pass
            # time.sleep(1)
            # urllib.request.urlretrieve(img, path + '%s' % (img[-12:]))
            # print('已经下载%s张' % i)
            # i += 1



if __name__ == '__main__':
    path_is_exists()
    get_image_url()
    download_image()