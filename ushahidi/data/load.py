import sys, os

sys.path.append('/var/projects')
os.environ['DJANGO_SETTINGS_MODULE'] ='mednet.settings'

from mednet.ushahidi.models import *
from django.contrib.gis.geos import *
import simplejson
import urllib2
import time

countries_url = 'http://haiti.ushahidi.com/api?task=countries&resp=json'
countries_json = simplejson.loads(urllib2.urlopen(countries_url).read())

country_count = 0
for country in countries_json['payload']['countries']:
	ushahidi_id = int(country['country']['id'])
	name = country['country']['name']
	iso = country['country']['iso']
	capital = country['country']['capital']
	try:
		existing_country = Country.objects.get(ushahidi_id = ushahidi_id)
		continue
	except:
		pass
	country_count += 1
	print ushahidi_id, iso, name, capital
	c = Country(ushahidi_id = ushahidi_id, name=name, iso=iso, capital=capital)
	c.save()

print "%d countries loaded" % (country_count)

categories_url = 'http://haiti.ushahidi.com/api?task=categories&resp=json'
categories_json = simplejson.loads(urllib2.urlopen(categories_url).read())

category_count = 0

for category in categories_json['payload']['categories']:
	ushahidi_id = int(category['category']['id'])
	title = category['category']['title']
	description = category['category']['description']
	color = category['category']['color']
	icon = category['category']['icon']
	try:
		existing_category = Category.objects.get(ushahidi_id = ushahidi_id)
		continue
	except:
		pass
	category_count += 1
	print ushahidi_id, title, description, color, icon
	cat = Category(ushahidi_id=ushahidi_id, title=title, description=description, color=color,icon=icon)
	cat.save()

print "%d categories loaded" % (category_count)


locations_url = 'http://haiti.ushahidi.com/api?task=locations&resp=json'
locations_json = simplejson.loads(urllib2.urlopen(locations_url).read())

locations_count = 0

for location in locations_json['payload']['locations']:
	ushahidi_id = int(location['location']['id'])
	name = location['location']['name']
	country_id = location['location']['country_id']
	latitude = float(location['location']['latitude'])
	longitude = float(location['location']['longitude'])
	cntry = None
	if(country_id):
		cntry = Country.objects.get(ushahidi_id=ushahidi_id)
	pnt = Point(longitude, latitude, srid=4326)
	try:
		existing_location = Location.objects.get(ushahidi_id = ushahidi_id)
		continue	
	except:
		pass
	print ushahidi_id, name, country_id, latitude, longitude
	locations_count += 1
	loc = Location(ushahidi_id = ushahidi_id, name=name, country=cntry, point=pnt)
	loc.save()	

print "%d locations loaded" % (locations_count)

categories = Category.objects.all()
	
incident_count = 0
new_location_count = 0

for category in categories:
	category_id = category.ushahidi_id

	incidents_url = 'http://haiti.ushahidi.com/api?task=incidents&resp=json&by=all&by=catid&id=%d' % (category_id)
	incidents_json = simplejson.loads(urllib2.urlopen(incidents_url).read())

	for incident in incidents_json['payload']['incidents']:
		ushahidi_id = int(incident['incident']['incidentid'])
		title = incident['incident']['incidenttitle']
		description = incident['incident']['incidentdescription']
		incident_date_str = incident['incident']['incidentdate']
		mode = incident['incident']['incidentmode']
		active = incident['incident']['incidentactive']
		verified = incident['incident']['incidentverified']
		location_id = incident['incident']['locationid']

		incident_date = None
		try:
			incident_date = time.strptime(incident_date_str, "%Y-%m-%d %H:%M:%S")
		except:
			incident_date_str = None

		try:
			existing_incident = Incident.objects.get(ushahidi_id = ushahidi_id)
			existing_incident.categories.add(category)
			existing_incident.save()
			continue	
		except:
			pass
		
		incident_count += 1

		location = None
		try:
			if(location_id):
				location = Location.objects.get(ushahidi_id=location_id)
		except:
			location_ushahidi_id = int(incident['incident']['locationid'])
			name = incident['incident']['locationname']
			latitude = float(incident['incident']['locationlatitude'])
			longitude = float(incident['incident']['locationlongitude'])
			cntry = None
			pnt = Point(longitude, latitude, srid=4326)
			location = Location(ushahidi_id = location_ushahidi_id, name=name, country=cntry, point=pnt)
			location.save()	
			new_location_count += 1

		'''
		TODO:
			1) Media
			2) If the Incident Exists, update it with new info
			3) Check that mode, active, verified are handled correctly
		'''

		inc = Incident(ushahidi_id=ushahidi_id, title=title, description=description, date_time=incident_date_str, mode=mode, active=active,verified=verified, location=location)
		inc.save()
		inc.categories.add(category)
		inc.save()

print "%d Incidents loaded" % (incident_count)
print "%d New Locations loaded" % (new_location_count)
