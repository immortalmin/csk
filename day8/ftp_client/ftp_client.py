#Author:immortal luo
# -*-coding:utf-8 -*-
import socket,os,json
client = socket.socket()
client.connect(("localhost",9999))

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg = '''
        ls
        ped
        cd../..
        get filename
        put filename
        '''
    def connect(self,ip,port):
        self.client.connect((ip,port))

    def interactive(self):
        while True:
            cmd = input(">>:").strip()
            if len(cmd)==0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,"cmd_%s"%cmd_str):
                func = getattr(self,"cmd_%s"%cmd_str)
                func(cmd)
            else:
                self.help()

    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action":"put",
                    "filename":filename,
                    "size":filesize
                }
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                #防止粘包，等待服务器确认
                server_response = self.client.recv(2048)
                f = open(filename,'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print("文件传送完毕")
                f.close()
            else:
                print(filename,"is not exist")
    def cmd_get(self):
        pass

ftp = FtpClient()
ftp.connect("localhost",9999)
ftp.interactive()