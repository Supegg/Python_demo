
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            # print('args', *args, **kargs)
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton

@Singleton
class A():
    a = 1

    def __init__(self, name):
        self.name = name

a1 = A('a1')
print(a1.name)
a2 = A('a2') # 直接返回a1实例
print(a2.name)

print(id(a1) ==id(a2))