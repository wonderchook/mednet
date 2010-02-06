import sys
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from sahana.forms import * 
from sahana.models import *

def bed_capacity_report(request):
	try:
		hospital_id = request.GET['hospital_id']
	except:
		hospital_id = None
	hbc = HmsBedCapacity()
	if request.POST:
		form = HospitalBedCapacityForm(data=request.POST, instance=hbc)
		if form.is_valid():
			form.save()
			hbc.hospital = HmsHospital.objects.get(pk=request.POST['hospital'])
			hbc.save()
			return HttpResponse('ok')
		else:
			return HttpResponse('errors')
	else:
		form = HospitalBedCapacityForm(instance=hbc)

	return render_to_response('sahana/hbc.html', {'hospital_id': hospital_id, 'form': form, 'request': request}, context_instance=RequestContext(request))

def hospital_request_form(request):
	try:
		hospital_id = request.GET['hospital_id']
	except:
		hospital_id = None
	hms_request = HmsRequest()
	if request.POST:
		form = HospitalRequestForm(data=request.POST, instance=hms_request)
		if form.is_valid():
			form.save()
			hms_request.hospital = HmsHospital.objects.get(pk=request.POST['hospital'])
			hms_request.save()
			return HttpResponse('ok')
		else:
			return HttpResponse('errors')
	else:
		form = HospitalRequestForm(instance=hms_request)

	return render_to_response('sahana/hospital_request.html', {'hospital_id': hospital_id, 'form': form, 'request': request}, context_instance=RequestContext(request))

def hospital_contact_form(request):
	try:
		hospital_id = request.GET['hospital_id']
	except:
		hospital_id = None
	contact = HmsContact()
	if request.POST:
		form = HospitalContactForm(data=request.POST, instance=contact)
		if form.is_valid():
			form.save()
			contact.hospital = HmsHospital.objects.get(pk=request.POST['hospital'])
			contact.save()
			return HttpResponse('ok')
		else:
			return HttpResponse('errors')
	else:
		form = HospitalContactForm(instance=contact)

	return render_to_response('sahana/hospital_contact.html', {'hospital_id': hospital_id, 'form': form, 'request': request}, context_instance=RequestContext(request))

def hospital_resources_form(request):
	try:
		hospital_id = request.GET['hospital_id']
	except:
		hospital_id = None
	resource = HmsResource()
	if request.POST:
		form = HospitalResourceForm(data=request.POST, instance=resource)
		if form.is_valid():
			form.save()
			resource.hospital = HmsHospital.objects.get(pk=request.POST['hospital'])
			resource.save()
			return HttpResponse('ok')
		else:
			return HttpResponse('errors')
	else:
		form = HospitalResourceForm(instance=resource)

	return render_to_response('sahana/hospital_resources.html', {'hospital_id': hospital_id, 'form': form, 'request': request}, context_instance=RequestContext(request))

def hospital_services_form(request):
	try:
		if(request.POST):
			hospital_id = request.POST['hospital']
		else:
			hospital_id = request.GET['hospital_id']
	except:
		hospital_id = None
	try:
		hospital = HmsHospital.objects.get(pk=hospital_id)
		services = HmsService.objects.get(hospital=hospital);
	except:
		print sys.exc_info()[0]
		services = HmsService();
	if request.POST:
		form = HospitalServiceForm(data=request.POST, instance=services)
		if form.is_valid():
			form.save()
			services.hospital = HmsHospital.objects.get(pk=request.POST['hospital'])
			services.save()
			return HttpResponse('ok')
		else:
			return HttpResponse('errors')
	else:
		form = HospitalServiceForm(instance=services)

	return render_to_response('sahana/hospital_services.html', {'hospital_id': hospital_id, 'form': form, 'request': request}, context_instance=RequestContext(request))

def hospital_activities_form(request):
	try:
		hospital_id = request.GET['hospital_id']
	except:
		hospital_id = None
	activities = HmsActivity()
	if request.POST:
		form = HospitalActivityForm(data=request.POST, instance=activities)
		if form.is_valid():
			form.save()
			activities.hospital = HmsHospital.objects.get(pk=request.POST['hospital'])
			activities.save()
			return HttpResponse('ok')
		else:
			return HttpResponse('errors')
	else:
		form = HospitalActivityForm(instance=activities)

	return render_to_response('sahana/hospital_activities.html', {'hospital_id': hospital_id, 'form': form, 'request': request}, context_instance=RequestContext(request))

def person_form(request):
	person =  PrPerson()
	if request.POST:
		pass
	else:
		form = PersonForm(instance=person)

	return render_to_response('sahana/person_form.html', {'form': form, 'request': request}, context_instance=RequestContext(request))
