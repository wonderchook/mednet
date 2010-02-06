import os, sys
from googlevoice import Voice
from googlevoice.util import input

sys.path.append('/var/projects')
os.environ['DJANGO_SETTINGS_MODULE'] ='mednet.settings'

from mednet import settings

voice = Voice()
voice.login(settings.GVOICE_USER, settings.GVOICE_PASS)

voice.send_sms('17602089488', 'Hmm, lets see if this works amigos!')
