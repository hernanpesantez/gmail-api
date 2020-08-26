import imaplib
import pprint
import json

import email

import imaplib
import base64
import os
import email




with open('auth.json') as f:
  auth = json.load(f)

imap_host = (auth['credentials']['imap_host'])
imap_user = (auth['credentials']['imap_user'])
imap_pass = (auth['credentials']['imap_pass'])

print(imap_host)
print(imap_user)
print(imap_pass)



import  poplib

user = input('email: ') 
# Connect to the mail box 
Mailbox = poplib.POP3_SSL('pop.googlemail.com', '995') 
Mailbox.user(user) 
passd = input('pass: ')
Mailbox.pass_(passd) 
NumofMessages = len(Mailbox.list()[1])
for i in range(NumofMessages):
    for msg in Mailbox.retr(i+1)[1]:
        print (msg)
Mailbox.quit()



# connect to host using SSL

# mail = imaplib.IMAP4_SSL(“host”,port)


# u = input("Enter email: ")
# p = input("Password: ")



imap = imaplib.IMAP4('imap.gmail.com',995)

print(dir(imap))


# login to server
imap.login(imap_user, imap_pass)



print(imap)
imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')
for num in data[0].split():
	tmp, data = imap.fetch(num, '(RFC822)')
	print('Message: {0}\n'.format(num))
	pprint.pprint(data[0][1])
	break
imap.close()

#=======================================================================

# import imaplib
# import ConfigParser
# import os

# def open_connection(verbose=False):
#     # Read the config file
#     config = ConfigParser.ConfigParser()
#     config.read([os.path.expanduser('~/.pymotw')])

#     # Connect to the server
#     hostname = config.get('server', 'hostname')
#     if verbose: print ('Connecting to', hostname)
#     connection = imaplib.IMAP4_SSL(hostname)

#     # Login to our account
#     username = config.get('account', 'username')
#     password = config.get('account', 'password')
#     if verbose: print ('Logging in as', username)
#     connection.login(username, password)
#     return connection

# if __name__ == '__main__':
#     c = open_connection(verbose=True)
#     try:
#         print (c)
#     finally:
#         c.logout()