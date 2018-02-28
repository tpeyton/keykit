#!/usr/bin/python
import MySQLdb

# initialize sql variables
sqlUser = "keyman"
sqlPasswd = "zooper$secret"
database = "keykit"

# host data
hostname = "test02"
ip = "10.0.0.101"
ssh_key = "234t3gtiwqervceqw234t3grfe234t3grf23r4tgrf32r4gf3"
fingerprint = "oinrweoqinweroiwer"

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

addHostToDB(hostname,ip,ssh_key,fingerprint)
