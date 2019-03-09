# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    client = models.ForeignKey('clients.Client', on_delete=models.PROTECT)
    address = models.ForeignKey('clients.Address', on_delete=models.PROTECT)
    agree = models.BooleanField('I read and agree')
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES)

    # def save(self):
    #     if self.id:
    #         send_email('TEST subject', 'TEST TEST MESSAGE!!!!!! DANIG IS GOD!!!',
    #                    'eshop@enofca.com', ['info@enofca.com', 'dan.nepejchal@gmail.com'])
    #     super(Order, self).save()

