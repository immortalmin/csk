#Author:immortal luo
# -*-coding:utf-8 -*-
# import urllib
from urllib import request
import gevent
from gevent import monkey

monkey.patch_all()#把当前程序的所有的IO操作给我单独地做上标记

def f(url):
    print("GET: %s"%url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open("url.html","wb")
    f.write(data)
    print("%d bytes recrived from %s"%(len(data),url))

gevent.joinall([
    gevent.spawn(f,'https://www.python.org/'),
    gevent.spawn(f,'https://www.yahoo.com/'),
    gevent.spawn(f,'https://github.com/'),
])
