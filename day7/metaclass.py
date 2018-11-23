#Author:immortal luo
# -*-coding:utf-8 -*-

class MyType(type):
    def __init__(self,what,bases=None,dict=None):
        print("----MyType init----")
        super(MyType,self).__init__(what,bases,dict)

    def __call__(self, *args, **kwargs):
        print("--MyType call--")
        obj = self.__new__(self,*args,**kwargs)
        self.__init__(obj,*args,**kwargs)


class Foo(object):
    __metaclass__ = MyType
    def __init__(self,name):
        self.name = name
        print("Foo __init__")

    def __new__(cls, *args, **kwargs):#用来创建实例
        print("Foo __new__")
        return object.__new__(cls)#继承父亲的__new__方法

f = Foo("csk")