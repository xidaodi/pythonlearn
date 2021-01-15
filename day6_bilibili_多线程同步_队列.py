'''

这部分理解参考：

https://www.bilibili.com/video/BV1QA411H7tK?from=search&seid=17305042509580602672

图文代码地址： https://blog.csdn.net/qq_30758629/article/details/112527763

'''

from queue import Queue
import threading
import time
import random

#生产者线程
class Producer(threading.Thread):

    def __init__(self,t_name,queque):
        threading.Thread.__init__(self,name=t_name)
        self.data=queque

    def run(self):
        for i in range(5):
            print("%s: %s is producing %d to the queue!\n" %(time.ctime(), self.getName(), i))
            self.data.put(i)  #向队列中添加数据
            time.sleep(random.randrange(10) / 5)
        print("%s: %s finished!" % (time.ctime(), self.getName()))

# 消费者线程
class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue


    def run(self):
        for i in range(5):
            val = self.data.get()  # 从队列中取出数据
            print("%s: %s is consuming. %d in the queue is consumed!\n" % (time.ctime(), self.getName(), val))
            time.sleep(random.randrange(10))
        print("%s: %s finished!" % (time.ctime(), self.getName()))

if __name__ == '__main__':

    queue=Queue()
    producer=Producer("Producer",queue)
    consumer=Consumer("Consumer",queue)
    producer.start()
    consumer.start()










