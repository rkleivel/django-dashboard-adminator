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

@login_required(login_url="/login/")
class RawfilesView(generic.ListView):
    model = Rawfile
    template_name = 'rawfiles.html'

@login_required(login_url="/login/")
class RawfilesmapView(generic.ListView):
    model = Rawfile
    template_name = 'leaflet-maps.html'

@login_required(login_url="/login/")
def rawfilesmap2(request):
    #mydata = [{'lat': 60.55, 'lon': 5.20}]
    mydata = list(Rawfile.objects.values())

    return(render(request,'leaflet-maps.html', context={"mydata": mydata}))

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
