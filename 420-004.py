#python
#ssh

#sudo pip install paramiko
#run python3

import paramiko
import time


ip = "198.18.134.140"
username = "admin"
password = ""

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())


remote_conn_pre.connect(ip, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)


remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)
remote_conn.send("show clock\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output)

