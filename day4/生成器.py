#Author:immortal luo
# -*-coding:utf-8 -*-

# print([i*2 for i in range(10)])
# print((i*2 for i in range(10)))
c=(i*2 for i in range(10))#生成器:只有在调用时才会生成相应的数据，只记住当前的位置，省内存
# a=[i*2 for i in range(10)]
# print(len(a))
# for i in c:
#     print(i)
# print(c.__next__())#取下一个值
def fib(max):#函数生成器
    n,a,b = 0,0,1
    while n<max:
        # print(b)
        yield b##
        a,b=b,a+b
        n+=1
    return 'done'
f = fib(10)
while True:#捕捉异常
    try:
        x = next(f)
        print("g:",x)
    except StopIteration as e:
        print("Generator return value:",e.value)
        break
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(fib(10))