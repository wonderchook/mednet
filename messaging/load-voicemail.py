import sys, os
from time import *

sys.path.append('/var/projects')
os.environ['DJANGO_SETTINGS_MODULE'] ='mednet.settings'

from mednet import settings
from mednet.messaging.models import *
from googlevoice import Voice,util

voice = Voice()
voice.login(settings.GVOICE_USER, settings.GVOICE_PASS)

for message in voice.voicemail().messages:
	vm = VoiceMessage()
	vm.gvoice_id = message.id
	try:
		existing_vm = VoiceMessage.objects.get(gvoice_id=message.id)
	except:
		print message.displayStartDateTime
		vm.start_time = message.displayStartDateTime
		vm.phone_number = message.phoneNumber.replace('+', '')
		vm.status = 'NW'
		vm.status_changed_date = message.displayStartDateTime
		print vm.phone_number
		try:
			message.download('/var/www/haiti/voicemails')
			vm.mp3_url = '/voicemails/' + message.id + '.mp3'
			vm.save()
		except:
			print "download failed"
