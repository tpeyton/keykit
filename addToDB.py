#!/usr/bin/python

# Dependencies
import MySQLdb
import socket
import os
import subprocess

# file imports
import getIP

# initialize sql variables
sqlUser = "keyman"
sqlPasswd = "zooper$secret"
database = "keykit"

# test data
#hostname = "test02"
#ip = "10.0.0.101"
#ssh_key = "234t3gtiwqervceqw234t3grfe234t3grf23r4tgrf32r4gf3"
#fingerprint = "oinrweoqinweroiwer"

# connect to database
db = MySQLdb.connect("localhost",sqlUser,sqlPasswd,database,ssl="")

# initialize the cursor and use dict mode so we can search by column name
cursor = db.cursor(MySQLdb.cursors.DictCursor)

# TODO: Consolidate the following sql related functions to avoid repeating all the duplicate code
# This function takes in ssh server characteristics and adds them to our database
def addHostToDB(hostname,ip,fingerprint,ssh_key):
	# sql command
	sql = "INSERT INTO keystore(hostname, ip, ssh_fingerprint, ssh_key) VALUES('{0}', '{1}', '{2}', '{3}')".format(hostname,ip,fingerprint,ssh_key)

	# execute sql command
	cursor.execute(sql)

	# DEBUG: make sure data was successfully added to db
	print(cursor.fetchall())

	# save changes to db
	db.commit()

# search database for queried host and return index if it exists, if not then report error and close
def searchForHost(hostname):
	# sql command
	sql = "SELECT * FROM keystore WHERE hostname ='{0}'".format(hostname)

	# execute sql command
	cursor.execute(sql)

	# store results in variables
	results = cursor.fetchall()

	# Check to see if search found any results
	if(cursor.rowcount > 0):
		# we only care about the first result so grab that
		result = results[0]

		# DEBUG: Output results
		#print("index: {0} name: {1}".format(result["id"], result["hostname"]))

		# Return ID
		return(result["id"])
	# Handle no results found
	else:
		return(0)

# Retrieves details of host from the db, input is the index which the host is located at
def getHostFromDB(index):
	# sql command
	sql = "SELECT * FROM keystore WHERE id = {0}".format(index)

	# execute sql command
	cursor.execute(sql)

	# Retrieves results
	results = cursor.fetchall()

	# grab the first result
	result = results[0]

	# output results (will later return variables)
	print("index: {0} \nname: {1} \nip: {2} \nssh_fingerprint: {3} \nssh_key: {4}".format(result["id"], result["hostname"], result["ip"], result["ssh_fingerprint"], result["ssh_key"]))

# testing: get details from localhost
hostname = getIP.get_hostname()
ip = getIP.get_ip_address()
ssh_key = getIP.get_sshPrivKey()
fingerprint = getIP.calc_sshPubFP()

# add above test details to last row in DB
addHostToDB(hostname,ip,fingerprint,ssh_key)

# search for hostname in DB and print details about it
hostID = searchForHost(hostname)

# Ensure a result was foun before attempting to search the db
if(hostID != 0):
	getHostFromDB(hostID)
else:
	print("No results found.")

# close connection to db
db.close()
