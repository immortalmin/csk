#Author:immortal luo
# -*-coding:utf-8 -*-

import paramiko
print("程序开始！")
transport = paramiko.Transport(('192.168.57.128',22))
print("准备连接！")
transport.connect(username='HP',password="csk13145200")
print("连接成功！")
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('hash.py','test.py')#上传
sftp.get('test.py','hash2.py')#下载

transport.close()
