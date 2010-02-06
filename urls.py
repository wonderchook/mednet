from django.conf.urls.defaults import *
from mednet.messaging.models import *
from mednet.sahana.models import *
from mednet.ushahidi.models import *
from django.contrib import databrowse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

databrowse.site.register(VoiceMessage)
databrowse.site.register(SmsMessage)
databrowse.site.register(MailMessage)

databrowse.site.register(Category)
databrowse.site.register(Country)
databrowse.site.register(Incident)
databrowse.site.register(Location)

databrowse.site.register(HmsHospital)

urlpatterns = patterns('',
    (r'^mednet/$', 'mednet.views.index'),
    (r'^mednet/map/$', 'mednet.views.map'),
    (r'^mednet/hospitals/$', 'mednet.views.hospitals'),
    (r'^mednet/hospital/(?P<hospital_id>\d+)/$', 'mednet.views.hospital'),
    (r'^mednet/about/$', 'mednet.views.about'),
    (r'^mednet/accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^mednet/accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/mednet/'}),
    (r'^mednet/messaging/$', 'mednet.messaging.views.index'),
    (r'^mednet/messaging/mark_message/$', 'mednet.messaging.views.mark_message'),
    (r'^mednet/ushahidi/api/incidents.kml', 'mednet.api.views.kml'),
    (r'^mednet/ushahidi/api/incidents.json', 'mednet.api.views.geojson'),
    (r'^mednet/ushahidi/api/incidents.gpx', 'mednet.api.views.gpx'),

    (r'^mednet/ushahidi/api/incidents/category/([0-9]+).kml', 'mednet.api.views.kml_category'),
    (r'^mednet/ushahidi/api/incidents/category/([0-9]+).json', 'mednet.api.views.geojson_category'),
    (r'^mednet/ushahidi/api/incidents/category/([0-9]+).gpx', 'mednet.api.views.gpx_category'),

    (r'^mednet/ushahidi/api/incident/([0-9]+).kml', 'mednet.api.views.kml_incident'),
    (r'^mednet/ushahidi/api/incident/([0-9]+).json', 'mednet.api.views.geojson_incident'),
    (r'^mednet/ushahidi/api/incidents/category/([0-9]+).gpx', 'mednet.api.views.gpx_category'),

    (r'^mednet/messaging/api/sms.json', 'mednet.api.views.sms_json'),
    (r'^mednet/messaging/api/voice.json', 'mednet.api.views.voice_json'),
    (r'^mednet/messaging/api/mail.json', 'mednet.api.views.mail_json'),

    (r'^mednet/proxy.cgi','mednet.proxy.views.index'), 
                       
    (r'^mednet/admin/', include(admin.site.urls)),
    (r'^mednet/databrowse/(.*)', databrowse.site.root),
    (r'^mednet/messaging/next_message/([a-z]+)', 'mednet.messaging.views.next_message'),
    (r'^mednet/sahana/add_hbc/', 'mednet.sahana.views.bed_capacity_report'),
    (r'^mednet/sahana/add_request/', 'mednet.sahana.views.hospital_request_form'),
    (r'^mednet/sahana/add_contact/', 'mednet.sahana.views.hospital_contact_form'),
    (r'^mednet/sahana/add_services/', 'mednet.sahana.views.hospital_services_form'),
    (r'^mednet/sahana/add_activities/', 'mednet.sahana.views.hospital_activities_form'),
    (r'^mednet/sahana/add_resources/', 'mednet.sahana.views.hospital_resources_form'),
    (r'^mednet/sahana/add_person/', 'mednet.sahana.views.person_form'),
    (r'^mednet/api/0.1/rest/', include('mednet.piston_api.urls')),
)
