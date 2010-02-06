# Create your views here.

# based off of proxy.cgi

import urllib2 
import sys, os
from django.http import HttpResponse


def index(request):
    
    allowedHosts = ['www.openlayers.org', 'openlayers.org',
                'labs.metacarta.com', 'world.freemap.in',
                'prototype.openmnnd.org', 'geo.openplans.org',
                'sigma.openplans.org', 'demo.opengeo.org',
                'www.openstreetmap.org', 'sample.avencia.com',
                'v-swe.uni-muenster.de:8080', 'local.yahooapis.com',
                'ispatial.t-sciences.com','haiti.sahanafoundation.org','haiti.opensgi.net',
                'haiti.ushahidi.com','ose.petschge.de','openstreetbugs.appspot.com',
                'www.sharedgeo.org', 'hurakan.ucsd.edu', 'www.google.com', 'hurakan.telascience.org']

    
    if request.POST:
        if "url" in request.POST:
            url = request.POST["url"]
        else:
            url = "http://www.openlayers.org"
    elif 'url' in request.GET:
        url = request.GET['url']
    else:
        return HttpResponse("No url supplied", mimetype="text/plain")

        
        
    try:
        host = url.split("/")[2]
        if allowedHosts and not host in allowedHosts:
            content = "Status: 502 Bad Gateway\n"
            content += "Content-Type: text/plain\n"
            content += "\n" 
            content += "This proxy does not allow you to access that location (%s)." % (host,)
            return HttpResponse(content, mimetype="text/plain", status=502)

        elif url.startswith("http://") or url.startswith("https://"):
            if request.POST:
                length = request.META["CONTENT_LENGTH"]
                headers = {"Content-Type": request.META["CONTENT_TYPE"]}
                body = request.META['QUERY_STRING']
                r = urllib2.Request(url, body, headers)
                y = urllib2.urlopen(r)
            else:
                y = urllib2.urlopen(url)


            i = y.info()
            if i.has_key("Content-Type"):
                mimetype = i["Content-Type"]
            else:
                mimetype = "text/plain"

            content = y.read()
            y.close()
            return HttpResponse(content, mimetype=mimetype)
        else:
            return HttpResponse("Illegal request.", mimetype="text/plain")

    except Exception, E:
        content = "Some unexpected error occurred. Error text was: %s" % E
        return HttpResponse(content, mimetype="text/plain", status=500)

