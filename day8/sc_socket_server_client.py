#Author:immortal luo
# -*-coding:utf-8 -*-
import socket,hashlib
import time
client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input(">>:").strip()#输入文件名
    if len(cmd)==0:#输入为空，则继续输入
        continue
    if cmd.startswith("get"):#判断是否以"get"开头
        client.send(cmd.encode())#发送需要传送的文件名
        server_response = client.recv(2048)#接收文件的大小
        print("server response:",server_response)
        client.send(b"ready to recv file")#发送准备好接收文件的消息
        file_total_size = int(server_response.decode())#转化格式
        received_size = 0#表示传输完成的文件大小
        filename = cmd.split()[1]#提取文件名
        f = open(filename + ".new",'wb')#新建一个文件
        m = hashlib.md5()#新建一个hash
        time_begin_1 = time.time()
        while received_size < file_total_size:#当传输完成的文件大小小于需要传输的文件总大小，则继续传输剩余内容
            if file_total_size - received_size > 2048:#表示剩余的文件大小大于一次最多可以传输的文件大小，还要传输不止一次
                size = 2048#size表示单次传输文件的大小
            else:#最后一次了，剩多少，传输多少
                size = file_total_size - received_size#剩下的文件大小
                print("last size:",size)
            data = client.recv(size)#接收文件
            received_size +=len(data)#累加
            m.update(data)#存入hash
            f.write(data)#写入文件中
        else:
            new_file_md5 = m.hexdigest()#转换进制（转成16进制好像）
            print("file recv done")
            f.close()#关闭文件
            time_end_1 = time.time()
        time_begin_2 = time.time()
        server_file_md5 = client.recv(2048)#接收hash传送的内容
        time_end_2 = time.time()
        print("server file md5",server_file_md5)#表示通过一行行传送的文件内容
        print("client file md5",new_file_md5)#表示通过传送hash的文件内容
        print("通过一行行传输文件的时间：",time_end_1-time_begin_1)
        print("通过传输hash文件的时间：",time_end_2-time_begin_2)
        if time_end_1-time_begin_1 > time_end_2-time_begin_2:
            print("第二种方法快")
        else:
            print("第一种方法快")
client.close()