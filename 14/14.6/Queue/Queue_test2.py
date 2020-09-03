#!/usr/bin/env python

# -*- *************** -*-
# @File  : Queue_test2.py
# @Description : 
# @Author: mql
# @Time  : 2020-09-03 11:31
# -*- *************** -*-


import threading
import time
import queue


def product(bq):
    str_tuple = ("Python", "Kotlin", "Swift")
    for i in range(99999):
        print(threading.current_thread().name + "生产者准备生产元组元素！")
        time.sleep(0.01)
        # 尝试放入元素， 如果队列已满，则线程被阻塞
        bq.put(str_tuple[i % 3])
        print(threading.current_thread().name + "生产者准备生产元组元素完成！")


def consume(bq):
    while True:
        print(threading.current_thread().name + "消费者准备消费元组元素！")
        time.sleep(0.01)
        # 尝试取出元素， 如果队列已空，则线程被阻塞
        t = bq.get()
        print(threading.current_thread().name + "消费者准备消费元组元素[ %s ]完成！" % t)


# 创建一个容量为1的queue
bq = queue.Queue(maxsize=1)

# 启动三个生产者
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()

# 启动一个消费者
threading.Thread(target=consume, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()
threading.Thread(target=consume, args=(bq,)).start()