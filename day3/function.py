#Author:immortal luo
# -*-coding:utf-8 -*-
import time
def logger():
    time_format = '%Y-%m-%d'
    time_current = time.strftime(time_format)
    with open('yesterday','a+') as f:
        f.write('%s end action\n' % time_current)

def text():
    print("OK")
    logger()

text()