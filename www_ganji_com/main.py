#!/usr/bin/python
#coding=utf-8

_auther = 'peili'

from get_mulu_url import fenlei_url
from get_all_url import get_one_links
from multiprocessing import Pool

def get_all_links(fenlei_url):
    for i in range(1,101):
        get_one_links(fenlei_url,i)

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links,fenlei_url.split())
    pool.close()
    pool.join()
    print('#'*25 + '\n' + '爬取赶集网所有商品链接-结束' + '\n' + '#'*25)