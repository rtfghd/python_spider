#!/usr/bin/env python
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

'''
微博被莫名奇妙关注一些广告营销号
写这个操作浏览器自动取消关注，速度教慢，仅仅练手用
'''

print('打开微博主页')
driver = webdriver.Chrome()
driver.get('http://weibo.com/')
time.sleep(5)

#登陆账号
driver.find_element_by_id('loginname').clear()
driver.find_element_by_id('loginname').send_keys('******@qq.com')
driver.find_element_by_css_selector('#pl_login_form > div > div:nth-child(3) > div.info_list.password > div > input').clear()
driver.find_element_by_css_selector('#pl_login_form > div > div:nth-child(3) > div.info_list.password > div > input').send_keys('******')
driver.find_element_by_css_selector('a[tabindex="6"]').click()
print('登陆账号成功')
time.sleep(1)

#打开关注页面
driver.find_element_by_css_selector('li> a > strong[node-type="follow"]').click()
time.sleep(1)
print('打开关注页面成功')



def quxiao_guanzhu():
    quxiao_guanzhu = driver.find_element_by_css_selector(
        '#Pl_Official_RelationMyfollow__93 > div > div > div > div.member_box > ul > li:nth-child(1) > div.member_wrap.clearfix > div.mod_info > div.opt > p > a.W_btn_b.btn_set > em')
    ActionChains(driver).move_to_element(quxiao_guanzhu).perform()
    time.sleep(0.5)
    driver.find_element_by_css_selector(
        '#Pl_Official_RelationMyfollow__93 > div > div > div > div.member_box > ul > li:nth-child(1) > div.member_wrap.clearfix > div.mod_info > div.opt > div > ul > li:nth-child(3) > a').click()
    time.sleep(0.5)
    driver.find_element_by_css_selector('a[node-type="ok"]').click()
    time.sleep(0.5)

    if i/28 in (1,2,3,4,5,6,7,8,9,10):
        print('本页即将取消关注完毕，自动刷新')
        driver.refresh()
        time.sleep(3)
    else:
        pass

#开始取消关注
if __name__ == "__main__":
    global i
    for i in range(110):
        try:
            quxiao_guanzhu()
            print('取消关注第%d个广告狗' % (i+1))
        except:
            print('操作太快,请稍等一下')
            time.sleep(10)
    print('取消关注完毕')

