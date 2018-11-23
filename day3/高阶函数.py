#Author:immortal luo
# -*-coding:utf-8 -*-

def abs2(x):#把一个函数当做另一个函数的参数
    if x<0:
        x = -x
    return x

def sum2(x,y,f):
    return f(x)+f(y)

a = sum2(1,-2,abs2)
print(a)