#Author:immortal luo
# -*-coding:utf-8 -*-

def bulk(self):
    print("yelling...")

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating..."%self.name)

d = Dog("小黑")
choice = input(">>:").strip()
# print(hasattr(d,choice))#判断对象d中是否有choice方法，hasattr(对象,方法的字符串类型)
# print(getattr(d,choice))#获取内存地址
if hasattr(d,choice):
    delattr(d,choice)#删除属性
    # func = getattr(d,choice)#调用
    # func()
else:
    # setattr(d,choice,bulk)#新建一个方法
    # d.talk(d)
    # getattr(d,choice)(d)
    print("...")
    # setattr(d,choice,None)
    # print(getattr(d,choice))
print(d.name)
