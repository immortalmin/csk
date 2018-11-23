#Author:immortal luo
# -*-coding:utf-8 -*-
import pika
import uuid
import time

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'
        ))
        self.channel = self.connection.channel()#生成一个通道
        result = self.channel.queue_declare(exclusive=True)#随机生成一个Queue
        self.callback_queue = result.method.queue#获取Queue的名称

        self.channel.basic_consume(self.on_response,#只要一收到消息就调用on_response
                                   no_ack=True,#不保存结果
                                   queue=self.callback_queue)

    def on_response(self,ch,method,props,body):#这个函数莫非是自动调用的
        if self.corr_id == props.correlation_id:#判断收到的数据id是否与发送数据的id相同
            self.response = body

    def call(self,n):
        self.response = None#设定其初始值为None
        self.corr_id = str(uuid.uuid4())#生成一个随机字符串
        self.channel.basic_publish(exchange='',#应该是交换机类型，选择默认的（我也不知道默认的是啥）
                                   routing_key='rpc_queue',#Queue的名称
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,#进行消息传递的Queue名称
                                       correlation_id=self.corr_id,#数据的id
                                   ),
                                   body=str(n)#传送的内容
                                   )
        while self.response is None:#当没有收到回复时，循环..
            self.connection.process_data_events()#非阻塞版的start_consuming()
            print("no message...")#如果没有收到数据就打印
            time.sleep(0.5)#睡眠..
        return int(self.response)#返回收到的数据

fibonacci_rpc = FibonacciRpcClient()#生成实例

print("[x]Requesting fib(6)")
response = fibonacci_rpc.call(6)
print("[.] Got %r"% response)