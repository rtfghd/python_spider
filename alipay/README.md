###  前言
这个脚本主要是用来查看个人支付宝的账户信息以及最近的消费记录，但是调式过程中发现支付宝的cookie几分钟就失效，因此前半部分先用selenium操作浏览器登陆支付宝来获取最新的cookie

### 用到的库
- selenium
- beautifulsoup
- requests
- time

注：需要下载好chrome浏览器驱动并配置好环境变量
### 修改账户和密码
修改这两行的账户和密码就可以直接运行了
```
driver.find_element_by_id('J-input-user').send_keys('支付宝账户')
driver.find_element_by_id('password_rsainput').send_keys('支付宝密码')
```
### 问题
在调试过程中发现，selenium操作浏览器登录的时候，账号密码都正确有时候仍然会失败，不清楚是不是支付宝的安全策略，目前没找到有效的解决办法，只能放在判断里面失败了重新执行，这里用网页的title做判断。
```
if web_title == '我的支付宝 － 支付宝':
```
