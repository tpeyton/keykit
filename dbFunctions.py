#!/usr/bin/python

# Dependencies
import MySQLdb
import socket
import os
import subprocess

# This function takes in ssh server characteristics and adds them to our database
def addHostToDB(db,cursor,hostname,ip,fingerprint,ssh_key):
	# sql command
	sql = "INSERT INTO keystore(hostname, ip, ssh_fingerprint, ssh_key) VALUES('{0}', '{1}', '{2}', '{3}')".format(hostname,ip,fingerprint,ssh_key)

	# execute sql command
	cursor.execute(sql)

	# DEBUG: make sure data was successfully added to db
	#print(cursor.fetchall())

	# save changes to db
	db.commit()

# search database for queried host and return index if it exists, if not then report error and close
def searchForHost(db,cursor,searchType,query):
	# sql command
	sql = "SELECT * FROM keystore WHERE {0} ='{1}'".format(searchType,query)

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
def getHostFromDB(db,cursor,index):
	# sql command
	sql = "SELECT * FROM keystore WHERE id = {0}".format(index)

	# execute sql command
	cursor.execute(sql)

	# Retrieves results
	results = cursor.fetchall()

	# grab the first result
	result = results[0]

	# DEBUG: output results
	#print("index: {0} \nname: {1} \nip: {2} \nssh_fingerprint: {3} \nssh_key: {4}".format(result["id"], result["hostname"], result["ip"], result["ssh_fingerprint"], result["ssh_key"]))

	# return result for later use
	return result
