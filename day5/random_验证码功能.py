#Author:immortal luo
# -*-coding:utf-8 -*-
import random

checkcode = ''
# print(random.randint(10000,99999))

for i in range(4):
    current = random.randrange(0,4)
    if(current == i):
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    checkcode += str(tmp)
print(checkcode)