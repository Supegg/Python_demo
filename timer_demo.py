import threading
import time

start = time.time()
tic = lambda: '%1.3fs:\t' % (time.time() - start)

def fun_timer():

    print(tic(), 'Hello Timer!', threading.Thread.name)
    global timer
    timer = threading.Timer(2, fun_timer)
    timer.start()

threading.Thread.name = 'main'
timer = threading.Timer(1, fun_timer)
timer.start()

time.sleep(15) # 15秒后停止定时器
timer.cancel()
