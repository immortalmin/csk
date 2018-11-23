#Author:immortal luo
# -*-coding:utf-8 -*-

# 上课 Foo(object):
#     def __init__(self,name):
#         self.name = name
#
# f = Foo("csk")
# print(type(f))
# print(type(Foo))

#*****************特殊方法********************
def func(self):
    print("hello",self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type('Foo',(object,),{'func':func,
                            '__init__':__init__
                            })
f = Foo("csk",19)
f.func()
#********************************************