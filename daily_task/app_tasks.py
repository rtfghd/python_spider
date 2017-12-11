#coding=utf-8
from appium import webdriver
import time,random
from appium.webdriver.common.touch_action import TouchAction


screenshot_path = 'H:/software_test/python/python_project/python_project/daily_task/screenshot/'


def basic(package_name, activity_name):
    '''启动应用'''
    global driver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['appPackage'] = package_name
    desired_caps['appActivity'] = activity_name
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(15)

def jd_finance():
    '''京东金融签到/领取提额包'''
    #----------启动应用----------
    print('[正在进行京东金融任务]')
    basic('com.jd.jrapp','.WelcomeActivity')

    #----------九宫格滑动解锁----------
    TouchAction(driver).press(x=180, y=598).move_to(x=0, y=0).wait(100).move_to(x=0, y=181).wait(100).move_to(x=0, y=181).wait(100).move_to(x=181, y=0).wait(100).move_to(x=181,y=0).release().perform()
    time.sleep(2)
    #这里重点注意，x,y的值是偏移量，不是坐标，参考https://testerhome.com/topics/9698

    #----------领取白条提额包----------
    cancel1 = driver.page_source.find('com.jd.jrapp:id/ibtn_zc_product_notice_board_close') #判断进入首页时是否有消息弹窗
    if cancel1 != -1:
        driver.find_element_by_id('com.jd.jrapp:id/ibtn_zc_product_notice_board_close').click()  # 点击关闭弹窗
        print('进入首页时的弹窗已关闭')
        driver.find_elements_by_id('com.jd.jrapp:id/tv_tab_strip')[1].click() #点击顶部白条按钮
        time.sleep(1)
        '''这里在做一次弹窗的判断，因为弹窗不一定只出现在主页'''
        cancel1 = driver.page_source.find('com.jd.jrapp:id/ibtn_zc_product_notice_board_close')
        if cancel1 == -1:
            driver.find_element_by_id('com.jd.jrapp:id/tv_mid_text').click() #点击白条资产卡片
            time.sleep(1)
        else:
            driver.find_element_by_id('com.jd.jrapp:id/ibtn_zc_product_notice_board_close').click()  # 点击关闭弹窗
            driver.find_element_by_id('com.jd.jrapp:id/tv_mid_text').click()  # 点击白条资产卡片
            time.sleep(1)
    else:
        driver.find_elements_by_id('com.jd.jrapp:id/tv_tab_strip')[1].click()  # 点击顶部白条按钮
        time.sleep(1)
        cancel1 = driver.page_source.find('com.jd.jrapp:id/ibtn_zc_product_notice_board_close')
        if cancel1 == -1:
            driver.find_element_by_id('com.jd.jrapp:id/tv_mid_text').click() #点击白条资产卡片
            time.sleep(3)
        else:
            driver.find_element_by_id('com.jd.jrapp:id/ibtn_zc_product_notice_board_close').click()  # 点击关闭弹窗
            driver.find_element_by_id('com.jd.jrapp:id/tv_mid_text').click()  # 点击白条资产卡片
            time.sleep(3)

    ti_button = driver.page_source.find('1个提额包') #判断是否有"1个提额包"的按钮
    if ti_button != -1: #如果不等于-1则证明提额的按钮存在，否则这里是"额度管理的按钮"
        time.sleep(1)
        driver.find_element_by_id('com.jd.jrapp:id/tv_right_oval_tips').click() #点击"1个提额包"按钮
        time.sleep(10)
        driver.swipe(640,430,640,430,10) #点击"提额"按钮
        time.sleep(1)
        driver.get_screenshot_as_file(screenshot_path + 'jd_ti_money.png') #提额完成后截图保存
        print('提额完成')
        driver.find_element_by_id('com.jd.jrapp:id/btn_left').click() #点击左上角的"X"返回上一步
        driver.keyevent(4)  # appium模拟手机按钮的方法，这里是模拟返回键继续返回上一步，详见:http://www.cnblogs.com/jiuyigirl/p/7126753.html
    else:
        time.sleep(3)
        driver.get_screenshot_as_file(screenshot_path + 'jd_ti_money.png')  # 提额完成后截图保存
        print('本周已经领取过提额包，下周再来')
        pass
        driver.keyevent(4)
    time.sleep(1)

    #----------个人中心签到----------
    driver.find_element_by_id('com.jd.jrapp:id/fourthLayout').click() #点击个人中心
    time.sleep(1)
    driver.find_elements_by_id('com.jd.jrapp:id/tv_item_label')[0].click() #获取这一类标签，签到是第一个,并点击签到
    time.sleep(20)
    '''如果直接点击签到失败的话，可能是有弹窗，先点击弹窗再点击签到'''
    try:
        driver.swipe(600, 410, 600, 410, 10)  # 点击"签到领钢镚"按钮
        time.sleep(1)
        driver.get_screenshot_as_file(screenshot_path + 'jd_check_in.png')  # 签到完成后截图保存
        print('今日签到完成')
    except:
        driver.swipe(360,1168,360,1160,10) #点击关闭弹窗
        driver.swipe(600, 410, 600, 410, 10)  # 点击"签到领钢镚"按钮
        time.sleep(1)
        driver.get_screenshot_as_file(screenshot_path + 'jd_check_in.png')  # 签到完成后截图保存
        print('今天已经签到过')

    #----------退出应用----------
    driver.quit()
    print('\n')

def jd_app():
    '''京东APP签到领京豆'''
    # ----------启动应用----------
    print('[正在进行京东APP任务]')
    basic('com.jingdong.app.mall', '.main.MainActivity')

    # ----------点击主页"领京豆"----------
    driver.find_element_by_xpath('//android.widget.RelativeLayout[contains(@index,6)]').click() #点击主页"领京豆"按钮
    time.sleep(15)
    ad_window = driver.page_source.find('1. 10月31日-11月11日，淘气的豆豆会在领京豆频道出没，找到它就能获得京豆或优惠券奖励！')
    if ad_window != -1: #判断签到页面是否有活动弹窗
        # driver.find_element_by_xpath('//android.view.View[contains(@index,0)]').click()
        driver.swipe(615,310,615,310) #关闭弹窗
        time.sleep(1)
        check_in = driver.page_source.find('签到领京豆')#判断是否已经领取过
        if check_in != -1:
            driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"签到领京豆")]').click() #点击签到
            time.sleep(2)
            driver.swipe(360, 600, 360, 600, 10)  # 点击翻牌
            time.sleep(2)
            print('今日签到领取京豆完成')
            driver.get_screenshot_as_file(screenshot_path + 'jd_dou.png')
        else:
            print('今天已经领取过京豆，明天再来')
            time.sleep(2)
            driver.get_screenshot_as_file(screenshot_path + 'jd_dou.png')
    else:
        check_in = driver.page_source.find('签到领京豆')  # 判断是否已经领取过
        if check_in != -1:
            driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"签到领京豆")]').click()  # 点击签到
            time.sleep(2)
            driver.swipe(360, 600, 360, 600, 10)  # 点击翻牌
            time.sleep(2)
            print('今日签到领取京豆完成')
            driver.get_screenshot_as_file(screenshot_path + 'jd_dou.png')
        else:
            print('今天已经领取过京豆，明天再来')
            time.sleep(2)
            driver.get_screenshot_as_file(screenshot_path + 'jd_dou.png')

    # ----------退出应用----------
    driver.quit()
    print('\n')

def wyy_music():
        '''网易云音乐每日签到'''
        # ----------启动应用----------
        print('[正在进行网易云任务]')
        basic('com.netease.cloudmusic', '.activity.MainActivity')

        # ----------左侧签到----------
        driver.find_element_by_id('com.netease.cloudmusic:id/l0').click() #点击主页左上角的汉堡菜单
        check_in = driver.page_source.find('已签到')
        if check_in == -1:
            driver.find_element_by_id('com.netease.cloudmusic:id/a29').click() # 点击个人中心的"签到"按钮
            time.sleep(5)
            driver.get_screenshot_as_file(screenshot_path + 'wyymusic_checkin.png')
        else:
            print('今日已经签到，明天再来')
            driver.get_screenshot_as_file(screenshot_path + 'wyymusic_checkin.png')

        # ----------退出应用----------
        driver.quit()
        print('\n')

def lt_yingyeting():
    '''联通手机营业厅每日签到'''
    # ----------启动应用----------
    print('[正在进行联通手机营业厅任务]')
    basic('com.sinovatech.unicom.ui', 'com.sinovatech.unicom.basic.ui.MainActivity')

    # ----------点击签到---------
    driver.find_element_by_id('com.sinovatech.unicom.ui:id/home_header_long_qiandao_image').click() #左上角签到LOGO
    time.sleep(8)

    check_in = driver.page_source.find('已签到')
    if check_in == -1:
        driver.swipe(600,260,600,260,10) #点击“签到”
        time.sleep(1)
        driver.get_screenshot_as_file(screenshot_path + 'lt_yingyeting.png')  # 签到完成后截图保存
        print('签到完成')
    else:
        driver.get_screenshot_as_file(screenshot_path + 'lt_yingyeting.png')
        print('签到完成')

    # ----------退出应用---------
    driver.quit()
    print('\n')

def zssh():
    '''掌上生活每日签到'''
    # ----------启动应用----------
    print('[正在进行掌上生活任务]')
    basic('com.cmbchina.ccd.pluto.cmbActivity', '.SplashActivity')

    # ----------执行签到----------
    driver.find_element_by_id('com.cmbchina.ccd.pluto.cmbActivity:id/btn_fourth_menu').click() #点击个人中心
    time.sleep(1)
    driver.find_element_by_xpath('//android.widget.TextView[contains(@index,0)]').click() #点击顶部登陆按钮
    time.sleep(3)

    #----------九宫格滑动解锁----------
    TouchAction(driver).press(x=140, y=586).move_to(x=0, y=0).wait(100).move_to(x=0, y=222).wait(100).move_to(x=0, y=222).wait(100).move_to(x=222, y=0).wait(100).move_to(x=222,y=0).release().perform()
    time.sleep(3)

    driver.find_element_by_xpath('//android.widget.ImageView[contains(@index,2)]').click() #点击"签到有礼"logo
    time.sleep(5)
    driver.swipe(355,490,355,490,10) #点击签到卡片页
    time.sleep(2)
    driver.find_element_by_id('com.cmbchina.ccd.pluto.cmbActivity:id/btn_get').click() #点击"签到领取1积分"
    time.sleep(3)

    check_in = driver.page_source.find('立即领取')
    if check_in != -1:
        driver.find_element_by_id('com.cmbchina.ccd.pluto.cmbActivity:id/btn_winner_unentity_order_pay').click() #点击"立即领取"按钮
        time.sleep(5)
        driver.get_screenshot_as_file(screenshot_path + 'zssh.png')  # 签到完成后截图保存
        print('签到完成')
    else:
        time.sleep(1)
        driver.get_screenshot_as_file(screenshot_path + 'zssh.png')  # 签到完成后截图保存
        print('签到完成')

    # ----------退出应用----------
    driver.quit()
    print('\n')

def taobao():
    '''淘宝每日淘金币'''
    # ----------启动应用----------
    print('[正在进行淘宝任务]')
    basic('com.taobao.taobao', 'com.taobao.tao.welcome.Welcome')

    # ----------领淘金币----------
    driver.find_element_by_name(u'领金币').click() #点击主页中间的领金币
    time.sleep(15)

    driver.swipe(354,321,354,321,10) #点击中间的金币箱图片
    time.sleep(3)
    driver.get_screenshot_as_file(screenshot_path + 'taobao_taojinbi.png')  # 签到完成后截图保存
    print('签到完成')

    # ----------领淘金币----------
    driver.quit()

def youguo():
    '''尤果圈每日任务'''
    # ----------启动应用----------
    print('[正在进行尤果圈任务]')
    basic('com.ugirls.app02', '.module.splash.SplashActivity')

    # ----------每日签到----------
    driver.find_element_by_id('com.ugirls.app02:id/spread_layout').click() #点击主页"签到"按钮
    time.sleep(2)
    driver.find_element_by_id('com.ugirls.app02:id/signin_bt').click() #点击"今日签到"按钮
    time.sleep(2)
    driver.keyevent(4) #返回上一页

    # ----------图片模块----------
    driver.find_element_by_id('com.ugirls.app02:id/ibt_photo').click()  # 点击下方图片模块
    time.sleep(3)
    driver.swipe(180,460,180,460,10) #点击第一张图片
    time.sleep(2)
    driver.swipe(350, 570, 350, 570, 10)  # 点击一下图片
    time.sleep(1)

    # ----------发表评论----------
    for i in range(7):
        comment_button = driver.page_source.find('评论吧') #判断页面是否有评论点赞等元素
        if comment_button != -1:
            driver.find_element_by_id('com.ugirls.app02:id/comment').click()  #点击评论框
            time.sleep(1)
            driver.find_element_by_id('com.ugirls.app02:id/edit_chat').send_keys('可以可以可以')  # 输入评论内容
            driver.find_element_by_id('com.ugirls.app02:id/btn_send').click()  # 点击"发送评论按钮"
            time.sleep(8)
        else:
            driver.swipe(350, 570, 350, 570, 10)  # 点击一下图片
            time.sleep(1)
            driver.find_element_by_id('com.ugirls.app02:id/comment').click()  # 点击评论框
            time.sleep(1)
            driver.find_element_by_id('com.ugirls.app02:id/edit_chat').send_keys('可以可以可以')  # 输入评论内容
            driver.find_element_by_id('com.ugirls.app02:id/btn_send').click()  # 点击"发送评论按钮"
            time.sleep(8)

    # ----------分享链接----------


    # ----------图片点赞----------


    # ----------个人中心----------
    # driver.find_element_by_id('com.ugirls.app02:id/ibt_mine').click()  # 点击个人中心
    # time.sleep(1)
    # driver.find_element_by_xpath('//android.widget.LinearLayout[contains(@index,5)]').click()#点击每日任务
    # time.sleep(1)
    # driver.get_screenshot_as_file(screenshot_path + 'youguoquan.png')  # 每日任务完成情况截图


