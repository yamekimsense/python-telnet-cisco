#works
#catalyst username password
#python2

import getpass
import sys
import telnetlib
import time

HOST = "192.168.20.103"
#user = raw_input("Enter your telnet username: ")
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write("admin\n")

tn.read_until("Password: ")
tn.write("cisco\n")

#tn.write("enable\n")
#tn.write("cisco\n")
#tn.write("\n\n")

tn.write("terminal length 0\n")
tn.write("\n\n")

tn.write("show ver\n")
tn.write("\n\n")


tn.write("show ip int br\n")
tn.write("\n\n")

tn.write("show cdp nei \n")
tn.write("\n\n")

tn.write("show cdp nei det\n")
tn.write("\n\n")

tn.write("exit\n")

with open(HOST+".txt", 'w') as myfile:
    myfile.write( tn.read_all() )

