#Author:immortal luo
# -*-coding:utf-8 -*-
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        print("成功创建一所大学:%s"%self.name)

sc1 = School("北京大学","北京")
sc1 = School("复旦大学","上海")