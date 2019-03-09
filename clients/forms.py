# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.exceptions import ValidationError
from .models import Address, Client

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
