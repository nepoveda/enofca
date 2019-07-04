# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from orders.models import Order
from clients.models import Address

# Register your models here.
# class AddressAdmin(admin.TabularInline):
#     model = Address

# class OrderAdmin(admin.ModelAdmin):
#     inlines = [AddressAdmin]

#     class Meta:
#         model = Order

admin.site.register(Order)
