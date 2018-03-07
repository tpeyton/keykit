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

<<<<<<< HEAD
# This function takes in ssh server characteristics and adds them to our database
def addHostToDB(hostname,ip,ssh_key,fingerprint):
	# sql command TODO: update this variable subsitution to best practice for python 3.1? - https://pyformat.info/
	sql = "insert into keystore(hostname, ip, ssh_fingerprint, ssh_key) VALUES('%s', '%s', '%s', '%s')" % (hostname, ip, ssh_key, fingerprint)
=======
def addHostToDB(hostname,ip,fingerprint,ssh_key):
	# sql command
	sql = "insert into keystore(hostname, ip, ssh_fingerprint, ssh_key) VALUES('%s', '%s', '%s', '%s')" % (hostname, ip, fingerprint, ssh_key)
>>>>>>> 30aee48ddd98b2a0d7827abc2b0010d6b1c1eb0c

	# execute sql command
	cursor.execute(sql)

	print(cursor.fetchall())

	# save changes to db
	db.commit()

	# close connection to db
	db.close()

# search database for queried host and return index if it exists, if not then report error and close
def searchForHost(hostname):
	# sql command using best practice variable subsitution for python 3.1
	sql = "select * from keystore where hostname ='{0}'".format(hostname)

	# execute sql command
	cursor.execute(sql)

	# store results in variables
	results = cursor.fetchall()

	# Output results
	print("index: {0} name: {1}".format(results["id"], results["hostname"]))
	return(results["id"])

# TODO: Retrieves details of host from the db, input is the index which the host is located at
def getHostFromDB(index):



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

<<<<<<< HEAD
addHostToDB(hostname,ip,ssh_key,fingerprint)

hostID = SearchForHost(hostname)
print("final id is {}".format(hostID))
=======
print(fingerprint)

addHostToDB(hostname,ip,fingerprint,ssh_key)
>>>>>>> 30aee48ddd98b2a0d7827abc2b0010d6b1c1eb0c
