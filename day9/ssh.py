#Author:immortal luo
# -*-coding:utf-8 -*-

import paramiko

ssh = paramiko.SSHClient()#创建SSH对象
ssh.set_missing_host_key_policy((paramiko.AutoAddPolicy()))#允许连接不在know_hosts文件中的主机
ssh.connect(hostname = '192.168.57.128', port=22,username="HP",password="csk1314520")#连接服务器
stdin, stdout, stderr = ssh.exec_command('df')#执行命令
result = stdout.read()#获取命令结果
print(result.decode())
ssh.close()#关闭连接

