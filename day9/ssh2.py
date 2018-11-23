#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko
# paramiko.util.log_to_file('/tmp/sshout')
def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
#           stdin.write("Y")   #简单交互，输入 ‘Y’
        print(stdout.read())
#        for x in  stdout.readlines():
#          print x.strip("n")
        print('%stOKn'%(ip))
        ssh.close()
    except :
        print('%stErrorn'%(ip))
ssh2("192.168.0.101","款爷","0408","hostname;ifconfig")
ssh2("192.168.0.101","款爷","0408","ifconfig")