#Author:immortal luo
# -*-coding:utf-8 -*-
import socket

server = socket.socket()
server.bind(('localhost',6969))#绑定要监听端口
server.listen(5)#监听
print("我要开始等电话了")
conn,addr = server.accept()#等电话打进来
# print(conn)
# print(addr)
#conn就是客户端连过来而在服务端为其生成的一个连接实例
print("电话来了")
while True:
    data = conn.recv(1024)
    print("recv:",data.decode())
    data2 = input(">>:")
    conn.send(data2.encode("utf-8"))

server.close()