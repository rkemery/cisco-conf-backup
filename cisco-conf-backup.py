#  ----------------------
# | cisco configuration backup
# | by rick kemery
# | will login to a cisco switch or router and save the configuration to a file
# | modify USER, PASSWORD, secret, ip, and filename_prefix to your liking
# | install paramiko: pip install paramiko
#  ----------------------
import sys
import time
import paramiko 
import os
import cmd
import datetime

now = datetime.datetime.now()

USER = 'enter username here'
PASSWORD = 'enter password here'
secret = 'enter secret here'
ip = 'enter ip address of device'
filename_prefix ='C:/Users/cooluser/Documents/CiscoConfBackup/' + ip
	
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, username=USER, password=PASSWORD)

chan = client.invoke_shell()
time.sleep(2)
chan.send('en\n')
chan.send(secret +'\n')
time.sleep(1)
chan.send('term len 0\n')
time.sleep(1)
chan.send('sh run\n')
time.sleep(30)
output = chan.recv(999999)
print (output)
filename = "%s_%.2i%.2i%i_%.2i%.2i%.2i" % (filename_prefix,now.year,now.month,now.day,now.hour,now.minute,now.second)
ff = open(filename, 'a')
ff.write(output.decode("utf-8") )
ff.close()
###close ssh session
client.close() 
print (ip)