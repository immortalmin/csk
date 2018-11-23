#Author:immortal luo
# -*-coding:utf-8 -*-
import threading,time
import queue

# def run():
#     print("running")
#     time.sleep(2)
#
# for i in range(10):
#     t = threading.Thread(target=run)
#     t.setDaemon(True)#守护线程
#     t.start()
#     t.join()
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
print(q)
