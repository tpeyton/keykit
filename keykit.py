#!/usr/bin/python
# main file for keykit

# import files
import getIP, dbFunctions, setSSH

# import Dependencies
import MySQLdb, getpass, argparse

# argparse stuff
parser = argparse.ArgumentParser(description='Retrieve SSH and system information')
# Create Arguments for getIP
parser.add_argument('-p','--publish',help='Uploads local SSH config to database',action="store_true")
parser.add_argument('-f','--find',help='search database by hostname',action="store_true")
parser.add_argument('-fI','--findIP',help='search database by ip',action="store_true")
parser.add_argument('-fF','--findFingerprint',help='search database by fingerprint',action="store_true")
parser.add_argument('-sK','--setPrivKey',help='Replace the SSH private key,action="store_true")
args = parser.parse_args()

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

### Handle argparse flags ###
# upload host info to keykit
if args.publish:
    # get details from host
    hostname = getIP.get_hostname()
    ip = getIP.get_ip_address()
    ssh_key = getIP.get_sshPrivKey()
    fingerprint = getIP.calc_sshPubFP()

    # add above details to last row in DB
    dbFunctions.addHostToDB(db,cursor,hostname,ip,fingerprint,ssh_key)

# search by hostname
if args.find:
        # search for hostname in DB and print details about it
        query = raw_input("Enter a hostname to search for: ")
        hostID = dbFunctions.searchForHost(db,cursor,"hostname",query)

        # Ensure a result was found before attempting to search the db
        if(hostID != 0):
        	result = dbFunctions.getHostFromDB(db,cursor,hostID)
        else:
        	print("No results found.")

# search by ip
if args.findIP:
        # search for hostname in DB and print details about it
        query = raw_input("Enter an IP address to search for: ")
        hostID = dbFunctions.searchForHost(db,cursor,"ip",query)

# search by fingerprint
if args.findFingerprint:
        # search for hostname in DB and print details about it
        query = raw_input("Enter a fingerprint to search for: ")
        hostID = dbFunctions.searchForHost(db,cursor,"fingerprint",query)

# set ssh keys on host
if args.setPrivKey:
    # test saving private keykit, broken currently
    hostID = raw_input("Please enter the index where the key is located: ")

    # Ensure a result was found before attempting to search the db
    if(hostID != 0):
        result = dbFunctions.getHostFromDB(db,cursor,hostID)
    else:
        print("No results found.")

    # set the server keys
    setSSH.set_sshPrivKey("{}".format(result["ssh_key"]))

# close connection to db after everything has run
db.close()
