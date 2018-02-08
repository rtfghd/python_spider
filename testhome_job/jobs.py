import requests
from bs4 import BeautifulSoup


jobs_list = []
jobs_file = r'E:\auto_task\testhome_job\jobs.txt'
jobs_file_chongqing = r'E:\auto_task\testhome_job\chongqing_jobs.txt'
error_file = r'E:\auto_task\testhome_job\error.txt'

#爬取一页的数据
def get_onepage_jobs(page):
    url = 'https://testerhome.com/jobs?page={}'.format(str(page))
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    jobs = soup.select('div.panel-body.item-list > div > div.infos.media-body > div.title.media-heading > a')
    for job in jobs:
        job_title = job.get('title')                                    #招聘标题
        job_url = 'https://testerhome.com' + job.get('href')            #招聘链接
        jobs_list.append(job_title + ' ===>> ' + job_url)


#爬取所有数据
def get_all_jobs():
    print('=' * 20 + '数据加载完毕后写入本地文本' + '=' * 20)
    all_page_number = BeautifulSoup(requests.get('https://testerhome.com/jobs').text,'lxml').select('div.panel-footer.clearfix > ul > li > a')[-2].get_text()  #获取总页数,select获取结果是个列表，最后一页的页码在列表倒数第二
    for page in range(1,int(all_page_number)+1):
        print('正在加载第%d页数据' %page)
        get_onepage_jobs(page)

    new_jobs_list = list(set(jobs_list))  # 去掉重复数据

    #结果写入本地文件
    print('='*20 + '正在将结果保存至本地' + '='*20)
    for i in new_jobs_list:
        try:
            f = open(jobs_file,'a+')
            f.write(i + '\n')
            f.close()
            print(i + ' 已完成(%d/%d)' %(new_jobs_list.index(i)+1,len(new_jobs_list)))

            #重庆的单独保存一遍
            if '重庆' in i:
                f = open(jobs_file_chongqing, 'a+')
                f.write(i + '\n')
                f.close()

        except Exception as e:
            f = open(error_file, 'a+')
            f.write(i.split(' ===>> ')[1] + '   ===>>   '+ str(e) + '\n')
            f.close()
            print(e)


if __name__ == '__main__':
    get_all_jobs()
    print('='*20 + '爬取完毕！' + '='*20)

