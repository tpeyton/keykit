#!/usr/bin/python
# main file for keykit

# import files
import getIP, dbFunctions, getpass

# import Dependencies
import MySQLdb

# initialize sql variables
dbHost = "keykit.tynet.lab"
sqlUser = raw_input("enter username: ")
sqlPasswd = getpass.getpass("enter password: ")
database = "keykit"

# connect to database using ssl
try:
    db = MySQLdb.connect(dbHost,sqlUser,sqlPasswd,database,ssl="")

# handle and print errors
except MySQLdb.Error as e:
    exit(e)

# initialize the cursor and use dict mode so we can search by column name
cursor = db.cursor(MySQLdb.cursors.DictCursor)

# TODO: remove/ reorganize the following code to be a part of the main function file
###############################################
# testing: get details from localhost
hostname = getIP.get_hostname()
ip = getIP.get_ip_address()
ssh_key = getIP.get_sshPrivKey()
fingerprint = getIP.calc_sshPubFP()

# add above test details to last row in DB
dbFunctions.addHostToDB(db,cursor,hostname,ip,fingerprint,ssh_key)

# search for hostname in DB and print details about it
hostID = dbFunctions.searchForHost(db,cursor,"hostname",hostname)

# Ensure a result was found before attempting to search the db
if(hostID != 0):
	dbFunctions.getHostFromDB(db,cursor,hostID)
else:
	print("No results found.")


# TODO: unsure if this line needs to occur at the end of each function
# close connection to db after everything has run
db.close()
