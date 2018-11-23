#Author:immortal luo
# -*-coding:utf-8 -*-

class Dog(object):
    def __init__(self,name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eating %s"%(self.name,self.__food))

    @eat.setter
    def eat(self,food):
        print(",,,")
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("已删除")


d = Dog("小黑")
d.eat = "骨头"
d.eat
del d.eat