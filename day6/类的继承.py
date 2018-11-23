#Author:immortal luo
# -*-coding:utf-8 -*-

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sleep(self):
        print("%s is sleeping..."%self.name)

    def eat(self):
        print("%s is eating..."%self.name)

    def __del__(self):
        pass

class Relation(object):
    def make_friends(self,obj):
        print("%s is making friends with %s"%(self.name,obj))

class Man(People,Relation):#多重继承
    def __init__(self,name,age,money):
        People.__init__(self,name,age)
        self.money = money

    def run(self):
        print("man %s is running..."%self.name)

class Woman(People):
    def __init__(self,name,age,size):
        # People.__init__(self,name,age)#方法1
        super(Woman,self).__init__(name,age)#方法2
        self.size = size

    def shop(self):
        print("Woman %s is shopping..."%self.name)

chen = Man("陈盛款",19,10000)
luo = Woman("罗敏敏",19,'B')
chen.run()
luo.shop()
chen.make_friends("罗敏敏")
