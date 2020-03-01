#python2
#snmp walk

import os
import sys

rc = os.system('snmpwalk -v 1 -c public 192.168.20.102 > /Users/wansookim/PycharmProjects/420-telnet/102v1python.txt')