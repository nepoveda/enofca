# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

CONTINENT_CHOICES= (
    ('af', 'Africa'),
    ('as', 'Asia'),
    ('eu', 'Europe'),
    ('na', 'North America'),
    ('sa', 'South America'),
    ('an', 'Antarctica'),
    ('au', 'Australia/Oceania'),
)

def company_upload(instance, filename):
    return 'company/{0}/{1}'.format(instance.name, filename)

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=company_upload, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    continent = models.CharField(max_length=10, choices=CONTINENT_CHOICES)

    paper = models.BooleanField()
    oil = models.BooleanField()
    fuel = models.BooleanField()
    clothing = models.BooleanField()
    medicine = models.BooleanField()
    science = models.BooleanField()
    food = models.BooleanField()
    buildings = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.name)
