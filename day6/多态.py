#Author:immortal luo
# -*-coding:utf-8 -*-
#一种接口，多种实现

class Animal:
    def __init__(self,name):
        self.name = name

    def talk(self):
        # raise NotImplementedError("Subclass must implement abstract metho")
        pass
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print("Meow!")

class Dog(Animal):
    def talk(self):
        print("Woof! Woof!")

d = Dog("小黑")
# d.talk()
Animal.animal_talk(d)

c = Cat("小白")
# c.talk()
Animal.animal_talk(c)