#! /usr/bin/env python
import os
import sys
import subprocess
import smtplib

from email.mime.text import MIMEText

#
#IP File
#
FILE = ''
#
#SMTP Options
#
EMAIL = ''
SMTPHOST = ''
SENDER = ''
#
#SCP Options
#
#RSERVER = ''
#RPATH = ''
#RUSER = ''
#SCPCOM = 'scp '+FILE+' '+RUSER+'@'+RSERVER+':'+RPATH

#test output
#print "Your current IP is: "
try:
	ipfile = open(FILE, 'r+')
except:
	print "file not found"
	exit(1)
currentip = ipfile.readline()
print (currentip)
#
#use a subprocess to query your
#current IP and place it into
#a string
#
proc = subprocess.Popen(["curl http://ifconfig.me/ip"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#test output
#print str(out)
#
#Check if IP has changed
#
if currentip != out:
	#print ("your ip has changed")
	ipfile.seek(0)
	ipfile.write(out)
	#
	#send email
	#
	msg = MIMEText(out)
	msg['Subject'] = 'Your IP has changed'
	msg['From'] = 'Host'
	msg['To'] = EMAIL
	s = smtplib.SMTP(SMTPHOST)
	s.sendmail(SENDER, [EMAIL], msg.as_string())
	s.quit()
	#
	#Send file with SCP
	#
	#os.system(SCPCOM)
else:
	#print ("Your ip has not changed")
#
#Close file
#
ipfile.close()
