import requests,os,random,socket,time
import urllib.request
from bs4 import BeautifulSoup
from all_albums import categories_dict

User_Agent = [
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "MQQBrowser/25 (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; OMNIA7)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; XBLWP7; ZuneWP7)",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 60; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; TheWorld)"
]


txt_path = 'D:/meizitu/文本地址/'
pic_path = 'D:/meizitu/全站图片/'
error_path = 'D:/meizitu/error.txt'

def mkdir():
    for categorie in categories_dict:
        if not os.path.exists(pic_path + categorie):
            os.mkdir(pic_path + categorie)                            #每个板块单独一个目录，板块路径 = 基础地址+板块名
        else:
            pass
    print('所有板块目录创建成功')


def download_pic():
    proxy = get_proxy()

    for categorie in categories_dict:
        if not os.path.exists(txt_path + categorie + '.txt'):         #若板块不存在，则跳过，因为有些板块有虽然网站有分类，但是没有内容所以爬取的时候也就没有该板块
            print(txt_path + categorie + '.txt')
            continue
        else:
            print('正在下载%s板块的图片' % categorie)
            f = open(txt_path + categorie + '.txt','r',encoding='utf-8')
            for line in f.readlines():
                album_name = line.split(' : ')[0]                              #从已经抓取好的专辑文本里获取专辑名称
                album_name = album_name.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','') #windows目录名中不支持这九个字符，如果遇到直接剔除
                album_url = line.split(' : ')[1][:-1]                          #从已经抓取好的专辑文本里获取专辑地址,注意最后的换行符'\n'通过切片去掉
                album_path = pic_path + categorie + '/' + album_name           #每个专辑单独一个目录，专辑目录 = 基础地址+板块名称+专辑名称
                if not os.path.exists(album_path):
                    os.mkdir(album_path)
                else:
                    pass
                web_data = requests.get(album_url)
                web_data.encoding = 'gb2312'
                soup = BeautifulSoup(web_data.text,'lxml')

                #测试时发现不同的专辑页面html结构不一样
                if len(soup.select('#picture > p > img')) != 0:
                    pics = soup.select('#picture > p > img')
                else:
                    pics = soup.select('div.postContent > p > img')

                print('【%s】正在下载专辑：%s' % (categorie,album_name))
                for pic in pics:
                    pic_url = pic.get('src')

                    #以下几行代码是方式使用urllib.request.urlretrieve方法下载图片时被网站403禁止
                    proxy_support = urllib.request.ProxyHandler({'http:': 'http://{}'.format(proxy)})  #将随机获取的IP填入代理
                    opener = urllib.request.build_opener(proxy_support)
                    opener.addheaders = [('User-Agent',random.choice(User_Agent))]   # 添加header
                    urllib.request.install_opener(opener)

                    try:
                        socket.setdefaulttimeout(20) #设置默认超时时间20秒
                        urllib.request.urlretrieve(pic_url,album_path + '/' + str(pics.index(pic)+1) + '.jpg')
                        print('[ %d / %d ]' %(pics.index(pic)+1,len(pics)))
                    except Exception as e:
                        f = open(error_path, 'a+', encoding='utf-8')
                        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
                        f.write(album_name + '\n')
                        f.write(pic_url + '\n')
                        f.write(str(e) + '\n')
                        f.write('='*30 + '\n'*2)
                        f.close()
                        continue


def get_proxy():
    '''
    使用之前先开启proxy_pool项目
    '''
    return requests.get("http://127.0.0.1:5010/get/").content




def all_num():
    '''统计一共专辑总数和图片总数'''
    album_num = 0
    pic_num = 0
    a = os.listdir(pic_path)
    for i in a:
        b = os.listdir(pic_path + i)
        album_num += len(b)
        # print(len(b)) #每个板块多少专辑
        for j in b:
            c = os.listdir(pic_path + i + '/' + j)
            # print(len(c))  #每个专辑几张图片
            pic_num += len(c)
    print(album_num)
    print(pic_num)

# mkdir()
# download_pic()