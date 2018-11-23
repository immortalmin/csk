#Author:immortal luo
# -*-coding:utf-8 -*-

#__doc__:表示类的描述信息
# 上课 Foo:
#     '''描述类信息'''
# print(Foo.__doc__)

#__module__:表示当前操作的对象所在的那个模块

#__class__:表示当前操作的对象的类是什么

#__init__:构造方法，通过类创建对象时，自动触发执行

#__del__:析构方法，当对象在内存中释放时，自动触发执行

#__call__:对象后面加括号，触发执行
# 上课 Foo:
#     def __init__(self):
#         print("执行__init__方法")
#
#     def __call__(self, *args, **kwargs):
#         print("执行__call__方法")
# obj = Foo()
# obj()

#__dict__:查看类或对象中的所有成员

#__str__：如果一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值
# 上课 Foo:
#     def __str__(self):
#         return "aaa"
# obj = Foo()
# print(obj)
