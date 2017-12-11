from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

#登陆账户
def login():
    '''selenium登陆支付宝'''
    global cookiestr,now_url,headers
    driver = webdriver.Chrome()
    print('\n' + '支付宝余额及最近消费记录查询' + '\n' + '-' * 30)
    print('进入支付宝登陆首页')
    driver.get('https://authet15.alipay.com/login/index.htm')
    # driver.maximize_window()
    driver.find_element_by_id('J-input-user').clear
    driver.find_element_by_id('J-input-user').send_keys('支付宝账户')
    driver.find_element_by_id('password_rsainput').clear
    driver.find_element_by_id('password_rsainput').send_keys('支付宝密码')
    driver.find_element_by_id('J-login-btn').click()
    print('正在登陆')
    web_title = driver.title #获取网页title
    if web_title == '我的支付宝 － 支付宝':
        print('登陆成功' + '\n' + '-' * 30)
        now_url = driver.current_url  # 返回当前页面的url
        # 返回登陆后的cookie
        cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
        cookiestr = ';'.join(item for item in cookie)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Cookie': cookiestr
        }
        driver.quit()
        return cookiestr, now_url, headers
    else:
        print('登陆失败，受到支付宝安全策略的限制，正在重新登陆...')
        driver.quit()
        login()


def zhanghu_info():
    '''账户信息'''
    wb_data = requests.get(now_url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    my_name = soup.select('div.i-banner > div.i-banner-content.fn-clear > div.i-banner-main > div.i-banner-main-hello.fn-clear > p > a')[0].text
    account_name = soup.select('#J-userInfo-account-userEmail')[0].text
    account_balance = soup.select('div > strong')[0].text
    yuebao = soup.select('p.i-assets-mFund-amount > strong')[0].text
    huabei_keyongedu = soup.select('div > div > div.i-assets-body > div > p:nth-of-type(1) > span > strong')[0].text
    huabei_zongedu = soup.select('div > div > div.i-assets-body > div > p:nth-of-type(2) > strong')[0].text
    print('账户信息 -->','\n')
    print('用户名称:' + my_name)
    print('账号:' + account_name)
    print('账户余额:' + account_balance)
    print('余额宝:' + yuebao)
    print('花呗可用额度:' + huabei_keyongedu)
    print('花呗总额度:' + huabei_zongedu)
    print('-'*100)


def trade_info():
    '''最近的交易记录'''
    wb_data = requests.get('https://consumeprod.alipay.com/record/standard.htm',headers = headers) #这个url是支付宝我的账单页面
    soup = BeautifulSoup(wb_data.text,'lxml')
    dates = soup.select(r'td.time > p')[::2] #[::2]指的从第一个元素开始，每隔一个取下一个元素
    names = soup.select('td.name > p.consume-title')
    amounts = soup.select('td.amount > span')
    statuses = soup.select('td.status > p[class="text-muted"]')[::2]

    print('最近20条消费记录 -->','\n')
    for date ,name , amount , status in zip(dates,names,amounts,statuses):
        data = {
            'date':date.text.strip(),
            'name':name.text.strip(),
            'amount':amount.text,
            'status':status.text
        }
        #字典格式化输出。中英文混排输出对齐现在有点问题
        a = r'%(date)-15s %(name)-30s %(amount)-30s %(status)-15s' % data
        print(a)
    print('-'*100)


if __name__ == '__main__':
    login()
    zhanghu_info()
    trade_info()
    a = input('按回车结束')
