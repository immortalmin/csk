#Author:immortal luo
# -*-coding:utf-8 -*-
import math

#详情网址：https://docs.python.org/3/library/functions.html?highlight=built

# print(all([0,1,5]))#判断是否都为真
# print(any([0,0,1]))#判断是否存在真
# print(ascii([1,2,3]))#使其变成字符串，输出[1,2,3]
# print(bin(12))#把数字转成二进制
# print(bool(12))#判断真假
# print(chr(97))#转char a
# print(ord('a'))#转数字97
# print(ord('a'))#转数字97
# code = '''
# for i in range(10):
#     print(i)
# '''
# py_obj = compile(code, "err.log", "exec")#使一段字符串变成一段可执行的代码，并运行  1
# exec(py_obj) #  1
# exec(code)#  2,直接exec()更方便
# print(dir(code))#返回对象可使用的方法
# print(divmod(5,2))#返回商和余数

# a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"#将字符串str当成有效的表达式来求值并返回计算结果
# b = eval(a)
# print(b[0])

#匿名函数：
# def calc(n):#1
#     print(n)
# calc(5)
#
# calc = lambda n:print(n)#2
# calc(5)
#
# (lambda n:print(n))(5)#3

#函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回True或False，
#最后将返回True的元素放到迭代器中（python2中返回新的列表）。
# def is_odd(n):
#     return n % 2 == 1
# newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# for i in newlist:
#     print(i)

#map() 会根据提供的函数对指定序列做映射。
#第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的迭代器。
# res = map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
# for i in res:
#     print(i)

#reduce() 函数会对参数序列中元素进行累积。
#函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对
#集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# import functools
# a =functools.reduce(lambda x, y: x+y, [1,2,3,4,5])
# print(a)
# print(round(1.2356,2))#保留两位有效数字

# a = {1:5,5:6,2:8}
# print(sorted(a.items()))#排序字典（按key排序）
# print(sorted(a.items(),key=lambda x:x[1]))#排序字典（按value排序）

#拉链，把两个列表组合成一个字典
# a = [1,2,3,4]
# b = ['a','b','c','d']
# for i in zip(a,b):
#     print(i)

