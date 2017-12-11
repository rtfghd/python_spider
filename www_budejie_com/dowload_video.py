#coding=utf-8
import requests,re,urllib

url_name = [] #空列表，用来放视频名称和视频链接
path = 'H:/software_test/python/python_project/www_budejie_com/video'

#获取视频链接主程序
def get_video():
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    html = requests.get(url,headers = header).text
    # print(html)

    #获取最大盒子的内容
    url_content = re.compile(r'<div class="j-r-list-c">(.*?)</div>(.*?)</div>',re.S) #conpile提高效率
    url_contents = re.findall(url_content,html)
    # print(url_contents)

    for i in url_contents:
        url_reg = r'data-mp4="(.*?)"'
        url_itmes = re.findall(url_reg,str(i)) #匹配视频地址
        # print(url_itmes)
        if url_itmes: #如果视频存在
            name_reg = re.compile(r'  <a href="/detail-.{8}?.html">(.*?)</a>',re.S) #.{8}?代表的是匹配原来链接里的8个数字
            name_itmes = re.findall(name_reg,str(i)) #匹配视频的标题名字
            # print(name_itmes)

            #把视频和标题放在字典里，让他们一 一对应
            for i,k in zip(name_itmes,url_itmes):
                url_name.append([i,k])
                # print(i,k)


#获取视频板块所有视频的链接
def get_all_page():
    global url
    url_host = 'http://www.budejie.com/video/'
    for i in range(1,51):
        url = url_host + str(i)
        get_video()


#下载视频
def download():
    global j
    j = 1
    for i in url_name:
        try:
            urllib.request.urlretrieve(i[1],path+'/%s.mp4' % (i[0]))
            print('第%d个视频下载成功' % j)
            j += 1
        except:
            pass


if __name__ == "__main__":
    get_all_page()
    download()