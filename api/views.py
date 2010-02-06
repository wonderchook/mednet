# Create your views here.

from django.shortcuts import render_to_response
from mednet.ushahidi.models import Location, Incident, Category
from mednet.messaging.models import MailMessage, SmsMessage, VoiceMessage
#from django.contrib.gis.shortcuts import render_to_kml
from django.core import serializers 
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

def sms_json(request):
    sms = SmsMessage.objects.all()
    return render_to_response("sms.json", {'sms' : sms }, mimetype='application/json')

def voice_json(request):
    voicemail = VoiceMessage.objects.all()
    return render_to_response("voice.json", {'voicemail' : voicemail }, mimetype='application/json')

def mail_json(request):
    mail = MailMessage.objects.all()
    return render_to_response("mail.json", {'mail' : mail }, mimetype='application/json')

def gpx(request):
     incidents = Incident.objects.all()
     return render_to_response("incidents.gpx", {'incidents' : incidents }, mimetype='application/xml')

#@cache_page
def kml(request):
    #locations = Location.objects.kml()
    incidents = Incident.objects.all()
    
    return render_to_response("incidents.kml", {'incidents' : incidents }, mimetype='application/vnd.google-earth.kml+xml')

def geojson(request):
    #locations = Location.objects.kml()
    incidents = Incident.objects.all()
    
    return render_to_response("incidents.json", {'incidents' : incidents }, mimetype='application/json')

#@cache_page
def kml_category(request, category_id):
    incidents = Incident.objects.filter(categories=category_id)
    # need to get the media associated with the incident 
    
    return render_to_response("incidents.kml", {'incidents' : incidents }, mimetype='application/vnd.google-earth.kml+xml')

def geojson_category(request, category_id):
    incidents = Incident.objects.filter(categories=category_id)
    return render_to_response("incidents.json", {'incidents' : incidents }, mimetype='application/json')

def gpx_category(request, category_id):
    incidents = Incident.objects.filter(categories=category_id)
    return render_to_response("incidents.gpx", {'incidents' : incidents }, mimetype='application/xml')

#@cache_page
def kml_incident(request, incident_id):
    incidents = Incident.objects.filter(ushahidi_id=incident_id)
    return render_to_response("incidents.kml", {'incidents' : incidents }, mimetype='application/vnd.google-earth.kml+xml')


def geojson_incident(request, incident_id):
    incidents = Incident.objects.filter(ushahidi_id=incident_id)
    return render_to_response("incidents.json", {'incidents' : incidents }, mimetype='application/json')


def gpx_incident(request, incident_id):
    incidents = Incident.objects.filter(ushahidi_id=incident_id)
    return render_to_response("incidents.gpx", {'incidents' : incidents }, mimetype='application/xml')

#@cache_page
def categories(rg, resp):
    if 'by' in rg:
        by = rg['by']

    if 'id' in rg:
        _id = rg['id']

        # lookup the categories
        c = Category.objects.filter((by, _id))
        
        if resp == 'xml':
            data = str(serializers.serialize("xml", c))
            print data

            return HttpResponse(data, mimetype="text/xml")

def api(request):
    print "running api"
    rg = request.GET

    #if 'resp' in rg:
    #    resp = rg['resp']
    #else:
        # json is default with no resp set
        # but a wrong resp will come back with xml but an incorrect mimetype
    #    resp = 'json'

    print "now looking at task"

    return kml()

    #if 'task' in rg:
    #    print "running kml"
    #    obj = kml()
    #    print obj
    #    return obj

    #elif rg['task'] == 'categories':
    #    return categories(rg, resp)
