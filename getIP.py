#!/usr/bin/python

import socket
import os
import subprocess

def check_if_admin(): #returns a boolean value whether or not the script is being run as root
    uid = os.getuid()
    if(uid != 0):
    	admin = False
    if(uid == 0):
        admin = True
    return(admin)

def get_ip_address(): #returns the current IP address as a string
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_hostname(): #returns the current hostname as a string
    return(socket.gethostname())

def get_sshPubKey(): #returns the SSH Public key as a string
    key = subprocess.check_output('cat /etc/ssh/ssh_host_rsa_key.pub', shell=True)
    key = key.rstrip()
    return(key)

def calc_sshPubFP(): #returns the SSH fingerprint as a string
    fPrint = subprocess.check_output('ssh-keygen -E md5 -lf /etc/ssh/ssh_host_rsa_key.pub', shell=True)
    fPrint = fPrint.rstrip()
    return(fPrint)

def get_sshPrivKey(): #returns the SSH Private key as a string
    privKey = subprocess.check_output('cat /etc/ssh/ssh_host_rsa_key', shell=True)
    privKey = privKey.rstrip()
    return(privKey)
