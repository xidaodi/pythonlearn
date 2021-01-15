# 线程创建，基于自定义函数

import os
import time
import threading

#线程执行函数
def fun(n):
    time.sleep(1)
    my_threat_name=threading.current_thread().name
    my_threat_id=threading.current_thread().ident
    print("当前线程名称为：{}，线程id为{}，所在进程为{}，参数为{}".format(my_threat_name,my_threat_id,os.getpid,n))
    print("end")

mythread=threading.Thread(target=fun,name="线程1",args=("参数1",))

mythread.start()
time.sleep(2)