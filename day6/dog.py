#Author:immortal luo
# -*-coding:utf-8 -*-

class Dog:

    def __init__(self,name):
        self.name = name

    def bulk(self):
        print(self.name+"wang wang wang")


d1 = Dog("xiaohuang")
d2 = Dog("xiaohei")
d1.color = "blue"#增加属性
print(d1.color)
del d1.color#删除某个属性

# d1.bulk()
# d2.bulk()

