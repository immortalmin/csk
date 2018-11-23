#Author:immortal luo
# -*-coding:utf-8 -*-
import time

def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("times is %s" %(stop_time-start_time))
        return func()
    return deco
@timer  #即（等同于）test1 = timer(test1)
def test1():
    time.sleep(1)
    print("in the test1")

def test2(s):
    time.sleep(1)
    print("in the test2")

# test1()
# test2()
# test1 = deco(test1)
# test2 = deco(test2)
# test1()
test2("csk")
# test1 = timer(test1)
test1()