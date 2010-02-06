from django.contrib.gis.db import models
from django.utils.encoding import *

MESSAGE_STATUS_CHOICE = (
	('NW', 'New Message'),
	('IP', 'In Process'),
	('CM', 'Complete'),
	('IG', 'Ignored')
)

class SmsMessage(models.Model):
	guid = models.CharField(max_length=512)
	sender = models.CharField(max_length=25)
	message = models.CharField(max_length=255, null=True, blank=True)
	date_sent = models.DateTimeField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	status = models.CharField(max_length=2, choices=MESSAGE_STATUS_CHOICE)
	status_changed_date = models.DateTimeField()
	objects = models.GeoManager()
	def __unicode__(self):
        	return str(self.sender + ' ' + str(self.date_sent)) 

class VoiceMessage(models.Model):
	gvoice_id = models.CharField(max_length=256)
	start_time = models.DateTimeField(null=True, blank=True)
	phone_number = models.CharField(max_length=100, null=True, blank=True)
	subject = models.CharField(max_length=255, null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	mp3_url = models.CharField(max_length=255, blank=True, null=True)
	status = models.CharField(max_length=2, choices=MESSAGE_STATUS_CHOICE)
	status_changed_date = models.DateTimeField()
	objects = models.GeoManager()
	def __unicode__(self):
        	return str(self.phone_number + ' ' + str(self.start_time))

class MailMessage(models.Model):
	from_address = models.EmailField()
	subject = models.CharField(max_length=512,null=True,blank=True)
	date_sent = models.DateTimeField(null=True,blank=True)
	message = models.TextField(null=True,blank=True)
	return_path = models.CharField(max_length=512, null=True, blank=True)
	message_id = models.CharField(max_length=512, null=True, blank=True)
	status = models.CharField(max_length=2, choices=MESSAGE_STATUS_CHOICE)
	status_changed_date = models.DateTimeField()
	objects = models.GeoManager()
	def __unicode__(self):
        	return str(self.return_path + ' ' + str(self.date_sent))
