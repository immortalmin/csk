#Author:immortal luo
# -*-coding:utf-8 -*-
import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)
    # print("done",threading.current_thread())
    print("done")

start_time = time.time()
t_obj = []
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True)#把当前线程设置成守护线程，必须写在start之前
    t.start()
    t_obj.append(t)
# t.join()
# for t in t_obj:
#     t.join()

print("-------all threads has finished...",threading.current_thread(),threading.active_count())#判断线程、个数
print("cost:",time.time()-start_time)
# t1 = threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()
# run('t1')
# run('t2')
