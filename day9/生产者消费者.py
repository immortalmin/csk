#Author:immortal luo
# -*-coding:utf-8 -*-
import threading,time
import queue

q = queue.Queue(maxsize=10)
def Producer(name):
    count = 1
    while True:
        q.put("骨头%s"%count)
        print("生产了骨头%s"%count)
        count += 1

def Consumer(name):
    # while q.qsize() > 0:
    while True:
        print("[%s] 取到[%s]，并且吃了它"%(name,q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer,args=("csk",))
c = threading.Thread(target=Consumer,args=("xiaohuang",))
p.start()
c.start()