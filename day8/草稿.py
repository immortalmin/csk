#Author:immortal luo
# -*-coding:utf-8 -*-
import os,time

# s = "ipconfig"
# res = os.popen(s).read()
# print(res)

# filename = "hash.py"
# file_size = os.stat(filename).st_size
# print(type(file_size))
# a = time.time()
# print("起始时间：",a)
# time.sleep(0.5)
# b = time.time()
# print("结束时间：",b)
# print("时间间隔：",b-a)

# msg = input(":>>")
# if msg.startswith("get"):
#     print("Yes")
# else:
#     print("No")
# filename = "hash.py"
# if os.path.isfile(filename):
#     print("Yes")
# else:
#     print("No")
filename = "hash.py"
size = os.stat(filename).st_size
print(size)