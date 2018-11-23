#Author:immortal luo
# -*-coding:utf-8 -*-
import socket
client = socket.socket()
client.connect(('localhost',6969))
while True:
    msg = input("发送消息:>>").strip()
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print("收到新消息:>>",data.decode("utf-8"))
client.close()