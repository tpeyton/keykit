#!/usr/bin/python

import subprocess
import getIP
import os

# sets server private key
def set_sshPrivKey(sshKey):

	# make sure we are root
	adminStatus = getIP.check_if_admin()

	# exit script if we aren't root
	if(adminStatus != True):
		exit("You do not have the proper permissions to perform this command. Please re-run this command as sudo.")

	# store backup copy
	os.rename("/etc/ssh/ssh_host_rsa_key","/etc/ssh/ssh_host_rsa_key.bak")
	print("Backup stored successfully as /etc/ssh/ssh_host_rsa_key.bak")

	# open key file for writing
	keyFile = open("/etc/ssh/ssh_host_rsa_key", "a")

	# write key to file
	keyFile.write("{}\n".format(sshKey))
