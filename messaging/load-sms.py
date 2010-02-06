import sys, os
from time import *
import urllib2
import feedparser
import rfc822

sys.path.append('/var/projects')
os.environ['DJANGO_SETTINGS_MODULE'] ='mednet.settings'

from mednet import settings
from mednet.messaging.models import *

feedurl = ('http://%s:%s@%s') % (settings.GEOCHAT_USER, settings.GEOCHAT_PASS, settings.GEOCHAT_FEED)

d = feedparser.parse(feedurl)

length = len(d.entries)

for i in range(1,length):
	guid = d.entries[i].guid

	try:
                existing_sms = SmsMessage.objects.get(guid=guid)
        except:
		print d.entries[i]
		sender = d.entries[i].author.replace('sms://', '')
		message = smart_unicode(d.entries[i].title,encoding='utf-8', strings_only=False, errors='strict')
		date_sent = rfc822.parsedate(d.entries[i].updated)
		date_sent = strftime("%Y-%m-%d %H:%M:%S", date_sent)
	
		sms = SmsMessage()
		sms.sender = sender
		sms.message = message
		sms.guid = guid
		sms.date_sent = date_sent
		sms.status = 'NW'
		sms.status_changed_date = date_sent
		sms.save()
		print sms
