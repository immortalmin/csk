#Author:immortal luo
# -*-coding:utf-8 -*-
import redis

r = redis.Redis(host='localhost',port=6379)
r.set('foo','bar')
print(r.get('foo'))