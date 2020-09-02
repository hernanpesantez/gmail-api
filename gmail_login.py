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

 
# Connect to the mail box 
Mailbox = poplib.POP3_SSL('pop.googlemail.com', '995') 
Mailbox.user(imap_user) 

Mailbox.pass_(imap_pass) 
NumofMessages = len(Mailbox.list()[1])
for i in range(NumofMessages):
    for msg in Mailbox.retr(i+1)[1]:
        print (msg)
Mailbox.quit()



# connect to host using SSL





# imap = imaplib.IMAP4_SSL('imap.gmail.com',993)

# # print(dir(imap))


# # login to server
# imap.login(imap_user, imap_pass)



# print(dir(imap))
# imap.select('Inbox')

# tmp, data = imap.search(None, 'ALL')

# print(data[0])
# for num in data[0].split():
# 	tmp, data = imap.fetch(num, '(RFC822)')
# 	print('Message: {0}\n'.format(num))
    
# 	pprint.pprint(data)
# 	break
# imap.close()

#=======================================================================



# import imaplib
# import pprint
# import imaplib_connect

# with imaplib_connect.open_connection() as c:
#     c.select('INBOX', readonly=True)

#     print('HEADER:')
#     typ, msg_data = c.fetch('1', '(BODY.PEEK[HEADER])')
#     for response_part in msg_data:
#         if isinstance(response_part, tuple):
#             print(response_part[1])

#     print('\nBODY TEXT:')
#     typ, msg_data = c.fetch('1', '(BODY.PEEK[TEXT])')
#     for response_part in msg_data:
#         if isinstance(response_part, tuple):
#             print(response_part[1])

#     print('\nFLAGS:')
#     typ, msg_data = c.fetch('1', '(FLAGS)')
#     for response_part in msg_data:
#         print(response_part)
#         print(imaplib.ParseFlags(response_part))



# ==================================================================
server = 'imap.gmail.com'
user = 'vcgdevtest@gmail.com'
password = 'Python@1822'
outputdir = '/temp'
subject = 'VCG Submissions Dep.' #subject line of the emails you want to download attachments from

def connect(server, user, password):
    m = imaplib.IMAP4_SSL(server)
    m.login(user, password)
    m.select()
    return m

def downloaAttachmentsInEmail(m, emailid, outputdir):
    resp, data = m.fetch(emailid, "(BODY.PEEK[])")
    email_body = data[0][1]
    mail = email.message_from_bytes(email_body)
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))

#download attachments from all emails with a specified subject line
def downloadAttachments(subject):
    m = connect(server, user, password)
    m.select("Inbox")
    typ, msgs = m.search(None, '(SUBJECT "' + subject + '")')
    msgs = msgs[0].split()
    for emailid in msgs:
        downloaAttachmentsInEmail(m, emailid, outputdir)

downloadAttachments(subject)

m = connect(server,user,password)

# downloaAttachmentsInEmail(m, 'vcgdevtest@gmail.com','/temp')




import imaplib
import email

m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
m.login(user,password)
m.select('"[Gmail]/All Mail"')

result, data = m.uid('search', None, "ALL") # search all email and return uids
if result == 'OK':
    for num in data[0].split():
        result, data = m.uid('fetch', num, '(RFC822)')
    if result == 'OK':
        email_message = email.message_from_bytes(data[0][1])    # raw email text including headers
        print('From:' + email_message['From'])

m.close()
m.logout()