#Author:immortal luo
# -*-coding:utf-8 -*-
import queue

#queue.Queue#先入先出
#queue.LifoQueue#后入先出
#queue.PriorityQueue#存储数据时可设置优先级的队列

# q = queue.Queue(maxsize=3)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(3)
# a = q.get()
# q.get(block=False)
# print(q.qsize())
# print(a)
# print(q.qsize())

q = queue.PriorityQueue()
q.put((10,"csk"))
q.put((1,"lmm"))
q.put((5,"zend"))
q.put((3,"sl"))
q.put((6,"wei"))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())