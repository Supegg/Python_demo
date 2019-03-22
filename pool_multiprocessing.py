#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Pool, Process, Queue, Pipe   # Queue 线程安全
# from multiprocessing.dummy import Pool, Process, Queue, Pipe  # thread
from time import sleep
import threading


def f(x):
    # print(threading.currentThread().getName(), threading.currentThread().ident)
    sleep(0.1)
    return x*x


def f1(q):
    q.put([42, None, 'Queue'])


def f2(conn):
    conn.send([43, None, 'Pipe'])
    conn.close()


if __name__ == '__main__':
    # Queue 通信
    q = Queue()
    p = Process(target=f1, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'Queue']"
    p.join()

    # Pipe通信
    parent_conn, child_conn = Pipe()
    p = Process(target=f2, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[43, None, 'Pipe']"
    p.join()

    # thread pool
    # start 4 worker processes/threads
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        # for i in pool.imap_unordered(f, range(10)):
        #     print(i)
        print(list(pool.imap_unordered(f, range(10))))

        # evaluate "f(10)" asynchronously
        res = pool.apply_async(f, [10])
        print(res.get(timeout=1))             # prints "100"

        # make worker sleep for 10 secs
        res = pool.apply_async(sleep, [10])
        # raises multiprocessing.TimeoutError
        print(res.get(timeout=1))

    # exiting the 'with'-block has stopped the pool

    '''
    同步或异步执行多进程/线程任务
    ref:
        https://docs.python.org/3/library/multiprocessing.html
    '''
