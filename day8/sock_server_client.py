#Author:immortal luo
# -*-coding:utf-8 -*-
import socket

client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input(">>:").strip()
    if len(cmd)==0:
        continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(2048)#接受命令结果的长度
    print("命令结果：",cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(2048)
        received_size += len(data)#每次收到的有可能小于2048，所以必须用len判断
        print(data.decode())
        received_data+=data
    else:
        print("cmd_res receive done...",received_size)
        print(received_data.decode())
client.close()