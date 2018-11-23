#Author:immortal luo
# -*-coding:utf-8 -*-

class CSkException(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    raise CSkException("我的异常")
except CSkException as e:
    print(e)