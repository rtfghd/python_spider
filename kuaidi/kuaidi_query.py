#!/usr/bin/env python
#coding:utf-8

import requests
import re
import json
import urllib.request

#post请求，从返回结果里获取快递公司信息  430898658680
def kuaidi_post():
    global comCode,num
    try:
        url = 'http://www.kuaidi100.com/autonumber/autoComNum?text='
        wb_data = requests.post(url+str(input('请输入你的快递单号：')))
        response = wb_data.text
        #正则表达获取快递公司名称和快递单号
        comCode = re.findall(r'"auto":\[\{"comCode":"(.*?)"',response,re.S)[0]
        num = re.findall(r'"num":"(\d+)"',response,re.S)[0]
        # print(comCode,num)
    except:
        print('订单号有误，请重新输入'+'\n'+'-'*25+'\n')
        kuaidi_post()

#get请求获取物流信息
def kuaidi_get():
    url2 = 'http://www.kuaidi100.com/query?type={}&postid={}'.format(comCode,num)
    wb_data = urllib.request.urlopen(url2).read().decode('utf-8')
    responsejson = json.loads(wb_data)
    # print(responsejson)
    message = responsejson['message']

    #正常的订单返回的值里面message是ok
    if 'ok' in message:
        dates = responsejson['data']
        infos = responsejson['data']
        for date,info in zip(dates,infos):
            date = date['time']
            info = info['context']
            print(date,'\t',info)

        #查完一笔快递单后继续查询
        print('-'*25+'\n')
        kuaidi_post()
        kuaidi_get()

    else:
        print('查无此订单，请重新输入'+'\n'+'-'*25+'\n')
        kuaidi_post()
        kuaidi_get()

if __name__ == '__main__':
    print('快递查询，速度极快！'+'\n'+'-'*25+'\n')
    kuaidi_post()
    kuaidi_get()
