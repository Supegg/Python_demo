import threading
import time


class Singleton():
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)


    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)  
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()

'''
实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__）
实例化对象；然后再执行类的__init__方法，对这个对象进行初始化
'''