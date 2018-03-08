#!/usr/bin/python

import subprocess
import argparse
import getIP
import os
from pathlib import Path

adminStatus = getIP.check_if_admin()

def set_sshPrivKey(sshKey):
	if(adminStatus == True):
		subprocess.call("mv ~/.ssh/id_rsa ~/.ssh/id_rsa.bak", shell=True)
		print("Backup stored successfully as ~/.ssh/id_rsa.bak")
		subprocess.call("echo {} > ~/.ssh/id_rsa".format(sshKey), shell=True)
		if(getIP.get_sshPrivKey() == sshKey):
				print("Success! The SSH private key was changed.")
		else:
				print("Error: The SSH private key was not replaced successfully.")
	else:
		print("You do not have the proper permissions to perform this command. Please re-run this command as sudo.")




