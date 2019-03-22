import time
import signal
import sys

def exit(signum, frame):
    print('exit gracefully.')
    sys.exit()

signal.signal(signal.SIGINT, exit)
signal.signal(signal.SIGTERM, exit)

while True:
    print(time.asctime())
    time.sleep(1)