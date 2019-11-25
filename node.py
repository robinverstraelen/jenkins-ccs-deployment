import paramiko
import os

class node:
    def __init__(self, ip):
        self.ip = ip
        k = paramiko.RSAKey.from_private_key_file("private.key")
        self.c = paramiko.SSHClient()
        self.c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.c.connect( hostname = ip, username = "cliqruser", pkey = k )
        print("connected to " + ip)
    
    def executeCommand(self, command):
        stdin, stdout, stderr = self.c.exec_command("sudo -s " + command)
        stdout.channel.recv_exit_status()