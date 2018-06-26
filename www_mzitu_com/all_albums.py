import requests,os,time
from bs4 import BeautifulSoup

txt_path = r'D:\meizitu\文本地址\\'
pic_path = r'D:\meizitu\全站图片\\'
categories_dict = {
    '清纯':'http://www.meizitu.com/a/qingchun.html',
    '福利':'http://www.meizitu.com/a/fuli.html',
    '运动':'http://www.meizitu.com/a/yundong.html',
    '成熟':'http://www.meizitu.com/tag/chengshu_487_1.html',
    '模特':'http://www.meizitu.com/tag/mote_6_1.html',
    '欧美美女':'http://www.meizitu.com/a/oumei.html',
    '足球宝贝':'http://www.meizitu.com/a/baobei.html',
    '颜值控':'http://www.meizitu.com/a/pure.html',
    '可爱':'http://www.meizitu.com/tag/keai_64_1.html',
    '长腿美臀':'http://www.meizitu.com/a/legs.html',
    '浴室':'http://www.meizitu.com/a/xinggan.html',
    '半裸':'http://www.meizitu.com/tag/banluo_5_1.html',
    '气质':'http://www.meizitu.com/tag/qizhi_53_1.html',
    '日系妹纸':'http://www.meizitu.com/a/rixi.html',
    '美臀':'http://www.meizitu.com/tag/meitun_42_1.html',
    '全裸':'http://www.meizitu.com/tag/quanluo_4_1.html',
    '性感1':'http://www.meizitu.com/a/sexy.html',
    '萌妹':'http://www.meizitu.com/a/cute.html',
    '性感2':'http://www.meizitu.com/a/xinggan.html',
    '女神':'http://www.meizitu.com/tag/nvshen_460_1.html',
}


def get_albums(categorie_url):
    global categorie
    for i in range(1, 1000):
        url = categorie_url + '_%d.html' % i
        web_data = requests.get(url)
        if web_data.status_code != 404:
            print('正在下载该板块%d页' % i)
            web_data.encoding = 'gb2312'  #网页编码为gb2312，不设置此条中文乱码
            soup = BeautifulSoup(web_data.text,'lxml')
            albums = soup.select('ul > li > div > h3 > a')
            for album in albums:
                album_name = album.get_text()
                album_url = album.get('href')
                print(album_name,album_url)
                f = open(txt_path + categorie + '.txt','a+',encoding='utf-8')
                f.write(album_name + ' : ' + album_url + '\n')
                f.close()
        else:
            print('该板块下载完毕','\n','='*30,'\n')
            break


def get_all_albums():
    global categorie

    #任务开始前先删除目录下的所有的txt，防止写入的数据重复
    ls = os.listdir(txt_path)
    for i in ls:
        os.remove(txt_path + i)
    print('初始化完毕')

    for categorie in categories_dict:
        categorie_url = categories_dict[categorie]
        # print(categorie,categories_dict[categorie])
        if '_' in categorie_url:
            categorie_url = categorie_url[:-7]
            # print(categorie_url)
            print('【正在抓取%s板块的图片】' % categorie)
            get_albums(categorie_url)
        else:
            categorie_url = categorie_url[:-5]
            print('【正在抓取%s板块的图片】' % categorie)
            get_albums(categorie_url)



# get_albums()
# get_all_albums()
