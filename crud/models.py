# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Member(models.Model):
    companyname = models.CharField(max_length=100, blank=False)
    fullname = models.CharField(max_length=100, blank=False)
    jobtitle = models.CharField(max_length=100, blank=True)
    emailaddress = models.EmailField()
    softwareusername = models.TextField(max_length=255, blank=False)
    expirationdate = models.DateField('%m/%d/%Y')
    version = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
