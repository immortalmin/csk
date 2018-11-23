#Author:immortal luo
# -*-coding:utf-8 -*-
from multiprocessing import Process,Pool,freeze_support
import time,os

def Foo(i):
    time.sleep(2)
    print("in process ",os.getpid())
    return i+100

def Bar(arg):
    print("-->exec done:",arg,os.getpid())

if __name__ == '__main__':
    pool = Pool(5)#允许进程池同时放入5个进程
    print("主进程",os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo,args=(i,),callback=Bar)#callback=回调，一个进程后面跟着一个线程（可能是这样）,回调函数通过父进程进行，可以提高程序的效率
        # pool.apply(func=Foo,args=(i,))#串行
        # pool.apply_async(func=Foo,args=(i,))#并行

    print("end")
    pool.close()
    pool.join()