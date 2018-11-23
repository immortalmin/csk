#Author:immortal luo
# -*-coding:utf-8 -*-
import pika
# Broker:它提供一种传输服务,它的角色就是维护一条从生产者到消费者的路线，保证数据能按照指定的方式进行传输,
# vhost:虚拟主机,一个broker里可以有多个vhost，用作不同用户的权限分离。

conneection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))

# Channel:消息通道,在客户端的每个连接里,可建立多个channel.
channel = conneection.channel()

# Exchange：消息交换机,它指定消息按什么规则,路由到哪个队列。
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# Queue:消息的载体,每个消息都会被投到一个或多个队列。
result = channel.queue_declare(exclusive=True)#随机创建一个Queue,程序结束后自动删除
queue_name = result.method.queue#获取刚创建的Queue的名称

# Binding:绑定，它的作用就是把exchange和queue按照路由规则绑定起来.
channel.queue_bind(exchange='logs',
                   queue=queue_name)
print("[*] Waiting for logs.To exit press CTRL+C")

def callback(ch,method,properties,body):
    print("[x] %r"%body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()