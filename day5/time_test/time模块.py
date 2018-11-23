#Author:immortal luo
# -*-coding:utf-8 -*-
import time

# x = time.localtime()
# print(time.localtime())#将一个时间戳转换为当前时区的struct_time
# print(time.gmtime())#和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time
# print(time.time())#返回当前时间的时间戳
# print(time.mktime(x))#将一个struct_time转化为时间戳
# time.sleep(1)#线程推迟指定的时间运行。单位为秒
# print(time.asctime(x))#把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。如果没有参数，将会将time.localtime()作为参数传入。
# print(time.ctime())#同上，转化时间戳

#格式化时间
# y = time.strftime("%Y-%m-%d %H:%M:%S",x)
# print(y)

# 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
# z = time.strptime(y,"%Y-%m-%d %H:%M:%S")
# print(z)


import datetime
print(datetime.datetime.now())#获取当前时间
print(datetime.datetime.now()+datetime.timedelta(days=3))#获取三天后的时间（时间加减）

#时间替换
x = datetime.datetime.now()
print(x.replace(minute=3))
