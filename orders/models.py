# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from address.models import AddressField
from django.db import models

# Create your models here.

class Order(models.Model):
    quantity = models.PositiveSmallIntegerField(default=1)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = AddressField()
