import sys
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from mednet.messaging.models import *
from mednet.sahana.models import *
from datetime import *
from time import *

@login_required
def index(request):
    voice_count =  VoiceMessage.objects.filter(status='NW').count() 
    sms_count =  SmsMessage.objects.filter(status='NW').count() 
    mail_count =  MailMessage.objects.filter(status='NW').count() 
    return render_to_response('messaging/index.html', {'voice_count': voice_count, 'sms_count': sms_count, 'mail_count': mail_count}, context_instance=RequestContext(request))

@login_required
def mark_message(request):
	msgtype = request.GET['msgtype']
	msgid = int(request.GET['msgid'])
	status = request.GET['status']
	if(msgtype == 'voice'):
		vm = VoiceMessage.objects.get(pk=msgid)
		vm.status = status
		vm.status_changed_date = datetime.now()
		vm.save()
		return HttpResponseRedirect('/mednet/messaging/next_message/voice/')
	elif(msgtype == 'sms'):
		sms = SmsMessage.objects.get(pk=msgid)
		sms.status = status
		sms.status_changed_date = datetime.now()
		sms.save()
		return HttpResponseRedirect('/mednet/messaging/next_message/sms/')
	elif(msgtype == 'mail'):
		mail = MailMessage.objects.get(pk=msgid)
		mail.status = status
		mail.status_changed_date = datetime.now()
		mail.save()
		return HttpResponseRedirect('/mednet/messaging/next_message/mail/')
	return HttpResponse('ok')
	pass

@login_required
def next_message(request, message_type):
	print message_type
	if(message_type == 'voice'):
		try:
			next_voice_message = VoiceMessage.objects.filter(status='NW').order_by('start_time')[0:1].get()
			#next_voice_message.status = 'IP'
			next_voice_message.status_changed_date = strftime("%Y-%m-%d %H:%M:%S", localtime())
			next_voice_message.save()
			hospitals = HmsHospital.objects.all().order_by('name')
			return render_to_response('messaging/next_voice_message.html', {'next_voice_message': next_voice_message, 'hospitals': hospitals}, context_instance=RequestContext(request) )
		except:
			#No Messages Matching Criteria
			print sys.exc_info()		
			return render_to_response('messaging/no_messages.html', {'type': 'Voice'}, context_instance=RequestContext(request))
	elif(message_type == 'mail'):
		try:
			next_mail_message = MailMessage.objects.filter(status='NW').order_by('date_sent')[0:1].get()
			#next_mail_message.status = 'IP'
			next_mail_message.status_changed_date = strftime("%Y-%m-%d %H:%M:%S", localtime())
			next_mail_message.save()
			hospitals = HmsHospital.objects.all().order_by('name')
			return render_to_response('messaging/next_email_message.html', {'next_mail_message': next_mail_message, 'hospitals': hospitals}, context_instance=RequestContext(request))
		except:
			#No Messages Matching Criteria
			print sys.exc_info()		
			return render_to_response('messaging/no_messages.html', {'type': 'Voice'}, context_instance=RequestContext(request))
	elif(message_type == 'sms'):
		try:
			next_sms_message = SmsMessage.objects.filter(status='NW').order_by('-date_sent')[0:1].get()
			#next_sms_message.status = 'IP'
			next_sms_message.status_changed_date = strftime("%Y-%m-%d %H:%M:%S", localtime())
			next_sms_message.save()
			hospitals = HmsHospital.objects.all().order_by('name')
			return render_to_response('messaging/next_sms_message.html', {'next_sms_message': next_sms_message, 'hospitals': hospitals}, context_instance=RequestContext(request))
		except:
			#No Messages Matching Criteria
			print sys.exc_info()		
			return render_to_response('messaging/no_messages.html', {'type': message_type}, context_instance=RequestContext(request))
	else:
		#message type not valid
		pass
