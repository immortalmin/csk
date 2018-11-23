#Author:immortal luo
# -*-coding:utf-8 -*-
import socket

HOST = 'localhost'
PORT = 9000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    msg = bytes(input(">>:"),encoding="utf-8")
    s.sendall(msg)
    data = s.recv(2048)
    print("Recvived",repr(data))

s.close()