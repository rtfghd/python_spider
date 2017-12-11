#!/usr/bin/python
#coding=utf-8
_auther = 'peili'

from bs4 import BeautifulSoup
import requests

start_url = 'http://sz.58.com/sale.shtml?utm_source=market&spm=b-31580022738699-me-f-824.bdpz_biaoti'
url_host = 'http://sz.58.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Cookie':'id58=Cra8GlhKdVvN68QDC/T6cQ==; mcity=sz; 58home=sz; ipcity=sz%7C%u6DF1%u5733%7C0; als=0; commonTopbar_myfeet_tooltip=end; myfeet_tooltip=end; bj58_new_session=1; bj58_init_refer="http://sz.58.com/sale.shtml?utm_source=market&spm=b-31580022738699-me-f-824.bdpz_biaoti"; bj58_new_uv=1; bj58_id58s="dnJHVlJ3dm89Mkx5NDI5NA=="; sessionid=d3cb238c-d09b-443b-92bf-2e37e2813688; 58cooper="userid=43395089459990&username=ncq3er&cooperkey=b0977b30030bb2e90272d2c301a36c83"; www58com="AutoLogin=true&UserID=43395089459990&UserName=ncq3er&CityID=0&Email=&AllMsgTotal=0&CommentReadTotal=0&CommentUnReadTotal=0&MsgReadTotal=0&MsgUnReadTotal=0&RequireFriendReadTotal=0&RequireFriendUnReadTotal=0&SystemReadTotal=0&SystemUnReadTotal=0&UserCredit=0&UserScore=0&PurviewID=&IsAgency=false&Agencys=null&SiteKey=2A31A22D9706340594BD65372F0241395129CD05CC06B4F5B&Phone=&WltUrl=&UserLoginVer=887EB60F8846773DBF927A4ED1B3481D1&LT=1481275340901"; city=sz; PPU="UID=43395089459990&PPK=db3d278d&PPT=3d5f9362&SK=4E2D7FDC8FC54575808AFF5F38597ED37D21E87AFC7D471B8&LT=1481275341413&UN=ncq3er&LV=e5d60885&PBODY=ieUhXn9kvsXLTUbepJvCKyHOjdJd4G9K5vf57tfbV5YKwEP0A7t7lwteHB_dcVo_q8u0n3saYeoYUQsSSBA3Sm4qYzicIbtLHecPsqJ91gaXNnj5dciKD6zMcRUwhYoP04Y2YEKllYlu8n7CGn66TgsgpEfJfR3K-uLIcRK_4TU&VER=1"; 58tj_uuid=7cd6d5dc-2e43-430a-afca-1e1be4573a18; new_session=0; new_uv=1; utm_source=market; spm=b-31580022738699-me-f-824.bdpz_biaoti; init_refer=; 43395089459990_opened_menu_id=-56-'
}
def get_chanel_urls(url):
    wb_data = requests.get(start_url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        page_url = url_host + link.get('href')
        print(page_url)

# get_chanel_urls(start_url)

category_list = '''
    http://sz.58.com/shouji/
    http://sz.58.com/tongxunyw/
    http://sz.58.com/danche/
    http://sz.58.com/fzixingche/
    http://sz.58.com/diandongche/
    http://sz.58.com/sanlunche/
    http://sz.58.com/peijianzhuangbei/
    http://sz.58.com/diannao/
    http://sz.58.com/bijiben/
    http://sz.58.com/pbdn/
    http://sz.58.com/diannaopeijian/
    http://sz.58.com/zhoubianshebei/
    http://sz.58.com/shuma/
    http://sz.58.com/shumaxiangji/
    http://sz.58.com/mpsanmpsi/
    http://sz.58.com/youxiji/
    http://sz.58.com/jiadian/
    http://sz.58.com/dianshiji/
    http://sz.58.com/ershoukongtiao/
    http://sz.58.com/xiyiji/
    http://sz.58.com/bingxiang/
    http://sz.58.com/binggui/
    http://sz.58.com/chuang/
    http://sz.58.com/ershoujiaju/
    http://sz.58.com/bangongshebei/
    http://sz.58.com/diannaohaocai/
    http://sz.58.com/bangongjiaju/
    http://sz.58.com/ershoushebei/
    http://sz.58.com/yingyou/
    http://sz.58.com/yingeryongpin/
    http://sz.58.com/muyingweiyang/
    http://sz.58.com/muyingtongchuang/
    http://sz.58.com/yunfuyongpin/
    http://sz.58.com/fushi/
    http://sz.58.com/nanzhuang/
    http://sz.58.com/fsxiemao/
    http://sz.58.com/xiangbao/
    http://sz.58.com/meirong/
    http://sz.58.com/yishu/
    http://sz.58.com/shufahuihua/
    http://sz.58.com/zhubaoshipin/
    http://sz.58.com/yuqi/
    http://sz.58.com/tushu/
    http://sz.58.com/tushubook/
    http://sz.58.com/wenti/
    http://sz.58.com/yundongfushi/
    http://sz.58.com/jianshenqixie/
    http://sz.58.com/huju/
    http://sz.58.com/qiulei/
    http://sz.58.com/yueqi/
    http://sz.58.com/chengren/
    http://sz.58.com/nvyongpin/
    http://sz.58.com/qinglvqingqu/
    http://sz.58.com/qingquneiyi/
    http://sz.58.com/chengren/
    http://sz.58.com/xiaoyuan/
    http://sz.58.com/ershouqiugou/
    http://sz.58.com/tiaozao/
    http://sz.58.com/tiaozao/
    http://sz.58.com/tiaozao/
'''