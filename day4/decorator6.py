#Author:immortal luo
# -*-coding:utf-8 -*-
import time
user,passwd='csk','123'
def auth(auth_type):
    print("auth_func:",auth_type)
    def outter_wrapper(func):
        def wrapper(*args,**kwargs):
            username = input("Username:").strip()
            password = input("Password:").strip()
            if user == username and passwd ==password:
                print("\033[32;1mUser has passed authentication\033[0m")
                func(*args,**kwargs)
                return func
            else:
                exit("\033[31;1mInvalid username or password\033[0m")
        return wrapper
    return outter_wrapper
@auth(auth_type="local")
def index():
    print("welcome to index page")

# @auth
# def home():
#     print("welcome to index page")
#
# @auth
# def bbs():
#     print("welcome to index page")

index()
