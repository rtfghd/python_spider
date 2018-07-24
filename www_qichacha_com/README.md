## 企查查信息查询

## 致谢项目
企查查爬虫用到了[proxy_poll](https://github.com/jhao104/proxy_pool)项目，在使用本脚本前先开启proxy_poll项目获取一定量的IP

## 使用方法
1. 更换cookie
打开两个软件，在header部分将登陆后的最新cookie替换
```
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Cookie':'XXXXX'
    }
```


2. 设置抓取量
非企查查会员查询结果最多只有10页，每页10条共100条，会员可以查询5000条数据。打开文件`qcc_company_list.py`修改get_all_page函数中的循环次数（也就是页码数）
```
def get_all_page():
    search_name = str(input('请输入查询关键字：'))
    for i in range(1,11):
        get_company_list(search_name,i)
    return company_list

```

3. 开启任务
执行命令`python qcc_company_info.py`即可