#Author:immortal luo
# -*-coding:utf-8 -*-

import socket

client = socket.socket()#声明socket类型，同时生成socket连接对象
client.connect(('localhost',9999))
while True:
    msg = input("client:").strip()
    client .send(msg.encode("utf-8"))
    data = client.recv(2048)
    print("recv:",data.decode())

client.close()