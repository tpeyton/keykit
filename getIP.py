#!/usr/bin/python

import socket
import os

def get_ip_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]
def get_hostname():
	return(socket.gethostname())
def get_sshPubKey():
	key = os.system('cat ~/.ssh/id_rsa.pub')
	return(key)
def calc_sshPubFP():
	fPrint = os.system('ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub')
	return(fPrint)
def get_sshPrivKey():
	privKey = os.system('cat ~/.ssh/id_rsa')
	return privKey	

print(get_ip_address())
print(get_hostname())
print(get_sshPubKey())
print(calc_sshPubFP())
print(get_sshPrivKey())


