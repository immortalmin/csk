#Author:immortal luo
# -*-coding:utf-8 -*-
import socket,os,hashlib
server = socket.socket()
server.bind(('localhost',9999))
server.listen()
while True:
    conn,addr = server.accept()#等待客户端
    print("new conn:",addr)#输出客户端IP地址
    while True:
        print("等待新命令")
        data = conn.recv(2048)#接收从客户端发来的指令（文件名）
        if not data:#如果接收到的是空数据，则表示与该客户端已断开
            print("客户端已断开")
            break
        cmd,filename = data.decode().split()#把收到的文件名以空格符切片
        print(filename)
        if os.path.isfile(filename):#如果文件名存在
            f = open(filename,"rb")#以二进制形式打开文件名为filename的文件
            m = hashlib.md5()#创建一个hashlib啥啥，存东西用的吧
            file_size = os.stat(filename).st_size#获取文件的大小
            conn.send(str(file_size).encode())#把文件的大小发送给客户端
            conn.recv(2048)#等待客户端的回复
            for line in f:#循环文件，一行行传送
                m.update(line)#存入hash
                conn.send(line)#传送到客户端
            print("file md5",m.hexdigest())#打印存入hash中的内容
            f.close()#关闭文件
            conn.send(m.hexdigest().encode())#传送hash中的内容
        print("send done")#传输完成

server.close()