from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from mednet.sahana.models import HmsHospital, HmsImage
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from olwidget.widgets import MapDisplay

def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def map(request):
    return render_to_response('map.html', {}, context_instance=RequestContext(request))

def hospitals(request):
    hospital_list = HmsHospital.objects.all().order_by('name')
    paginator = Paginator(hospital_list, 25)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        hospitals = paginator.page(page)
    except (EmptyPage, InvalidPage):
        hospitals = paginator.page(paginator.num_pages)

    return render_to_response('sahana/hospitals.html', {"hospitals": hospitals}, context_instance=RequestContext(request))

def hospital(request, hospital_id):
	h = get_object_or_404(HmsHospital, pk=hospital_id)
	images = HmsImage.objects.filter(hospital=h);
	if(h.location):
		map = MapDisplay(fields=[h.location,], options={'default_zoom': 15})
	else:
		map = None
	return render_to_response('sahana/hospital.html', {'hospital': h, 'map': map, 'images': images}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))
