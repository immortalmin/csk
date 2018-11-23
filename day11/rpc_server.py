#Author:immortal luo
# -*-coding:utf-8 -*-
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

def fib(n):#斐波那契数列的生成函数
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def on_request(ch,method,props,body):
    n = int(body)#转换数据类型
    print("[.] fib(%s)"%n)
    response = fib(n)#调用fib函数，把返回结果赋值给response
    ch.basic_publish(exchange='',#交换机，默认模式
                     routing_key=props.reply_to,#Queue名称
                     properties=pika.BasicProperties(correlation_id=\
                                                     props.correlation_id),#这句不知道啥意思
                     body=str(response))#转换数据类型
    ch.basic_ack(delivery_tag=method.delivery_tag)

# channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request,queue='rpc_queue')
print("[x] Awaiting RPC requests")
channel.start_consuming()