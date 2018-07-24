import requests,lxml
from bs4 import BeautifulSoup
import xlrd
from xlutils.copy import copy
from qcc_company_list import get_all_page

def get_info(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Cookie':'zg_did=%7B%22did%22%3A%20%22163268abaacd2b-0a56a8f4f023b-3961430f-1fa400-163268abaad25%22%7D; _uab_collina=152536002242267742180513; PHPSESSID=2n5ml5la8cm3li0h40gabdt1i0; hasShow=1; acw_tc=AQAAAPIS/R5FugYAW0t7d2HOqRA711H/; _umdata=C234BF9D3AFA6FE779B1CD6846A3DA9DFFE2EB350A84557AC2C245EC0989FF42E08F1CD3634DB93FCD43AD3E795C914CF28EDC8C09D318898F43E52D4CA01A63; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201532354259628%2C%22updated%22%3A%201532355452950%2C%22info%22%3A%201532354259630%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%2224187846c82469625300ff462ad2ac0a%22%7D'
    }
    proxy = get_proxy()

    r = requests.get(url,headers=headers,proxies={'http:': 'http://{}'.format(proxy)})
    soup = BeautifulSoup(r.text,'lxml')

    company_name = soup.select('#company-top > div.row > div.content > div.row.title > h1')[0].text  # 公司名称

    '''基本信息'''
    #判断是否上市
    is_shangshi = soup.select('#company-top > div.row > div.content > div:nth-of-type(2) > span > span.cdes')[0].text    #判断基本信息里面是否有上市
    if '上市' in is_shangshi:
        print('已经上市')
        shangshi_code = soup.select('#company-top > div.row > div.content > div:nth-of-type(2) > span > span > a')[0].text.strip() #上市代码
        try:
            phone = soup.select('#company-top > div.row > div.content > div:nth-of-type(3) > span.fc > span > span')[0].text.strip()   #公司电话
        except:
            phone = soup.select('#company-top > div.row > div.content > div:nth-of-type(3) > span.fc > span')[1].text.strip()   #没有公司电话的情况下少一层span标签
        try:
            website = soup.select('#company-top > div.row > div.content > div:nth-of-type(3) > span > a')[0].text.strip()  #公司官网
        except:
            website = soup.select('#company-top > div.row > div.content > div:nth-of-type(3) > span')[1].text.strip()  # 公司官网不存在的时候少一层a标签
        try:
            email = soup.select('#company-top > div.row > div.content > div:nth-of-type(4) > span.fc > span > a')[0].text.strip()  #公司邮箱
        except:
            email = soup.select('#company-top > div.row > div.content > div:nth-of-type(4) > span.fc > span')[1].text.strip()  #没有公司邮箱的情况下少一层a标签
        address = soup.select('#company-top > div.row > div.content > div:nth-of-type(4) > span > a:nth-of-type(1)')[0].text.strip()  #公司地址
        try:
            about = ''.join([i.text.strip().replace('\n','').replace('\t','').replace(' ','') for i in soup.select('#jianjieModal > div > div > div.modal-body > div')]) #公司简介
        except:
            about = ''            #没有公司简介的直接记为空字符串
        base_info = [company_name,shangshi_code, phone, website, email, address, about]
        # print(base_info)
    else:
        print('未上市')
        shangshi_code = ''   #上市代码留空
        try:
            phone = soup.select('#company-top > div.row > div.content > div:nth-of-type(2) > span.fc > span > span')[0].text    #公司电话
        except:
            phone = soup.select('#company-top > div.row > div.content > div:nth-of-type(2) > span.fc > span')[1].text           #没有公司电话的情况下少一层span标签
        try:
            website = soup.select('#company-top > div.row > div.content > div:nth-of-type(2) > span > a')[0].text               #公司官网
        except:
            website = soup.select('#company-top > div.row > div.content > div:nth-of-type(2) > span')[1].text                   # 公司官网不存在的时候少一层a标签
        try:
            email = soup.select('#company-top > div.row > div.content > div:nth-of-type(3) > span.fc > span > a')[0].text       #公司邮箱
        except:
            email = soup.select('#company-top > div.row > div.content > div:nth-of-type(3) > span.fc > span')[1].text           #没有公司邮箱的情况下少一层a标签
        address = soup.select('#company-top > div.row > div.content > div:nth-of-type(3) > span > a')[0].text.strip()           #公司地址
        try:
            about = ''.join([i.text.strip().replace('\n','').replace('\t','').replace(' ','') for i in soup.select('#jianjieModal > div > div > div.modal-body > div')]) #公司简介
        except:
            about = ''               #没有公司简介的直接记为空字符串
        base_info = [company_name,shangshi_code,phone,website,email,address,about]
        # print(base_info)


    for i in base_info:                                                #基本信息写入表格
        write_excel(index,base_info.index(i),i)


    '''工商信息'''
    a = str(soup.find_all('table')[0])                                 #这个table是法定代表人信息，企业关联图，股权结构图等
    result = BeautifulSoup(a,'lxml')
    boss_name = result.find('a',{'class':'bname'}).text                #法定代表人信息

    b = str(soup.find_all('table')[1])                                 #这个table是详细的工商信息
    result1 = BeautifulSoup(b,'lxml').select('table > tr > td')        #提取工商信息，结果为列表
    result2 = [i.text.strip().replace('：','') for i in result1]                        #过滤结果，提取文字
    result3 = [result2[i:i+2] for i in range(0,len(result2),2)]        #将列表中的元素每两个放在一个小列表，两个元素刚好是工商信息的名称和实际值
    gs_info = dict(result3)                                            #将上一步的结构转化为字典，每个工商信息的key喝value对应
    gs_info['boss_name'] = boss_name                                   #将法人信息添加进字典
    # print(gs_info)


    #将工商信息写入excel表格
    write_excel(index,7,gs_info['boss_name'])
    write_excel(index, 8, gs_info['注册资本'])
    write_excel(index, 9, gs_info['实缴资本'])
    write_excel(index, 10, gs_info['经营状态'])
    write_excel(index, 11, gs_info['成立日期'])
    write_excel(index, 12, gs_info['统一社会信用代码'])
    write_excel(index, 13, gs_info['纳税人识别号'])
    write_excel(index, 14, gs_info['注册号'])
    write_excel(index, 15, gs_info['组织机构代码'])
    write_excel(index, 16, gs_info['公司类型'])
    write_excel(index, 17, gs_info['所属行业'])
    write_excel(index, 18, gs_info['核准日期'])
    write_excel(index, 19, gs_info['登记机关'])
    write_excel(index, 20, gs_info['所属地区'])
    write_excel(index, 21, gs_info['英文名'])
    write_excel(index, 22, gs_info['曾用名'])
    write_excel(index, 23, gs_info['参保人数'])
    write_excel(index, 24, gs_info['人员规模'])
    write_excel(index, 25, gs_info['营业期限'])
    # write_excel(index, 26, gs_info['企业地址'])
    write_excel(index, 27, gs_info['经营范围'])
    print('写入成功')



#     '''股东信息'''
#     #表头分别为序号、股东（发起人）、持股比例、认缴出资额(万元)、认缴出资日期
#     c = str(soup.find_all('table')[2])                                 #这个table是股东信息
#     result1 = BeautifulSoup(c,'lxml').select('table > tr > td')        #提取工商信息，结果为列表
#     result2 = [i.text.strip() for i in result1]                        #过滤结果，提取文字
#     result3 = [result2[i:i+5] for i in range(0,len(result2),5)]        #将列表中的元素每五个放在一个小列表，五个元素刚好是一组股东信息
#     for i in result3:
#         i[1] = i[1].split(' ',1)[0]                                    #将股东名后面的关联公司数去除
#         i[3] = i[3] + '万元'                                           #将任教出额度的数字加上万元单位
#
#
#
#     '''对外投资'''
#     #表头分别为被投资企业名称、被投资法定代表人、注册资本、出资比例、成立日期、状态
#     d = str(soup.find_all('table')[3])
#     result1 = BeautifulSoup(d,'lxml').select('table > tbody > tr > td')        #提取工商信息，结果为列表
#     result2 = [i.text.strip() for i in result1]                        #过滤结果，提取文字
#     result3 = [result2[i:i+6] for i in range(0,len(result2),6)]        #将列表中的元素每五个放在一个小列表，五个元素刚好是一组对外投资信息
#     for i in result3:
#         i[1] = i[1].split(' ',1)[0]                                    #将被投资法定代表人后面的关联公司数去除
#
#
#
#     '''主要人员'''
#     #表头分别为序号、姓名、职务
#     e = str(soup.find_all('table')[4])
#     result1 = BeautifulSoup(e,'lxml').select('table > tr > td')        #提取工商信息，结果为列表
#     result2 = [i.text.strip() for i in result1]                        #过滤结果，提取文字
#     result3 = [result2[i:i+3] for i in range(0,len(result2),3)]        #将列表中的元素每三个放在一个小列表，三个元素刚好是一组主要人员信息
#     for i in result3:
#         i[1] = i[1].split(' ',1)[0]                                    #将姓名后面的关联公司数去除
#
#
#
#     '''分支机构'''
#     f = str(soup.find_all('table')[5])
#     result1 = BeautifulSoup(f,'lxml').select('table > tr > td')        #提取工商信息，结果为列表
#     result2 = [i.text.strip() for i in result1]                        #过滤结果，提取文字
#     result3 = [result2[i:i+2] for i in range(0,len(result2),2)]        #将列表中的元素每两个放在一个小列表，两个元素刚好是一组分支机构信息


def write_excel(row,column,str):
    oldWb = xlrd.open_workbook('C:/Users/PEI/Desktop/企查查/qcc.xls', formatting_info=True)  # 打开需要写入的excel文件
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0)  # 获取excel文件的第一张表
    newWs.write(row, column, str)  # 第3行第3列写入内容
    newWb.save('C:/Users/PEI/Desktop/企查查/qcc.xls')  # 保存

def get_proxy():
    '''使用之前先开启proxy_pool项目'''
    return requests.get("http://127.0.0.1:5010/get/").content

if __name__ == '__main__':
    global company_urls,company_url,index
    company_urls = get_all_page()
    for company_url in company_urls:
        index = company_urls.index(company_url) + 1
        get_info(company_url)