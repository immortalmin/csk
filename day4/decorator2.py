#Author:immortal luo
# -*-coding:utf-8 -*-
import time

def bar():
    time.sleep(1)
    print("in the bar")

def test2(func):
    print(func)
    return func

# print(test2(bar))
bar = test2(bar)
bar()