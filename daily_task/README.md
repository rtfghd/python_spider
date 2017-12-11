# 环境准备
JDK (1.8.0_91)
SDK (25.1.7)
python 3
node.js (6.11.0)
appium server (1.4.16)
Appium-Python-Client (0.24)
雷电安卓模拟器（安卓5.1.1，720*1280）

---

# 目录详解
```
C:.
│  appium_server.py
│  python.exe
│  README.md
│  run.py
│  start_appium_server.bat
│  stop_appium_server.bat
├─public
│  │  get_device.py
│  │  schedule.py
├─report
│      report.txt
├─screenshot
```

- [ run.py ] 启动整个项目就运行这个文件
- [ public ] 放一些执行每个任务都会用到的公共文件，包括启动/关闭安卓模拟器脚本，启动/关闭appium服务的bat文件，运行bat文件的python脚本，以及项目进度说明。
- [ report ] 任务执行结果写在这个目录下的.txt文件
- [ screenshot ] 执行APP任务时的截图放在目录下

# Windows计划任务
直接运行上面run.py文件就可以开始任务，但是要添加到Windows计划任务定时运行的话需要修改一些地方。

##### 配置计划任务
1.在Python安装目录，找到python.exe复制到项目主目录的daily_task文件夹下。

2.在计划任务的操作栏做如下修改
- "程序或脚本(P)" 填写`python.exe`
- "添加参数(可选)"填写`run.py`的绝对路径
- "起始于(可选)"填写上一步复制到`daily_task`目录下的`python.exe`的绝对路径，只写到目录，不包括python.exe

##### 修改路径
把run.py文件中的screenshot_path和report_path变量的相对路径改成局对路径。

---

# 不足之处
任务执行部分的内容用的是用appium，我对appium只是处于会用的地步，不是很精通，里面的元素处理方法也有很多不是很好，这里可以按照自己的习惯编写就好。
