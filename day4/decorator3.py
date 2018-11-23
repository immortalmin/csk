#Author:immortal luo
# -*-coding:utf-8 -*-

#函数即“变量”
#函数的嵌套：在一个函数的体内用def定义一个新的函数
def foo():
    print("in the foo")
    def bar():
        print("in the bar")
    bar()
foo()



