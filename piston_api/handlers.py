from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.emitters import Emitter, JSONEmitter
from piston_api.emitters import GeoJSONEmitter
from mednet.sahana.models import *

JSONEmitter.unregister('json')
Emitter.register('json', GeoJSONEmitter, 'application/javascript; charset=utf-8')

#Hospitals
class AnonymousHospitalHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsHospital

   def read(self, request, hospital_id=None):
	if(hospital_id):
		return HmsHospital.objects.get(pk=hospital_id)
	else:
		return HmsHospital.objects.all()

class HospitalHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsHospital
	anonymous = AnonymousHospitalHandler

#Hospital Activities
class AnonymousHospitalActivityHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsActivity

   def read(self, request, hospital_activity_id=None):
	if(hospital_activity_id):
		return HmsActivity.objects.get(pk=hospital_activity_id)
	else:
		return HmsActivity.objects.all()

class HospitalActivityHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsActivity
	anonymous = AnonymousHospitalActivityHandler

#Hospital Bed Capacity
class AnonymousHospitalBedCapacityHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsBedCapacity

   def read(self, request, hospital_bed_capacity_id=None):
	if(hospital_bed_capacity_id):
		return HmsBedCapacity.objects.get(pk=hospital_bed_capacity_id)
	else:
		return HmsBedCapacity.objects.all()

class HospitalBedCapacityHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsBedCapacity
	anonymous = AnonymousHospitalBedCapacityHandler

#Hospital Contacts
class AnonymousHospitalContactHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsContact

   def read(self, request, hospital_contact_id=None):
	if(hospital_contact_id):
		return HmsContact.objects.get(pk=hospital_contact_id)
	else:
		return HmsContact.objects.all()

class HospitalContactHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsContact
	anonymous = AnonymousHospitalContactHandler

#Hospital Images 
class AnonymousHospitalImageHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsImage

   def read(self, request, hospital_image_id=None):
	if(hospital_image_id):
		return HmsImage.objects.get(pk=hospital_image_id)
	else:
		return HmsImage.objects.all()

class HospitalImageHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsImage
	anonymous = AnonymousHospitalImageHandler

#Hospital Request 
class AnonymousHospitalRequestHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsRequest

   def read(self, request, hospital_request_id=None):
	if(hospital_request_id):
		return HmsRequest.objects.get(pk=hospital_request_id)
	else:
		return HmsRequest.objects.all()

class HospitalRequestHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsRequest
	anonymous = AnonymousHospitalRequestHandler

#Hospital Resource 
class AnonymousHospitalResourceHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsResource

   def read(self, request, hospital_resource_id=None):
	if(hospital_resource_id):
		return HmsResource.objects.get(pk=hospital_resource_id)
	else:
		return HmsResource.objects.all()

class HospitalResourceHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsResource
	anonymous = AnonymousHospitalResourceHandler

#Hospital Service 
class AnonymousHospitalServiceHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = HmsService

   def read(self, request, hospital_service_id=None):
	if(hospital_service_id):
		return HmsService.objects.get(pk=hospital_service_id)
	else:
		return HmsService.objects.all()

class HospitalServiceHandler(BaseHandler):
	allow_methods = ('GET',)
	model = HmsService
	anonymous = AnonymousHospitalServiceHandler
