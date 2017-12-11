from multiprocessing import Pool
from all_category import category_list
from page_parsing import get_links_from,urls_,get_item_info,get_zhuan_info,url_list,item_info
import threading



#获取1-100页的商品链接
def get_all_links_from(category):
    for num in range(1,101):
        get_links_from(category,num)



#使用哪段代码来爬去取商详页
def use_which_code():
    urls = urls_()
    for url in urls:
        is_zhuanzhuan = 'http://zhuanzhuan' in url.split('.')[0]
        is_oldxiangqingye = 'http://sz' in url.split('.')[0]
        if  is_zhuanzhuan:
            get_zhuan_info(url)
        elif is_oldxiangqingye:
            get_item_info(url)
        else:
            pass


#中断后继续爬取并防止重复
def urls_huifu():
    db_urls = [item['url'] for item in url_list.find()]
    index_urls = [item['url'] for item in item_info.find()]
    x = set(db_urls)
    y = set(index_urls)
    rest_of_urls = x-y

    for url in rest_of_urls:
        is_zhuanzhuan = 'http://zhuanzhuan' in url.split('.')[0]
        is_oldxiangqingye = 'http://sz' in url.split('.')[0]
        if is_zhuanzhuan:
            get_zhuan_info(url)
        elif is_oldxiangqingye:
            print(url)
            get_item_info(url)
        else:
            pass


# #爬取深圳二手所有商品链接
# if __name__ == '__main__':
#     pool = Pool()
#     pool.map(get_all_links_from,category_list.split())
#     pool.close()
#     pool.join()
# print('#' * 25 + '\n' + '爬取58同城所有商品链接完成' + '\n' + '#' * 25)


# 爬取深圳二手所有商品详情(单线程，以后做优化)
if __name__ == '__main__':
    urls_()
    use_which_code()
print('#' * 25 + '\n' + '爬取58同城所有商品详情完成' + '\n' + '#' * 25)


# #意外中断重新回复的时候运行这个
# if __name__ == '__main__':
#     urls_huifu()