#!/usr/bin/python
import MySQLdb
import socket
import os
import subprocess

# initialize sql variables
sqlUser = "keyman"
sqlPasswd = "zooper$secret"
database = "keykit"

# host data
# hostname = "test02"
# ip = "10.0.0.101"
# ssh_key = "234t3gtiwqervceqw234t3grfe234t3grf23r4tgrf32r4gf3"
#fingerprint = "oinrweoqinweroiwer"

# connect to database
db = MySQLdb.connect("localhost",sqlUser,sqlPasswd,database)

# get the cursor
cursor = db.cursor()

def addHostToDB(hostname,ip,ssh_key,fingerprint):
	# sql command
	sql = "insert into keystore(hostname, ip, ssh_fingerprint, ssh_key) VALUES('%s', '%s', '%s', '%s')" % (hostname, ip, ssh_key, fingerprint)

	# execute sql command
	cursor.execute(sql)

	print(cursor.fetchall())

	# save changes to db
	db.commit()

	# close connection to db
	db.close()

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_hostname():
    return(socket.gethostname())

def calc_sshPubFP():
    fPrint = subprocess.check_output('ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub', shell=True)
    fPrint = fPrint.rstrip()
    return(fPrint)

def get_sshPrivKey():
    privKey = subprocess.check_output('cat ~/.ssh/id_rsa', shell=True)
    privKey = privKey.rstrip()
    return(privKey)

hostname = get_hostname()
ip = get_ip_address()
ssh_key = get_sshPrivKey()
fingerprint = calc_sshPubFP()

addHostToDB(hostname,ip,ssh_key,fingerprint)
