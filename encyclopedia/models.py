# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Strain(models.Model):
    name = models.CharField(u'název', max_length=100)
    info = models.TextField(u'informace')

    def __str__(self):
        return '%s' %self.name
