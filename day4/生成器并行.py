#Author:immortal luo
# -*-coding:utf-8 -*-
import time
def consumer(name):
    print("%s 准备吃包子啦！"%name)
    while True:
        baozi = yield
        print("%s包子来了，被%s吃了！"%(baozi,name))

# c = consumer("chen")
# c.__next__()
# b1 = "韭菜馅"
# c.send(b1)#唤醒生成器并给yield传值

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("开始做包子")
    for i in range(10):
        time.sleep(1)
        print("做了两个包子！")
        c.send(i)
        c2.send(i)

producer("chen")