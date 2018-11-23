#Author:immortal luo
# -*-coding:utf-8 -*-
import re
#*************************************
def chengchu(stri):
    rr1 = re.split("[*/]",stri)#数字
    rs1 = re.split("[0-9.]+",stri)#符号
    rs1.pop()
    rs1.pop(0)
    sum1 = float(rr1[0])
    rr1.pop(0)
    le1 = len(rr1)
    for i in range(le1):
        if rs1[i]=='*':
            sum1=sum1*float(rr1[i])
        else:
            sum1=sum1/float(rr1[i])
    return sum1
#
def jiajian(stri):
    rr2 = re.split("[+-]", stri)  # 数字
    rs2 = re.split("[0-9.]+", stri)  # 符号
    rs2.pop()
    rs2.pop(0)
    sum2 = float(rr2[0])
    rr2.pop(0)
    le2 = len(rr2)
    for i in range(le2):
        if rs2[i] == '+':
            sum2 = sum2 + float(rr2[i])
        else:
            sum2 = sum2 - float(rr2[i])
    return sum2

def xiao(stri):#5*5+1
    res = re.findall("[0-9]+[*/.0-9]+[0-9]+",stri)
    k=0
    for i in res:
        k+=1
        if '*' in i or '/' in i:
            res2 = chengchu(i)
            stri = re.sub("[0-9]+[*/.0-9]+[0-9]+", str(res2), stri, count=k)
    a = jiajian(stri)
    return a
#*********************************************




#******************
s = "((5*5+1)-(1*4/2))"
while '(' in s or ')' in s or '+' in s or '-' in s or '*' in s or '/' in s :
    res = re.findall("[(]([0-9-+.*/]*)[)]",s)
    for i in res:
        res1 = xiao(i)
        s = re.sub("[(]([0-9-+.*/]*)[)]", str(res1), s,count=1)
    print(s)

#***********************

# res = re.findall("[(]([0-9-+.*/]*)[)]",s)
# for i in res:
    # res1 = xiao(i)
    # s = re.sub("[(]([0-9-+.*/]*)[)]", str(res1), s,count=1)
    # print(type(i))
#5*5+1
#1*4/2
# print(xiao("5*5+1"))
# print(xiao("5*5+1"))
