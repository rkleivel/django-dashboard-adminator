# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rawfile(models.Model):
    name = models.CharField(max_length=2000, null=True)
    mtime = models.IntegerField(null=True)
    vidLength = models.FloatField(null=True)
    vidNumFrames = models.IntegerField(null=True)
    camFirmware = models.CharField(max_length=100, null=True)
    fullPath = models.CharField(max_length=2000, null=True)
    fileName = models.CharField(max_length=2000, null=True)
    fileFullName = models.CharField(max_length=2000, null=True)
    gpsInfoFullPath = models.CharField(max_length=2000, null=True)
    recNum = models.IntegerField(null=True)
    seqNum = models.IntegerField(null=True)
    firstGoodGPSLat = models.FloatField(null=True)
    firstGoodGPSLon = models.FloatField(null=True)
    lastGoodGPSLat = models.FloatField(null=True)
    lastGoodGPSLon = models.FloatField(null=True)
    tagLocationLat = models.FloatField(null=True) # default=60.53
    tagLocationLon = models.FloatField(null=True) # default=5.14
    timeZone = models.CharField(max_length=100, null=True)
    timeOffset = models.IntegerField(null=True)
    country_int = models.CharField(max_length=2000, null=True)
    country_loc = models.CharField(max_length=2000, null=True)
    county = models.CharField(max_length=2000, null=True)
    municipality = models.CharField(max_length=2000, null=True)
    UTCtime = models.IntegerField(null=True)
    localTime = models.IntegerField(null=True)
    trail = models.CharField(max_length=2000, null=True)
    def __str__(self):
        return self.file_name
