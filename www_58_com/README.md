# 58tongcheng_spider

### 爬取58同城二手市场每个模块最近100页的内容，结果存放在mongo db

* all_category.py === 获取每个二手市场板块的url
* page_parsing.py === 爬虫主要函数
* counts.py  === 计数函数，从DB查看商品链接爬取进度
* counts2.py  === 计数函数，从DB查看商品详情爬取进度
* main.py === 此爬虫项目运行这个文件来执行
