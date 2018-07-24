import requests,lxml
from bs4 import BeautifulSoup

company_list = []

def get_company_list(search_name,i):
    url = 'https://www.qichacha.com/search_index?key=%s&ajaxflag=2&p=%d&' %(search_name,i)
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Cookie': 'zg_did=%7B%22did%22%3A%20%22163268abaacd2b-0a56a8f4f023b-3961430f-1fa400-163268abaad25%22%7D; _uab_collina=152536002242267742180513; PHPSESSID=2n5ml5la8cm3li0h40gabdt1i0; hasShow=1; acw_tc=AQAAAPIS/R5FugYAW0t7d2HOqRA711H/; _umdata=C234BF9D3AFA6FE779B1CD6846A3DA9DFFE2EB350A84557AC2C245EC0989FF42E08F1CD3634DB93FCD43AD3E795C914CF28EDC8C09D318898F43E52D4CA01A63; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201532354259628%2C%22updated%22%3A%201532355452950%2C%22info%22%3A%201532354259630%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%2224187846c82469625300ff462ad2ac0a%22%7D'
    }

    requests.packages.urllib3.disable_warnings()
    r = requests.get(url,headers=headers,verify=False)
    soup = BeautifulSoup(r.text,'lxml')


    a = str(soup.find_all('table')[0])                                 #这个table是查询出来的公司列表
    result = BeautifulSoup(a,'lxml').select('table > tbody > tr > td > a')        #提取工商信息，结果为列表
    for company in result:
        company_url = 'https://www.qichacha.com' + company.get('href')
        company_name = company.text
        print(company_url,company_name)
        company_list.append(company_url)


def get_all_page():
    search_name = str(input('请输入查询关键字：'))
    for i in range(1,11):
        get_company_list(search_name,i)
    return company_list


if __name__ == '__main__':
    get_all_page()