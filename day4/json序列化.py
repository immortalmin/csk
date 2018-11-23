#Author:immortal luo
# -*-coding:utf-8 -*-

import json
import pickle

# info = {
#     'name' : 'csk',
#     'age':19
# }

def sayhi(name):
    print("hello",name)

info = {
    'name':'csk',
    'age':19,
    'func':sayhi
}


f = open("test.test","wb")
# f.write(str(info))
# f.write(json.dumps(info))#转字符串
f.write(pickle.dumps(info))
f.close()