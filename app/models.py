# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rawfile(models.Model):
    file_name = models.CharField(max_length=200)
    mtime = models.IntegerField(default=0)
    lat = models.FloatField(default=60.53)
    lon = models.FloatField(default=5.14)
    def __str__(self):
        return self.file_name
