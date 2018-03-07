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

# This function takes in ssh server characteristics and adds them to our database
def addHostToDB(hostname,ip,ssh_key,fingerprint):
	# sql command TODO: update this variable subsitution to best practice for python 3.1? - https://pyformat.info/
	sql = "INSERT INTO keystore(hostname, ip, ssh_fingerprint, ssh_key) VALUES('%s', '%s', '%s', '%s')" % (hostname, ip, ssh_key, fingerprint)

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
	sql = "SELECT * FROM keystore WHERE hostname ="{0}"".format(hostname)

	# execute sql command
	cursor.execute(sql)

	# store results in variables
	results = cursor.fetchall()

	# TODO: handle empty results

	# Output results
	print("index: {0} name: {1}".format(results["id"], results["hostname"]))
	return(results["id"])

# TODO: Retrieves details of host from the db, input is the index which the host is located at
def getHostFromDB(index):
	# sql command
	sql = "SELECT body FROM keystore WHERE id = {0}".format(index)

	# execute sql command
	cursor.execute(sql)

	result = cursor.fetchall()

	# output results
	print("index: {0} \nname: {1} \nip: {2} \nssh_fingerprint: {3} \nssh_key: {4}".format(results["id"], results["hostname"], results["ip"], results["ssh_fingerprint"], results["ssh_key"]))

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

hostID = SearchForHost(hostname)
print("final id is {}".format(hostID))
print("Details for " + hostID)
getHostFromDB(hostID)
