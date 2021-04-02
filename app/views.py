# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template

from django.views import generic
from .models import Rawfile

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

#@login_required(login_url="/login/") Kan ikkje bruka decorator på Class(?)
class RawfilesView(generic.ListView):
    model = Rawfile
    template_name = 'rawfiles.html'

#@login_required(login_url="/login/") Kan ikkje bruka decorator på Class(?)
class RawfilesmapView(generic.ListView):
    model = Rawfile
    template_name = 'leaflet-maps.html'

@login_required(login_url="/login/")
def rawfilesmap2(request):
    #mydata = [{'lat': 60.55, 'lon': 5.20}]
    #mydata = list(Rawfile.objects.values()) #alle data frå app_rawfile
    mydata = list(Rawfile.objects.values('id', 'fileName', 'fullPath', 'vidLength', 'mtimeStr', 'localTimeStr', 'firstGoodGPSLat', 'firstGoodGPSLon', 'recNum', 'seqNum') #blue
        .filter(firstGoodGPSLat__isnull=False)
        .filter(GPSfreq__gte=8)
        .exclude(seqNum__exact=1)) 
    greendata = list(Rawfile.objects.values('id', 'fileName', 'fullPath', 'vidLength', 'mtimeStr', 'localTimeStr', 'firstGoodGPSLat', 'firstGoodGPSLon', 'recNum', 'seqNum')
        .filter(firstGoodGPSLat__isnull=False)
        .filter(GPSfreq__gte=8)
        .filter(seqNum__exact=1)
        .filter(vidLength__gt=10)) 
    reddata = list(Rawfile.objects.values('id', 'fileName', 'fullPath', 'vidLength', 'mtimeStr', 'localTimeStr', 'tagLocationLat', 'tagLocationLon', 'recNum', 'seqNum')
        .filter(tagLocationLat__isnull=False)
        .exclude(GPSfreq__gt=8)
        .filter(vidLength__gt=10)) #alle data where tagLocationLat not null
    for idx, x in enumerate(mydata):
        mydata[idx]['vidLengthStr'] = str(int(mydata[idx]['vidLength']//60)).zfill(2) + ":" + str(int(mydata[idx]['vidLength']%60)).zfill(2)
        mydata[idx]['vidRecNumSeqNum'] = str(mydata[idx]['recNum']).zfill(4) + "-" + str(mydata[idx]['seqNum']).zfill(2)
    for idx, x in enumerate(greendata):
        greendata[idx]['vidLengthStr'] = str(int(greendata[idx]['vidLength']//60)).zfill(2) + ":" + str(int(greendata[idx]['vidLength']%60)).zfill(2)
        greendata[idx]['vidRecNumSeqNum'] = str(greendata[idx]['recNum']).zfill(4) + "-" + str(greendata[idx]['seqNum']).zfill(2)
    for idx, x in enumerate(reddata):
        reddata[idx]['vidLengthStr'] = str(int(reddata[idx]['vidLength']//60)).zfill(2) + ":" + str(int(reddata[idx]['vidLength']%60)).zfill(2)
        reddata[idx]['vidRecNumSeqNum'] = str(reddata[idx]['recNum']).zfill(4) + "-" + str(reddata[idx]['seqNum']).zfill(2)

    return(render(request,'leaflet-maps.html', context={"mydata": mydata, "reddata": reddata, "greendata": greendata}))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
