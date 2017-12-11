#coding=utf-8
from app_tasks import *
from public.get_device import *
from public.schedule import *
from appium_server import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

report_path = 'H:/software_test/python/python_project/python_project/daily_task/report'

def write_report():
    '''任务执行结果写入文本'''
    all_time = ((end-start)/60) #计算任务总用时
    result = '今日手机任务已经完成，总共用时%.0f分钟'%all_time
    f = open(report_path + 'report.txt', 'w+')
    f.write(result + '\n'*2)
    f.write('[运行的任务如下]' + '\n')
    for i in done: #这里的done是schedule.py文件下的已完成任务列表
        f.write(i+'\n')
    f.write('\n' + '注:任务截图在执行程序所在目录的screenshot文件夹下')
    f.close()
    print('报告编写完成')

def send_mail():
        '''任务完成后发送邮件通知'''
        # ----------正文及主题----------
        f = open(report_path + 'report.txt', 'r')
        mail_body = f.read()
        f.close()

        msg = MIMEText(mail_body, 'plain', 'utf-8')
        msg['Subject'] = Header('每日手机任务','utf-8') #这个是邮件主题名称
        msg['From'] = Header('woziji','utf-8')
        msg['To'] = Header('peili','utf-8')

        # ----------登录并发送----------
        try:
            smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)  # QQ邮箱发送服务器以及端口，SMTP默认端口是25，这里改成465
            smtp.login('lipei@rayvision.com', 'tmVkc9tAQDNH4UfK')  # 如果是QQ邮箱的话，第二个参数不是直接用的密码，用的是QQ邮箱的授权码
            smtp.sendmail('lipei@rayvision.com', '691849609@qq.com', msg.as_string())  # 前两个参数分别是发送邮箱和接收邮箱
            smtp.quit()
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print(e)


if __name__ == '__main__':
    start = time.clock() #开始时间戳

    start_appium_server() #启动appium服务
    process() #打印当前开发进度
    start_android_devices() #启动模拟器
    time.sleep(20)

    #--------------任务区域--------------
    jd_finance()
    jd_app()
    wyy_music()
    lt_yingyeting()
    zssh()
    taobao()
    youguo()
    #------------------------------------

    end = time.clock() #结束时间戳

    write_report() #结果写入报告文本
    send_mail() #发送邮件

    stop_android_devices() #关闭模拟器
    stop_appium_server()  # 关闭appium服务
