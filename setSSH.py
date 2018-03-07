#!/usr/bin/python

import socket
import os
import subprocess
import argparse
import getIP
from pathlib import Path

adminStatus = getIP.check_if_admin()
backupFile = Path("~/.ssh/id_rsa.bak")

def set_sshPrivKey(sshKey):
        if(adminStatus == True):
                subprocess.run("mv ~/.ssh/id_rsa ~/.ssh/id_rsa.bak", shell=True)
                if(backupFile.is_file()):
                        subprocess.run("echo", sshKey, ">", "~/.ssh/id_rsa.bak")
                        if(getIP.get_sshPrivKey() == sshKey):
                                print("Success.")
                else:
                        print("Error creating backup. Please try again.")
        else:
                print("You do not have the proper permissions to perform this command. Please re-run t$

set_sshPrivKey("test")
