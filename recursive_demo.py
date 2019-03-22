from random import randint

def r(retry=2):
    if retry == 0:
        return -1
    try:
        2/randint(0,1) 

        return retry
    except:
        retry-=1
        return r(retry)

if __name__ == '__main__':
    print(r())
