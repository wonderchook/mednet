from mednet.messaging.models import * 
from django.contrib.gis import admin

class VoiceMessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'phone_number', 'start_time', 'mp3_url')

class MailMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'return_path', 'subject', 'date_sent')
    
class SmsMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'status','sender', 'message', 'date_sent')


admin.site.register(VoiceMessage, VoiceMessageAdmin)
admin.site.register(MailMessage, MailMessageAdmin)
admin.site.register(SmsMessage, SmsMessageAdmin)
