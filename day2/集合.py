#Author:immortal luo
# -*-coding:utf-8 -*-

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)
# print(list_1,type(list_1))
list_2 = set([2,6,0,66,22,8,4])
# print(list_1.intersection(list_2))#交集&
# print(list_1.union(list_2))#并集|
# print(list_1.difference(list_2))#差集（我有你没有）-
# print(list_1.issubset(list_2))#是否是子集
# print(list_1.issuperset(list_2))#判断是否是父集
# print(list_1.symmetric_difference(list_2))#对称差集（并集去掉交集）^
# print(list_1.isdisjoint(list_2))#判断是否有交集
# print(9 in list_1)判断元素是否在列表里
# list_1.remove(9);#删除元素
# list_1.add(99)#增加元素
# list_1.update([888,777,555])#可能是增加列表
# list_1.pop()#据说是删除最后一个元素，可我自己试验后是删除第一个元素
# list_1.discard(99)#和remove效果差不多，区别在于删除不存在的元素时不会报错
print(list_1)