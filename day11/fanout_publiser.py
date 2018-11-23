#Author:immortal luo
# -*-coding:utf-8 -*-

import pika
import sys

# Broker:它提供一种传输服务,它的角色就是维护一条从生产者到消费者的路线，保证数据能按照指定的方式进行传输,
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.57.128'
))

# Channel:消息通道,在客户端的每个连接里,可建立多个channel.
channel = connection.channel()

#Exchange:消息交换机,它指定消息按什么规则,路由到哪个队列
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)
# message = ' '.join(sys.argv[1:]) or "info:Hello World!"
message = "info:Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',#路由关键字,exchange根据这个关键字进行消息投递
                      body=message
                      )
print("[x] Sent %r"%message)
connection.close()