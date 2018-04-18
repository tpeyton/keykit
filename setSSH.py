#!/usr/bin/python

import subprocess
import argparse
import getIP
import os
from pathlib import Path

# sets server private key
def set_sshPrivKey(sshKey):

	# make sure we are root
	adminStatus = getIP.check_if_admin()

	if(adminStatus == True):
		subprocess.call("mv /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_rsa_key.bak", shell=True)
		print("Backup stored successfully as /etc/ssh/ssh_host_rsa_key.bak")
		subprocess.call("echo {} > /etc/ssh/ssh_host_rsa_key".format(sshKey), shell=True)
		if(getIP.get_sshPrivKey() == sshKey):
				print("Success! The SSH private key was changed.")
		else:
				print("Error: The SSH private key was not replaced successfully.")
	else:
		print("You do not have the proper permissions to perform this command. Please re-run this command as sudo.")
