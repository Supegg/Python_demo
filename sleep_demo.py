import time
from threading import Thread

class worker(Thread):
    def run(self):
        for x in range(0,11):
            print(x)
            time.sleep(1)   #阻塞当前线程

class waiter(Thread):
    def run(self):
        for x in range(100,103):
            print(x)
            time.sleep(5)


worker().start()
waiter().start()
