'''

这部分理解参考：

https://www.bilibili.com/video/BV1QA411H7tK?from=search&seid=17305042509580602672

图文代码地址： https://blog.csdn.net/qq_30758629/article/details/112527763

'''

import threading
import time

data=0
lock=threading.Lock()  #创建一个锁对象

def func():
    global data
    print("%s is acquire lock..\n" %threading.current_thread().getName())

    if lock.acquire():
        print("%s get lock "%threading.current_thread().getName())
        data+=1
        time.sleep(2)
        print("%s release lock "%threading.current_thread().getName())
        print(data)
        lock.release()

t1=threading.Thread(target=func)
t2=threading.Thread(target=func)
t3=threading.Thread(target=func)
t1.start()
t2.start()
t3.start()