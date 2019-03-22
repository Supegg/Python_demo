import time
import threading
class Singleton(object):
    _instance_lock = threading.Lock() # 线程安全

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


def task(arg):
    obj = Singleton.instance()
    print(obj)
for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
time.sleep(2)
obj = Singleton.instance()
print(obj)

'''
这种方式实现的单例模式，使用时会有限制，以后实例化必须通过 obj = Singleton.instance() 
如果用 obj=Singleton() ,这种方式得到的不是单例
'''