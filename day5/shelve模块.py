#Author:immortal luo
# -*-coding:utf-8 -*-
import shelve
#shelve类似于一个存储持久化对象的持久化字典，即字典文件。
#使用方法也类似于字典。

#保存对象至shelve文件中：
# wangzhe = dict(zip(['name','age'],['wangzhe',24]))
# lijianguo = dict(zip(['name','age'],['lijianguo',25]))
# chen = {'name':'chen','age':19}
# db = shelve.open('shelveDict')
# db['wangzhe'] = wangzhe
# db['lijianguo'] = lijianguo
# db['chen'] = chen
# db.close()

#从文件中读取对象：
# db = shelve.open('shelveDict')
# print(db['wangzhe'])
# print(db['lijianguo'])
# db.close()

#更新文件中的数据：
# db = shelve.open('shelveDict')
# wangzhe = db['wangzhe']
# wangzhe['name']='wang zhe'
# db['wangzhe'] = wangzhe
# print(db['wangzhe'])
# db['wangzhe']['age'] = 15#这句自己想的，行不通
# print(db['wangzhe'])
# db.close()