#!/usr/bin/env python
# -*- coding: utf-8 -*-

from queue import Queue # 非线程安全
import threading
import time


class Consumer(threading.Thread):
    """没打印一个数字等待1秒，并发打印10个数字需要多少秒？"""

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        done = False
        while not done:
            # 消费者端，从队列中获取num
            num = self.queue.get()
            if num is None:  # 收到None信号，后台线程退出
                done = True
            else:
                print(f"{self.name} Retrieved", num)
            time.sleep(1)
            # 在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号
            self.queue.task_done()

        print(f"{self.name} Consumer Finished")


if __name__ == '__main__':
    '''
    threading.Thread 和 queue.Queue 完成线程池功能
    '''
    start = time.time()
    queue = Queue()  # 生产队列
    threads = list()
    n = 5
    # 产生一个 threads pool, 并把消息传递给thread函数进行处理，这里开启n个并发
    for _ in range(n):
        t = Consumer(queue)
        t.setDaemon(True)
        threads.append(t)
        t.start()

    # 往队列中填充数据
    for num in range(10):
        queue.put(num)

    for _ in range(n):
        queue.put(None)

    queue.join()  # 等待数据消费完
    # Fatal Python error: could not acquire lock for <_io.BufferedWriter name='<stdout>'> at interpreter shutdown,
    # possibly due to daemon threads
    for t in threads:  # 所有线程退出
        t.join(timeout=1)

    print("Elapsed Time: %s" % (time.time() - start))


'''
1、创建一个 Queue.Queue() 的实例，然后使用数据对它进行填充。
2、将经过填充数据的实例传递给线程类，后者是通过继承 threading.Thread 的方式创建的。
3、生成守护线程池。
4、每次从队列中取出一个项目，并使用该线程中的数据和 run 方法以执行相应的工作。
5、在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号。
6、对队列执行 join 操作，实际上意味着等到队列为空，再退出主程序。
在使用这个模式时需要注意一点：通过将守护线程设置为 true，程序运行完自动退出。好处是在退出之前，可以对队列执行 join 操作、或者等到队列为空。
--------------------- 
作者：lx59 
来源：CSDN 
原文：https://blog.csdn.net/u012474535/article/details/79570011 
版权声明：本文为博主原创文章，转载请附上博文链接！

'''
