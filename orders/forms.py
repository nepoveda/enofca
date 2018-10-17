# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from address.forms import AddressField
from .models import Order

class OrderForm(forms.ModelForm):
    address = AddressField()

    class Meta:
        model = Order
        fields = '__all__'
