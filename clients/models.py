# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Client(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)

class Address(models.Model):
   street = models.CharField(max_length=100)
   street2 = models.CharField(max_length=100, null=True, blank=True)
   city = models.CharField(max_length=100)
   region = models.CharField(max_length=50)
   zip_code = models.CharField(max_length=50)
   country = models.CharField(max_length=50)
