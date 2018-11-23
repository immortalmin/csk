#Author:immortal luo
# -*-coding:utf-8 -*-
from collections import Iterable
from collections import Iterator
#Iterable 可迭代对象
#Iterator 迭代器
# print(isinstance([],Iterable))#判断是否是可迭代对象
a = [1,2,3]
a = iter(a)#使可迭代对象转化成迭代器，即Iterable->Iterator
# print(isinstance(a,Iterator))#判断是否是迭代器
# print(a)
print(range(10))#输出range(0, 10)