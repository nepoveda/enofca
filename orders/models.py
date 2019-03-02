# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from address.models import AddressField
from django.db import models
from django.core.mail import send_mail

STATUS_CHOICES = (
    (1, 'new'),
    (2, 'confirmed'),
    (4, 'payed'),
    (5, 'sended')
)

class Order(models.Model):
    quantity = models.PositiveSmallIntegerField(default=1)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    agree = models.BooleanField('I read and agree', default=False)
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES)

    def save(self):
        if self.id:
            send_email('TEST subject', 'TEST TEST MESSAGE!!!!!! DANIG IS GOD!!!',
                       'eshop@enofca.com', ['info@enofca.com', 'dan.nepejchal@gmail.com'])
        super(Order, self).save()
