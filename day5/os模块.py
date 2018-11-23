#Author:immortal luo
# -*-coding:utf-8 -*-
import os
#提供对操作系统进行调用的接口

# print(os.getcwd())#获取当前工作目录
# os.chdir(dirname)#改变工作目录到dirname，os.chdir("c://csk")或os.chdir(r"c:/csk")
# print(os.curdir)#返回当前目录（'.'）
# print(os.pardir)#获取当前目录的父目录字符串名
# os.makedirs(r"c:\a\b\c\d")#可生成多层递归目录
# os.mkdir(name)#创建单级目录
# os.removedirs(name)#若目录为空，则删除，并递归到上一层，若也为空，则删除，以此类推
# os.rmdir(name)#删除单级空目录，若目录不为空则无法删除，报错
# print(os.listdir("."))#返回指定目录下的所有文件和目录名
# print(os.sep)#输出操作系统特定的路径分隔符
# print(os.linesep)#输出当前平台使用的行终止符
# print(os.pathsep)#输出用于分割文件路径的字符串
# print(os.environ)#查看系统环境变量
# print(os.name)#输出当前使用的平台
# os.system("pip list")#运行shell
# os.path.abspath("")#获取文件的绝对路径