#Author:immortal luo
# -*-coding:utf-8 -*-
import json
#json:用于字符串和python数据类型间进行转换

#将 python 对象编码转化为 json 字符串
data = {'Citizen_Wang':1, 'Always fall in love':2, 'with neighbours.':3}
json_str = json.dumps(data)
# print('Python 原始数据是：', data)
# print('json 对象：',json_str)
# print(type(data))
# print(type(json_str))
# for i,v in enumerate(json_str):
#     print(i, v)

#将 json 格式转化为 python 格式
# date2 = json.loads(json_str)
# print(date2)
# print(type(date2))

#dump 和 dumps 的功能一样，将 dict 转化为 str 的格式，然后存入文件中。
# file = open('1.txt', 'w')
# json.dump(json_str, file)
# file.close()

#load 和 loads 的功能一样，从文件中读取 str 格式并将其转化为字符串。
# file = open('1.txt', 'r')
# print(json.load(file))

# file.close()