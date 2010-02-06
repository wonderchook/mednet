import sys, os

sys.path.append('/var/projects')
os.environ['DJANGO_SETTINGS_MODULE'] ='mednet.settings'

from mednet.sahana.models import Hospital
#from django.contrib.gis.geos import *
import simplejson
import urllib2
import time


hospital_url = "http://haiti.sahanafoundation.org/prod/hms/hospital.json"
hospital_json =  simplejson.loads(urllib2.urlopen(hospital_url).read())

for h in hospital_json['$_hms_hospital']:
    print h
    oh = Hospital()
    oh.phone_emergency = h['phone_emergeny']
    oh.phone_business = h['phone_business']
    oh.postcode = h['postcode']
    oh.city = h['city']
    oh.uuid = h['uuid']
    oh.name = h['name']
    oh.comments = h['comments']
    oh.created_on = h['2010-01-23 11:34:29']
    oh.address = h['address']
    lat = h['$k_location_id']['@lat']
    lon = h['$k_location_id']['@lon']
    location_uuid = h['$k_location_id']['@uuid']
    #location_resource = h[['$k_location_id']['@resource']

