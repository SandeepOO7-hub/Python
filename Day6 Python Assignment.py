Q:- Email sending using python.


Ans:-


# Sending emails with attachments using Python  

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "email_address_of_the_sender"
toaddr = "email_address_of_the_receiver"

# MIMEMultipart 
msg = MIMEMultipart() 

# senders email address 
msg['From'] = fromaddr 

# receivers email address 
msg['To'] = toaddr 

# the subject of mail
msg['Subject'] = "subject_of_the_mail"

# the body of the mail 
body = "body_of_the_mail"

# attaching the body with the msg 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent
# rb is a flag for readonly 
filename = "file_name_with_extension"
attachment = open("Path of the file", "rb") 

# MIMEBase
attac= MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
attc.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(attc) 

attc.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(attc) 

# creates SMTP session 
email = smtplib.SMTP('smtp.gmail.com', 587) 

# TLS for security 
email.starttls() 

# authentication 
email.login(fromaddr, "Password_of_the_sender") 

# Converts the Multipart msg into a string 
message = msg.as_string() 

# sending the mail 
email.sendmail(fromaddr, toaddr, message) 

# terminating the session 
s.quit() 





OR:-


#!/usr/bin/python

import smtplib
import base64

filename = "/tmp/test.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'webmaster@tutorialpoint.com'
reciever = 'amrood.admin@gmail.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: From Person <me@fromdomain.net>
To: To Person <amrood.admin@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, reciever, message)
   print "Successfully sent email"
except Exception:
   print "Error: unable to send email"