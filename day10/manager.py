#Author:immortal luo
# -*-coding:utf-8 -*-
from multiprocessing import Manager,Process
import os

def f(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()#生成一个字典，可在多个进程间共享和传递
        l = manager.list(range(5))#生成一个列表，可在多个进程间共享和传递
        p_list = []
        for i in range(10):
            p = Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)