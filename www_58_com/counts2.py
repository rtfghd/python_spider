'''
这个文件是用来计数显示给我看的
每5秒查看一次item_info表并显示一共有多少数据
item_info表存放的是商品链接
'''

import time
from page_parsing import item_info

while True:
    print('已爬取【58同城】商品详情', end=' ')
    print((item_info.find()).count(), end=' ')
    print('条，' + '#每5秒从DB读取一次')
    time.sleep(5)