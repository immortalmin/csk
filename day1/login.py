#Author:immortal luo
import getpass

_username = 'csk'
_password = '123456'
user = input("请输入用户名：")
pwd = input("请输入密码：")
if user == _username and pwd == _password:
    print("welcome user %s login"% user)
else:
    print("wrong username or password")