#coding=utf-8
import os,time

def start_android_devices():
    '''调用cmd启动安卓模拟器'''
    command = r'start D:\Application\dnplayer2\dnplayer.exe'
    os.system(command)
    print('模拟器启动成功')
    print('\n')

def stop_android_devices():
    '''调用cmd结束安卓模拟器进程'''
    command = r'taskkill -f -im dnplayer.exe'
    os.system(command)
    print('所有任务执行完毕，关闭模拟器')
    print('\n')

if __name__ == '__main__':
    start = time.clock()
    # start_android_devices()
    # time.sleep(15)
    # stop_android_devices()
    end = time.clock()