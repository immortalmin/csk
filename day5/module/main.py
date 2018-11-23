#Author:immortal luo
# -*-coding:utf-8 -*-
# import module_csk
import sys,os

# print(module_csk.name)
# module_csk.say_hello("csk2")
print(sys.path)#打印查找路径
print(os.path.abspath(__file__))#打印当前文件的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))#获取目录名
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#再上一层
x = os.path.dirname(os.path.abspath(__file__))
sys.path.append(x)#追加路径
sys.path.insert(1,x)#在第一个位置加入路径
print(sys.path)#打印查找路径