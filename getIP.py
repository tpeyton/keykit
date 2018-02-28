#!/usr/bin/python

import socket
import os
import subprocess

def check_if_admin():
    uid = os.getuid()
    if(uid != 0):
    	admin = False
    if(uid == 0):
        admin = True
    return(admin)

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_hostname():
    return(socket.gethostname())

def get_sshPubKey():
    key = subprocess.check_output('cat ~/.ssh/id_rsa.pub', shell=True)
    key = key.rstrip()
    return(key)

def calc_sshPubFP():
    fPrint = subprocess.check_output('ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub', shell=True)
    fPrint = fPrint.rstrip()
    return(fPrint)

def get_sshPrivKey():
    privKey = subprocess.check_output('cat ~/.ssh/id_rsa', shell=True)
    privKey = privKey.rstrip()
    return(privKey)
