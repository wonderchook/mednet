import sys, os

sys.path.append('/var/projects')
os.environ['DJANGO_SETTINGS_MODULE'] ='mednet.settings'


from mednet.sahana.models import HmsHospital
from django.contrib.gis.geos import Point
import simplejson
import urllib2
import time
from datetime import datetime 

hospital_url = "http://haiti.sahanafoundation.org/prod/hms/hospital.json"
hospital_json =  simplejson.loads(urllib2.urlopen(hospital_url).read())

# delete out old stuff
HmsHospital.objects.all().delete()

#def assign(value):
#    if value in h:
#        oh[value] = h[value]
#    return

for h in hospital_json['$_hms_hospital']:
 
    print h
    #sys.exit()

    oh = HmsHospital()
    if '@uuid' in h: oh.uuid = h['@uuid']
    if 'name' in h: oh.name = h['name']
    if 'phone_emergency' in h: oh.phone_emergency = h['phone_emergency']
    if 'phone_business' in h: oh.phone_business = h['phone_business']
    if 'postcode' in h: oh.postcode = h['postcode']
    if 'city' in h: oh.city = h['city']
    if 'comments' in h: oh.comments = h['comments']
    if '@created_on' in h: created_on = h['@created_on']
    if '@modified_on' in h: modified_on = h['@modified_on']
    if 'address' in h: oh.address = h['address']
    
    if '$k_location_id' in h: 
        lat = h['$k_location_id']['@lat']
        lon = h['$k_location_id']['@lon']
        location = Point(float(lon), float(lat))
        oh.location = location
    
    oh.created_on = datetime.strptime(created_on, "%Y-%m-%d %H:%M:%S")
    oh.modified_on = datetime.strptime(modified_on, "%Y-%m-%d %H:%M:%S")
    

    oh.save()
