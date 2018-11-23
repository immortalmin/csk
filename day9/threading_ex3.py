#Author:immortal luo
# -*-coding:utf-8 -*-
import threading
import time

def run(n):
    lock.acquire()#线程锁
    global num
    num += 1
    lock.release()

lock = threading.Lock()
num = 0
t_obj = []
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True)#把当前线程设置成守护线程，必须写在start之前
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

print("-------all threads has finished...",threading.current_thread(),threading.active_count())#判断线程、个数
print("num:",num)
