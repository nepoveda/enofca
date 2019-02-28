# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.exceptions import ValidationError
from address.forms import AddressField
from .models import Order

class OrderForm(forms.ModelForm):
    address = AddressField()

    class Meta:
        model = Order
        exclude = ['status']

    def clean_address(self):
        address = self.cleaned_data['address'].as_dict()
        if not all(len(address[field]) for field in ['street_number', 'route', 'country_code', 'postal_code', 'locality']):
            raise ValidationError('Please enter full address', 'invalid')
        return form_data
