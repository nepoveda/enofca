# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Seed(models.Model):
    name = models.CharField(u'název', max_length=100)
    info = models.TextField(u'informace')

class SeedBank(models.Model):
    name = models.CharField(u'název', max_length=100)
    link = models.CharField(u'link', max_length=100)
