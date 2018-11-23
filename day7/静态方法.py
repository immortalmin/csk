#Author:immortal luo
# -*-coding:utf-8 -*-

class Dog(object):
    n=50
    def __init__(self,name):
        self.name = name

    @staticmethod
    def eat(self):
        print("%s is eating %s"%(self,"aaa"))

    @classmethod
    def talk(self):
        print(self.n)

d = Dog("小黑")
d.eat("骨头")
# d.eat(d)
d.talk()