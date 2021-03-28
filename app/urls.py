# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    #
    path('rawfiles', views.RawfilesView.as_view(), name='rawfiles'),
    path('rawfilesmap', views.RawfilesmapView.as_view(), name='rawfilesmap'),
    path('rawfilesmap2', views.rawfilesmap2, name='rawfilesmap2'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
