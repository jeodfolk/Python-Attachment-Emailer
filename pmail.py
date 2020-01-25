#  Only works with gmail and only text based files.
# 1. Run file
# 2. Enter email and password if no default entered. May need to allow 
# less secure appsunder google account security settings
# 3. Select directory with file you want to attach
# 4. Enter name of file/s. Leave empty when done entering files
# 5. Recieve 'Email Sent' or error message

import smtplib
from smtplib import *
from email.message import EmailMessage
from getpass import getpass
import re
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

#Enter a default email and password to skip console inputs else leave as ""
defaultUser = ""
defaultPass = ""
gmailUser = input("Enter Email: ") if defaultUser == "" else defaultUser
gmailPass = getpass("Enter Password : ") if defaultPass == "" else defaultPass

files=[]
data=[]

Tk().withdraw()
os.chdir(askdirectory(title='Select Folder')) # shows dialog box and change working directory
print(os.getcwd())

while(True):
    newFile = input("Enter filename (Leave empty to continue): ")
    if newFile == "":
        break
    else:
        files.append(newFile)

for i in range(0,len(files)): 
    with open (files[i], "r") as myfile:
        data.append(myfile.read())

#Construct email with all inputted attachments
msg = EmailMessage()
for i in range(0,len(files)):
    msg.add_attachment(data[i], filename=files[i])

msg['Subject'] = files[0]
msg['From'] = gmailUser
msg['To'] = gmailUser

try:
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(gmailUser,gmailPass)
    s.send_message(msg)
    s.quit()
    print("Email Sent")
except SMTPResponseException as e:
    print(e.smtp_code, e.smtp_error)
