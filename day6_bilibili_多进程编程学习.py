'''

https://www.bilibili.com/video/BV1fz4y1D7tU?p=10

进程：操作系统资源分配的基本单位
线程：程序执行的最小单位,CPU调度的基本单位

如何实现多进程：
1，导入进程包
2，使用进程类创建进程对象
3，使用进程对象启动进程执行指定任务

'''
import time
import multiprocessing
import os

def sing(num,name):
    # print("the sing process id :",os.getpid())
    # print("the main process id :",os.getppid())
    for i in range(num):
        print("%s is sing..."%name)
        time.sleep(1)

def dance(num,name):
    print("the dance process id :",os.getpid())
    print("the main process id :",os.getppid())
    for i in range(num):
        print("%s is dancing..."%name)
        time.sleep(1)

if __name__ == '__main__':
    print("the current mian fucntion process id :",os.getpid())
    sing_process=multiprocessing.Process(target=sing,args=(3,"the bird"))  #使用元组传参
    #dance_process=multiprocessing.Process(target=dance,kwargs={"num":3,"name":"the tiger"})  #使用字典传参


    #设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
    sing_process.daemon= True
    sing_process.start()
    #dance_process.start()
    time.sleep(1)

    print("the main process has finished")
