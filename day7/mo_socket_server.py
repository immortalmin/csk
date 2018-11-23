#Author:immortal luo
# -*-coding:utf-8 -*-
import socket

server = socket.socket()
server.bind(('localhost',6969))
server.listen()
conn,addr = server.accept()
while True:
    data = conn.recv(1024)
    print("收到消息:>>",data.decode("utf-8"))
    data2 = input("发送消息：>>")
    conn.send(data2.encode("utf-8"))
server.close()