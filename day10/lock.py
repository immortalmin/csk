#Author:immortal luo
# -*-coding:utf-8 -*-
from multiprocessing import Lock,Process

def f(l,i):
    l.acquire()
    print("hello world ",i)
    l.release()

if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f,args=(lock,num)).start()