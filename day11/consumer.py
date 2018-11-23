#Author:immortal luo
# -*-coding:utf-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'
))
channel = connection.channel()
channel.queue_declare(queue='hello',durable=True)

def callback(ch,method,propertise,body):
    print("[x] Received %r"%body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(#消费信息
                      callback,#如果收到消息，就调用CALLBACK函数来处理消息
                      queue='hello',
                      no_ack=True#是否保证消息完全传送
                      )

print('[*] Waiting for messages.To exit press CTRL+C')
channel.start_consuming()