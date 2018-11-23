#Author:immortal luo
# -*-coding:utf-8 -*-

# def test(x,y):
#     print(x)
#     print(y)
#
# test(1,2)
#位置函数必须在啥函数之前
# 默认参数
# def test2(*args):#*args表示参数个数不确定
#     print(args)
#
# test2(1,2,3,4,5)
# test2(*[1,2,3,4,5])
# def test(**kwargs):#把N个关键字参数转化成字典
#     print(kwargs)
#     print(kwargs['name'])
#     print(kwargs['age'])
#
# test(name = "csk",age = 19)
name = "chen"
def change_name():
    # global name#使局部变量变成全局变量
    name = "luomin"
    print(name)

change_name()
print(name)