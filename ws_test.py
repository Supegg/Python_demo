#!/usr/bin/env python

import json
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import argparse
import uuid
import threading


statics = {}
s_time=time.time()

def on_message(ws, message):
    if message in ['pong', 'error'] :
        return
        
    ws.send('ping')
    #print(threading.current_thread().ident)
    tid=threading.current_thread().ident
    if statics.get(tid):
        statics[tid] +=1
    else:
        statics[tid] = 1

    global s_time
    if time.time() - s_time > 5:
        print(f'{time.strftime("%H:%M:%S", time.localtime())}\t{json.loads(message)["time"]}\n{statics}\n')
        s_time = time.time()

def on_error(ws, error):
    print(error)

def on_close(ws):
    print(f"### {threading.current_thread().ident} closed ###")

def on_open(ws):
    d = {"cmd":"query","data":{"group":"Binance","sign":"1","uid":"c9ed3d9e45452d54e2503eb2a8697a6b"},"time":"1545363844"}
    #ws.__dict__['uuid'] = str(uuid.uuid1()) 
    #print(ws.__dict__['uuid'])
    ws.send(json.dumps(d))

def test(n):
    def run():
        #websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://testnet.bibo.camwallet.cn:8282",
                                  on_message = on_message,
                                  on_error = on_error,
                                  on_open = on_open,
                                  on_close = on_close)
        
        ws.run_forever()
    
    for _ in range(0, n):
        thread.start_new_thread(run, ())
        #time.sleep(1)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help="threads")
    args = parser.parse_args()

    print(f'start {args.n} threads')
    test(args.n)
    
    print("press enter to exit...")
    input()
    

