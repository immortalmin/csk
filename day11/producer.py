#Author:immortal luo
# -*-coding:utf-8 -*-
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()#声明一个管道
#声明queue
channel.queue_declare(queue='hello',durable=True)#队列持久化，但只是保存队列名

channel.basic_publish(exchange='',
                      routing_key='hello',#queue名字
                      body='Hello World!',
                      properties=pika.BasicProperties(#消息持久化
                          delivery_mode=2#1是非持久化
                      )
                      )
print("[x] Sent 'Hello World!'")
connection.close()