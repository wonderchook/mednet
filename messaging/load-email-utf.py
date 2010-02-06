import sys, os
from time import * 
import rfc822

sys.path.append('/var/projects')
os.environ['DJANGO_SETTINGS_MODULE'] ='mednet.settings'

from mednet import settings
from mednet.messaging.models import *

import getpass, poplib
import string
import email
from email.header import decode_header

M = poplib.POP3_SSL(settings.MAIL_SERVER, settings.MAIL_PORT)
M.user(settings.MAIL_USER)
M.pass_(settings.MAIL_PASS)
numMessages = len(M.list()[1])

print numMessages


from email.Iterators import typed_subpart_iterator

def get_charset(message, default="ascii"):
    """Get the message charset"""

    if message.get_content_charset():
        return message.get_content_charset()

    if message.get_charset():
        return message.get_charset()

    return default

def get_body(message):
    """Get the body of the email message"""

    if message.is_multipart():
        #get the plain text version only
        text_parts = [part
                      for part in typed_subpart_iterator(message,
                                                         'text',
                                                         'plain')]
        body = []
        for part in text_parts:
            charset = get_charset(part, get_charset(message))
            body.append(unicode(part.get_payload(decode=True),
                                charset,
                                "replace"))

        return u"\n".join(body).strip()

    else: # if it is not multipart, the payload will be a string
          # representing the message body
        body = unicode(message.get_payload(decode=True),
                       get_charset(message),
                       "replace")
        return body.strip()

for i in range(numMessages):

	msg = M.retr(i+1)
	#msg = decode_header(msg)
	print msg

	_str = string.join(msg[1], "\n")
	
	mail = email.message_from_string(_str)
	#import code; code.interact(local=locals())

	print mail


	m =  MailMessage()
	print "MessageID", mail["Message-ID"]
	try:
		existing_mail = MailMessage.objects.get(message_id=mail["Message-ID"])
	except:
	
		m.from_address = mail["From"]
	        subject = decode_header(mail["Subject"])
		#print subject
		if subject[0][1] == None:
			sub = subject[0][0]
		else:
			sub = subject[0][0].decode(subject[0][1])
		print sub
		m.subject = sub
		date_sent = rfc822.parsedate(mail["Date"])
		date_sent = strftime("%Y-%m-%d %H:%M:%S", date_sent)
		
		m.date_sent = date_sent
		m.return_path =  mail["Return-Path"].replace('<', '').replace('>', '')
		m.message_id =  mail["Message-ID"].replace('<', '').replace('>', '')
		m.status = 'NW'
		m.status_changed_date = date_sent
		
                pay = get_body(mail)
                
                m.message = pay
	
		m.save()
M.quit()
