'''
这个文件是用来计数显示给我看的
每5秒查看一次url_list表并显示一共有多少数据
url_list表存放的是商品链接
'''
import time
from get_all_url import goods_url

while True:
    print('已爬取【赶集网】商品链接',end=' ')
    print((goods_url.find()).count(),end=' ')
    print('条，' + '    #每5秒从DB读取一次')
    time.sleep(5)