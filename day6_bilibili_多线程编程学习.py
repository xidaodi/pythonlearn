
'''
进程：操作系统资源分配的基本单位
线程：程序执行的最小单位,CPU调度的基本单位

线程的创建步骤：
1，导入模块
2，通过线程类创建线程对象
3，启动线程对象

'''

import os
import time
import threading

def sing(num):

    for i in range(num):
        print("%s is sing...")
        time.sleep(2)

def dance(num):

    for i in range(num):
        print("%s is dancing...")
        time.sleep(2)

if __name__ == '__main__':

    sing_thread=threading.Thread(target=sing,args=(3,),daemon=False,name="sing_thread")
    dance_thread=threading.Thread(target=dance,kwargs={"num":3},daemon=False,name="dance_thread")

    sing_thread.start()
    dance_thread.start()

    print(threading.current_thread())
    print("main thread finished ")