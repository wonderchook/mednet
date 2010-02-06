import sys, os

sys.path.append('/var/projects')
os.environ['DJANGO_SETTINGS_MODULE'] ='mednet.settings'

from mednet import settings
from clickatell import Clickatell

gateway = Clickatell(settings.CLICKATELL_USER, settings.CLICKATELL_PASS, settings.CLICKATELL_API_ID)
message = {'to': '573008438443', 'text': 'can you send a test msg to +15597152722'} 
retval, msg = gateway.sendmsg(message)
if retval == 0:
	print 'ok'
else:
    print msg
