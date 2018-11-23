#Author:immortal luo
# -*-coding:utf-8 -*-
import json
import pickle

def sayhi(name):
    print("hello",name)

f = open("test.test","rb")
data = pickle.loads(f.read())
data["func"]("chen")