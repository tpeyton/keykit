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

# initialize the cursor and use dict mode so we can search by column name
cursor = db.cursor(MySQLdb.cursors.DictCursor)

# This function takes in ssh server characteristics and adds them to our database
def addHostToDB(hostname,ip,fingerprint,ssh_key):
	# sql command TODO: update this variable subsitution to best practice for python 3.1? - https://pyformat.info/
	sql = "INSERT INTO keystore(hostname, ip, ssh_fingerprint, ssh_key) VALUES('%s', '%s', '%s', '%s')" % (hostname, ip, fingerprint, ssh_key)

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
	sql = "SELECT * FROM keystore WHERE hostname ='{0}'".format(hostname)
	#sql = "SELECT * FROM keystore WHERE hostname ='test'"

	# execute sql command
	cursor.execute(sql)

	# store results in variables
	results = cursor.fetchall()

	# we only care about the first result so let's filter to that
	result = results[0]

	# TODO: handle empty results

	# DEBUG: Output results
	#print("index: {0} name: {1}".format(result["id"], result["hostname"]))

	# Return ID
	return(result["id"])

# Retrieves details of host from the db, input is the index which the host is located at
def getHostFromDB(index):
	# sql command
	sql = "SELECT * FROM keystore WHERE id = {0}".format(index)

	# execute sql command
	cursor.execute(sql)

	results = cursor.fetchall()

	# grab the first result
	result = results[0]

	# output results
	print("index: {0} \nname: {1} \nip: {2} \nssh_fingerprint: {3} \nssh_key: {4}".format(result["id"], result["hostname"], result["ip"], result["ssh_fingerprint"], result["ssh_key"]))

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

# hostname = get_hostname()
hostname = "test"
ip = get_ip_address()
ssh_key = get_sshPrivKey()
fingerprint = calc_sshPubFP()

#addHostToDB(hostname,ip,fingerprint,ssh_key)

hostID = searchForHost(hostname)
print("final id is {}".format(hostID))
getHostFromDB(hostID)
