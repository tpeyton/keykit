#!/usr/bin/python

import socket
import os
import subprocess
import argparse
import math
import getIP
import setSSH

parser = argparse.ArgumentParser(description='Retrieve SSH and system information')
# Create Arguments for getIP
parser.add_argument('-cA','--checkAdmin',help='Is the current user an Administrator?',action="store_true")
parser.add_argument('-ip','--getIP',help='Get the IP of the system',action="store_true")
parser.add_argument('-H','--getHName',help='Get the Hostname of the system',action="store_true")
parser.add_argument('-k','--getPubKey',help='Get the SSH public key',action="store_true")
parser.add_argument('-f','--calcPubFP',help='Get the SSH fingerprint',action="store_true")
parser.add_argument('-PK','--getPrivKey',help='Get the SSH Private key',action="store_true")
# Create Arguments for setSSH
parser.add_argument('-sK','--setPrivKey',help'Replace the SSH private key,action="store_true")
args = parser.parse_args()




if args.checkAdmin:
        print(getIP.check_if_admin())
if args.getIP:
        print(getIP.get_ip_address())
if args.getHName:
        print(getIP.get_hostname())
if args.getPubKey:
        print(getIP.get_sshPubKey())
if args.calcPubFP:
        print(getIP.calc_sshPubFP())
if args.getPrivKey:
        print(getIP.get_sshPrivKey())
if args.setPrivKey:
        print("You called setPrivKey)
