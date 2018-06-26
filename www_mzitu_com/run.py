from all_albums import get_all_albums
from main import mkdir,download_pic,all_num
import time



if __name__ == '__main__':
    get_all_albums()      # 获取所有板块下所有专辑的链接，保存至txt文本
    time.sleep(1)
    mkdir()               # 创建所有板块图片的主目录
    time.sleep(1)
    download_pic()        # 开始抓取图片，目录层级自动创建
    all_num()             # 统计一共抓取了多少专辑和图片