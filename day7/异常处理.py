#Author:immortal luo
# -*-coding:utf-8 -*-

# 上课 Dog:
#     def __init__(self,name):
#         self.name = name
#
# d = Dog("小黑")
# choice = input(">>:").strip()
# getattr(d,choice)
names = ["csk","lmm"]
date = {}
try:
    names[3]
    # date['name']
# except (KeyError,IndexError) as e :
#     print("Wrong:",e)
except KeyError as e :
    print("没有这个key:",e)
except IndexError as e:
    print("列表操作错误",e)
except Exception as e:
    print("未知错误:",e)
else:
    print("一切正常")
finally:
    print("不管有没有错都执行")