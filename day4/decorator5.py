#Author:immortal luo
# -*-coding:utf-8 -*-
import time
user,passwd='csk','123'
def auth(func):
    def wrapper(*args,**kwargs):
        username = input("Username:").strip()
        password = input("Password:").strip()
        if user == username and passwd ==password:
            print("\033[32;1mUser has passed authentication\033[0m")
            func(*args,**kwargs)
        else:
            exit("\033[31;1mInvalid username or password\033[0m")
    return wrapper

@auth
def index():
    print("welcome to index page")

@auth
def home():
    print("welcome to index page")

@auth
def bbs():
    print("welcome to index page")

index()
home()
bbs()
