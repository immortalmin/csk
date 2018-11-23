#Author:immortal luo
# -*-coding:utf-8 -*-

# data = open("yesterday",encoding="utf-8").read()
f = open("yesterday",'r+',encoding="utf_8")#文件句柄（内存对象）#r：只读;w：只写;a：追加;r+：读写（追加）;w+：写读
# data = f.read()
# print(data)
# f.write("你是傻逼2")
# print(f)
# print(f.readlines())
# for index,line in enumerate(f.readlines()):#获取下标
#     if index == 4:
#         print(line)
# for line in f:#逼格高一点
#     print(line)
# print(f.read(5))#读5个字符
# print(f.tell())#打印当前光标位置
# f.seek(0)#移动光标
# print(f.encoding)#打印文件编码
# print(f.flush())#强制刷新
# f.truncate(20)#从开头截断20个字符
f.write("123")
f.close()