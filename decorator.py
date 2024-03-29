from functools import wraps


def decorator_a(func):
    print ('Get in decorator_a')
    @wraps(func)
    def inner_a(*args, **kwargs):
        print ('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a

def decorator_b(func):
    print ('Get in decorator_b')
    @wraps(func)
    def inner_b(*args, **kwargs):
        print ('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print ('Get in f')
    return x * 2

f(1)